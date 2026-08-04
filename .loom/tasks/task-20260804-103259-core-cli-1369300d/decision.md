# 결정

- `core`는 `cli`를 import하지 않도록 유지하고, `main.py`에서 의존성을 조립한다.
- `Quiz`는 개별 문제와 정답 검증을 담당하고, `QuizGame`은 퀴즈 목록과 최고 점수 상태를 관리한다.
- 저장 경계는 `StateRepository` 추상 클래스로 두고, 파일 구현은 `JsonStateRepository`가 담당한다.
- `state.json`은 런타임 데이터로 보고 `.gitignore`에 포함했다. 기본 퀴즈 데이터는 코드 안에 둬 첫 실행과 파일 손상 복구 시 사용할 수 있게 했다.
- 이번 Task는 구조 고정이 목적이라 퀴즈 풀기와 퀴즈 추가 메뉴는 안내 메시지만 출력하도록 두었다.
