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
- Task count: `1`

## Task

- Title: core/cli 분리 프로젝트 구조 잡기
- Description: 미션 요구사항을 바탕으로 core 하위에 모델, 게임 조율, 저장소 인터페이스/구현을 두고 cli 하위에 콘솔 진입 어댑터를 둔 초기 Python 구조를 만든다.
- Expected output: main.py, core 패키지, cli 패키지, .gitignore, README 초안이 생성되고 의존 방향이 cli -> core로 정리되어 있다.
- Done condition: python main.py가 실행 가능한 메뉴 골격을 보여주고, python -m compileall . 검증이 통과하며, 구조 생성 변경이 커밋되어 있다.
- In scope: 프로젝트 폴더 구조, 핵심 클래스/인터페이스 골격, CLI 엔트리포인트, README 초안, .gitignore
- Out of scope: 전체 퀴즈 플레이 기능 완성, GitHub clone/pull 실습, 스크린샷 제출물 생성
- Validation hint: python -m compileall . 및 python main.py의 기본 실행 흐름을 확인한다.
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
