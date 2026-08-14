# 트러블슈팅

- 최초 `apply_patch`는 `doc/architecture.md` 문맥 매칭 실패로 적용되지 않았다. 파일을 다시 읽은 뒤 변경 단위를 작게 나누어 적용했다.
- `python3 -m compileall .`는 `.git`과 `.loom`까지 순회해 출력이 과하게 길었다. 실제 검증은 `python3 -m compileall main.py core cli`로 다시 수행했다.
- 커밋 수는 이번 Task 완료 커밋 이후에도 늘어나므로 문서에는 고정 숫자 대신 `20개 이상`과 확인 명령을 함께 표기했다.
