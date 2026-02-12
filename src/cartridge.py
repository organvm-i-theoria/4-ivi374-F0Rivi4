"""Cartridge module for pluggable epistemological units.

A cartridge encapsulates a self-contained knowledge domain with its own
axioms, inference rules, and validation criteria. Cartridges can be
composed, versioned, and hot-swapped within the governance framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class CartridgeState(Enum):
    """Lifecycle states for a cartridge."""

    DRAFT = "draft"
    VALIDATED = "validated"
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ARCHIVED = "archived"


@dataclass
class Axiom:
    """A foundational assertion within a cartridge's knowledge domain."""

    identifier: str
    statement: str
    domain: str
    confidence: float = 1.0

    def validate(self) -> bool:
        """Check that the axiom meets structural requirements."""
        if not self.identifier or not self.statement:
            return False
        if not 0.0 <= self.confidence <= 1.0:
            return False
        return True


@dataclass
class Cartridge:
    """A pluggable epistemological unit containing axioms and inference rules.

    Cartridges are the fundamental building blocks of the governance framework.
    Each cartridge encapsulates a coherent knowledge domain that can be composed
    with other cartridges to form larger epistemological structures.
    """

    name: str
    version: str
    domain: str
    axioms: list[Axiom] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    state: CartridgeState = CartridgeState.DRAFT

    def add_axiom(self, axiom: Axiom) -> None:
        """Register a new axiom within this cartridge.

        Args:
            axiom: The axiom to add. Must pass structural validation.

        Raises:
            ValueError: If the axiom fails validation or has a duplicate identifier.
        """
        if not axiom.validate():
            raise ValueError(f"Axiom '{axiom.identifier}' failed structural validation")
        if any(a.identifier == axiom.identifier for a in self.axioms):
            raise ValueError(f"Duplicate axiom identifier: '{axiom.identifier}'")
        self.axioms.append(axiom)

    def activate(self) -> None:
        """Transition the cartridge to ACTIVE state.

        Requires at least one validated axiom and VALIDATED current state.

        Raises:
            RuntimeError: If preconditions for activation are not met.
        """
        if self.state != CartridgeState.VALIDATED:
            raise RuntimeError(
                f"Cannot activate cartridge in state '{self.state.value}'; "
                "must be VALIDATED first"
            )
        if not self.axioms:
            raise RuntimeError("Cannot activate cartridge with no axioms")
        self.state = CartridgeState.ACTIVE

    def validate_all(self) -> bool:
        """Validate all axioms and transition to VALIDATED if all pass.

        Returns:
            True if all axioms are valid and state transitioned successfully.
        """
        if not self.axioms:
            return False
        if all(axiom.validate() for axiom in self.axioms):
            self.state = CartridgeState.VALIDATED
            return True
        return False

    def export_manifest(self) -> dict[str, Any]:
        """Export a machine-readable manifest of this cartridge.

        Returns:
            Dictionary containing cartridge metadata, axiom count, and state.
        """
        return {
            "name": self.name,
            "version": self.version,
            "domain": self.domain,
            "axiom_count": len(self.axioms),
            "state": self.state.value,
            "metadata": self.metadata,
        }
