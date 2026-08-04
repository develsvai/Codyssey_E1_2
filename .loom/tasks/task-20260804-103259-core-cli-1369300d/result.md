# 결과

- `main.py` 엔트리포인트를 만들고 `cli -> core` 방향으로 앱을 조립했다.
- `core` 패키지에 `Quiz`, `GameState`, `QuizGame`, `StateRepository`, `JsonStateRepository` 골격을 추가했다.
- `cli` 패키지에 콘솔 메뉴 루프와 기본 입력 검증, 안전 종료 흐름을 추가했다.
- `README.md` 초안을 작성하고 실행 방법, 구조, 데이터 파일 스키마를 정리했다.
- `.gitignore`를 추가해 Python 캐시, 가상환경, 런타임 `state.json`을 제외했다.

## 검증

- `python3 -m compileall .` 통과.
- `python3 main.py` 실행 후 메뉴 출력 확인.
- 메뉴에서 `3` 입력 시 기본 퀴즈 5개 목록 출력 확인.
- 메뉴에서 `5` 입력 시 저장 후 정상 종료 확인.

## 남은 작업

- 퀴즈 풀기와 퀴즈 추가는 이번 Task 범위 밖이라 다음 Task에서 완성해야 한다.
- GitHub `clone`/`pull` 실습과 제출 스크린샷도 후속 Task로 분리해야 한다.
- 현재 환경에는 `python` 명령 alias가 없어 `python3`로 검증했다.
