"""Governance pillars module for structural integrity validation.

Defines the foundational pillars that support the governance framework.
Each pillar represents a dimension of organizational accountability:
transparency, recursion, and coherence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ComplianceResult:
    """Result of evaluating a governance pillar against a target."""

    pillar_name: str
    target_name: str
    score: float
    passing: bool
    findings: list[str] = field(default_factory=list)

    def summary(self) -> str:
        """Return a human-readable summary of the compliance result."""
        status = "PASS" if self.passing else "FAIL"
        finding_text = "; ".join(self.findings) if self.findings else "No findings"
        return f"[{status}] {self.pillar_name} -> {self.target_name}: {self.score:.2f} ({finding_text})"


@dataclass
class GovernancePillar:
    """A foundational dimension of organizational accountability.

    Pillars define evaluation criteria and thresholds. Any entity
    (cartridge, organ, repo) can be evaluated against a pillar to
    produce a ComplianceResult.
    """

    name: str
    description: str
    threshold: float = 0.7
    criteria: list[str] = field(default_factory=list)
    weight: float = 1.0

    def evaluate(self, target_name: str, evidence: dict[str, Any]) -> ComplianceResult:
        """Evaluate a target entity against this pillar's criteria.

        Args:
            target_name: Human-readable name of the entity being evaluated.
            evidence: Dictionary mapping criterion names to boolean or float scores.

        Returns:
            ComplianceResult with aggregate score and per-criterion findings.
        """
        if not self.criteria:
            return ComplianceResult(
                pillar_name=self.name,
                target_name=target_name,
                score=0.0,
                passing=False,
                findings=["No criteria defined for this pillar"],
            )

        findings: list[str] = []
        met_count = 0

        for criterion in self.criteria:
            value = evidence.get(criterion)
            if value is None:
                findings.append(f"Missing evidence for '{criterion}'")
            elif isinstance(value, bool):
                if value:
                    met_count += 1
                else:
                    findings.append(f"Criterion '{criterion}' not met")
            elif isinstance(value, (int, float)):
                if value >= self.threshold:
                    met_count += 1
                else:
                    findings.append(f"Criterion '{criterion}' below threshold ({value:.2f} < {self.threshold})")
            else:
                findings.append(f"Invalid evidence type for '{criterion}': {type(value).__name__}")

        score = met_count / len(self.criteria) if self.criteria else 0.0
        passing = score >= self.threshold

        return ComplianceResult(
            pillar_name=self.name,
            target_name=target_name,
            score=score,
            passing=passing,
            findings=findings,
        )

    def add_criterion(self, criterion: str) -> None:
        """Add a new evaluation criterion to this pillar.

        Args:
            criterion: Description of the criterion to add.

        Raises:
            ValueError: If the criterion is empty or already exists.
        """
        if not criterion.strip():
            raise ValueError("Criterion cannot be empty")
        if criterion in self.criteria:
            raise ValueError(f"Duplicate criterion: '{criterion}'")
        self.criteria.append(criterion)


class PillarRegistry:
    """Registry that manages the canonical set of governance pillars."""

    def __init__(self) -> None:
        self._pillars: dict[str, GovernancePillar] = {}

    def register(self, pillar: GovernancePillar) -> None:
        """Register a governance pillar.

        Args:
            pillar: The pillar to register.

        Raises:
            ValueError: If a pillar with the same name is already registered.
        """
        if pillar.name in self._pillars:
            raise ValueError(f"Pillar '{pillar.name}' already registered")
        self._pillars[pillar.name] = pillar

    def get(self, name: str) -> GovernancePillar:
        """Retrieve a pillar by name.

        Raises:
            KeyError: If no pillar with the given name exists.
        """
        return self._pillars[name]

    def evaluate_all(self, target_name: str, evidence: dict[str, Any]) -> list[ComplianceResult]:
        """Evaluate a target against all registered pillars.

        Returns:
            List of ComplianceResult objects, one per pillar.
        """
        return [pillar.evaluate(target_name, evidence) for pillar in self._pillars.values()]

    @property
    def pillar_names(self) -> list[str]:
        """Return names of all registered pillars."""
        return list(self._pillars.keys())
