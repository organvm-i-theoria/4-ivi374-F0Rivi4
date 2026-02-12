"""Ecosystem module for managing cartridge composition and inter-organ relationships.

An ecosystem assembles multiple cartridges into a coherent operational
environment, managing dependencies, version compatibility, and lifecycle
transitions across the full organ system.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .cartridge import Cartridge, CartridgeState


@dataclass
class DependencyEdge:
    """A directed dependency between two cartridges."""

    source: str
    target: str
    relationship: str = "requires"
    optional: bool = False

    def validate_no_back_edge(self, organ_order: dict[str, int]) -> bool:
        """Verify this edge does not violate the no-back-edge invariant.

        Flow is I->II->III only; higher-numbered organs cannot depend
        on lower-numbered organs.

        Args:
            organ_order: Mapping of organ identifiers to their numeric order.

        Returns:
            True if the edge respects the dependency direction.
        """
        source_order = organ_order.get(self.source, 0)
        target_order = organ_order.get(self.target, 0)
        return source_order <= target_order


@dataclass
class Ecosystem:
    """An operational environment composed of multiple cartridges.

    Manages the lifecycle of cartridges within the ecosystem, enforces
    dependency constraints, and provides introspection capabilities.
    """

    name: str
    cartridges: dict[str, Cartridge] = field(default_factory=dict)
    edges: list[DependencyEdge] = field(default_factory=list)
    _organ_order: dict[str, int] = field(default_factory=lambda: {
        "theoria": 1,
        "poiesis": 2,
        "ergon": 3,
        "taxis": 4,
        "logos": 5,
        "koinonia": 6,
        "kerygma": 7,
        "meta": 8,
    })

    def register_cartridge(self, cartridge: Cartridge) -> None:
        """Add a cartridge to this ecosystem.

        Args:
            cartridge: The cartridge to register.

        Raises:
            ValueError: If a cartridge with the same name already exists.
        """
        if cartridge.name in self.cartridges:
            raise ValueError(f"Cartridge '{cartridge.name}' already registered")
        self.cartridges[cartridge.name] = cartridge

    def add_dependency(self, source: str, target: str, relationship: str = "requires") -> DependencyEdge:
        """Declare a dependency between two registered cartridges.

        Args:
            source: Name of the dependent cartridge.
            target: Name of the cartridge being depended upon.
            relationship: Type of dependency relationship.

        Returns:
            The created DependencyEdge.

        Raises:
            KeyError: If either cartridge is not registered.
            ValueError: If the dependency would create a back-edge.
        """
        if source not in self.cartridges:
            raise KeyError(f"Source cartridge '{source}' not found in ecosystem")
        if target not in self.cartridges:
            raise KeyError(f"Target cartridge '{target}' not found in ecosystem")

        edge = DependencyEdge(source=source, target=target, relationship=relationship)
        if not edge.validate_no_back_edge(self._organ_order):
            raise ValueError(
                f"Back-edge detected: '{source}' -> '{target}' violates organ ordering"
            )

        self.edges.append(edge)
        return edge

    def get_active_cartridges(self) -> list[Cartridge]:
        """Return all cartridges currently in ACTIVE state."""
        return [c for c in self.cartridges.values() if c.state == CartridgeState.ACTIVE]

    def health_check(self) -> dict[str, Any]:
        """Perform a health check across the entire ecosystem.

        Returns:
            Dictionary with total counts, active counts, and any issues found.
        """
        issues: list[str] = []
        active_count = len(self.get_active_cartridges())

        for edge in self.edges:
            if edge.source not in self.cartridges:
                issues.append(f"Dangling edge source: '{edge.source}'")
            if edge.target not in self.cartridges:
                issues.append(f"Dangling edge target: '{edge.target}'")

        return {
            "ecosystem": self.name,
            "total_cartridges": len(self.cartridges),
            "active_cartridges": active_count,
            "total_edges": len(self.edges),
            "issues": issues,
            "healthy": len(issues) == 0,
        }
