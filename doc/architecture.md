# 설계 구조 문서

## 목적

이 문서는 Python 콘솔 퀴즈 게임 미션의 현재 설계 구조를 고정하고, 이후 구현 작업에서 지켜야 할 의존 방향과 역할 분리를 명확히 하기 위해 작성한다.

현재 설계의 핵심 원칙은 다음과 같다.

- 사용자 입출력은 `cli` 패키지에서만 처리한다.
- 게임 규칙, 퀴즈 모델, 저장 경계는 `core` 패키지에 둔다.
- `core`는 `cli`를 import하지 않는다.
- `main.py`는 객체를 조립하고 실행을 시작하는 진입점 역할만 한다.
- 저장 구현은 추상 인터페이스 뒤에 둬서 core 로직과 파일 저장 방식을 분리한다.

## 현재 파일 구조

```text
main.py
core/
  __init__.py
  interfaces.py
  models.py
  game.py
  storage.py
cli/
  __init__.py
  app.py
README.md
.gitignore
state.json
```

`state.json`은 프로그램 실행 중 생성되는 런타임 데이터 파일이다. 현재 `.gitignore`에 포함되어 있어 저장소에는 커밋하지 않는다.

## 의존 방향

```text
main.py
  -> cli.app
  -> core.game
  -> core.storage

cli.app
  -> core.game

core.game
  -> core.interfaces
  -> core.models

core.storage
  -> core.interfaces
  -> core.models

core.models
  -> 표준 라이브러리
```

금지할 의존 방향은 다음과 같다.

```text
core -> cli
core.models -> core.game
core.models -> core.storage
```

## 패키지별 책임

### `main.py`

앱의 조립 지점이다. `JsonStateRepository`, `QuizGame`, `QuizCli`를 생성하고 CLI 실행을 시작한다.

현재 역할:

- `state.json` 경로 결정
- 저장소 구현체 생성
- 게임 객체 생성
- CLI 객체 생성
- 프로세스 종료 코드 반환

### `core.models`

도메인 데이터를 표현한다.

현재 클래스:

- `Quiz`: 개별 퀴즈의 문제, 선택지 4개, 정답 번호를 가진다.
- `GameState`: 퀴즈 목록과 최고 점수를 가진다.

`Quiz`는 생성 시 다음 불변 조건을 검증한다.

- 문제는 빈 문자열일 수 없다.
- 선택지는 정확히 4개여야 한다.
- 선택지는 빈 문자열일 수 없다.
- 정답 번호는 1부터 4 사이여야 한다.

### `core.interfaces`

core가 외부 저장 방식에 의존하지 않도록 추상 경계를 정의한다.

현재 인터페이스:

- `StateRepository`
  - `load() -> LoadResult`
  - `save(state: GameState) -> None`

`LoadResult`는 저장 파일의 로드 상태를 다음처럼 구분한다.

- `LOADED`: 저장된 상태를 정상 로드
- `MISSING`: 저장 파일 없음
- `RECOVERED`: JSON 손상 또는 스키마 오류로 기본 상태 복구 필요
- `ERROR`: 읽기 오류로 기본 상태 사용 필요

### `core.storage`

파일 저장 구현체를 둔다.

현재 클래스:

- `JsonStateRepository`

현재 역할:

- 프로젝트 루트의 `state.json` 읽기
- JSON 데이터를 `GameState`와 `Quiz`로 변환
- `GameState`를 JSON 형태로 저장
- 파일 없음, JSON 손상, 타입 오류, 스키마 오류, 읽기 오류를 `LoadResult`로 구분

### `core.game`

게임 상태와 유스케이스를 조율한다.

현재 클래스:

- `QuizGame`

현재 역할:

- 저장된 상태 불러오기
- 저장된 상태가 없으면 기본 퀴즈 5개 사용
- 퀴즈 목록 조회
- 퀴즈 추가 및 저장 실패 시 rollback
- 정답 수를 100점 기준 점수로 환산
- 최고 점수 갱신 및 저장
- 현재 상태 저장

### `cli.app`

사용자와 직접 만나는 콘솔 어댑터다.

현재 클래스:

- `QuizCli`

현재 역할:

- 메뉴 출력
- 메뉴 번호 입력
- 빈 입력, 숫자 변환 실패, 범위 밖 입력 처리
- `KeyboardInterrupt`, `EOFError` 발생 시 저장 후 안전 종료
- 저장 파일 상태별 시작 안내
- 퀴즈 풀이 진행
- 퀴즈 추가 입력과 검증
- 퀴즈 목록 출력
- 최고 점수 출력
- 종료 시 저장

## `state.json` 스키마

현재 저장 스키마는 다음 형태를 기준으로 한다.

```json
{
  "quizzes": [
    {
      "question": "Python의 창시자는?",
      "choices": ["Guido", "Linus", "Bjarne", "James"],
      "answer": 1
    }
  ],
  "best_score": 0
}
```

필드 규칙:

- `quizzes`: 퀴즈 객체 배열
- `quizzes[].question`: 문제 문자열
- `quizzes[].choices`: 선택지 4개를 담은 문자열 배열
- `quizzes[].answer`: 1부터 4 사이의 정답 번호
- `best_score`: 0부터 100 사이의 최고 점수

## 미션 조건 부합성 점검

이 표는 현재 커밋 기준의 구현 상태와 제출 전 사용자가 수행해야 할 항목을 구분한다.

