"""Tests for the governance_pillars module."""

from src.governance_pillars import ComplianceResult, GovernancePillar, PillarRegistry


def test_compliance_result_summary_pass():
    """A passing result should format with [PASS] prefix."""
    result = ComplianceResult(
        pillar_name="transparency",
        target_name="repo-x",
        score=0.9,
        passing=True,
        findings=[],
    )
    summary = result.summary()
    assert "[PASS]" in summary
    assert "transparency" in summary


def test_compliance_result_summary_fail():
    """A failing result should format with [FAIL] prefix and include findings."""
    result = ComplianceResult(
        pillar_name="recursion",
        target_name="repo-y",
        score=0.3,
        passing=False,
        findings=["Missing docs"],
    )
    summary = result.summary()
    assert "[FAIL]" in summary
    assert "Missing docs" in summary


def test_pillar_evaluate_all_criteria_met():
    """Pillar evaluation should pass when all criteria have positive evidence."""
    pillar = GovernancePillar(
        name="transparency",
        description="Openness of process",
        threshold=0.7,
        criteria=["has_readme", "has_license", "has_changelog"],
    )
    evidence = {"has_readme": True, "has_license": True, "has_changelog": True}
    result = pillar.evaluate("test-repo", evidence)
    assert result.passing is True
    assert result.score == 1.0


def test_pillar_evaluate_below_threshold():
    """Pillar evaluation should fail when score is below threshold."""
    pillar = GovernancePillar(
        name="coherence",
        description="Internal consistency",
        threshold=0.7,
        criteria=["tests_pass", "lint_clean", "docs_current"],
    )
    evidence = {"tests_pass": True, "lint_clean": False, "docs_current": False}
    result = pillar.evaluate("test-repo", evidence)
    assert result.passing is False
    assert len(result.findings) == 2


def test_pillar_add_criterion_rejects_empty():
    """Adding an empty criterion should raise ValueError."""
    pillar = GovernancePillar(name="test", description="test")
    try:
        pillar.add_criterion("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_registry_evaluate_all():
    """Registry should evaluate a target against all registered pillars."""
    registry = PillarRegistry()
    p1 = GovernancePillar(name="alpha", description="First", criteria=["c1"])
    p2 = GovernancePillar(name="beta", description="Second", criteria=["c2"])
    registry.register(p1)
    registry.register(p2)
    results = registry.evaluate_all("target", {"c1": True, "c2": False})
    assert len(results) == 2
    assert results[0].passing is True
    assert results[1].passing is False


def test_registry_rejects_duplicate_pillar():
    """Registering a pillar with duplicate name should raise ValueError."""
    registry = PillarRegistry()
    p1 = GovernancePillar(name="alpha", description="First")
    registry.register(p1)
    try:
        registry.register(p1)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
