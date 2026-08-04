# 트러블슈팅

- 전체 `git diff --check`는 기존 `AGENTS.md` EOF 빈 줄 변경 때문에 실패할 수 있어, 이번 Task 변경 파일인 `cli/app.py`, `core/game.py`, `core/interfaces.py`, `core/storage.py` 대상으로 공백 검사를 수행했다.
- 손상 파일 안내 검증은 실제 프로젝트 `state.json`을 망가뜨리지 않기 위해 `/private/tmp/codyssey_broken_state_for_check.json` 임시 파일로 수행했다.
- 재시작 유지 검증 과정에서 프로젝트 루트의 ignored `state.json`에 `저장 검증용 문제는?` 테스트 퀴즈가 추가되었다.
