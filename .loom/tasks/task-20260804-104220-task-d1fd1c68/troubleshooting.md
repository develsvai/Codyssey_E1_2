# 트러블슈팅

- 전체 `git diff --check`는 `AGENTS.md`의 기존 EOF 빈 줄 변경 때문에 실패했다. 이번 Task에서 수정한 `cli/app.py`, `core/game.py`만 대상으로 한 `git diff --check -- cli/app.py core/game.py`는 통과했다.
- 수동 검증 중 생성/갱신된 `state.json`은 런타임 데이터이며 `.gitignore` 대상이라 커밋하지 않는다.
