"""Command-line entry point for the bounded Beal search."""

from __future__ import annotations

import argparse

from beal_lab import search


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-base", type=int, default=100)
    parser.add_argument("--max-exponent", type=int, default=10)
    args = parser.parse_args()

    results = search(args.max_base, args.max_exponent)
    print(
        f"searched bases 2..{args.max_base}, "
        f"exponents 3..{args.max_exponent}"
    )
    if not results:
        print("No primitive solutions found.")
        return
    for result in results:
        print(
            f"{result.a}^{result.x} + {result.b}^{result.y} "
            f"= {result.c}^{result.z}"
        )


if __name__ == "__main__":
    main()
