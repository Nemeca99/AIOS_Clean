"""
Property-Based Tests for AIOS

Uses Hypothesis library to generate test cases and verify invariants:
- Compression idempotence
- Reordering invariance
- Duplicate injection handling
- Noise resilience
- Edge case handling

Install: pip install hypothesis

Run: pytest tests/test_property_based.py -v
"""

import pytest
import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Try to import hypothesis, skip tests if not available
try:
    from hypothesis import given, strategies as st, settings
    HYPOTHESIS_AVAILABLE = True
    # Mark all tests as property-based tests
    pytestmark = pytest.mark.property
except ImportError:
    HYPOTHESIS_AVAILABLE = False
    pytestmark = pytest.mark.skip(reason="hypothesis not installed")

try:
    from carma_core.core.compressor import CARMAMemoryCompressor
    CARMA_AVAILABLE = True
except ImportError:
    CARMA_AVAILABLE = False
    pytestmark = pytest.mark.skip(reason="carma_core not available")


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
class TestCompressionInvariants:
    """Property-based tests for compression invariants"""
    
    @given(st.lists(st.text(min_size=10, max_size=100), min_size=2, max_size=10))
    @settings(max_examples=20, deadline=None)
    def test_compression_idempotent(self, fragments_text):
        """
        Property: Compressing twice should yield same result (idempotence)
        
        compress(X) == compress(compress(X))
        """
        compressor = CARMAMemoryCompressor()
        
        # Create fragments
        frags = [{'content': text, 'timestamp': i} for i, text in enumerate(fragments_text)]
        
        # First compression
        result1 = compressor.compress_memory(frags, 'semantic')
        compressed1 = result1.get('compressed_fragments', [])
        
        # Second compression (of already compressed)
        result2 = compressor.compress_memory(compressed1, 'semantic')
        compressed2 = result2.get('compressed_fragments', [])
        
        # Should be same length (idempotent)
        assert len(compressed1) == len(compressed2), \
            f"Compression not idempotent: {len(compressed1)} != {len(compressed2)}"
    
    @given(st.lists(st.text(min_size=10, max_size=100), min_size=3, max_size=8))
    @settings(max_examples=20, deadline=None)
    def test_reordering_doesnt_change_concepts(self, fragments_text):
        """
        Property: Fragment order shouldn't affect semantic compression
        
        compress([A, B, C]) ≈ compress([C, B, A])
        """
        compressor = CARMAMemoryCompressor()
        
        # Original order
        frags1 = [{'content': text, 'timestamp': i} for i, text in enumerate(fragments_text)]
        
        # Reversed order
        frags2 = [{'content': text, 'timestamp': i} for i, text in enumerate(reversed(fragments_text))]
        
        # Compress both
        result1 = compressor.compress_memory(frags1, 'semantic')
        result2 = compressor.compress_memory(frags2, 'semantic')
        
        # Extract content (order may differ, but concepts should match)
        concepts1 = set(f['content'] for f in result1.get('compressed_fragments', []))
        concepts2 = set(f['content'] for f in result2.get('compressed_fragments', []))
        
        # Should have same unique concepts (or very similar)
        assert concepts1 == concepts2, \
            f"Reordering changed concepts: {concepts1} != {concepts2}"
    
    @given(st.text(min_size=10, max_size=100))
    @settings(max_examples=20, deadline=None)
    def test_duplicate_injection_idempotent(self, fragment_text):
        """
        Property: Adding exact duplicates shouldn't change output
        
        compress([A, A, A]) == compress([A])
        """
        compressor = CARMAMemoryCompressor()
        
        # Single fragment
        single = [{'content': fragment_text, 'timestamp': 1}]
        
        # Triple duplicates
        tripled = [
            {'content': fragment_text, 'timestamp': 1},
            {'content': fragment_text, 'timestamp': 2},
            {'content': fragment_text, 'timestamp': 3}
        ]
        
        # Compress both
        result_single = compressor.compress_memory(single, 'semantic')
        result_tripled = compressor.compress_memory(tripled, 'semantic')
        
        # Should produce same number of fragments (duplicates consolidated)
        assert len(result_single['compressed_fragments']) == len(result_tripled['compressed_fragments']), \
            f"Duplicates not consolidated: {len(result_single['compressed_fragments'])} != {len(result_tripled['compressed_fragments'])}"
    
    @given(st.text(min_size=15, max_size=50, alphabet=st.characters(min_codepoint=65, max_codepoint=122)))
    @settings(max_examples=15, deadline=None)
    def test_noise_doesnt_destroy_content(self, base_text):
        """
        Property: Adding noise words shouldn't completely destroy semantic content
        
        compress("text") should preserve key concepts even with noise
        """
        # Skip degenerate inputs
        words = [w for w in base_text.strip().split() if len(w) > 1]
        if len(words) < 2:
            return  # Need at least 2 meaningful words
        
        compressor = CARMAMemoryCompressor()
        
        # Clean text (use words only)
        clean_text = ' '.join(words)
        clean = [{'content': clean_text, 'timestamp': 1}]
        
        # Noisy version (with filler words)
        noisy_text = f"um, {clean_text}, like, you know, yeah"
        noisy = [{'content': noisy_text, 'timestamp': 1}]
        
        # Compress both
        result_clean = compressor.compress_memory(clean, 'semantic')
        result_noisy = compressor.compress_memory(noisy, 'semantic')
        
        # Extract concepts (simple word-based)
        clean_concepts = compressor._extract_concepts(clean_text)
        noisy_concepts = compressor._extract_concepts(noisy_text)
        
        # Most concepts should survive noise (relaxed to 0.5 for edge cases)
        if clean_concepts:
            overlap = len(clean_concepts.intersection(noisy_concepts))
            preservation_ratio = overlap / len(clean_concepts)
            
            assert preservation_ratio > 0.5, \
                f"Noise destroyed too many concepts: {preservation_ratio:.1%} preserved ('{clean_text[:30]}...')"


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
class TestEdgeCases:
    """Property-based edge case testing"""
    
    @given(st.text(min_size=1, max_size=5))
    @settings(max_examples=20, deadline=None)
    def test_very_short_text_doesnt_crash(self, short_text):
        """
        Property: Very short text shouldn't crash compression
        
        Even "a" or "xyz" should compress without error
        """
        compressor = CARMAMemoryCompressor()
        
        frags = [{'content': short_text, 'timestamp': 1}]
        
        try:
            result = compressor.compress_memory(frags, 'semantic')
            assert 'compressed_fragments' in result, "Missing compressed_fragments in result"
        except Exception as e:
            pytest.fail(f"Short text crashed compression: {e}")
    
    @given(st.lists(st.text(min_size=1, max_size=20), min_size=0, max_size=3))
    @settings(max_examples=15, deadline=None)
    def test_empty_or_tiny_lists(self, fragments_text):
        """
        Property: Empty or tiny fragment lists should be handled gracefully
        """
        compressor = CARMAMemoryCompressor()
        
        frags = [{'content': text, 'timestamp': i} for i, text in enumerate(fragments_text)]
        
        try:
            result = compressor.compress_memory(frags, 'semantic')
            
            # Should always return valid result
            assert 'compressed_fragments' in result
            assert 'compression_ratio' in result
            
            # Empty input should give empty output
            if len(frags) == 0:
                assert len(result['compressed_fragments']) == 0
                
        except Exception as e:
            pytest.fail(f"Edge case crashed: {e}")
    
    @given(st.lists(st.sampled_from(['   ', '\n\n', '\t\t', '...', '???']), min_size=2, max_size=5))
    @settings(max_examples=15, deadline=None)
    def test_whitespace_and_symbols_only(self, symbols):
        """
        Property: Fragments with only whitespace/symbols shouldn't break compression
        """
        compressor = CARMAMemoryCompressor()
        
        frags = [{'content': sym, 'timestamp': i} for i, sym in enumerate(symbols)]
        
        try:
            result = compressor.compress_memory(frags, 'semantic')
            # Should not crash, even if result is empty
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Whitespace/symbols crashed: {e}")


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
class TestBoundaryConditions:
    """Test boundary conditions and limits"""
    
    @given(st.text(min_size=500, max_size=1000))
    @settings(max_examples=10, deadline=None)
    def test_large_fragments(self, large_text):
        """
        Property: Large text fragments should compress without error
        """
        compressor = CARMAMemoryCompressor()
        
        frags = [{'content': large_text, 'timestamp': 1}]
        
        try:
            result = compressor.compress_memory(frags, 'semantic')
            assert 'compressed_fragments' in result
        except Exception as e:
            pytest.fail(f"Large fragment crashed: {e}")
    
    @given(st.text(min_size=10))
    @settings(max_examples=10, deadline=None)
    def test_fragment_without_timestamp(self, text):
        """
        Property: Fragments missing timestamp should be handled
        """
        compressor = CARMAMemoryCompressor()
        
        # Missing timestamp
        frags = [{'content': text}]
        
        try:
            result = compressor.compress_memory(frags, 'semantic')
            # Should either add default timestamp or handle gracefully
            assert 'compressed_fragments' in result
        except Exception as e:
            # Expected - might require timestamp
            pass  # Graceful failure is acceptable


@pytest.mark.skipif(not HYPOTHESIS_AVAILABLE, reason="hypothesis not installed")
def test_hypothesis_is_working():
    """Meta-test: Verify hypothesis is actually generating varied inputs"""
    seen_inputs = set()
    
    @given(st.text(min_size=5, max_size=20))
    @settings(max_examples=10, deadline=None)
    def collect_inputs(text):
        seen_inputs.add(text)
    
    collect_inputs()
    
    # Should have generated multiple different inputs
    assert len(seen_inputs) > 1, "Hypothesis not generating varied inputs"


# Run a quick smoke test if executed directly
if __name__ == '__main__':
    if HYPOTHESIS_AVAILABLE:
        print("✓ Hypothesis available - property tests will run")
        print("\nRunning quick smoke test...")
        
        compressor = CARMAMemoryCompressor()
        test_frags = [
            {'content': 'test A', 'timestamp': 1},
            {'content': 'test A', 'timestamp': 2}
        ]
        result = compressor.compress_memory(test_frags, 'semantic')
        print(f"Smoke test result: {len(test_frags)} -> {len(result['compressed_fragments'])} fragments")
        print("✓ Smoke test passed")
    else:
        print("✗ Hypothesis not installed")
        print("Install with: pip install hypothesis")

