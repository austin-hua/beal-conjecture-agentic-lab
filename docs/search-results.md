# Search results

This file records completed searches, not conjectural claims.

## Baseline

- **Code:** `beal_lab.search`
- **Arithmetic:** exact Python integers
- **Filter:** residues modulo 3, 5, 7, 11, 13, 17, 19, 23, 29, and 31
- **Bases:** 2 through 20
- **Exponents:** 3 through 5
- **Result:** no primitive solutions found
- **Validation:** `tests/test_search.py`

This is a finite computational result. It is not a proof of Beal's
Conjecture and does not exclude solutions outside these bounds.

Search runs can emit a JSON certificate with:

```text
python search.py --max-base 20 --max-exponent 5 --certificate result.json
```

The certificate records the bounds, moduli, result count, and any exact
solutions found.
