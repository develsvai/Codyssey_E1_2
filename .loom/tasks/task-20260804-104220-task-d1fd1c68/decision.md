# 결정

- Active Memory `memory-20260804-104931-memory-47cda9f4`에 따라 `core`가 `cli`를 import하지 않는 방향을 유지했다.
- 점수는 사용자에게 `점`으로 보여주기 위해 정답률 기반 0~100점으로 계산했다.
- 점수 계산은 게임 규칙으로 보고 `QuizGame.calculate_score()`에 두었다.
- 사용자 입출력, 재입력 루프, 정답/오답 출력은 `cli.app.QuizCli`에 두었다.
- 메뉴 입력과 정답 입력의 중복 검증을 줄이기 위해 `_read_number()`로 공통화했다.
