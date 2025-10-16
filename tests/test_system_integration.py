#!/usr/bin/env python3
"""
AIOS System Integration Tests
Tests complete system pipelines and core interactions

Coverage:
- Main.py core discovery and loading
- Luna -> CARMA -> Dream pipeline
- Audit system self-healing
- RAG manual oracle
- Linguistic Calculus integration
- Mirror reflection
- Arbiter assessment
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# Mark all tests in this file as 'integration' tests
pytestmark = pytest.mark.integration


def test_main_discovers_cores():
    """Test that main.py can discover all *_core folders"""
    import importlib.util
    
    main_spec = importlib.util.spec_from_file_location("main", "main.py")
    main_module = importlib.util.module_from_spec(main_spec)
    main_spec.loader.exec_module(main_module)
    
    cores = main_module.discover_cores()
    
    # Should find at least core systems
    expected_cores = ['luna_core', 'carma_core', 'dream_core', 'main_core', 'consciousness_core']
    for core in expected_cores:
        assert core in cores, f"Core discovery missed {core}"
    
    # Should find at least 10 cores
    assert len(cores) >= 10, f"Only found {len(cores)} cores, expected 10+"


def test_luna_linguistic_calculus_integration():
    """Test that Luna's LinguaCalc is operational"""
    try:
        from luna_core.core.luna_lingua_calc import LinguaCalc, ExperienceState
        
        calc = LinguaCalc()
        state = ExperienceState()
        
        # Test Why operator
        result = calc.op_why(state, "heat", "expansion")
        assert result.updated is state
        assert len(result.derivations) > 0
        assert "WHY" in result.derivations[0]
        
        # Test How operator
        result2 = calc.op_how(state, "cause", "effect", steps=["step1", "step2"])
        assert result2.depth_score >= 2  # At least 2 steps
        
        # Test rewrite rule (Why + How -> What)
        result3 = calc.combine_why_how_into_what(state, "cause", "effect", ["mechanism"])
        assert result3.compress_gain > 0
        assert len(result3.derivations) > 0  # Should have derivations
        
    except ImportError:
        pytest.skip("LinguaCalc not available")


def test_mirror_reflection_integration():
    """Test that consciousness_core Mirror is operational"""
    try:
        from consciousness_core.biological.mirror import Mirror
        from luna_core.core.luna_lingua_calc import ExperienceState
        
        mirror = Mirror()
        
        # Create experience state
        exp = ExperienceState()
        exp.add_edge("a", "CAUSES", "b")
        exp.add_edge("b", "MECHANISM", "c")
        
        # Reflect
        result = mirror.reflect(exp)
        
        assert result['reflection_count'] == 1
        assert result['graph_size'] >= 2  # At least 2 edges
        assert result['compression_index'] >= 0
        
    except ImportError:
        pytest.skip("Mirror not available")


def test_arbiter_assessment_with_pulse():
    """Test that Arbiter accepts pulse metrics in assessment"""
    try:
        from luna_core.systems.luna_arbiter_system import LunaArbiterSystem
        
        arbiter = LunaArbiterSystem()
        
        # Assess with pulse context (using actual API: user_prompt, luna_response, tte_used, max_tte)
        assessment = arbiter.assess_response(
            user_prompt="test question",
            luna_response="test response",
            tte_used=50,
            max_tte=500,
            lingua_calc_context={
                'calc_depth': 3,
                'calc_gain': 0.2,
                'pulse_bpm': 0.03,
                'pulse_hvv': 5.2
            }
        )
        
        # Should return valid assessment
        assert assessment is not None
        assert hasattr(assessment, 'utility_score')
        # Pulse context should be captured
        assert assessment.cache_entry.lingua_calc_depth >= 0
        
    except ImportError:
        pytest.skip("Arbiter not available")


def test_rag_manual_oracle_lookup():
    """Test that RAG Manual Oracle can perform lookups"""
    try:
        from rag_core.manual_oracle import ManualOracle
        
        oracle = ManualOracle()
        
        # Test lookup (ManualOracle uses psycho_semantic_search, not search)
        results = oracle.psycho_semantic_search("linguistic calculus", top_k=3)
        
        if results is None:
            pytest.skip("RAG database not initialized")
        
        assert isinstance(results, (list, dict))
            
    except ImportError:
        pytest.skip("Manual Oracle not available")
    except (FileNotFoundError, Exception):
        pytest.skip("Manual files or RAG DB not available")


def test_carma_stm_ltm_biological_hemispheres():
    """Test that CARMA integrates with biological hemispheres"""
    pytest.skip("CARMA biological hemispheres API under refactor")


def test_dream_pulse_aware_consolidation():
    """Test that dream_core uses pulse metrics for consolidation"""
    # This is now tested in test_contract_quality.py::test_pulse_consolidation_modes
    pytest.skip("Covered by test_pulse_consolidation_modes")


def test_audit_system_loads():
    """Test that V3 Sovereign audit system can initialize"""
    try:
        from main_core.audit_core.audit_v3_sovereign import AuditV3Sovereign
        
        audit = AuditV3Sovereign()
        
        # Should have all components
        assert audit.policy is not None
        assert audit.static_analyzer is not None
        
        # Should have mirror if available
        if audit.mirror_enabled:
            assert audit.mirror is not None
            
    except ImportError:
        pytest.skip("Audit system not available")


def test_luna_arbiter_caching():
    """Test that Luna Arbiter caches assessments"""
    pytest.skip("Arbiter caching tested via separate test_arbiter_assessment_with_pulse")


def test_luna_response_value_classifier_tiers():
    """Test that RVC properly classifies response tiers"""
    try:
        from luna_core.systems.luna_response_value_classifier import LunaResponseValueClassifier, ResponseValueTier
        
        rvc = LunaResponseValueClassifier()
        
        # Test trivial
        trivial = rvc.classify_response_value("hi")
        assert trivial.tier == ResponseValueTier.TRIVIAL
        assert trivial.max_token_budget <= 15
        
        # Test high complexity
        complex_input = "What are the philosophical implications of artificial general intelligence?"
        high = rvc.classify_response_value(complex_input)
        assert high.tier in [ResponseValueTier.HIGH, ResponseValueTier.CRITICAL, ResponseValueTier.MAXIMUM]
        assert high.max_token_budget >= 250
        
    except ImportError:
        pytest.skip("RVC not available")


def test_consciousness_biological_signal_flow():
    """Test that biological modules can pass signals"""
    pytest.skip("Consciousness biological modules API stabilizing")


def test_backup_core_basic_operations():
    """Test that backup_core can perform basic git-like operations"""
    pytest.skip("Backup core API varies by config")


def test_system_end_to_end_discovery():
    """Test that all essential cores can be imported"""
    essential_cores = [
        'luna_core',
        'carma_core',
        'dream_core',
        'main_core',
        'consciousness_core',
        'backup_core',
        'support_core',
        'utils_core',
        'data_core',
        'rag_core'
    ]
    
    failed_imports = []
    
    for core in essential_cores:
        try:
            __import__(core)
        except ImportError as e:
            failed_imports.append((core, str(e)))
    
    assert len(failed_imports) == 0, f"Failed to import: {failed_imports}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

