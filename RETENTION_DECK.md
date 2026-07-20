# Retention Deck

Spaced-retrieval card deck. Maintained by Claude; retrieval done by Rudra, cold, no notes.
Intervals: new → 1d → 3d → 7d → 21d → graduated. Miss = reset to 1d.
Graduation = two consecutive cold passes, one of them ELI5.
**Every session opens with the due cards. Non-negotiable.**

Format per card: `[interval | due date | streak]`

**Scoping rule (added 2026-07-09, Rudra's correction):** only run cards for material
actually re-taught in the CURRENT pass of the curriculum. Cards from weeks/phases not
yet reached in the restructured plan (concurrency = Week 3, evals/observability =
Phase 2, Redis = Week 6) stay parked below, untouched, until we actually get there.

**Delivery format rule (added 2026-07-10, Rudra's instruction):** the stored Q/A per card
below is the CONCEPT DEFINITION — what's being tested and the correct answer — not the
literal script to read aloud. When actually delivering a due card in a session, generate
a fresh **FITB (fill-in-the-blank) or MCQ** variant testing the same underlying concept,
with **varied wording/scenario each time it comes up** — never the same static phrasing
twice in a row. Open-ended short-answer questions (the old format) are retired. Reasoning:
static repeated phrasing risks pattern-matching on a remembered question instead of
genuinely re-deriving the concept — directly the same recognition-vs-application concern
flagged at `W37`. Dynamic FITB/MCQ forces fresh recall every time.

**Recency scoping rule (added 2026-07-15, Rudra's instruction):** day-to-day quiz
sessions surface cards from only the MOST RECENTLY taught session/week, not the full
cumulative backlog. Older cards remain in the deck as a historical record and stay
technically "due" per their own schedule, but aren't actively surfaced unless Rudra
explicitly asks for a full backlog run. **Known tradeoff, flagged and accepted:** this
breaks the core premise of spaced repetition (resurfacing old material before it fades)
— Week 1–3 content will not get reinforced under this rule and should be expected to
decay. If retention on older weeks turns out to matter later (e.g. before Phase 1 gate
or a mock interview), a full backlog run should be explicitly requested.

---

## PARKED — future-phase content, not yet re-taught, do not test until that week arrives

**C08** `[1d | 2026-07-05 | 0]` (Phase 2 — evals)
Q: Judge scores outputs by similarity to one golden `expected` answer; a better differently-
worded answer scores 0.4. Flaw? Fix?
A: Reference-based eval on an open-ended task — punishes valid variation. Switch to
rubric-based judging: binary criteria checks ("contains refund window? y/n"). Reference-
based only when exactly one correct answer exists.

**C09** `[1d | 2026-07-05 | 0]` (Phase 2 — evals)
Q: Why must an LLM judge be (a) not weaker than the generator and (b) ideally a different
family?
A: (a) A weaker judge approves what it can't understand — eval reads healthy while quality
drops. (b) Same-family judges have self-preference bias toward sibling outputs.

**C10** `[1d | 2026-07-05 | 0]` (Phase 2 — observability)
Q: Agent makes 6 auto-instrumented calls; dashboard shows 6 separate trace_ids. Missing
piece + mechanism?
A: A root span around the agent run (`start_as_current_span("agent_run")`). OTel tracks
the current span in context; auto-instrumented spans attach as children of whatever is
active, inheriting its trace_id. No active span → every call starts its own trace.

**C15** `[3d | 2026-07-07 | 1]` (Phase 2 — observability)
Q: OTel LLM span — why token counts in attributes but prompt text in events?
A: Attributes are small indexed key-values you FILTER by across traces; oversized values
get truncated/dropped. Events are timestamped payloads you READ on one trace.

**C16** `[3d | 2026-07-07 | 1]` (Week 6 — Redis)
Q: Redis lookup taking 12ms instead of ~0.5ms — top 3 causes?
A: (1) No connection pooling — TCP handshake per call. (2) Slow O(n) command (KEYS *,
big SMEMBERS) blocking the single-threaded event loop. (3) Cross-region Redis (~100ms RTT).

---

## Passed cold 2026-07-09 — second consecutive pass, advanced to 7d (still need one ELI5 pass to graduate)

**C11** `[7d | 2026-07-16 | 2]`
Q: `def add(item, box=[])` — why does the list persist across calls?
A: Default args evaluate ONCE at def time; all calls share that one list. Fix: `box=None`,
create inside.

**C12** `[7d | 2026-07-16 | 2]`
Q: `b = a; b += [3]` — why does `a` change? What if it were `b = b + [3]`?
A: `b = a` copies the reference (aliasing); `+=` on a list mutates in place (`__iadd__`).
`b = b + [3]` builds a NEW list and rebinds b — a unchanged.

**C13** `[7d | 2026-07-16 | 2]`
Q: `g = gen(); print("created")` — has any of the generator body run?
A: No — zero lines, not even the first print. Body runs lazily on first next(), pausing
at each yield.

---

## Passed cold 2026-07-09 — first pass, advanced to 3d

**C01** `[3d | 2026-07-11 | 1]`
Q: `funcs = [lambda: i for i in range(3)]` — what does calling each print, why, fix?
A: `[2, 2, 2]`. Closures capture the *variable*, not the value; all lambdas share `i`,
which is 2 after the loop. Fix: `lambda i=i: i` (default arg snapshots at def time).

**C03** `[3d | 2026-07-11 | 1]`
Q: Inner function does `count += 1` on enclosing var without `nonlocal` — what happens, why?
A: UnboundLocalError. Assignment anywhere in a function makes the name local at COMPILE
time, shadowing the closure variable. `nonlocal count` binds to enclosing scope. Pure
reads don't need it — only rebinding does.

**C04** `[3d | 2026-07-12 | 1]`
Q: Decorated function's `__name__` prints what, why, fix?
A: `wrapper` — the name IS the wrapper after decoration; metadata (name, docstring) is
wrapper's. Fix: `@functools.wraps(fn)` on the wrapper (note: "wraps" WITH an s). Matters
for tracebacks, FastAPI route names, any introspection.

**C07** `[3d | 2026-07-12 | 1]`
Q: `g = gen()` yielding 1, 2. `print(sum(g)); print(sum(g))` — output?
A: 3 then 0. Generators are single-use; once exhausted they're silently empty (no error).
Classic silent bug: two consumers of one generator — second gets nothing.

**C02** `[3d | 2026-07-12 | 1]` — ⚠️ history: missed 2026-07-04 AND 2026-07-08, PASSED CLEAN
2026-07-09 on the third attempt. Weak spot genuinely closed, not just memorized — verify
this stays solid on the 07-12 retry before fully trusting it.
Q: Decorator prints A in deco body, B in wrapper, C in fn. Two calls after `@deco` — output?
A: A B C B C. Decoration runs once at def time (A). The name permanently points to
wrapper — EVERY call runs wrapper (B) then the original fn (C).

**N18** `[3d | 2026-07-12 | 1]`
Q: `x=[1,2]; y=x; x.append(3); print(y)` vs `a="hi"; b=a; a=a+" there"; print(b)` — outputs
+ the rule?
A: `[1,2,3]` (mutable — append reaches into the SAME box) vs `"hi"` (immutable — `+` always
builds a new box). Rule: `.append()` mutates the existing box; `a + "..."` always rebinds
to a new one.

**N20** `[3d | 2026-07-12 | 1]`
Q: Why is `x is None` preferred over `x == None`, and why can `a is b` for `a=5,b=5` be
True but misleading?
A: There's exactly one `None` object ever — `is` is correct and faster. Small ints/short
strings are cached by CPython (implementation detail) so `is` can accidentally "work" on
them, then silently break on larger values — always use `==` for value comparison.

**N21** `[3d | 2026-07-12 | 1]`
Q: What does a `with` block guarantee that manual `open()`/`close()` doesn't?
A: `__exit__` runs no matter how the block ends — clean finish OR exception. Manual
`f.close()` after `f.read()` never runs if `read()` crashes — resource leaks.

**N22** `[3d | 2026-07-12 | 1]`
Q: `__exit__` returns `True` vs `None` when an exception occurred — difference? Does code
after `raise` (still inside the block) ever run either way?
A: `True` suppresses the exception; `None`/`False` lets it propagate. Either way, code
after `raise` inside the block NEVER runs — `raise` jumps out immediately and permanently;
suppression is decided only at the with-block boundary, it doesn't rewind execution.

**N24** `[3d | 2026-07-12 | 1]`
Q: `with A(), B(): body` — order of enter/exit calls?
A: enter A → enter B → body runs once → exit B → exit A. Enters in written order, exits
in reverse (LIFO) — innermost closes first.

**N25** `[3d | 2026-07-12 | 1]` (card rewritten 07-09 with concrete example — original
phrasing was too abstract, Rudra correctly flagged "didn't understand the q")
Q: `try: risky() / except Exception as e: print(...); raise` — does the bare `raise`
suppress the exception? Does code after the whole try/except block run?
A: No — bare `raise` RE-THROWS the same exception, doesn't suppress it. This is the
"log/rollback on the way out, still crash" pattern. Nothing after the block runs unless
something further up catches it.

**N27** `[3d | 2026-07-12 | 1]`
Q: `@multiply_by(2)` then `@multiply_by(3)` stacked — which applies to the function first?
A: Closest to the function applies first (bottom-up). Common trap: people assume
top-to-bottom reading order = application order; it's the reverse.

**N28** `[3d | 2026-07-12 | 1]`
Q: `@retry(times=3)` above a function — what gets called first, before the target function
is touched at all?
A: `retry(times=3)` fires FIRST as a plain function call, returns the real decorator (a
closure remembering `times=3`). THAT returned function is then called with the target
function — same as any plain decorator, one extra round of closures.

**N29** `[3d | 2026-07-12 | 1]`
Q: A closure does `store[n] = fn(n)` on an enclosing dict — no `nonlocal` needed. Why,
precisely (not just "mutable")?
A: The local-detection rule only fires on bare NAME reassignment (`store = ...`).
`store[n] = ...` never rebinds the name — it reads `store` then calls
`store.__setitem__`. No reassignment of the name = no local created = nothing for
`nonlocal` to fix.

---

## MISSED 2026-07-09 — needed real correction, stay at 1d, retry tomorrow

**N17** `[1d | 2026-07-10 | 0]`
Q: `y = x` then later `x = 10` — does `y` change? How many boxes exist right after
`y = x` runs (before `x = 10`)?
A: `y` unaffected. Exactly ONE box exists after `y = x` — it does NOT create a new box
copying x's value; it just adds a second sticky note onto the SAME box `x` already
points to. (First-attempt miss: said "creates a box... puts the value of x in it" —
that's describing a copy, which is wrong. Corrected to "1 box, 2 notes.")

**N19** `[1d | 2026-07-10 | 0]`
Q: State the LEGB order. What does `nonlocal` target vs what does `global` target —
precisely, no overlap?
A: Local → Enclosing → Global → Built-in. `nonlocal` targets ONLY the nearest Enclosing
scope — if not found there, SyntaxError, it never falls through to Global. `global`
targets ONLY the module-level Global scope, unrelated to how many enclosing functions
exist. Non-overlapping, not interchangeable. (First-attempt miss: said nonlocal could mean
"either enclosing or global" — false, it's enclosing-only.)

**N23** `[1d | 2026-07-10 | 0]` — ⚠️ biggest miss of the session, needed full re-teach
Q: In `@contextmanager`, why must `yield` be wrapped in `try/finally` for cleanup to run
on exception? Is the resulting crash "silent"?
A: The exception from the with-block gets thrown INTO the generator AT the yield point.
No try/finally = nothing catches it there = cleanup after yield never runs. The CRASH
itself is loud (full traceback) — only the cleanup silently gets skipped, which is the
actually dangerous part (e.g. a DB connection leak: original crash is loud and gets
logged/forgotten, connection never released, pool exhausts weeks later with a totally
different, seemingly-unrelated error). (First attempt confused this with the unrelated
`@retry` decorator example and answer had no real mechanism; second attempt on the
DB-connection follow-up incorrectly brought in ACID instead of identifying the resource
leak. Needs a clean retry before trusting this is solid.)

**N26** `[1d | 2026-07-10 | 0]`
Q: `t = timer()` (a `@contextmanager` object), reused in two separate `with t:` blocks —
does the second one work? What specifically is exhausted, and is the error compile-time
or runtime?
A: No — crashes with `RuntimeError: generator didn't yield`. It's the GENERATOR living
inside `t` that's exhausted (not `t` itself, which is still a valid object) — same
single-use mechanism as `sum(g)` returning 0 on a second call. This is a RUNTIME error —
`__enter__` calls `next()` on the exhausted generator live, during execution; there is no
separate compile-time check for this. (Two rounds of imprecision before landing: "null"
instead of "exhausted," then "thrown by the compiler" instead of "runtime.")

**N30** `[1d | 2026-07-10 | 0]`
Q: `x = yield 1` then `g.send(10)` (generator already paused at `yield 1` from a prior
`next(g)`) — what does that ONE `send(10)` call do, start to finish?
A: `send(10)` resumes the generator, completes `x = 10`, and then KEEPS RUNNING without
pausing again until it hits the next `yield` — so the `print(f"received: {x}")` line
fires immediately as a side effect WITHIN that same call, and `send(10)` itself RETURNS
`20` (from `yield x*2`). No further calls needed to reach the print or the 20 — both
happen inside that one `send()`. (Miss: treated print and reaching the second yield as
requiring separate additional calls, when they all happen within the single `send(10)`.)

---

## Passed cold 2026-07-09 (same session, new card) — first pass, advanced to 3d

**N31** `[3d | 2026-07-12 | 1]`
Q: `g = (x for x in range(3)); print(list(g)); print(list(g))` — both outputs, and why?
A: `[0, 1, 2]` then `[]`. Generator expressions ARE generators (just `()` syntax instead
of a full `def`/`yield` function) — same single-use exhaustion as C07/N26. First `list(g)`
consumes it fully; second call has nothing left.

---

## Week 3 (concurrency) — taught + tested 2026-07-09. C05/C06/C14 un-parked, passed via
## repeated correct application during the quiz — advanced to 3d.

**C05** `[3d | 2026-07-12 | 1]`
Q: Two 2s fetches: (a) `await a(); await b()` vs (b) `create_task` both then await both.
Times?
A: (a) 4s — bare await starts AND finishes one coroutine before the next exists.
(b) 2s — create_task starts work immediately; awaits just collect. Concurrency exists
only between things STARTED before either is awaited — not just "using async."

**C06** `[3d | 2026-07-12 | 1]`
Q: 10 Python threads downloading 10 files (~3s each) — faster than serial despite GIL? Why?
A: Yes, ~3s total vs 30s. Threads release the GIL specifically during blocking I/O waits.
GIL blocks parallel COMPUTING, never parallel WAITING.

**C14** `[3d | 2026-07-12 | 1]`
Q: 2s CPU-bound call inside `async def` endpoint — what breaks, fix?
A: Freezes the single-threaded event loop — ALL concurrent requests stall, including
unrelated ones, because the loop only switches tasks at `await` points (cooperative, not
forced) and a blocking call never offers one. Fix: `run_in_executor` with a
ProcessPoolExecutor.

**W32** `[1d | 2026-07-10 | 0]`
Q: Why can't a busy CPU with multiple threads just get "forced" to switch to another
runnable thread the way the OS does with real threads?
A: `asyncio`'s event loop uses COOPERATIVE scheduling, not preemptive — it only switches
at `await` points, voluntarily offered by the running code. It never forcibly interrupts
a coroutine mid-execution. No `await` anywhere = no opportunity to switch, no matter how
"free" the CPU technically is.

**W33** `[1d | 2026-07-10 | 0]`
Q: Offloading CPU work from an async handler: ThreadPoolExecutor vs ProcessPoolExecutor —
what specifically does each one fix, and what does thread pool NOT fix?
A: Both keep the EVENT LOOP itself responsive (neither blocks the loop's own thread).
ThreadPoolExecutor does NOT give real parallelism among the offloaded CPU tasks
themselves — they still serialize via the GIL. ProcessPoolExecutor gives both:
loop stays responsive AND the CPU tasks genuinely run in parallel.

**W34** `[1d | 2026-07-10 | 0]`
Q: What does `asyncio.TaskGroup` guarantee that scattering bare `create_task()` calls
with no group does not?
A: Structured concurrency — if any task in the group raises, the others are automatically
cancelled and the error propagates (as an ExceptionGroup) when the `async with` block
exits. Bare untracked `create_task()` calls can fail silently with nobody watching.

**W35** `[1d | 2026-07-10 | 0]`
Q: Sending a 500MB object to a ProcessPoolExecutor for a 1ms computation — faster or
slower than doing it directly, single-threaded? Why?
A: Slower, often dramatically. Every argument in and result out must be pickled,
transferred across a process boundary, and unpickled — for 500MB that cost is vastly
larger than 1ms of real work. Multiprocessing wins only when computation is expensive
RELATIVE to the data being shipped, not just whenever something is technically CPU-bound.

**W36** `[1d | 2026-07-10 | 0]`
Q: 1000 records, 0.5ms of pure computation each, sent individually to
`ProcessPoolExecutor.map()` — runs slower than a plain loop. Two fixes?
A: (1) Honest fix: skip multiprocessing entirely, the work is too cheap — plain loop
(500ms total, zero serialization) beats it outright. (2) If the real workload were
bigger: use `chunksize=N` to batch many records per task, paying the serialize/
deserialize round trip far fewer times instead of once per individual record.

**W37** `[1d | 2026-07-10 | 0]` — ⚠️ real, fresh catch, application not just recognition
Q: You're DESIGNING a fix (not being quizzed) for a pure-computation, zero-I/O workload,
and your instinct is "use threads/workers for concurrency." Before writing that code —
what single detail must you check first, and why does it override the instinct?
A: Check whether there's ANY I/O in the workload at all. Zero I/O = GIL is never
released = threads give no real speedup regardless of how they're structured (locks,
worker pools, however dressed up) — same mechanism as C06, just applied while
*generating* a solution instead of *recognizing* the fact under direct quiz. Rudra
correctly explained the GIL mechanism when tested on it directly earlier the same
session, then proposed threads anyway when designing his own fix minutes later —
recognition and application are different skills, this card tests the second one.

---

## Week 4 (testing + debugging) — quizzed 2026-07-15 in FITB/MCQ format. Results below.

**W38** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: `pytest.raises` is itself a context manager, but the success condition is
inverted from a normal `try/except` — the test PASSES only if the code inside the
`with` block DOES raise the specified exception; it FAILS if the block completes
without raising. `match=` additionally checks the exception message against a regex,
so the test confirms it failed for the right reason, not just that something broke.

**W39** `[3d | 2026-07-18 | 1]` — passed after one correction (confused `conftest.py`
with the `scope="session"` value on the third blank — two different concepts: where
fixtures live vs how often they rerun).
Concept: fixture scopes control how often expensive setup reruns. `scope="function"`
(default) = fresh every test. `scope="module"` = built once, shared across all tests in
one file. `scope="session"` = built once for the entire test run, across all files.

**W40** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: `conftest.py` makes fixtures automatically visible to every test file in its
directory (and subdirectories) with zero imports — pytest auto-discovers it.

**W41** `[1d | 2026-07-16 | 0]` — ⚠️ real miss, two corrections needed (skipped
`TypeError` entirely, then answered "attribute/method access" instead of "protocol"
for what MagicMock specifically enables). Retry.
Concept: `Mock()` doesn't implement Python's dunder/magic methods — `len()` on it
raises `TypeError`. `MagicMock()` does implement them with sensible defaults. Use
`MagicMock` when the code under test invokes a Python PROTOCOL (`len()`, `in`, iteration
— special syntax that secretly calls dunder methods) on the mocked object — plain
attribute/method access already works fine on either.

**W42** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: four `side_effect` configurations — LIST (different return value per
successive call, only way to simulate "fails twice then succeeds"), single EXCEPTION
instance (every call raises, no return value), CALLABLE (return value computed from
actual call arguments).

**W43** `[1d | 2026-07-16 | 0]` — ⚠️ real miss, wrong/incomplete on all three blanks
(said `assert_called_once` missing the `_with`, "assert_never_called" instead of
`assert_not_called`, left `call_count` unanswered). Retry.
Concept: mock call verification — `assert_called_once_with(...)` = called exactly once
AND with these exact arguments (the `_with` is what makes it check arguments, not just
count). `assert_not_called()` = confirms zero calls ever (exact method name, not
"never"). `call_count` = plain int attribute, no parens, total calls regardless of args.

**W44** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: scientific debugging method, five steps in order — reproduce reliably → read
traceback bottom-up → form ONE hypothesis → test that one thing → bisect if still stuck.

**W45** `[3d | 2026-07-18 | 1]` — passed after one correction (had the leak direction
backwards — said the second call's results leaked into the first call's, when it's the
reverse: first call's entries persist into the second call's list, since call 1 runs
first and populates the shared default before call 2 ever touches it).
Concept: `def f(x, results=[])` — mutable default evaluated once, shared across every
call that doesn't pass its own `results`. Call 1's entries are already in the shared
list before call 2 runs, so call 2's result list silently contains call 1's leftovers.

**W46** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: `pdb` — `n` (next line, black-boxes function calls) vs `s` (step, enters the
function call) — `s` is the only way to actually get inside a suspect function.

**W47** `[3d | 2026-07-18 | 1]` — passed clean.
Concept: `git bisect` = binary search over commit history — checks the midpoint commit
repeatedly, narrowing the range. `git bisect run <script>` automates it via the
script's EXIT CODE specifically (0 = good, non-zero = bad) — git never reads output.

---

## Week 5 (SQL) — quizzed 2026-07-15, all three passed clean on first try.

**W48** `[3d | 2026-07-18 | 1]`
Concept: four JOIN types. `INNER JOIN` = only rows with a match on BOTH sides —
unmatched rows vanish. `LEFT JOIN` = every row from the left table regardless of a
match, NULLs filling the right side where there's none. `RIGHT`/`FULL OUTER` are the
mirror/union versions. "Show all agents including zero-failure ones" needs LEFT JOIN.

**W49** `[3d | 2026-07-18 | 1]`
Concept: `GROUP BY` collapses rows into one summary per distinct value, enabling
aggregates (`COUNT`/`SUM`/`AVG`/etc.) per group. Every `SELECT` column must be in
`GROUP BY` or wrapped in an aggregate — otherwise SQL can't know which row's value
you meant.

**W50** `[3d | 2026-07-18 | 1]` — the actual gotcha, most important of the three.
Concept: `COUNT(*)` counts ALL rows regardless of content — a `LEFT JOIN` non-match
still produces one NULL-filled row, so `COUNT(*)` wrongly reports `1` for zero real
matches. `COUNT(column_name)` skips NULLs of that specific column, correctly reporting
`0`. Always use `COUNT(right_table_column)`, never bare `COUNT(*)`, with LEFT JOIN.

---

## Week 5 continued (SQL basics + window functions) — taught 2026-07-15, not yet
## quizzed. Due 2026-07-16. Verified hands-on against real SQLite (`agents.db`).

**W51** `[1d | 2026-07-16 | 0]`
Concept: `WHERE column = NULL` NEVER matches anything, ever — `NULL` means "unknown,"
and "is unknown equal to unknown" is itself unknown, never true. The only correct way
to check for NULL is `IS NULL` (or `IS NOT NULL`) — dedicated syntax, not a comparison.

**W52** `[1d | 2026-07-16 | 0]`
Concept: `AND` binds tighter than `OR` in SQL — mixing them in one `WHERE` without
parentheses silently changes the logic. `WHERE a AND b OR c` parses as
`(a AND b) OR c`, not `a AND (b OR c)`. Always parenthesize the `OR` group explicitly
whenever `AND` and `OR` mix in the same clause.

**W53** `[1d | 2026-07-16 | 0]`
Concept: `UPDATE`/`DELETE` with no `WHERE` clause silently affects EVERY row in the
table — syntactically legal, one of the most damaging real-world SQL mistakes. Safety
habit: always run the equivalent `SELECT` with the same `WHERE` clause FIRST, confirm
exactly which rows would be affected, only then run the real `UPDATE`/`DELETE`.

**W54** `[1d | 2026-07-16 | 0]`
Concept: `SELECT DISTINCT column` collapses a result down to unique values only —
`SELECT agent_name` returns one row per underlying row (duplicates included);
`SELECT DISTINCT agent_name` returns each distinct value exactly once, regardless of
how many underlying rows share it.

**W55** `[1d | 2026-07-16 | 0]`
Concept: a subquery in parentheses inside `WHERE` runs FIRST, computing a value (or
set of values), which the outer query then uses as if it had been typed in literally —
e.g. `WHERE latency_ms > (SELECT AVG(latency_ms) FROM agent_runs)` filters against the
computed average without a separate manual step.

**W56** `[1d | 2026-07-16 | 0]`
Concept: `ROW_NUMBER()`/`RANK()`/`DENSE_RANK()` all number rows via `OVER (ORDER BY ...)`
but differ ONLY on ties. `ROW_NUMBER()` never ties — arbitrarily breaks ties, sequential
numbers with no repeats. `RANK()` ties rows equally but leaves a GAP afterward (counts
rows: two tied at 2nd means next is 4th). `DENSE_RANK()` ties equally with NO gap
(counts distinct values: next is 3rd, since only 2 distinct values seen so far).

**W57** `[1d | 2026-07-16 | 0]`
Concept: window functions (`OVER (...)`) do NOT collapse rows like `GROUP BY` does —
every original row survives, gaining an extra calculated column instead. `PARTITION BY`
inside `OVER` is the window-function version of `GROUP BY`, but it partitions the
CALCULATION only — e.g. `RANK() OVER (PARTITION BY agent_name ORDER BY latency DESC)`
restarts the ranking from 1 separately for each agent, rather than one ranking across
the whole table.

**W58** `[1d | 2026-07-16 | 0]`
Concept: `LAG(col) OVER (ORDER BY ...)` grabs that column's value from ONE ROW BACK
(previous row, per the given order) and attaches it to the current row — first row
gets NULL (nothing before it). `LEAD(col)` is the mirror — grabs the NEXT row's value,
last row gets NULL. Both let you compare a row to its neighbor directly in one
`SELECT`, without a self-join.

---

## Week 5 continued (Docker) — taught 2026-07-15/16, not yet quizzed. Due 2026-07-17.
## First topic taught via the newly codified 5-stage pipeline (teach-rudra skill).

**W59** `[1d | 2026-07-17 | 0]`
Concept: image vs container — an IMAGE is a frozen, read-only blueprint (does nothing
by itself). A CONTAINER is a running instance of that image. Same relationship as a
Python class (image) and objects instantiated from it (containers) — one image, many
independent containers, none sharing state with each other.

**W60** `[1d | 2026-07-17 | 0]`
Concept: Docker caches each Dockerfile layer. The moment ONE layer's cache invalidates
(e.g. `COPY requirements.txt .` sees a content diff), EVERY layer downstream reruns
too — regardless of whether that later layer's own command changed (`RUN pip install`
reruns even though its command text never changed, because it's built on top of the
now-invalidated layer). This is why slow/rarely-changing steps go FIRST in a
Dockerfile and fast/frequently-changing steps (copying app code) go LAST.

**W61** `[1d | 2026-07-17 | 0]`
Concept: `docker run -v <volume_name>:<path_inside_container> <image_name>` — three
distinct pieces in that order. Volumes persist data OUTSIDE the container's own
filesystem, surviving container deletion/recreation — containers themselves are
disposable by design, anything written to their own filesystem vanishes when deleted.

**W62** `[1d | 2026-07-17 | 0]`
Concept: `docker run -e KEY=value <image>` injects config/secrets at RUNTIME, not baked
into the image at build time. Same exact image can run against dev/staging/prod just
by changing what's passed at `docker run` time — no rebuild needed. This is why
secrets never get hardcoded directly into a Dockerfile.

**W63** `[1d | 2026-07-17 | 0]` — the actual gotcha, most important of the Docker set
Concept: in `docker-compose.yml`, the SERVICE NAME (the key under `services:`) becomes
the automatically resolvable HOSTNAME other containers use to reach it — e.g. a
service named `redis:` is reached at hostname `redis`, not `localhost`. `localhost`
is wrong here because each container is its own isolated machine — `app` and `redis`
containers don't share a `localhost` with each other at all. `depends_on` must
reference this exact same service name too, or the intended startup order silently
fails to apply.

---

## Graduated
(none yet — C11/C12/C13 are two passes deep but neither pass was ELI5-style; need one
ELI5-format cold pass each to actually graduate)
