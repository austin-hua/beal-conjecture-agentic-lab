"""Measure bounded-search runtime for reproducible local comparisons."""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path

from beal_lab import search


@dataclass(frozen=True)
class Measurement:
    max_base: int
    max_exponent: int
    seconds: float
    primitive_solution_count: int


def measure(max_base: int, max_exponent: int) -> Measurement:
    started = time.perf_counter()
    results = search(max_base, max_exponent)
    return Measurement(
        max_base=max_base,
        max_exponent=max_exponent,
        seconds=time.perf_counter() - started,
        primitive_solution_count=len(results),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-bases", nargs="+", type=int, default=[20, 50, 100, 250])
    parser.add_argument("--max-exponent", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    measurements = [measure(base, args.max_exponent) for base in args.max_bases]
    payload = [asdict(measurement) for measurement in measurements]
    print(json.dumps(payload, indent=2))
    if args.output is not None:
        args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
