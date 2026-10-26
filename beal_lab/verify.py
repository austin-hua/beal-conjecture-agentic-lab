"""Independent verification of bounded-search certificates."""

from __future__ import annotations

import json
from pathlib import Path
from math import gcd


def independently_recompute(max_base: int, max_exponent: int) -> list[dict[str, int]]:
    """Enumerate candidates directly, without the search module or sieves."""
    bases = range(2, max_base + 1)
    results: list[dict[str, int]] = []
    for x in range(3, max_exponent + 1):
        for y in range(3, max_exponent + 1):
            for z in range(3, max_exponent + 1):
                for a in bases:
                    for b in bases:
                        if gcd(a, b) != 1:
                            continue
                        total = a**x + b**y
                        for c in bases:
                            if total != c**z:
                                continue
                            if gcd(a, c) == 1 and gcd(b, c) == 1:
                                results.append(
                                    {"a": a, "x": x, "b": b, "y": y, "c": c, "z": z}
                                )
    return results


def verify_certificate(path: Path) -> None:
    certificate = json.loads(path.read_text(encoding="utf-8"))
    expected = independently_recompute(
        certificate["max_base"], certificate["max_exponent"]
    )
    actual = certificate["solutions"]
    if actual != expected:
        raise ValueError(f"certificate solutions differ: expected {expected}, got {actual}")
    if certificate["primitive_solution_count"] != len(expected):
        raise ValueError("certificate count does not match its solutions")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    verify_certificate(args.certificate)
    print(f"verified {args.certificate}")
