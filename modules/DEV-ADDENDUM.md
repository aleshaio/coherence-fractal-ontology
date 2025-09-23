# Developer Addendum: Universality Contract

- See `UNIVERSALITY_AXIOMS` and `UNIVERSAL_DECOMPOSER_PROTOCOL` in JSON.
- Any subsystem consuming this repo MUST:
  1) run reduction on inputs (produce reduction trace),
  2) expose planes and ops used,
  3) attach evidence+confidence,
  4) optionally stitch complex objects via composition graph,
  5) refuse to output if no reduction item exists.

Examples available in `tests.ud.jsonl`.
