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

- Title: README와 Git workflow 제출 조건 정리
- Description: README를 최종 요구사항에 맞게 보강하고, Git 커밋 수/브랜치 병합/clone/pull 실습/제출 스크린샷 준비 상태를 점검한다.
- Expected output: README가 최종 제출 체크리스트를 충족하고 Git workflow 요구사항의 남은 항목이 명확히 정리되어 있다.
- Done condition: README 검토, git log 확인, 필요한 문서 변경 커밋이 완료되고 사용자가 수행해야 할 GitHub/스크린샷 항목이 보고되어 있다.
- In scope: README 보강, 파일 구조/실행 방법/데이터 스키마 설명, Git 이력 점검, 제출 체크리스트 정리
- Out of scope: 사용자 GitHub 계정 인증이 필요한 원격 작업 대행, 실제 스크린샷 촬영
- Validation hint: README 항목과 git log --oneline --graph 결과를 확인한다.
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

### 설계 구조 문서를 구현 기준으로 유지

- ID: `memory-20260804-104931-memory-47cda9f4`
- Type: `principles`
- Category: `principle`
- Source proposal: `proposal-20260804-104625-proposal-85a42753`

doc/architecture.md를 현재 core/cli 분리 설계의 기준 문서로 두고, 후속 구현 Task에서 의존 방향(cli -> core), core의 CLI 비의존성, StateRepository 저장 경계를 유지하도록 참조한다.
