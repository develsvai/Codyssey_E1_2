# 과제 목표와 레포 구조 근거

## 목적

이 문서는 입학 연수 과제 목표를 이 레포의 실제 구조와 연결해서 설명하기 위해 작성한다. 단순히 “기능이 된다”가 아니라, Python 기초, 클래스와 객체, 파일 입출력, Git 기초 질문에 대해 어떤 코드와 구조를 근거로 설명할 수 있는지 정리한다.

## 설계 의도 요약

### 사용자의 생각

문제에서는 단순히 두 개의 클래스를 정의하라고 했지만, 이 레포는 그 요구를 최소한으로만 맞추는 대신 역할이 보이는 구조로 잡았다.

- `core` 아래에 `Quiz`, `QuizGame` 중심 모델과 게임 로직을 둔다.
- 저장 방식은 `StateRepository` 인터페이스로 경계를 잡아 필요한 메서드 구현을 강제한다.
- 사용자 입출력은 `/cli`에 따로 두어 콘솔 진입성을 분리한다.
- 의존 방향은 아래로 흐르게 유지한다. 즉, CLI가 core를 사용하지만 core가 CLI를 알지는 않는다.
- Loom을 기준 workflow로 고정해 설계, 구현, 검증, 커밋 기록이 흩어지지 않게 한다.

### Codex 보충 판단

이 구조는 과제 난이도에 비해 과하게 복잡하지 않으면서도, 학습 목표를 설명하기 좋은 단위를 만든다.

- `Quiz`는 “하나의 문제 데이터”를 설명하는 클래스다.
- `QuizGame`은 “게임 상태와 규칙”을 설명하는 클래스다.
- `QuizCli`는 “사용자와 대화하는 콘솔 어댑터”다.
- `JsonStateRepository`는 “파일 저장 방식”을 담당한다.
- `main.py`는 여러 객체를 조립하는 시작점으로만 둔다.

이렇게 나누면 메뉴 출력, 정답 검증, 점수 계산, JSON 저장을 한 파일이나 한 함수에 몰아넣지 않아도 된다. 그래서 기능별 함수 분리, 클래스 책임 분리, 파일 입출력 오류 처리라는 과제 목표를 코드 구조 자체로 설명할 수 있다.

## 전체 구조 근거

```text
main.py
  -> cli.app.QuizCli
  -> core.game.QuizGame
  -> core.storage.JsonStateRepository

cli.app
  -> core.game
  -> core.models
  -> core.interfaces

core.game
  -> core.interfaces
  -> core.models

core.storage
  -> core.interfaces
  -> core.models

core.models
  -> 표준 라이브러리
```

핵심은 `core`가 `cli`를 import하지 않는다는 점이다. 그래서 콘솔 출력 문구가 바뀌어도 `Quiz`, `QuizGame`, `JsonStateRepository`의 핵심 규칙은 유지된다.

## Python 기초 목표와 구조적 근거

| 과제 목표 | 레포에서의 근거 | 설명 포인트 |
| --- | --- | --- |
| 변수가 무엇이고 왜 사용하는지 | `cli/app.py`의 `choice`, `answer`, `correct_count`, `score`, `core/game.py`의 `_state`, `_repository` | 값에 이름을 붙여 메뉴 선택, 정답 수, 점수, 저장소 상태를 추적한다. |
| `int`, `str`, `bool`, `list`, `dict`의 차이 | `Quiz.answer: int`, `Quiz.question: str`, `QuizGame.record_score() -> bool`, `GameState.quizzes: list[Quiz]`, `Quiz.to_dict() -> dict` | 숫자, 문자열, 참/거짓, 여러 값의 묶음, 키-값 구조가 각각 다른 역할로 쓰인다. |
| `if/elif/else` 조건 처리 | `QuizCli._handle_choice()`, `_print_load_message()`, `_read_number()`, `Quiz.__post_init__()` | 메뉴 번호, 저장 파일 상태, 입력 오류, 퀴즈 유효성을 조건에 따라 다르게 처리한다. |
| `for`와 `while`의 차이 | `QuizCli.run()`과 `_read_number()`의 `while`, `_play_quizzes()`와 `_add_quiz()`의 `for` | `while`은 사용자가 종료하거나 올바른 입력을 할 때까지 반복하고, `for`는 정해진 퀴즈/선택지 개수만큼 반복한다. |
| 함수 정의, 매개변수, 반환값 | `main() -> int`, `QuizGame.calculate_score(correct_count, total_count) -> int`, `_read_number(prompt, minimum, maximum) -> int 또는 None` | 입력값을 받아 처리하고 결과를 반환하는 흐름을 메서드 단위로 나누었다. |

