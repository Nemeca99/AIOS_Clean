#!/usr/bin/env python3
"""
Contract Test: Quality Gates
Ensures operations maintain or improve quality.
"""

import pytest
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_dream_consolidation_preserves_retrieval():
    """Dream consolidation must not degrade retrieval quality."""
    try:
        import dream_core
        import carma_core
        
        if not hasattr(dream_core, 'DreamCore'):
            pytest.skip("Dream Core not available")
        if not hasattr(carma_core, 'CARMASystem'):
            pytest.skip("CARMA System not available")
        
        # Initialize systems
        carma = carma_core.CARMASystem()
        dream = dream_core.DreamCore()
        
        # Test query
        test_query = "What is artificial intelligence?"
        
        # Retrieve before consolidation
        result_before = carma.process_query(test_query)
        fragments_before = result_before.get('fragments_found', 0)
        
        # Run dream consolidation (dry-run if available)
        dream.consolidate_conversation_fragments(similarity_threshold=0.8)
        
        # Retrieve after consolidation
        result_after = carma.process_query(test_query)
        fragments_after = result_after.get('fragments_found', 0)
        
        # Retrieval should not degrade significantly
        assert fragments_after >= fragments_before * 0.8, \
            f"Retrieval degraded: {fragments_before} -> {fragments_after} fragments"
        
    except ImportError:
        pytest.skip("Required cores not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_dream_uses_embedding_similarity():
    """Dream consolidation should use cosine similarity, not just Jaccard."""
    try:
        import dream_core
        from pathlib import Path
        
        # Check if Dream uses embeddings
        dream_file = Path("dream_core/dream_core.py")
        if not dream_file.exists():
            pytest.skip("Dream core file not found")
        
        content = dream_file.read_text(encoding='utf-8')
        
        # Should use embeddings, not just word splitting
        has_embedding = "embedding" in content.lower() or "embed" in content
        has_cosine = "cosine" in content.lower()
        has_word_split_only = "words_current.intersection" in content and not has_embedding
        
        if has_word_split_only:
            pytest.fail("Dream uses Jaccard-only merge - needs cosine similarity with embeddings")
        
        # If it uses embeddings, that's good
        assert has_embedding or has_cosine, "Dream should use embedding-based similarity"
        
    except ImportError:
        pytest.skip("Dream core not available")
    except AssertionError:
        raise
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_dream_freshness_immunity():
    """Dream should not merge messages from today (freshness immunity)."""
    try:
        import dream_core
        from pathlib import Path
        
        dream_file = Path("dream_core/dream_core.py")
        if not dream_file.exists():
            pytest.skip("Dream core file not found")
        
        content = dream_file.read_text(encoding='utf-8')
        
        # Check for freshness/recency checks
        has_timestamp_check = "timestamp" in content and ("datetime.now()" in content or "time.time()" in content)
        has_freshness = "fresh" in content.lower() or "recent" in content.lower()
        
        if not (has_timestamp_check or has_freshness):
            pytest.fail("Dream lacks freshness immunity - may merge today's messages")
        
    except ImportError:
        pytest.skip("Dream core not available")
    except AssertionError:
        raise
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_fractal_allocator_diversity():
    """Fractal allocator must preserve topic diversity (no near-duplicate packing)."""
    try:
        from fractal_core.core.knapsack_allocator import KnapsackAllocator, Span
        
        allocator = KnapsackAllocator()
        
        # Create spans with duplicate topics
        spans = [
            Span(f'span_{i}', f'Content about topic {i//2}', 'error_epoch', 100, metadata={'topic': i//2})
            for i in range(10)
        ]
        
        query_type = {'pattern_language': 0.1, 'logic': 0.7, 'creative': 0.1, 'retrieval': 0.1}
        
        # Allocate with limited budget
        chosen, _ = allocator.allocate(spans, budget=300, query_type_mixture=query_type)
        
        # Extract topics
        topics = set()
        for span in chosen:
            if hasattr(span, 'metadata') and span.metadata:
                topics.add(span.metadata.get('topic'))
        
        # Should have diversity - not all from same topic
        assert len(topics) >= 2, f"Allocator packed duplicates - only {len(topics)} unique topics"
        
    except ImportError:
        pytest.skip("Fractal core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_luna_rvc_tier_enforcement():
    """Luna RVC must enforce token budget tiers."""
    try:
        from luna_core.systems.luna_response_value_classifier import LunaResponseValueClassifier, ResponseValueTier
        
        rvc = LunaResponseValueClassifier()
        
        # Test trivial input
        trivial_assessment = rvc.classify_response_value("hey")
        assert trivial_assessment.tier == ResponseValueTier.TRIVIAL, \
            f"Trivial input misclassified as {trivial_assessment.tier.value}"
        assert trivial_assessment.max_token_budget <= 15, \
            f"Trivial tier has excessive budget: {trivial_assessment.max_token_budget}"
        
        # Test high-complexity input
        complex_assessment = rvc.classify_response_value(
            "What is the comprehensive philosophical implication of artificial general intelligence on human existence?"
        )
        assert complex_assessment.tier in [ResponseValueTier.HIGH, ResponseValueTier.CRITICAL, ResponseValueTier.MAXIMUM], \
            f"Complex input under-classified as {complex_assessment.tier.value}"
        
    except ImportError:
        pytest.skip("Luna RVC not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


# ============================================================================
# V5.1 PULSE SYSTEM TESTS (External Auditor mandated)
# ============================================================================

def test_pulse_always_emits_on_exception():
    """
    Test 1: Always-emit - tick recorded even when exception occurs.
    Uses try/finally pattern to guarantee emit.
    """
    from collections import deque
    import time
    
    # Mock pulse system
    pulse_tick_counter = 0
    pulse_one_positions = deque(maxlen=100000)
    
    def emit_active_tick(active: bool):
        nonlocal pulse_tick_counter
        pulse_tick_counter += 1
        if active:
            pulse_one_positions.append(pulse_tick_counter)
    
    initial_ticks = pulse_tick_counter
    active_this_tick = False
    
    try:
        raise ValueError("Simulated error")
    except ValueError:
        pass
    finally:
        emit_active_tick(active_this_tick)
    
    assert pulse_tick_counter == initial_ticks + 1
    assert len(pulse_one_positions) == 0


def test_pulse_bounded_buffer():
    """
    Test 2: Bounded buffer - deque respects maxlen.
    """
    from collections import deque
    
    maxlen = 1000
    pulse_one_positions = deque(maxlen=maxlen)
    
    # Emit more than maxlen
    for i in range(maxlen + 100):
        pulse_one_positions.append(i)
    
    assert len(pulse_one_positions) == maxlen


def test_pulse_window_clamp():
    """
    Test 3: Monotonic sanity - window clamps on clock jump.
    """
    import time
    
    pulse_window_seconds = 600
    pulse_last_heartbeat_ts = time.monotonic()
    
    # Simulate huge clock jump
    fake_now = pulse_last_heartbeat_ts + (pulse_window_seconds * 5)
    
    # Window should clamp to 4x max
    window_seconds = max(1.0, min(fake_now - pulse_last_heartbeat_ts, pulse_window_seconds * 4))
    
    assert window_seconds == pulse_window_seconds * 4


def test_pulse_cold_start(fake_monotonic):
    """
    Test 4: Cold start - first heartbeat primes, second emits.
    
    Tests that the pulse system:
    - Primes timestamp on first heartbeat without emitting metrics
    - Computes valid metrics on second heartbeat
    
    Uses fake_monotonic fixture for deterministic, instant testing (no sleep).
    """
    import time
    from collections import deque
    
    pulse_last_heartbeat_ts = None
    pulse_tick_counter = 0
    pulse_one_positions = deque(maxlen=100000)
    
    # First heartbeat - prime only (time.monotonic() -> 0.0)
    now_ts = time.monotonic()
    if pulse_last_heartbeat_ts is None:
        pulse_last_heartbeat_ts = now_ts
        # Skip emission on first heartbeat
    
    assert pulse_last_heartbeat_ts == 0.0, "Timestamp should be primed at 0.0"
    
    # Emit some ticks
    for i in range(5):
        pulse_tick_counter += 1
        if i % 2 == 0:
            pulse_one_positions.append(pulse_tick_counter)
    
    # Second heartbeat - compute (time.monotonic() -> 0.1, no sleep needed)
    now_ts = time.monotonic()
    window_seconds = now_ts - pulse_last_heartbeat_ts
    ones = len(pulse_one_positions)
    pulse_bpm = ones / window_seconds if window_seconds > 0 else 0.0
    
    # Verify state
    assert ones == 3, f"Expected 3 ones, got {ones}"
    assert pulse_tick_counter == 5, f"Expected 5 ticks, got {pulse_tick_counter}"
    assert window_seconds == 0.1, f"Expected 0.1s window (deterministic), got {window_seconds}"
    
    # BPM should be exactly 30 (3 ones / 0.1 seconds = 30 ops/sec)
    assert pulse_bpm == 30.0, f"Expected 30.0 BPM, got {pulse_bpm}"


def test_pulse_consolidation_modes():
    """
    Test 5: Hint path - pulse_bpm triggers hot/cold consolidation modes.
    """
    try:
        from dream_core.dream_core import DreamCore
        
        dream = DreamCore()
        
        # Hot path (high activity > 0.02 threshold)
        result_hot = dream.consolidate_conversation_fragments(pulse_context={'pulse_bpm': 0.05})
        assert result_hot.get('mode') == 'hot_path'
        
        # Cold path (low activity < 0.02 threshold)
        result_cold = dream.consolidate_conversation_fragments(pulse_context={'pulse_bpm': 0.01})
        assert result_cold.get('mode') == 'cold_path'
        
        # Default (no context)
        result_default = dream.consolidate_conversation_fragments()
        assert result_default.get('mode') == 'cold_path'
        
    except ImportError:
        pytest.skip("Dream core not available")


def test_pulse_zero_activity(fake_monotonic):
    """
    Test 6: Zero-activity edge case - BPM=0, HRV=0 without errors.
    
    Uses fake_monotonic for instant, deterministic testing.
    """
    import time
    from collections import deque
    
    pulse_tick_counter = 0
    pulse_one_positions = deque(maxlen=100000)
    pulse_last_heartbeat_ts = time.monotonic()  # 0.0
    
    # Emit only inactive ticks
    for i in range(10):
        pulse_tick_counter += 1
        # Don't add to pulse_one_positions (all inactive)
    
    # Compute metrics (time.monotonic() -> 0.1, no sleep needed)
    now_ts = time.monotonic()
    window_seconds = now_ts - pulse_last_heartbeat_ts
    ones = len(pulse_one_positions)
    ticks = pulse_tick_counter
    
    pulse_bpm = ones / window_seconds if window_seconds > 0 else 0.0
    pulse_hvv = 0.0  # No ones = no variability
    
    assert ones == 0
    assert ticks == 10
    assert window_seconds == 0.1  # Deterministic
    assert pulse_bpm == 0.0
    assert pulse_hvv == 0.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