| 미션 조건 | 현재 상태 | 근거 | 후속 작업 |
| --- | --- | --- | --- |
| Python 콘솔 프로그램 1개 | 충족 | `python3 main.py` 실행 시 콘솔 메뉴가 출력된다. | 없음. |
| 메뉴에서 퀴즈 출제/등록/목록/점수/종료 선택 | 충족 | 메뉴 1~5번이 각각 퀴즈 풀기, 추가, 목록, 점수, 종료로 동작한다. | 없음. |
| 퀴즈 풀기 기능 | 충족 | 저장된 퀴즈를 순서대로 출제하고 정답/오답과 결과 점수를 출력한다. | 없음. |
| 퀴즈 추가 기능 | 충족 | 문제, 선택지 4개, 정답 번호를 입력받아 저장한다. | 없음. |
| 퀴즈 목록 기능 | 충족 | 등록된 퀴즈 제목과 총 개수를 출력하고 빈 목록을 처리한다. | 없음. |
| 점수 확인 기능 | 충족 | 퀴즈 풀이 후 최고 점수를 갱신하고 메뉴 4번에서 출력한다. | 없음. |
| 본인 선택 주제 퀴즈 5개 이상 | 충족 | Python, Git, JSON 기초 주제로 기본 퀴즈 5개가 있고 README에 선정 이유를 적었다. | 없음. |
| 종료 후 추가 퀴즈와 최고 점수 유지 | 충족 | `JsonStateRepository`가 `state.json`에 퀴즈와 최고 점수를 저장하고 재시작 시 불러온다. | 없음. |
| 최소 2개 이상의 클래스 | 충족 | `Quiz`, `GameState`, `QuizGame`, `JsonStateRepository`, `QuizCli`가 있다. | 없음. |
| 기능별 메서드 분리 | 충족 | 메뉴 처리, 입력 검증, 풀이, 추가, 목록, 점수, 저장 책임이 메서드와 클래스로 분리되어 있다. | 없음. |
| `state.json` UTF-8 저장/불러오기 | 충족 | `core/storage.py`가 UTF-8로 읽고 쓰며 `ensure_ascii=False`로 저장한다. | 없음. |
| 잘못된 숫자 입력 처리 | 충족 | 메뉴, 정답, 퀴즈 추가 정답 번호에서 빈 값, 숫자 변환 실패, 범위 밖 숫자를 처리한다. | 없음. |
| `KeyboardInterrupt`, `EOFError` 안전 종료 | 충족 | 메뉴, 풀이, 추가 입력 중 발생 시 저장 후 종료한다. | 없음. |
| 데이터 파일 없음/손상 처리 | 충족 | `LoadStatus`로 파일 없음/손상/오류를 구분하고 CLI에서 안내한다. | 없음. |
| README 필수 항목 | 충족 | README에 개요, 주제, 실행 방법, 기능, 구조, 데이터 파일 설명을 포함했다. | 없음. |
| GitHub 저장소 업로드 | 부분 충족 | `origin` 원격 저장소는 연결되어 있다. | 사용자 인증 후 `git push origin develop` 및 제출 URL 확인이 필요하다. |
| 최소 10개 이상 의미 있는 커밋 | 충족 | 현재 `develop` 기준 12개 커밋이 있다. | 없음. |
| 브랜치 생성 및 병합 기록 | 부분 충족 | `develop` 브랜치에서 기능 작업을 진행했다. | 최종 제출 전에 `develop`을 `master` 또는 제출 기준 브랜치로 병합해야 한다. |
| Git 기초 명령어 7종 사용 | 부분 충족 | 현재 저장소에서 `add`, `commit`, `checkout` 계열 흐름은 확인된다. | 제출 전 `init`, `push`, `clone`, `pull` 사용 여부를 사용자 환경에서 확인한다. |
| `clone`, `pull` 실습 기록 | 미충족 | 사용자 GitHub 인증이 필요한 별도 실습이라 아직 수행하지 않았다. | `doc/submission-checklist.md` 절차에 따라 별도 디렉터리에서 수행한다. |
| 제출 스크린샷 | 미충족 | 실제 화면 캡처는 아직 생성하지 않았다. | 실행 화면, 환경 설정, `git log --oneline --graph --decorate` 화면을 캡처한다. |

## 현재 결론

현재 구현은 Python 콘솔 퀴즈 게임의 기능 요구사항에 부합한다.

- 클래스 2개 이상 요구사항을 충족한다.
- `Quiz`와 `QuizGame` 중심 구조를 유지한다.
- CLI를 분리해 사용자 입출력과 core 로직의 경계를 명확히 했다.
- `StateRepository` 인터페이스로 저장소 구현을 분리했다.
- 기본 퀴즈 5개, 퀴즈 풀이, 퀴즈 추가, 최고 점수, `state.json` 영속성이 동작한다.

남은 항목은 코드 구현이 아니라 제출 절차에 가깝다. GitHub push, 최종 브랜치 병합, `clone`/`pull` 실습, 스크린샷 촬영은 사용자 인증과 실제 화면 캡처가 필요하므로 제출 직전에 수행한다.

제출 전 우선순위는 다음과 같다.

1. `develop` 변경사항을 GitHub에 push
2. `develop`을 `master` 또는 제출 기준 브랜치로 병합
3. 별도 디렉터리에서 `clone`/`pull` 실습
4. 실행 화면, 개발 환경, Git log 스크린샷 준비