### 설명 예시

이 레포에서 변수는 단순히 값을 담는 통이 아니라 프로그램 흐름을 설명하는 이름이다. 예를 들어 `correct_count`는 맞힌 문제 수를 기억하고, `score`는 점수 계산 결과를 저장한다. `if/elif/else`는 메뉴 번호나 저장 파일 상태에 따라 서로 다른 동작을 선택할 때 사용한다. `for`는 등록된 퀴즈를 순서대로 낼 때 적합하고, `while`은 사용자가 올바른 입력을 할 때까지 계속 묻는 상황에 적합하다.

## 클래스와 객체 목표와 구조적 근거

| 과제 목표 | 레포에서의 근거 | 설명 포인트 |
| --- | --- | --- |
| 클래스가 무엇이고 왜 사용하는지 | `Quiz`, `GameState`, `QuizGame`, `JsonStateRepository`, `QuizCli` | 관련 데이터와 동작을 한 책임 단위로 묶기 위해 사용한다. |
| `__init__`과 `self`의 역할 | `QuizGame.__init__()`, `JsonStateRepository.__init__()`, `QuizCli.__init__()` | 객체가 만들어질 때 필요한 의존성과 초기 상태를 저장한다. `self`는 현재 객체 자신의 속성과 메서드에 접근하는 이름이다. |
| 속성과 메서드 정의 및 활용 | `Quiz.question`, `Quiz.choices`, `Quiz.answer`, `Quiz.is_correct()`, `QuizGame.add_quiz()`, `QuizCli._play_quizzes()` | 속성은 객체가 가진 데이터이고, 메서드는 그 데이터로 수행하는 행동이다. |

### 왜 클래스를 이렇게 나눴는가

`Quiz`와 `QuizGame`만으로도 과제의 최소 클래스 요구사항은 만족할 수 있다. 하지만 실제 프로그램을 만들면 사용자 입력, 저장 파일, 게임 규칙이 서로 다른 이유로 바뀔 수 있다. 그래서 아래처럼 책임을 나눴다.

- `Quiz`: 문제, 선택지, 정답이라는 퀴즈 한 개의 데이터와 정답 판정.
- `GameState`: 퀴즈 목록과 최고 점수라는 저장 가능한 전체 상태.
- `QuizGame`: 퀴즈 추가, 점수 계산, 최고 점수 갱신, 저장 호출.
- `QuizCli`: 메뉴 출력, 입력 검증, 사용자 안내.
- `JsonStateRepository`: JSON 파일 읽기와 쓰기.

이 구조는 “클래스는 왜 필요한가?”라는 질문에 답하기 좋다. 한 클래스가 모든 일을 하는 대신, 각 클래스가 바뀌는 이유를 하나씩 갖도록 나누었기 때문이다.

## 파일 입출력 목표와 구조적 근거

| 과제 목표 | 레포에서의 근거 | 설명 포인트 |
| --- | --- | --- |
| 파일 열기, 읽기, 쓰기 과정 | `JsonStateRepository.load()`, `JsonStateRepository.save()` | `Path.read_text()`로 읽고 `Path.write_text()`로 저장한다. |
| JSON 형식과 사용 이유 | `Quiz.to_dict()`, `Quiz.from_dict()`, `json.loads()`, `json.dumps()` | 객체 상태를 문자열 기반의 저장 가능한 구조로 바꿔 `state.json`에 보관한다. |
| `try/except` 오류 처리 | `JsonStateRepository.load()`, `QuizCli._read_number()`, `QuizCli._save_before_exit()` | 파일 없음, JSON 손상, 읽기 오류, 잘못된 입력, 저장 실패를 프로그램이 중단되지 않게 처리한다. |

### 왜 저장소 인터페이스를 뒀는가

`StateRepository`는 core가 “어디에 저장하는지”보다 “저장하고 불러올 수 있다”는 약속에 의존하게 만든다. 현재 구현은 `JsonStateRepository` 하나뿐이지만, 이 경계를 두면 나중에 저장 방식이 바뀌어도 `QuizGame`의 규칙을 크게 바꾸지 않아도 된다.

