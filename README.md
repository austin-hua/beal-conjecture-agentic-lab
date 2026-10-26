# Beal Conjecture Lab

An open-source attempt to **break—or prove—Beal’s Conjecture** with
reproducible computation, rigorous mathematics, and agentic AI.

> A search is not a proof. A pattern is not a theorem. Every result in this
> repository should be independently checkable.

## The problem

Beal’s Conjecture says that if

\[
a^x+b^y=c^z
\]

for positive integers \(a,b,c\) and exponents \(x,y,z>2\), then \(a,b,c\)
share a common prime factor. Equivalently, a counterexample would be a
pairwise-coprime solution with all three exponents greater than two.

## Project goals

1. **Search for counterexamples.** Build fast, exact, independently validated
   searches over bases and exponent triples.
2. **Make negative results meaningful.** Publish explicit bounds, algorithms,
   hashes, machine details, and certificates for every completed search.
3. **Exploit mathematics before hardware.** Develop modular sieves, local
   obstructions, descent ideas, and reductions between exponent triples.
4. **Use agentic AI responsibly.** Let agents propose conjectures, code,
   optimizations, and proof ideas—but require human-readable reasoning and
   independent verification.
5. **Formalize what we can.** Translate useful lemmas and computational
   certificates into Lean, Isabelle, or another proof assistant where practical.
6. **Study near-misses.** Record close identities and residue patterns that may
   reveal structure even when no counterexample exists.
7. **Welcome serious criticism.** Treat failed approaches, bug reports, and
   adversarial review as first-class contributions.
8. **Produce durable research artifacts.** Keep the code, datasets, methods,
   and conclusions reproducible by people who are not part of this project.

## What counts as a counterexample?

An alleged counterexample must include:

- exact integers satisfying the equation;
- \(x,y,z>2\);
- pairwise coprime bases \(a,b,c\);
- an independently reproduced verification;
- a minimal, reviewable certificate and the code used to generate it.

Floating-point evidence, truncated output, or an unreviewed AI claim is not
enough.

## Research tracks

- `search/` — exact and parallel counterexample searches
- `sieves/` — modular and local filters
- `proof/` — lemmas, reductions, and proof-assistant formalizations
- `certificates/` — independently checkable result files
- `experiments/` — exploratory work, benchmarks, and near-misses
- `docs/` — methods, decisions, and replication instructions

## Contribution principles

Small, reproducible contributions are encouraged. Every pull request should
state what was tested, what bounds were covered, and whether the result is a
proof, a computation, a heuristic, or an experiment.

## Prize-money policy — draft

This project does not own or administer any external prize, and participation
does not by itself create a legal claim to prize money. The official prize
rules and the prize administrator’s decision control eligibility and payment.

Before accepting donations or making a prize claim as a group, contributors
should approve a written agreement. Until then, the project’s default position
is:

1. No one promises, assigns, or transfers prize rights on behalf of anyone
   else.
2. A valid result is credited to the people who made identifiable,
   indispensable contributions, with a public contribution ledger.
3. The team will negotiate a written split before submitting a joint claim,
   using documented contributions rather than commit count, seniority, or
   popularity.
4. Infrastructure, review, formalization, and discovery work are all eligible
   contribution categories.
5. Disputes go to an independent panel agreed upon in advance; unresolved
   legal questions go to qualified counsel.

This is a research-governance draft, not legal advice. A binding agreement
should be reviewed and signed before a prize claim is filed.

## Status

Early stage. No proof or counterexample is claimed here.

## License

To be decided by the founding contributors before accepting substantial code.
