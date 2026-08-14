# 결과

- `main.py`에 최상위 `KeyboardInterrupt` 처리 흐름을 추가해 CLI 밖으로 빠진 중단도 저장 시도 후 종료하도록 보강했다.
- `README.md`에 기본 퀴즈 예시, 손상 파일 복구 정책, 스키마 버전 확장 가능성, 백업/대량 데이터 한계를 추가했다.
- `doc/architecture.md`에 오류 처리 경계, 운영 한계, 백업 전략, 최상위 안전 종료 근거를 추가했다.
- `doc/submission-checklist.md`에 커밋 메시지 기준, clone/pull 증빙, GitHub 제출 증빙, 사용자가 직접 수행해야 할 항목을 명확히 정리했다.

## 검증

- `python3 -m compileall main.py core cli`
- `printf '5\n' | python3 main.py`
- `git diff --check`
- `loom validate --strict`
