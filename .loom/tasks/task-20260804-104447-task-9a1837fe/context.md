# Context

## Loom 코드 계약

아래 항목은 Loom 코드에 고정된 runtime 동작 계약입니다. 관련 흐름을 바꾸기 전 `loom contract show <id>`로 확인합니다.

- `task-execution`: Task 실행 전 prompt/context/previous-results에 들어가는 입력 경계입니다. 명령: `loom contract show task-execution`. Source: `loom/application/context_pack.py`, `loom/application/team_policy.py`
- `done-guardrail`: Task를 DONE으로 인정하기 전에 필요한 산출물과 상태 전이를 검증하는 계약입니다. 명령: `loom contract show done-guardrail`. Source: `loom/application/services.py`

## Project Memory

# Codyssey_E1_2

Loom 프로젝트 메모리 루트입니다.

이 파일은 `loom init`으로 생성되며 `loom analyze-repo`로 보강할 수 있습니다.

## Workspace Policy

- Output language: `ko`
- Agent provider: `claude`
- Agent model: `adapter-default`
- Reasoning effort: `high`
- Required branch: `develop`
- Dirty branch switch: `blocked`
- Commit policy: `manual`
- Include `.loom` metadata in Git: `yes`
- Read-only parallel execution: `allowed`
- Validation environment: `auto`
- Previous Task result limit: `2`
- Workspace required docs: -
- Loom fixed guardrails and verified Team required policies take precedence over this Workspace Policy.

## Job

- Title: Python 콘솔 퀴즈 게임 미션 구현
- Goal: Python 콘솔 퀴즈 게임을 core/cli 분리 구조로 구현하고 README, state.json 영속성, Git/GitHub workflow 요구사항을 충족한다.
- Branch: develop
- Task count: `5`

## Task

- Title: 현재 설계 구조 문서화와 미션 조건 재점검
- Description: 현재 core/cli 분리 설계를 doc 아래 Markdown 문서로 고정하고, 미션 요구사항 대비 현재 충족/미충족 상태를 점검한다.
- Expected output: doc/architecture.md가 생성되고 현재 설계 구조, 의존 방향, 파일 역할, 미션 조건 점검표가 포함된다. Loom proposal에도 설계 문서 추가 제안이 남아 있다.
- Done condition: 문서가 저장되고 Loom docs index 또는 파일 확인이 가능하며, 미션 조건 점검 결과와 후속 작업이 기록되고 커밋되어 있다.
- In scope: 설계 구조 문서, 미션 조건 적합성 점검, Loom memory proposal 생성, docs index 갱신
- Out of scope: 퀴즈 풀이/추가 기능 구현, GitHub 원격 push, 스크린샷 생성
- Validation hint: doc/architecture.md 내용을 확인하고 loom validate --strict 및 git status를 확인한다.
- Required docs: -
- Memory refs: -
- Source proposal: `-`
- Status: PENDING
- Assigned agent: codex

## Advisor Source Prompt

No Advisor source prompt recorded for this Task.

## Inclusion Policy

- Mandatory execution files: `prompt.md`, `context.md`, and `previous-results.md`.
- Always included: project memory, current Job/Task metadata, and Job notes.
- Previous results: up to the latest 2 recorded results from earlier Tasks in this Job.
- Job context refs: explicit Job-scoped references selected by the controlling agent or user.
- Task required docs: mandatory Task-scoped documents; missing refs block validation and execution.
- Task memory refs: mandatory Task-scoped workflow memory references; missing or non-memory refs block validation and execution.
- Repository documents, validation documents, and skill rules: included only through explicit Job context refs, Task required docs, or Task memory refs.
- Verified Team Policy Snapshot: included before Active Memory; required policy cannot be overridden by lower-priority context.
- Active workflow memory with an `always` category is included automatically while its status is `ACTIVE`.
- `task_selected` and `reference_only` memory is included only through explicit Task memory refs.
- Consumed proposals, rejected proposals, resolved memory, superseded memory, and archived memory are excluded.
- Unreferenced repository files and results from other Jobs are not included.
- `AGENTS.md` and `CLAUDE.md` remain session-level controlling-agent entrypoints and are not treated as task context artifacts by default.

## Job Notes

# Notes

## Context References

No explicit context references recorded for this job.

## Required Documents and Memory

No task-level required docs or memory refs recorded.

## Verified Team Policies

No verified Team Policy Snapshot is active.

## Active Workflow Memory

No active workflow memory recorded.
