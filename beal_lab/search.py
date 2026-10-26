"""Bounded, exact-arithmetic searches for primitive Beal solutions."""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class Solution:
    """A primitive solution to a^x + b^y = c^z."""

    a: int
    x: int
    b: int
    y: int
    c: int
    z: int

    @property
    def equation_holds(self) -> bool:
        return self.a**self.x + self.b**self.y == self.c**self.z

    @property
    def pairwise_coprime(self) -> bool:
        return (
            gcd(self.a, self.b) == 1
            and gcd(self.a, self.c) == 1
            and gcd(self.b, self.c) == 1
        )


DEFAULT_MODULI = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def search(
    max_base: int = 100,
    max_exponent: int = 10,
    moduli: tuple[int, ...] = DEFAULT_MODULI,
) -> list[Solution]:
    """Return primitive solutions within explicit finite bounds.

    Bases range from 2 through ``max_base`` and exponents range from 3 through
    ``max_exponent``. Python integers are used throughout; no floating-point
    roots or approximate equality are involved.
    """
    if max_base < 2:
        raise ValueError("max_base must be at least 2")
    if max_exponent < 3:
        raise ValueError("max_exponent must be at least 3")

    if any(modulus < 2 for modulus in moduli):
        raise ValueError("moduli must contain integers at least 2")

    bases = range(2, max_base + 1)
    exponents = range(3, max_exponent + 1)
    results: list[Solution] = []

    for x in exponents:
        left = {a: a**x for a in bases}
        for y in exponents:
            right = {b: b**y for b in bases}
            for z in exponents:
                powers = {c**z: c for c in bases}
                residue_targets = {
                    modulus: {pow(c, z, modulus) for c in bases}
                    for modulus in moduli
                }
                for a, a_power in left.items():
                    for b, b_power in right.items():
                        if gcd(a, b) != 1:
                            continue
                        if any(
                            (a_power + b_power) % modulus
                            not in residue_targets[modulus]
                            for modulus in moduli
                        ):
                            continue
                        c = powers.get(a_power + b_power)
                        if c is None:
                            continue
                        candidate = Solution(a, x, b, y, c, z)
                        if candidate.pairwise_coprime:
                            results.append(candidate)
    return results
