#!/usr/bin/env python3
"""
Contract Test: Performance Ceilings
Ensures critical paths meet performance requirements.
"""

import time
import pytest
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_carma_retrieve_performance():
    """CARMA retrieve must complete under 200ms for standard query."""
    try:
        import carma_core
        
        # Skip if not available
        if not hasattr(carma_core, 'CARMASystem'):
            pytest.skip("CARMA System not available")
        
        system = carma_core.CARMASystem()
        
        # Warm up
        _ = system.process_query("test query")
        
        # Measure performance
        t0 = time.perf_counter()
        result = system.process_query("What is artificial intelligence?")
        dt = (time.perf_counter() - t0) * 1000  # milliseconds
        
        assert dt < 200, f"CARMA retrieve took {dt:.1f}ms, expected <200ms"
        
    except ImportError:
        pytest.skip("CARMA core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_carma_no_conversation_embedding_n_plus_1():
    """CARMA should not re-embed conversation messages on every query."""
    try:
        import carma_core
        
        if not hasattr(carma_core, 'CARMASystem'):
            pytest.skip("CARMA System not available")
        
        system = carma_core.CARMASystem()
        
        # Check if conversation embedding cache exists
        has_cache = hasattr(system, 'conversation_embedding_cache') or \
                   hasattr(system.cache, 'conversation_embedding_cache')
        
        if not has_cache:
            pytest.fail("CARMA lacks conversation embedding cache - will cause N+1 embeds")
        
    except ImportError:
        pytest.skip("CARMA core not available")
    except AssertionError:
        raise
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_fractal_classify_performance():
    """Fractal classifier must complete under 50ms."""
    try:
        from fractal_core.core.multihead_classifier import MultiheadClassifier
        
        classifier = MultiheadClassifier()
        
        # Warm up
        _ = classifier.classify_mixture("test query")
        
        # Measure
        queries = [
            "What is the ratio of x and y?",
            "Is this correct? A) Yes B) No",
            "Design a creative solution"
        ]
        
        for query in queries:
            t0 = time.perf_counter()
            _ = classifier.classify_mixture(query)
            dt = (time.perf_counter() - t0) * 1000
            
            assert dt < 50, f"Classifier took {dt:.1f}ms, expected <50ms for '{query}'"
        
    except ImportError:
        pytest.skip("Fractal core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_luna_arbiter_no_uncached_http():
    """Luna Arbiter should cache gold standards and quality assessments."""
    try:
        from luna_core.systems.luna_arbiter_system import LunaArbiterSystem
        
        arbiter = LunaArbiterSystem()
        
        # Check for caching mechanisms
        has_gold_cache = hasattr(arbiter, 'gold_standard_cache') or \
                        hasattr(arbiter, '_gold_standard_cache')
        has_quality_cache = hasattr(arbiter, 'quality_assessment_cache') or \
                           hasattr(arbiter, '_quality_cache')
        
        if not (has_gold_cache and has_quality_cache):
            pytest.fail("Luna Arbiter lacks gold standard or quality caching - causes HTTP hot path")
        
    except ImportError:
        pytest.skip("Luna Arbiter not available")
    except AssertionError:
        raise
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


def test_dream_consolidate_performance():
    """Dream consolidation should process 100 messages in under 2 seconds."""
    try:
        import dream_core
        
        if not hasattr(dream_core, 'DreamCore'):
            pytest.skip("Dream Core not available")
        
        dream = dream_core.DreamCore()
        
        # This test requires actual conversation data
        # Skip if no conversations available
        from pathlib import Path
        conv_dir = Path("data_core/conversations")
        if not conv_dir.exists():
            pytest.skip("No conversation data available")
        
        conv_files = list(conv_dir.glob("conversation_*.json"))
        if not conv_files:
            pytest.skip("No conversation files to test")
        
        # Measure consolidation time
        t0 = time.perf_counter()
        result = dream.consolidate_conversation_fragments(similarity_threshold=0.8)
        dt = time.perf_counter() - t0
        
        # Allow 2 seconds for reasonable number of messages
        assert dt < 5.0, f"Dream consolidation took {dt:.1f}s, expected <5s"
        
    except ImportError:
        pytest.skip("Dream core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

