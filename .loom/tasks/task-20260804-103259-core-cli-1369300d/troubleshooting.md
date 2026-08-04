# 트러블슈팅

- 첫 `loom task run`은 Job/Task 생성으로 생긴 `.loom` 메타데이터가 커밋되지 않아 브랜치 전환 전에 차단되었다. `.loom` workflow 설정을 `Chore: Loom workflow setup` 커밋으로 먼저 기록한 뒤 Task run을 다시 열었다.
- sandbox 환경에서 `git add`가 `.git/index.lock`을 만들 수 없어 승인 기반 권한으로 Git index 쓰기를 수행했다.
- 현재 셸에는 `python` 명령이 없어 `python main.py`를 그대로 실행할 수 없었다. 설치된 `Python 3.14.4`의 `python3` 명령으로 `python3 -m compileall .` 및 `python3 main.py`를 검증했고, README 실행 명령도 `python3 main.py`로 맞췄다.
