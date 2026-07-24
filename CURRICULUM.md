# The December Plan — Evals & Observability Mastery

**Owner:** Rudra Dudhat · **Created:** 2026-07-04 · **Deadline:** internship offers by December 2026
**Time budget:** 10–15 hrs/week ≈ 220–320 total hours over 21 weeks (Jul 7 → Nov 29)
**Spine:** Evals + LLM Observability. **Differentiator layer:** agent security (eval-driven red teaming).
**Safety net:** 1 practical coding rep/week (Palantir/Scale screens — practical, not LeetCode).

---

## 0. The Thesis

AI-infra companies (Langfuse, Arize, Braintrust, Portkey) and FDE roles (Palantir, Scale,
OpenAI) do NOT interview like Big Tech. Research findings (July 2026):

- FDE interviews: 3-hour continuous practical sessions, live debugging, case studies,
  system design, deep interrogation of YOUR projects. Explicitly no LeetCode.
  Sources: [Exponent FDE guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde),
  [Sundeep Teki FDE guide](https://www.sundeepteki.org/advice/the-definitive-guide-to-forward-deployed-engineer-interviews-in-2026),
  [first-person FDE interview account](https://medium.com/@bagheshri/i-interviewed-for-a-forward-deployed-ai-engineer-role-heres-what-no-one-tells-you-192929a7fe45)
- Take-homes of 4–8 hours are common. The winning move is having already done harder
  versions of the take-home in public.
- These companies hire on **proof-of-work**: merged OSS PRs, shipped artifacts, public
  case studies. Rudra already has the rarest asset — merged PRs in OTel, MLflow,
  LiteLLM, Kedro ×2, Strix. The plan weaponizes that.

**The bet:** in 5 months, one person cannot become "untouchable" at everything. He CAN
become the strongest third-year in the world at ONE thing — building evaluation systems
for AI agents — with the OSS receipts to prove it. Everything below serves that.

### Timeline reality (from research, not vibes)

Langfuse/Arize/Braintrust have **no formal winter internship programs** — rolling hiring,
Langfuse is Europe-centric (mandatory Berlin weeks). The realistic December paths:

1. Indian AI startups (Lyzr warm lead, similar cos) — recruit Oct–Nov for Dec start
2. Remote gigs/trials at small US AI startups via founder outreach on OSS proof
3. FDE-track junior roles — interviewed on proof-of-work

**Therefore: proof-of-work locks by OCT 11. Outreach runs Oct 12 → Nov 15.
Interviews Nov–Dec. December is when offers land, not when prep ends.**

---

## 1. The Anti-AI-Dependence Operating System

The higher goal: think and code without AI as a crutch. These are standing rules,
enforced every week, no exceptions:

1. **Division of labor.** Claude writes and maintains all notes — clerical work is what
   AI is for; that's using AI wisely. Rudra's thinking happens where it counts: the
   no-AI reps, predict-first, and explain-it-cold. The muscle is built in the doing,
   not the transcription.
2. **No-AI reps.** One timed exercise per week written cold in the editor — Copilot off,
   no Claude tab. AI is allowed only AFTER completion, as a reviewer. The rep list lives
   in `practice/` and mirrors real screens (LRU cache, rate limiter, worker pool,
   log parser, retry decorator, trace-tree builder...).
3. **Predict-first.** Before running any code or command, state the expected output out
   loud/in writing. Wrong prediction = the learning moment, dig in.
4. **Explain-it-cold.** End of each week: 5-minute verbal explanation of the week's core
   concept, interview-style, no notes. Claude interrogates like a skeptical senior.
5. **Debugging discipline** (from README): reproduce → read traceback bottom-up → ONE
   hypothesis → test that one thing → bisect. Never guess-and-poke. State the hypothesis
   before touching code.
6. **The parking lot.** Any new project/pivot idea goes into `PARKING_LOT.md` and is
   reviewed ONLY at phase gates. (The historical failure mode is mid-plan pivots —
   SD curriculum paused, multiple project pivots. The plan survives only if pivots are
   quarantined.)
7. **The retention engine** (added 2026-07-04 — the fix for "I forget it by week 4-5").
   Every concept taught becomes a card in `RETENTION_DECK.md` (question + model answer +
   due date). Claude maintains the deck; Rudra does the retrieval. **Every session opens
   with a 5-minute recall quiz of due cards** — answered cold, out loud or typed, no notes.
   Intervals: new card → 1d → 3d → 7d → 21d → graduated. A miss resets the card to 1d.
   A card graduates only after two consecutive cold passes, one of which must be an
   ELI5 explanation ("explain it to a five-year-old"). Graduated cards still get sampled
   randomly in Phase 4 mocks. Nothing is "done" because it was taught — only because
   it survived the schedule.
8. **Fair testing only** (added 2026-07-08, after a real violation). A synthesis question
   combining two ALREADY-FULLY-TAUGHT concepts is fair game — that's the actual skill this
   plan builds. Demanding precision on a mechanism that was only mentioned in passing while
   teaching something else is not fair, and Rudra correctly called this out mid-session.
   Rule: if a question's model answer requires a mechanism that hasn't been taught as its
   own standalone explanation, teach it properly first, THEN ask. Never let "I gestured at
   it once" count as "I taught it."
9. **Theory → dynamic hands-on practice, every topic, no exceptions** (added 2026-07-10,
   codifying what actually worked in the Week 4 session). Deep theory alone isn't enough —
   every topic gets followed by REAL practice: actual files on disk, actual test suites
   written and run with real `pytest`, actual bugs planted and found with real `pdb`
   sessions, not chat-only Q&A. Concretely, this looked like: Claude writes a function +
   an example test suite (verified with a real `python -m pytest` run, never just written
   and assumed correct) → Rudra writes tests for a NEW function himself, iterated live
   against real pytest output → Claude plants a genuine bug in a realistic-sized dataset →
   Rudra finds it with actual `pdb` commands, not by reading the file. Practice work lives
   in `practice/<week>/`.
   **The scope constraint (this is Rule 8 applied to practice, not just quiz questions):**
   practice must draw ONLY from what's actually been taught, and only from material Rudra
   has already demonstrated he knows. A practice exercise that requires a mechanism never
   explained is the same fairness violation as a quiz question that does — teach it
   standalone first, or don't include it in the exercise at all.

---

## 2. Phase Plan

```
PHASE 1 — RELEARN THE CORE              Wk 1–5    Jul 7  – Aug 9
PHASE 2 — EVALS + OBSERVABILITY CORE    Wk 6–11   Aug 10 – Sep 20
PHASE 3 — SECURITY LAYER + OSS SPRINT   Wk 12–14  Sep 21 – Oct 11   ← proof-of-work gate
PHASE 4 — OUTREACH + INTERVIEW REPS     Wk 15–21  Oct 12 – Nov 29
```

**Phase 1 was restructured 2026-07-04** after a 16-question trap-level quiz scored 4/8 and
2.5/8 on areas the old calibration called "Strong" (functions, async ≈ 5/10 at trap level).
Foundations get relearned from first principles with retention machinery, not skipped.

One project threads through everything: **the Attribution Engine** — a multi-agent
pipeline (Researcher with RAG → Analyst → Writer → Critic, built Wk 5) paired with a
tool that automatically finds which agent caused a failure when the pipeline breaks —
the same idea as `git bisect`, applied to agents talking to each other. Competitive
research (2026-07-05) confirmed this specific angle is genuinely underbuilt: existing
agent-security tools (DeepTeam, PyRIT, Agent Security Bench) score *whether* an attack
succeeded, but nothing cleanly attributes *which agent* caused a multi-agent failure —
recent papers (BlindGuard, trust-propagation studies) confirm this is still open. It
gets instrumented, traced, benchmarked against synthetic failures with known ground
truth, judged, gated in CI, and stress-tested by planting an adversarial agent inside
the pipeline. By October it is a complete, public case study AND a genuinely novel OSS
tool. That artifact is the interview.

### PHASE 1 — Relearn the Core (Wk 1–5)

The 2026-07-04 quiz showed the June foundations were taught but not retained. The misses
trace to two root confusions, and Phase 1 is organized around killing them permanently:

- **Root confusion 1 — variable vs value:** closures capture variables not values,
  aliasing (`b = a` copies the reference), the lambda-in-loop trap.
- **Root confusion 2 — def-time vs call-time:** mutable defaults evaluate at def,
  decorators run at def but wrap every call, generators run at next() not at call,
  `create_task` starts work now vs bare `await` starts it later.

Weekly structure:

- **Wk 1 — The Python execution model.** Names as references (sticky-note model), objects
  and identity, aliasing and in-place vs rebinding (`+=`), scopes/LEGB, compile-time
  locals (`UnboundLocalError`, `nonlocal`), def-time vs call-time as a unifying lens.
  *One evening, off-plan: ship the Brok launch (merge PR, X post). Then it's parked.*
- **Wk 2 — Functions deep, relearned.** Closures (variable capture, loop trap), decorators
  (the name IS the wrapper, `@functools.wraps`, decorators with arguments), generators
  (laziness, single-use exhaustion, generator expressions), context managers.
- **Wk 3 — Concurrency from first principles.** The three models (threads/processes/async)
  derived from what actually blocks; GIL = blocks parallel *computing*, not parallel
  *waiting*; event loop mechanics; WHEN WORK STARTS (bare await vs create_task vs gather
  vs TaskGroup); run_in_executor for CPU work.
- **Wk 4 — Testing + professional debugging.** pytest, fixtures, parametrize, mocking —
  through the evals lens (assertions ARE Level-1 evals). Scientific debugging method,
  pdb, git bisect. Reps: 2 planted-bug hunts in unfamiliar code (the FDE live-debug format).
- **Wk 5 — SQL essentials + Docker + build the pipeline.** SQL, full week's depth, not a
  few exchanges (corrected 2026-07-15 after being taught too shallow initially — see
  [[feedback-curriculum-depth]]): basics first (`SELECT`/`WHERE` + comparison/logical
  operators incl. the `= NULL` never-matches trap vs `IS NULL`, `ORDER BY`/`LIMIT`,
  `INSERT`/`UPDATE`/`DELETE` with the preview-SELECT-before-DELETE safety habit,
  `DISTINCT`, basic subqueries) — THEN the four JOIN types (`INNER`/`LEFT`/`RIGHT`/
  `FULL OUTER`, the LEFT JOIN + `COUNT(*)` vs `COUNT(column)` gotcha), `GROUP BY` +
  aggregates, and window functions (`ROW_NUMBER`/`RANK`/`DENSE_RANK`/`LAG`/`LEAD`, each
  taught individually on the same traced example before ever combining with
  `PARTITION BY` — see the sequencing addendum in [[feedback-curriculum-depth]]).
  Practiced hands-on against a real SQLite db (`practice/week5_sql/agents.db`), every
  query actually run and verified, not just written.

  **Docker — taught 2026-07-15/16 via the newly codified 5-stage pipeline (see the
  `teach-rudra` skill), first full run of the new methodology.** Theory: image vs
  container (class/instance analogy), layer caching + the cascading invalidation rule,
  core commands, volumes, environment variables, `docker-compose` with the
  service-name-is-hostname rule. Worked application + sample Q&A on a real FastAPI +
  Postgres example. Live Q&A gated MCQ/FITB. Practice done as reasoned code-review
  ("mock it," Rudra's choice, not live-executed this round) — 4 gradual exercises
  (Dockerfile, volume flag, env var flag, full docker-compose.yml combining app +
  Redis), several real bugs caught and corrected (missing image name in `docker run`,
  `port` vs `ports`, missing YAML list syntax, `depends_on` referencing a service name
  that didn't match the actual service, env var nested under the wrong service).
  Reference notes with diagrams written and pushed: `ai_notes/full notes/module_docker.md`.

  **Week 5 (SQL + Docker) is now fully complete.** Next: assemble the base system — a
  LangGraph pipeline with 4 distinct agent roles (Researcher with RAG over a small doc
  set → Analyst → Writer → Critic) doing a real report-writing
  task, containerized, OTel-instrumented from day one. The Phase 1 gate build.

  **Build started 2026-07-16 — own repo, not nested in december-plan:**
  github.com/RudraDudhat2509/attribution-engine (matches how Brok/receipts/cacheguard/
  mimic-eval are each set up). Routing design upgraded from a naive "always loop back
  to Writer" to metric-based attribution (Rudra's design improvement): the Critic
  scores retrieval quality/grounding/generation quality (RAGAS-inspired: context
  precision-recall / faithfulness / coherence) in that priority order — checking
  retrieval first matters because a retrieval failure makes grounding look bad too as
  a downstream symptom, not a separate root cause, same logic as bisecting to the
  earliest broken commit rather than flagging every commit that fails afterward.
  Researcher gets real tools (search + rerank), not a single fixed retrieve call.
  Every Critic routing decision is logged in `routing_history` (an accumulating
  LangGraph reducer, not overwritten each loop) — this running log IS the attribution
  dataset the project is meant to produce.

  Skeleton built and verified for real (deterministic stub nodes, no LLM calls yet —
  proves the graph structure/looping/state accumulation before adding LLM cost and
  non-determinism): 5/5 pytest passing, run in a dedicated venv (caught and fixed a
  real bug along the way — was accidentally running in a completely unrelated
  project's (`cartography`) leftover venv). Roadmap tracked in the repo's own README:
  real LLM calls next, then real RAG, then OTel, then the ablation-based attribution
  method as a second, deterministic approach to compare against the Critic's live
  routing, then the synthetic benchmark with known ground-truth culprits.

**Phase 1 gate (Aug 9):** the pipeline runs in Docker, has tests, emits traces; Rudra
explains every line cold; retention deck shows ≥90% recall on all Phase 1 cards, each
passed twice including one ELI5 pass.

**Progress note (2026-07-08):** Week 1 content taught and tested in full depth in one
session — reference/box model, mutable vs immutable, LEGB, `nonlocal`/`global`,
`is`/`==`, def-time vs call-time as the unifying lens. Went further than planned: also
covered most of Week 2 ahead of schedule — closures, decorator stacking order, decorator
factories (`@retry(times=3)`), context managers (class-based + `@contextmanager`,
suppression semantics, nested enter/exit order, log-and-reraise, single-use generator
gotcha), and generator `.send()`. Tested adversarially, not just taught — see
`RETENTION_DECK.md` C01–C03, N17–N30. **C02 (decorator execution order) had failed
twice** — flagged as a real weak spot. Session also produced one process correction:
rule 8 above, added after Rudra caught a fairness violation in how a synthesis question
was tested.

**Progress note (2026-07-09):** Retention run on 22 cards (scoped to Week 1/2 material
only, per Rudra's correction — future-phase cards for concurrency/evals/Redis stay
parked until those weeks arrive). **C02 passed clean on the third attempt — the weak
spot is genuinely closed.** C11/C12/C13 hit second consecutive passes (7d interval, one
ELI5 pass still needed each to graduate). 5 real misses surfaced and got corrected:
N17 (sticky-note model — said `y=x` copies a value, wrong), N19 (said `nonlocal` could
fall through to global — false, non-overlapping targets), N23 (biggest miss — confused
`@contextmanager`'s try/finally with an unrelated decorator example, needed full
re-teach), N26 (two rounds of imprecision before landing on "exhausted generator,
runtime error"), N30 (timing confusion on what one `send()` call actually does). All 5
retry tomorrow (2026-07-10). Closed out Week 2's last item — generator expressions
(`(x for x in range(n))`) — clean pass first try, correctly connected to the existing
single-use-generator lesson (N31). **Week 1 AND Week 2 content are now both fully
taught and tested**, ahead of the original 5-week Phase 1 schedule.

**Same session, continued — Week 3 (concurrency) taught + tested in full:** CPU-bound vs
I/O-bound distinction, GIL mechanics (releases on I/O, never on compute), event loop
cooperative scheduling (switches only at `await`, never forced), `run_in_executor`
(thread pool keeps the loop responsive but doesn't parallelize CPU work; process pool
does both), multiprocessing tradeoffs (pickling cost, `chunksize` batching). Un-parked
and passed C05/C06/C14 through repeated correct application during the quiz. Added 6 new
cards (W32–W37) — see `RETENTION_DECK.md`.

**Real catch worth flagging directly: `W37`.** Rudra correctly explained the GIL
mechanism when tested on it directly (`compute_hash()` question), then — minutes later,
designing his own fix for an unrelated pure-computation workload — proposed threads with
locks anyway, the exact thing he'd just correctly ruled out. Caught and corrected in the
moment. This is a recognition-vs-application gap, not a knowledge gap: he can state the
rule cold, but it isn't yet automatic when he's the one generating a design instead of
being asked to recall a fact. Worth watching for this same pattern in other topics —
retention cards test recall, but design/application under his own initiative is the
actual bar for FDE-style interviews, and needs separate verification.

**Week 1, 2, and 3 are now all taught and tested**, three weeks ahead of the original
5-week Phase 1 schedule (was: Wk1–5, now: Wk1–3 content done). Next: Week 4 (testing +
professional debugging) or Week 5 (SQL + Docker + start the Attribution Engine build).

**New session (2026-07-10) — retention run, methodology change, Week 4 in full.**

Opened with the 11 cards due from 2026-07-09: all 5 flagged misses (N17, N19, N23, N26,
N30) retried clean, including `N23` (the biggest miss) which needed two more rounds of
pushing before the actual injection mechanism (`gen.throw()` at the `yield` point) was
stated precisely. `W32` turned out to have a genuinely ambiguous question on Claude's
end (tested threads/GIL when it meant to test the event loop specifically) — fixed and
re-asked correctly, logged as a real card-authoring bug, not a Rudra miss. `W33` caught
a real, meaningful misunderstanding: conflated "offload to ThreadPoolExecutor" with
"call directly, no executor at all" — `run_in_executor`'s `await` IS a real yield point
back to the loop, event loop stays responsive even with a thread pool; corrected.

**Methodology change, mid-run:** Rudra: "i want fitb or mcq type questions in cards from
now on and cards should be dynamic." Retention cards are now delivered as FITB/MCQ, with
varied wording each retry — never the same static phrasing twice. See
`RETENTION_DECK.md` header and [[feedback-retention-card-format]] in Claude's memory.
Directly motivated by the same recognition-vs-application concern as `W37`.

**Curriculum depth correction, also mid-session:** after Week 4 got covered in a
handful of exchanges, Rudra: "your weeks curriculum is super not that great... it
should teach me a lottt... i should learn a little deeper/more breadth/more examples."
This is now a standing calibration for the whole plan, not a one-time fix — see
[[feedback-curriculum-depth]]. Week 4 was then re-taught properly with real depth:

- **pytest, full breadth:** `assert` as Level-1 evals (direct tie to the Hamel
  methodology), fixtures (including `yield`-based teardown, scopes: function/module/
  session, `conftest.py` sharing), `parametrize`, `pytest.raises` with `match`, marks
  (`skip`/`skipif`/`xfail`), `Mock` vs `MagicMock`, `return_value` vs `side_effect`
  (list / single exception / callable — all four variants with worked examples),
  `pytest-asyncio` for testing coroutines, and a full mock-verification pass
  (`assert_called_once_with`, `assert_not_called`, `call_count`, `call_args_list`) —
  though the last one was explicitly scaled back at Rudra's request mid-lesson ("i
  wouldnt need this level of detail") — logged as calibration, not a gap.
- **Scientific debugging method** (5 steps, reproduce → bottom-up traceback → one
  hypothesis → test it → bisect) taught and applied to two real bug hunts — a
  `ZeroDivisionError` and a genuine mutable-default-argument cross-contamination bug
  (`results=[]` shared across calls) that Rudra correctly diagnosed via the exact
  symptom (`len(processed_1) == 2` instead of `1`).
- **`pdb`** — real command table (`n`/`s`/`c`/`p`/`pp`/`l`/`w`/`b`/`q`), conditional
  breakpoints, and a genuine buried-bug exercise: an 80-record trace dataset
  (`practice/week4_testing/trace_data.json`) with one malformed span (`t54`, missing
  `duration_ms`) that Rudra correctly localized.
- **`git bisect`** — manual workflow and `git bisect run` with a script, including the
  exit-code mechanism specifically (0 = good, non-zero = bad — same convention pytest
  itself uses).

**Real, hands-on artifact built this session:** `december-plan/practice/week4_testing/`
— `payment.py` + `test_payment_example.py` (Claude's reference suite, all passing),
`inventory.py` + `test_inventory.py` (Rudra's own tests, iterated live against real
pytest runs — caught his own false-positive immutability test via the `copy = items`
aliasing trap, a direct callback to Week 1), `debug_me.py` + `trace_data.json` (the
pdb exercise). All verified by actually running pytest, not just written and assumed
correct — every fix in this session was confirmed with a real `python -m pytest` run
before being presented as working.

**Week 1–4 are now all fully taught and tested.** Next: Week 5 (SQL + Docker + start
the Attribution Engine build) — the last week of the original Phase 1 scope.

### PHASE 2 — Evals + Observability Core (Wk 6–11)

The spine. Methodology = Hamel Husain + Shreya Shankar's critique-shadowing process
(the field's canonical curriculum — 4,500+ engineers trained), executed on the pipeline
with synthetic traffic AND synthetic injected failures (known root-cause agent, for the
attribution benchmark). Primary sources, all free:
[Your AI Product Needs Evals](https://hamel.dev/evals) ·
[LLM-as-a-Judge complete guide](https://hamel.dev/llm-judge/) ·
[Field Guide to Rapidly Improving AI Products](https://hamel.dev/field-guide) ·
[Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) ·
[Who Validates the Validators (Shankar et al.)](https://arxiv.org/abs/2404.12272) ·
[DeepLearning.AI × Arize: Evaluating AI Agents](https://www.deeplearning.ai/courses/evaluating-ai-agents) ·
[Eugene Yan: LLM evaluators survey](https://eugeneyan.com/writing/llm-evaluators/) ·
[AlignEval](https://aligneval.com/) ·
[Arize Recipe-Bot workflow (the Maven course homework, free)](https://arize.com/blog/ai-evals-maven-course-homework-the-recipe-bot-workflow/)

- **Wk 6 — Instrumentation deep.** OTel GenAI semantic conventions, spans/context
  propagation hands-on, Langfuse AND Arize Phoenix wired to the pipeline (knowing both
  tools = interview currency at both companies). Every agent's span carries which-agent
  metadata from day one — the attribution tool needs clean per-agent trace boundaries
  to work at all. Generate 200+ traces of synthetic tasks (topics × difficulty ×
  failure-injection grid, per Hamel's taxonomy, extended with known-root-cause failures).
- **Wk 7 — Error analysis + the attribution benchmark.** THE skill, the highest-ROI
  activity in AI engineering. Open coding on 100+ real traces (free-text notes, no
  preconceived categories) → axial coding (build the failure taxonomy from the notes) →
  frequency counting → prioritized fix list. Build the custom data viewer (FastHTML/
  Streamlit, built in hours — Hamel: "the most important AI investment"). Rudra does the
  annotation HIMSELF — this cannot be delegated to AI, that's the point. Alongside this:
  build the 20–30 case attribution benchmark (deliberately corrupt one agent's output per
  case, record the true culprit) — this is the ground truth the whole project is scored
  against.
- **Wk 8 — Two attribution methods, judged like Hamel teaches.** Method 1 (deterministic,
  core): ablation — re-run the pipeline swapping one agent's output at a time back to a
  known-good version; whichever swap fixes the outcome names the culprit. Method 2
  (comparison baseline): an LLM-as-judge that reads the full trace and names a culprit
  with a written critique — built via critique shadowing exactly as taught: binary
  pass/fail, Rudra as principal domain expert, few-shot critiques, judge↔human agreement
  via precision/recall (not raw agreement). Score both methods against the Wk 7 benchmark
  — % correct culprit identification is the headline metric, exactly like Mimic's
  agreement-with-LLM number.
- **Wk 9 — Eval infrastructure.** Golden datasets with versioning, Level-1 assertion
  gates in CI (GitHub Actions) — now gating on BOTH quality regression and attribution-
  accuracy regression — the dataset-harvesting flywheel (prod failures → eval set),
  regression gates on prompt changes. Connect diffprompt's behavioral-divergence idea as
  the early-warning layer alongside the quality gate.
- **Wk 10 — Online evals + RAG evals.** Background scoring, rolling alerts, cost/latency
  tracking. RAGAS internals (faithfulness, context precision/recall) — implement two
  metrics from scratch before using the library, so it's never magic, then apply them to
  the Researcher agent's retrieval step directly (not a toy example — it's already in
  the pipeline).
- **Wk 11 — Consolidation buffer.** Life happens; at 10–15 hrs/wk a buffer is load-bearing.
  If on schedule: write case-study part 1 and start scouting OSS issues in
  Phoenix/Langfuse/OpenLLMetry/RAGAS from real friction hit in Wk 6–10 (the best PR
  source is "this annoyed me while using it").

**Phase 2 gate (Sep 20):** Full eval system live on the pipeline — viewer, taxonomy,
attribution benchmark, both attribution methods scored against it, CI gate, online
scoring. Rudra can run the whole loop and defend every design decision cold.

### PHASE 3 — Security Layer + OSS Sprint (Wk 12–14)

The differentiator: almost nobody entering evals also speaks attack surfaces; almost no
security person builds rigorous evals. The fusion — **eval-driven red teaming, attack
success rate as a measured metric** — is Rudra's unique positioning, and his garak/Strix
history already backs it.

- **Wk 12 — Plant an adversarial agent + systematic probing.** Prompt injection (direct +
  indirect), tool poisoning, memory poisoning, RAG retrieval poisoning against the
  Researcher agent — the sharpest test of the whole project: does the attribution tool
  correctly name a COMPROMISED agent as the culprit, same as it names a buggy one? Attack
  success rate becomes a tracked metric on the same dashboard as quality and attribution
  accuracy. garak-style probe/detector harness; finish the in-flight garak PR
  (#74 tag-injection) if still open.
- **Wk 13–14 — OSS sprint + publish.** Two targeted PRs in eval/obs repos (Phoenix,
  Langfuse, OpenLLMetry, RAGAS — from the Wk 10 friction list). Publish the flagship
  case study: repo + long-form write-up + X thread. Update resume + portfolio around it.

**Phase 3 gate — PROOF-OF-WORK LOCK (Oct 11):** public case study live, 2+ new PRs
merged/open, resume rebuilt. This gate does not slip; scope shrinks instead.

### PHASE 4 — Outreach + Interview Reps (Wk 15–21)

Prep and pipeline in parallel, ~half time each.

- **Outreach (from Oct 12):** Lyzr follow-up first. Then founder/eng-lead DMs at AI-infra
  startups with the case study + PR links (use the Personal Outreach Engine — dogfooding
  is itself a story). Target: 30+ quality touches by Nov 15. Public building on X continues.
- **Weekly interview reps:**
  - 1 × mock interview with Claude in FDE format — live-debug an unfamiliar system,
    design an eval pipeline under questioning, defend the case study against attack
  - 1 × timed cold system design from the AI-infra set: LLM gateway (Portkey), tracing
    backend at scale (Langfuse), eval platform (Braintrust), agent platform with
    isolation (Palantir), rate-limiter-as-a-service, RAG at scale
  - 1 × no-AI practical rep (the Palantir/Scale net, continued)
  - Once in Wk 16–17: a full 6-hour take-home simulation, reviewed brutally
- **Story bank:** STAR write-ups for every project (Altagic, diffprompt, case study, each
  OSS PR — especially the "how I navigated the maintainer review" stories).

**Phase 4 gate = the actual goal:** offers in hand by early December.

---

## 3. The Weekly Template (10–15 hrs)

| Block | Time | What |
|---|---|---|
| Deep session ×2 | 5–6 h | Teach → Rudra builds live (Claude never writes the solution) |
| Project build | 3–5 h | Solo work on the week's Attribution Engine milestone |
| No-AI rep | 1–1.5 h | Timed, cold, editor only. AI review after. |
| Notes review | 15 min | Claude writes the notes; Rudra reads + flags gaps |
| Explain-it-cold | 15 min | Verbal, interrogated |

Phase 4 swaps the deep sessions for mocks/system design.

---

## 4. Success Metrics (checked at every phase gate)

1. Can rebuild the week's artifact cold, no AI, and explain every line — sampled randomly.
2. Passes explain-it-cold every week — 5 min verbal, interrogated, no notes open.
3. Attribution Engine milestones on schedule (traces → viewer → benchmark → both attribution methods scored → CI → adversarial-agent test).
4. By Oct 11: public case study + 2 new OSS PRs + rebuilt resume.
5. By Nov 15: 30+ outreach touches, ≥5 conversations.
6. By early Dec: offer(s).

## 5. Risks — named honestly

- **The #1 risk is pivoting.** History: SD curriculum paused mid-way, multiple project
  pivots. Mitigation: the parking lot + phase-gate-only reviews. New shiny idea ≠ plan change.
- **10–15 hrs/wk is thin.** Hence: one spine, one artifact, buffers, and a gate that cuts
  scope instead of slipping dates.
- **Altagic/CCPS surges.** If a week collapses, the no-AI rep and notes survive (2.5 h);
  the project milestone shifts into the buffer. Never skip the reps — they're the compound
  interest.
- **Claude-dependence during the plan itself.** The operating system in §1 is the defense;
  if Rudra notices Claude writing code he should be writing, call it out — that's a
  standing instruction.
