# Retention Deck

Spaced-retrieval card deck. Maintained by Claude; retrieval done by Rudra, cold, no notes.
Intervals: new → 1d → 3d → 7d → 21d → graduated. Miss = reset to 1d.
Graduation = two consecutive cold passes, one of them ELI5.
**Every session opens with the due cards. Non-negotiable.**

Format per card: `[interval | due date | streak]`

---

## Due 2026-07-05 (misses from 2026-07-04 quiz — interval 1d, streak 0)

**C01** `[1d | 2026-07-05 | 0]`
Q: `funcs = [lambda: i for i in range(3)]` — what does calling each print, why, fix?
A: `[2, 2, 2]`. Closures capture the *variable*, not the value; all lambdas share `i`,
which is 2 after the loop. Fix: `lambda i=i: i` (default arg snapshots at def time).

**C02** `[1d | 2026-07-05 | 0]`
Q: Decorator prints A in deco body, B in wrapper, C in fn. Two calls after `@deco` — output?
A: A B C B C. Decoration runs once at def time (A). The name permanently points to
wrapper — EVERY call runs wrapper (B) then the original fn (C).

**C03** `[1d | 2026-07-05 | 0]`
Q: Inner function does `count += 1` on enclosing var without `nonlocal` — what happens, why?
A: UnboundLocalError. Assignment anywhere in a function makes the name local at COMPILE
time, shadowing the closure variable. `nonlocal count` binds to enclosing scope. Pure
reads don't need it — only rebinding does.

**C04** `[1d | 2026-07-05 | 0]`
Q: Decorated function's `__name__` prints what, why, fix?
A: `wrapper` — the name IS the wrapper after decoration; metadata (name, docstring) is
wrapper's. Fix: `@functools.wraps(fn)` on the wrapper. Matters for tracebacks, FastAPI
route names, any introspection.

**C05** `[1d | 2026-07-05 | 0]`
Q: Two 2s fetches: (a) `await a(); await b()` vs (b) `create_task` both then await both.
Times?
A: (a) 4s — bare await starts AND finishes one coroutine before the next exists.
(b) 2s — create_task starts work immediately; awaits just collect. THE RULE: concurrency
is decided by WHEN WORK STARTS, not by the word await. gather/create_task start early.

**C06** `[1d | 2026-07-05 | 0]`
Q: 10 Python threads downloading 10 files (~3s each) — faster than serial despite GIL? Why?
A: Yes, ~3s total vs 30s. Threads release the GIL during blocking I/O. GIL blocks parallel
COMPUTING, not parallel WAITING. Threads: useless for CPU, fine for I/O; async scales
further for thousands of connections.

**C07** `[1d | 2026-07-05 | 0]`
Q: `g = gen()` yielding 1, 2. `print(sum(g)); print(sum(g))` — output?
A: 3 then 0. Generators are single-use; once exhausted they're silently empty (no error).
Classic silent bug: two consumers of one generator — second gets nothing.

**C08** `[1d | 2026-07-05 | 0]`
Q: Judge scores outputs by similarity to one golden `expected` answer; a better differently-
worded answer scores 0.4. Flaw? Fix?
A: Reference-based eval on an open-ended task — punishes valid variation. Switch to
rubric-based judging: binary criteria checks ("contains refund window? y/n"). Reference-
based only when exactly one correct answer exists.

**C09** `[1d | 2026-07-05 | 0]`
Q: Why must an LLM judge be (a) not weaker than the generator and (b) ideally a different
family?
A: (a) A weaker judge approves what it can't understand — eval reads healthy while quality
drops. (b) Same-family judges have self-preference bias toward sibling outputs.

**C10** `[1d | 2026-07-05 | 0]`
Q: Agent makes 6 auto-instrumented calls; dashboard shows 6 separate trace_ids. Missing
piece + mechanism?
A: A root span around the agent run (`start_as_current_span("agent_run")`). OTel tracks
the current span in context; auto-instrumented spans attach as children of whatever is
active, inheriting its trace_id. No active span → every call starts its own trace.

---

## Due 2026-07-07 (passes from 2026-07-04 quiz — interval 3d, streak 1)

**C11** `[3d | 2026-07-07 | 1]`
Q: `def add(item, box=[])` — why does the list persist across calls?
A: Default args evaluate ONCE at def time; all calls share that one list. Fix: `box=None`,
create inside.

**C12** `[3d | 2026-07-07 | 1]`
Q: `b = a; b += [3]` — why does `a` change? What if it were `b = b + [3]`?
A: `b = a` copies the reference (aliasing); `+=` on a list mutates in place (`__iadd__`).
`b = b + [3]` builds a NEW list and rebinds b — a unchanged.

**C13** `[3d | 2026-07-07 | 1]`
Q: `g = gen(); print("created")` — has any of the generator body run?
A: No — zero lines, not even the first print. Body runs lazily on first next(), pausing
at each yield.

**C14** `[3d | 2026-07-07 | 1]`
Q: 2s CPU-bound call inside `async def` endpoint — what breaks, fix?
A: Freezes the single-threaded event loop — ALL concurrent requests stall. Fix:
`await loop.run_in_executor(process_pool, fn, arg)` — processes because GIL blocks
CPU parallelism in threads.

**C15** `[3d | 2026-07-07 | 1]`
Q: OTel LLM span — why token counts in attributes but prompt text in events?
A: Attributes are small indexed key-values you FILTER by across traces; oversized values
get truncated/dropped. Events are timestamped payloads you READ on one trace.

**C16** `[3d | 2026-07-07 | 1]`
Q: Redis lookup taking 12ms instead of ~0.5ms — top 3 causes?
A: (1) No connection pooling — TCP handshake per call. (2) Slow O(n) command (KEYS *,
big SMEMBERS) blocking the single-threaded event loop. (3) Cross-region Redis (~100ms RTT).

---

## Graduated
(none yet)
