# Retention Deck

Spaced-retrieval card deck. Maintained by Claude; retrieval done by Rudra, cold, no notes.
Intervals: new → 1d → 3d → 7d → 21d → graduated. Miss = reset to 1d.
Graduation = two consecutive cold passes, one of them ELI5.
**Every session opens with the due cards. Non-negotiable.**

Format per card: `[interval | due date | streak]`

---

## OVERDUE — never retried, do these FIRST next session

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

## Passed cold today (2026-07-08) — interval advanced to 3d

**C01** `[3d | 2026-07-11 | 1]`
Q: `funcs = [lambda: i for i in range(3)]` — what does calling each print, why, fix?
A: `[2, 2, 2]`. Closures capture the *variable*, not the value; all lambdas share `i`,
which is 2 after the loop. Fix: `lambda i=i: i` (default arg snapshots at def time).

**C03** `[3d | 2026-07-11 | 1]`
Q: Inner function does `count += 1` on enclosing var without `nonlocal` — what happens, why?
A: UnboundLocalError. Assignment anywhere in a function makes the name local at COMPILE
time, shadowing the closure variable. `nonlocal count` binds to enclosing scope. Pure
reads don't need it — only rebinding does.

---

## FAILED again today (2026-07-08) — 2ND CONSECUTIVE MISS, flagged as a real weak spot

**C02** `[1d | 2026-07-09 | 0]`
Q: Decorator prints A in deco body, B in wrapper, C in fn. Two calls after `@deco` — output?
A: A B C B C. Decoration runs once at def time (A). The name permanently points to
wrapper — EVERY call runs wrapper (B) then the original fn (C).
⚠️ Missed 2026-07-04 AND 2026-07-08. Re-taught in full both times. If missed a 3rd time,
stop and rebuild the explanation from the def-time/call-time model line by line with Rudra
writing it, not reading it.

---

## New cards from today's deep session (2026-07-08) — first due 2026-07-09

**N17** `[1d | 2026-07-09 | 0]`
Q: `y = x` then later `x = 10` — does `y` change? Explain with the box/sticky-note model.
A: No. `x = 10` doesn't touch the box `x` was pointing at — it moves `x`'s sticky note to
a brand-new box containing `10`. `y`'s sticky note never moved, still on the old box.

**N18** `[1d | 2026-07-09 | 0]`
Q: `x = [1,2]; y = x; x.append(3); print(y)` vs `a = "hi"; b = a; a = a + " there"; print(b)`
— outputs, and the one-line rule?
A: `[1,2,3]` (mutable — append reaches into the SAME box) vs `"hi"` (immutable — `+` always
builds a new box). Rule: mutation changes the existing box; rebinding moves to a new one.

**N19** `[1d | 2026-07-09 | 0]`
Q: State the LEGB lookup order and what `global` does differently from `nonlocal`.
A: Local → Enclosing → Global → Built-in, first match wins. `nonlocal` targets the nearest
Enclosing notepad; `global` targets the Global (module-level) notepad from inside any
function, same mechanism, different target layer.

**N20** `[1d | 2026-07-09 | 0]`
Q: Why is `x is None` preferred over `x == None`, and why can `a is b` for `a=5,b=5` be
True but misleading?
A: There's exactly one `None` object ever — `is` is correct and faster. Small ints/short
strings are cached by CPython (implementation detail) so `is` can accidentally "work" on
them, then silently break on larger values — always use `==` for value comparison.

**N21** `[1d | 2026-07-09 | 0]`
Q: What does a `with` block guarantee that manual `open()`/`close()` doesn't?
A: `__exit__` runs no matter how the block ends — clean finish OR exception. Manual
`f.close()` after `f.read()` never runs if `read()` crashes — resource leaks.

**N22** `[1d | 2026-07-09 | 0]`
Q: `__exit__` returns `True` vs returns nothing (`None`) when an exception occurred inside
the `with` block — what's the difference, and does code AFTER the `raise` line (still
inside the block) ever run either way?
A: `True` suppresses the exception (with-statement exits normally); `None`/`False` lets it
keep propagating outward. Either way, code after `raise` inside the block NEVER runs —
`raise` jumps out immediately and permanently, suppression is decided only at the
with-block boundary, it does not rewind execution.

**N23** `[1d | 2026-07-09 | 0]`
Q: In a `@contextmanager` generator, why must the `yield` be wrapped in `try/finally` to
guarantee cleanup on exception, and is a crash without that finally "silent"?
A: An exception in the with-block gets thrown INTO the generator at the yield point. No
try/finally = nothing catches it there = cleanup code after yield never runs. The crash
itself is LOUD (full traceback) — only the cleanup silently gets skipped, which is the
actually dangerous part (e.g. a leaked DB connection riding along with a loud crash).

**N24** `[1d | 2026-07-09 | 0]`
Q: `with A(), B(): body` — order of enter/exit calls?
A: enter A → enter B → body runs once (not incrementally) → exit B → exit A. Enters in
written order, exits in reverse (LIFO) — same idea as nested nesting, innermost closes first.

**N25** `[1d | 2026-07-09 | 0]`
Q: `except Exception as e: print(...); raise` (bare raise, no argument) — does this
suppress the exception?
A: No — bare `raise` re-throws the SAME exception. This is "log/rollback on the way out,
still crash" — common production pattern (e.g. transaction rollback + re-raise), not
exception handling that hides the error.

**N26** `[1d | 2026-07-09 | 0]`
Q: `t = timer()` (a `@contextmanager` object) used in two separate `with t:` blocks —
does the second one work?
A: No — crashes with `RuntimeError: generator didn't yield`. `@contextmanager` is built on
ONE generator per call; the first `with` runs it to completion (exhausted, like any
generator). Reusing the same instance tries to pull from an already-finished generator.
Fix: call `timer()` fresh each time, don't reuse the same instance.

**N27** `[1d | 2026-07-09 | 0]`
Q: `@multiply_by(2)` then `@multiply_by(3)` stacked above one function — which applies
first?
A: Closest to the function applies first (bottom-up) — `multiply_by(3)` wraps the
original function, then `multiply_by(2)` wraps THAT. Common interview trap: people assume
top-to-bottom reading order = application order; it's the reverse.

**N28** `[1d | 2026-07-09 | 0]`
Q: `@retry(times=3)` above a function — what actually gets called first, and when does the
real "decorator" get created?
A: `retry(times=3)` is evaluated FIRST as a plain function call — it returns the real
decorator (a closure remembering `times=3`). THAT returned function is then called with
the target function, same as any plain decorator. Two rounds of closures chain together.

**N29** `[1d | 2026-07-09 | 0]`
Q: A closure does `store[n] = fn(n)` on an enclosing-scope dict — no `nonlocal` needed.
Why, precisely (not just "mutable")?
A: The local-detection rule only fires on bare NAME reassignment (`store = ...`).
`store[n] = ...` never rebinds the name `store` — it reads store then calls
`store.__setitem__`. If it were `store = {...}` instead, THAT would need `nonlocal`
regardless of dict being mutable — the rule is about the assignment pattern, not the type.

**N30** `[1d | 2026-07-09 | 0]`
Q: `x = yield 1` then later `g.send(10)` — what does send() actually do that next() doesn't?
A: Both resume the paused generator, but `send(value)` also supplies the RESULT of the
paused `yield` expression — completing `x = 10`. Plain `next()` is equivalent to
`send(None)`. The assignment in `x = yield 1` happens in two moments: yield fires and
pauses (nothing assigned yet), THEN whatever resumes it delivers the value that `x` becomes.

---

## Graduated
(none yet)
