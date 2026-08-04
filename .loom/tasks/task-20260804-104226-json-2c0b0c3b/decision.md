# 결정

- Active Memory `memory-20260804-104931-memory-47cda9f4`에 따라 `core`의 CLI 비의존성을 유지했다.
- 저장소 로드 결과는 `LoadStatus`와 `LoadResult`로 표현해 core 저장 경계를 유지하면서 CLI가 사용자 안내를 결정할 수 있게 했다.
- `state.json` 파일이 손상되었거나 스키마가 맞지 않으면 기본 퀴즈로 복구하는 흐름을 유지했다.
- 저장 실패 시 추가된 퀴즈를 rollback하여 메모리 상태와 파일 상태가 엇갈리지 않도록 했다.
- 테스트로 추가된 `state.json` 데이터는 런타임 상태이며 `.gitignore` 대상이라 커밋하지 않는다.
