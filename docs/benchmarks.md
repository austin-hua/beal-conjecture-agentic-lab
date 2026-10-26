# Benchmarks

These timings measure the current single-process search with the default
moduli. They are hardware- and interpreter-dependent; they are useful for
comparing commits, not for comparing machines.

## Baseline environment

- Python 3.14.5
- Windows
- Default modular sieve
- Exponents 3 through 5

## Initial measurements

Generated with:

```text
python -m benchmarks.benchmark --max-bases 20 50 100 250 --max-exponent 5
```

| Maximum base | Maximum exponent | Result count | Runtime |
|---:|---:|---:|---:|
| 20 | 5 | 0 | 0.0044 s |
| 50 | 5 | 0 | 0.0241 s |
| 100 | 5 | 0 | 0.0989 s |
| 250 | 5 | 0 | 0.6409 s |

The measurements show roughly quadratic growth in the base bound, confirming
that candidate/filter counters and parallelization are the next performance
targets.
