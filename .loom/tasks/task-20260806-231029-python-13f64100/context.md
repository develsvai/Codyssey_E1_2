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

- Title: Python 시험 대비 총정리 문서 작성
- Goal: 미션 원문, README, 학습 목표 문서, 실제 구현 코드를 기반으로 Python 기초 시험에 대비할 수 있는 총정리 문서를 작성하고 README에서 접근 가능하게 한다.
- Branch: develop
- Task count: `1`

## Task

- Title: Python 시험 예상 내용 총정리 문서 추가
- Description: 미션 원문과 레포 학습 자료, 실제 구현 코드를 바탕으로 Python 기초 시험에 나올 가능성이 높은 내용을 우선순위별로 정리한 문서를 doc/ 아래에 추가하고 README에서 링크한다.
- Expected output: doc/python-exam-summary.md에 클래스, 기본 문법, JSON 파일 입출력, 예외 처리, 실행 흐름, Git 기초를 한 번에 복습할 수 있는 총정리 문서가 추가되고 README 설계 문서 섹션에서 접근할 수 있다.
- Done condition: 문서 추가, README 링크 반영, Markdown 링크/파일 경로 확인, git diff --check, loom validate --strict, 커밋 및 Loom finish 기록 커밋이 완료되어 있다.
- In scope: doc/python-exam-summary.md 작성, README 링크 추가, 기존 학습 문서와 코드 근거 반영
- Out of scope: Python 코드 동작 변경, 미션 구현 변경, GitHub push, 시험 문제 생성기 구현
- Validation hint: rg로 README 링크와 주요 섹션을 확인하고 git diff --check 및 loom validate --strict를 실행한다.
- Required docs: -
- Memory refs: -
- Source proposal: `-`
- Status: PENDING
- Assigned agent: foreground

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

### 설계 구조 문서를 구현 기준으로 유지

- ID: `memory-20260804-104931-memory-47cda9f4`
- Type: `principles`
- Category: `principle`
- Source proposal: `proposal-20260804-104625-proposal-85a42753`

doc/architecture.md를 현재 core/cli 분리 설계의 기준 문서로 두고, 후속 구현 Task에서 의존 방향(cli -> core), core의 CLI 비의존성, StateRepository 저장 경계를 유지하도록 참조한다.
