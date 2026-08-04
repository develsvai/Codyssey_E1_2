# 트러블슈팅

- `loom docs index --json`은 기본 `docs/` 경로와 `.loom/memory` 문서만 인덱싱했고, 사용자가 요청한 `doc/architecture.md`는 인덱스에 포함하지 않았다.
- `.loom` 설정을 직접 수정하지 않고, 요청 경로인 `doc/`를 유지했다. 필요하면 후속 작업에서 Loom 설정 명령으로 docs 경로 정책을 별도 변경해야 한다.
