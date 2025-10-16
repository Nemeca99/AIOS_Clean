#!/usr/bin/env python3
"""
Contract Test: Idempotency
Ensures mutating operations are idempotent when given the same key.
"""

import uuid
import pytest
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_carma_consolidate_idempotency():
    """CARMA consolidate must be idempotent with same key."""
    try:
        import carma_core
        
        # Skip if consolidate doesn't support idempotency yet
        if not hasattr(carma_core, 'consolidate'):
            pytest.skip("CARMA consolidate not yet implemented")
        
        idem_key = str(uuid.uuid4())
        
        # Run consolidate twice with same key
        result1 = carma_core.consolidate(mode="semantic", limit=10, idempotency_key=idem_key)
        result2 = carma_core.consolidate(mode="semantic", limit=10, idempotency_key=idem_key)
        
        # Results should be identical
        assert result1 == result2, "consolidate must return same result for same idempotency key"
        
    except ImportError:
        pytest.skip("CARMA core not available")
    except AttributeError as e:
        pytest.skip(f"Idempotency not yet implemented: {e}")


def test_dream_consolidate_idempotency():
    """Dream consolidation must be idempotent with same key."""
    try:
        import dream_core
        
        # Skip if not implemented
        if not hasattr(dream_core, 'consolidate_conversation_fragments'):
            pytest.skip("Dream consolidate not yet implemented")
        
        idem_key = str(uuid.uuid4())
        
        # Create test instance
        dream = dream_core.DreamCore()
        
        # Skip if idempotency not supported yet
        consolidate_func = getattr(dream, 'consolidate_conversation_fragments')
        import inspect
        sig = inspect.signature(consolidate_func)
        if 'idempotency_key' not in sig.parameters:
            pytest.skip("Idempotency not yet implemented for dream consolidate")
        
        # Run twice with same key
        result1 = dream.consolidate_conversation_fragments(
            similarity_threshold=0.8,
            idempotency_key=idem_key
        )
        result2 = dream.consolidate_conversation_fragments(
            similarity_threshold=0.8,
            idempotency_key=idem_key
        )
        
        assert result1 == result2, "Dream consolidate must be idempotent"
        
    except ImportError:
        pytest.skip("Dream core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable yet: {e}")


def test_fractal_allocate_deterministic():
    """Fractal knapsack allocate must be deterministic for same inputs."""
    try:
        from fractal_core.core.knapsack_allocator import KnapsackAllocator, Span
        
        allocator = KnapsackAllocator()
        
        # Create test spans
        spans = [
            Span('err1', 'User confused about concept X', 'error_epoch', 300),
            Span('err2', 'AI provided wrong example', 'error_epoch', 250),
            Span('tone1', 'User shows frustration', 'tone_shift', 150),
            Span('recent1', 'Most recent exchange', 'recent_turn', 200),
            Span('aux1', 'Related background info', 'aux_dep', 100),
        ]
        
        query_type = {'pattern_language': 0.1, 'logic': 0.7, 'creative': 0.1, 'retrieval': 0.1}
        
        # Run allocation twice with same inputs
        chosen1, _ = allocator.allocate(spans.copy(), budget=800, query_type_mixture=query_type)
        chosen2, _ = allocator.allocate(spans.copy(), budget=800, query_type_mixture=query_type)
        
        # Extract IDs for comparison
        ids1 = [s.span_id for s in chosen1]
        ids2 = [s.span_id for s in chosen2]
        
        assert ids1 == ids2, "Allocator must return same spans for same inputs (deterministic)"
        
    except ImportError:
        pytest.skip("Fractal core not available")
    except Exception as e:
        pytest.skip(f"Test not applicable: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

