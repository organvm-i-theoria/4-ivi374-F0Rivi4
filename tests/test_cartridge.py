"""Tests for the cartridge module."""

from src.cartridge import Axiom, Cartridge, CartridgeState


def test_axiom_validates_with_valid_data():
    """A well-formed axiom should pass validation."""
    axiom = Axiom(identifier="A1", statement="All models are wrong", domain="epistemology")
    assert axiom.validate() is True


def test_axiom_rejects_empty_identifier():
    """An axiom with an empty identifier should fail validation."""
    axiom = Axiom(identifier="", statement="Some statement", domain="test")
    assert axiom.validate() is False


def test_axiom_rejects_invalid_confidence():
    """An axiom with confidence outside [0, 1] should fail validation."""
    axiom = Axiom(identifier="A2", statement="Statement", domain="test", confidence=1.5)
    assert axiom.validate() is False


def test_cartridge_add_axiom_success():
    """Adding a valid axiom to a cartridge should succeed."""
    cart = Cartridge(name="test-cart", version="0.1.0", domain="epistemology")
    axiom = Axiom(identifier="A1", statement="First axiom", domain="epistemology")
    cart.add_axiom(axiom)
    assert len(cart.axioms) == 1
    assert cart.axioms[0].identifier == "A1"


def test_cartridge_rejects_duplicate_axiom():
    """Adding an axiom with a duplicate identifier should raise ValueError."""
    cart = Cartridge(name="test-cart", version="0.1.0", domain="epistemology")
    axiom = Axiom(identifier="A1", statement="First axiom", domain="epistemology")
    cart.add_axiom(axiom)
    try:
        cart.add_axiom(axiom)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Duplicate" in str(e)


def test_cartridge_validate_all_transitions_state():
    """validate_all should transition to VALIDATED when all axioms pass."""
    cart = Cartridge(name="test-cart", version="0.1.0", domain="epistemology")
    cart.add_axiom(Axiom(identifier="A1", statement="Axiom one", domain="epistemology"))
    result = cart.validate_all()
    assert result is True
    assert cart.state == CartridgeState.VALIDATED


def test_cartridge_activate_requires_validated():
    """activate should fail if cartridge is not in VALIDATED state."""
    cart = Cartridge(name="test-cart", version="0.1.0", domain="epistemology")
    cart.add_axiom(Axiom(identifier="A1", statement="Axiom one", domain="epistemology"))
    try:
        cart.activate()
        assert False, "Should have raised RuntimeError"
    except RuntimeError as e:
        assert "VALIDATED" in str(e)


def test_cartridge_export_manifest():
    """export_manifest should return complete metadata dictionary."""
    cart = Cartridge(name="test-cart", version="0.1.0", domain="epistemology")
    cart.add_axiom(Axiom(identifier="A1", statement="Axiom one", domain="epistemology"))
    manifest = cart.export_manifest()
    assert manifest["name"] == "test-cart"
    assert manifest["axiom_count"] == 1
    assert manifest["state"] == "draft"
