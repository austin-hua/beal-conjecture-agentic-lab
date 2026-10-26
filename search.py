"""Command-line entry point for the bounded Beal search."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from beal_lab import search


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-base", type=int, default=100)
    parser.add_argument("--max-exponent", type=int, default=10)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()

    results = search(args.max_base, args.max_exponent)
    print(
        f"searched bases 2..{args.max_base}, "
        f"exponents 3..{args.max_exponent}"
    )
    if not results:
        print("No primitive solutions found.")
    else:
        for result in results:
            print(
                f"{result.a}^{result.x} + {result.b}^{result.y} "
                f"= {result.c}^{result.z}"
            )

    if args.certificate is not None:
        certificate = {
            "max_base": args.max_base,
            "max_exponent": args.max_exponent,
            "moduli": [3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
            "primitive_solution_count": len(results),
            "solutions": [result.__dict__ for result in results],
        }
        args.certificate.write_text(
            json.dumps(certificate, indent=2) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    main()
