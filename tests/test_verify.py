from pathlib import Path

from beal_lab.verify import independently_recompute, verify_certificate


def test_independent_recompute_matches_baseline() -> None:
    assert independently_recompute(20, 5) == []


def test_baseline_certificate_verifies() -> None:
    verify_certificate(Path("certificates/baseline-20-5.json"))