이 과제에서는 JSON 파일 저장이 핵심이므로 실제 구현은 단순하게 유지했다. 다만 저장 실패와 손상 파일 복구 안내는 사용자 경험에 직접 영향을 주기 때문에 `LoadResult`, `LoadStatus`로 상태를 구분했다.

## Git 기초 목표와 레포 근거

| 과제 목표 | 레포에서의 근거 | 설명 포인트 |
| --- | --- | --- |
| Git이 무엇이고 왜 필요한지 | 기능 단위 커밋 이력, Loom 작업 기록 커밋 | 변경 과정을 되돌아보고, 기능별 작업 단위를 추적하기 위해 사용한다. |
| `init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone` 설명 | `doc/submission-checklist.md`의 Git 명령어 체크 | 각 명령의 역할과 제출 전 수행할 흐름을 문서로 정리했다. |
| 브랜치 생성과 병합 | `develop` 브랜치 작업 이력, 최종 제출 전 병합 항목 | 기능 작업은 `develop`에서 진행하고, 제출 기준 브랜치로 병합해야 한다. |
| 원격 저장소 clone/pull | `doc/submission-checklist.md`의 clone/pull 실습 절차 | 별도 디렉터리에서 원격 저장소를 복제하고 기존 작업 디렉터리에서 변경사항을 가져오는 흐름을 설명한다. |

Git은 Python 코드 안에서 실행되는 기능이 아니라 프로젝트를 관리하는 방법이다. 이 레포에서는 기능 구현, 문서화, Loom 완료 기록이 모두 커밋 단위로 남아 있다. 그래서 “Git은 왜 필요한가?”라는 질문에는 “내가 어떤 기능을 언제, 왜 바꿨는지 추적하기 위해 필요하다”고 설명할 수 있다.

## 질문에 답할 때 사용할 수 있는 구조적 설명

### 왜 `core`와 `cli`를 분리했는가

콘솔 입출력과 게임 규칙은 바뀌는 이유가 다르다. 메뉴 문구나 입력 방식은 `cli`의 관심사이고, 정답 판정과 점수 계산은 `core`의 관심사다. 둘을 분리하면 콘솔 화면을 고쳐도 게임 규칙은 흔들리지 않는다.

### 왜 `QuizGame` 안에 모든 기능을 넣지 않았는가

`QuizGame`이 메뉴 출력, 입력, 파일 저장, 점수 계산을 모두 담당하면 클래스 하나가 너무 많은 이유로 바뀐다. 그래서 `QuizGame`은 게임 규칙과 상태 조율만 맡고, `QuizCli`는 사용자 입력, `JsonStateRepository`는 파일 저장을 맡도록 나눴다.

### 왜 `StateRepository` 인터페이스가 필요한가

저장 구현을 바로 `QuizGame`에 넣으면 게임 규칙이 파일 시스템과 강하게 묶인다. `StateRepository`를 두면 `QuizGame`은 `load()`와 `save()`라는 약속만 알면 된다. 이 방식은 “구현을 강제한다”는 사용자의 생각과도 맞고, 저장 방식이 바뀔 때 수정 범위를 줄이는 효과도 있다.

### 왜 `main.py`는 짧게 두었는가

`main.py`는 프로그램을 시작하기 위한 조립 지점이다. `JsonStateRepository`, `QuizGame`, `QuizCli` 객체를 만들고 실행할 뿐이다. 시작점이 짧으면 실제 기능이 어느 파일에 있는지 찾기 쉽고, 책임 분리가 더 분명해진다.

## 결론

이 레포의 구조는 과제 목표를 설명하기 위한 근거를 코드 안에 남기는 방향으로 구성되어 있다.

- Python 기초는 입력 처리, 조건문, 반복문, 함수 반환값에서 확인할 수 있다.
- 클래스와 객체는 `Quiz`, `QuizGame`, `QuizCli`, `JsonStateRepository`의 책임 분리에서 확인할 수 있다.
- 파일 입출력은 `state.json`을 읽고 쓰는 저장소 구현에서 확인할 수 있다.
- Git 기초는 기능 단위 커밋, `develop` 브랜치 작업, 제출 체크리스트에서 확인할 수 있다.

따라서 이 프로젝트는 단순히 퀴즈 게임을 완성한 결과물이 아니라, 각 학습 목표를 실제 코드 구조와 연결해서 설명할 수 있도록 만든 학습용 레포다.
