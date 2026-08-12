# Python 시험 대비 총정리

## 목적

이 문서는 입학 연수 미션과 현재 레포 구현을 기준으로 Python 기초 시험에 나올 가능성이 높은 내용을 빠르게 복습하기 위해 작성한다.

시험 범위는 깊은 알고리즘보다 아래 내용에 가까울 가능성이 높다.

1. 클래스와 객체
2. Python 기본 문법
3. 파일 입출력과 JSON
4. 입력 검증과 예외 처리
5. 프로그램 실행 흐름
6. Git 기초

가장 중요한 포인트는 "이 코드가 왜 이렇게 나뉘었는지"를 말로 설명할 수 있는 것이다.

## 0. 시험 직전 우선순위

| 우선순위 | 주제 | 봐야 할 파일 | 핵심 문장 |
| --- | --- | --- | --- |
| 1 | 클래스와 객체 | `core/models.py`, `core/game.py`, `cli/app.py` | 관련 데이터와 동작을 하나의 책임 단위로 묶기 위해 클래스를 사용한다. |
| 2 | 조건문, 반복문, 함수 | `cli/app.py`, `core/game.py` | 조건문은 상황에 따라 분기하고, 반복문은 메뉴나 퀴즈 목록을 반복 처리한다. |
| 3 | JSON 파일 저장 | `core/storage.py`, `core/models.py` | 객체 상태를 `dict`로 바꾼 뒤 JSON 문자열로 저장한다. |
| 4 | 예외 처리 | `core/storage.py`, `cli/app.py`, `main.py` | 잘못된 입력이나 파일 오류가 나도 프로그램이 바로 종료되지 않게 한다. |
| 5 | 실행 흐름 | `main.py`, `cli/app.py` | `main.py`에서 객체를 만들고 `QuizCli.run()`이 메뉴 반복을 시작한다. |
| 6 | Git | `doc/submission-checklist.md` | Git은 작업 이력을 기록하고 원격 저장소와 동기화하기 위해 사용한다. |

## 1. 클래스와 객체

### 나올 가능성

매우 높다. 미션 원문에서 최소 2개 이상의 클래스를 요구했고, 실제 구현도 여러 클래스로 역할을 나눴다.

### 반드시 알아야 할 개념

- 클래스: 객체를 만들기 위한 설계도.
- 객체: 클래스로부터 만들어진 실제 값.
- 속성: 객체가 가진 데이터.
- 메서드: 객체가 수행하는 동작.
- `self`: 현재 객체 자신을 가리키는 이름.
- `__init__`: 객체가 만들어질 때 초기값을 넣는 생성자 메서드.

### 이 레포의 클래스 역할

| 클래스 | 파일 | 역할 |
| --- | --- | --- |
| `Quiz` | `core/models.py` | 문제, 선택지, 정답을 가진 퀴즈 한 문제를 표현한다. |
| `GameState` | `core/models.py` | 퀴즈 목록과 최고 점수를 묶어 저장 가능한 상태로 표현한다. |
| `QuizGame` | `core/game.py` | 퀴즈 추가, 점수 계산, 최고 점수 갱신, 저장 호출을 담당한다. |
| `JsonStateRepository` | `core/storage.py` | `state.json` 파일을 읽고 쓰는 저장소 역할을 한다. |
| `QuizCli` | `cli/app.py` | 메뉴 출력, 사용자 입력, 안내 메시지를 담당한다. |

### 답변 템플릿

```text
클래스는 관련된 데이터와 기능을 묶기 위해 사용한다.
이 프로젝트에서 Quiz는 한 문제의 데이터와 정답 판정을 담당하고,
QuizGame은 전체 게임 상태와 점수 계산 같은 규칙을 담당한다.
역할을 나누면 한 클래스가 너무 많은 일을 하지 않아서 코드가 이해하기 쉬워진다.
```

### 코드 예시

```python
class QuizGame:
    def __init__(self, repository: StateRepository) -> None:
        self._repository = repository
        self._state = self._load_initial_state()
```

여기서 `repository`는 외부에서 받은 저장소 객체이고, `self._repository`는 현재 `QuizGame` 객체가 계속 사용할 속성이다.

## 2. Python 기본 문법

### 변수

변수는 값에 이름을 붙여 프로그램 흐름에서 다시 사용하기 위한 것이다.

예시:

- `choice`: 사용자가 선택한 메뉴 번호.
- `answer`: 사용자가 입력한 정답 번호.
- `correct_count`: 맞힌 문제 수.
- `score`: 계산된 점수.
- `_state`: 현재 퀴즈 목록과 최고 점수.

답변 템플릿:

```text
변수는 값을 저장하고 이름으로 다시 사용하기 위해 필요하다.
예를 들어 correct_count는 맞힌 문제 수를 기억하고,
score는 점수 계산 결과를 저장한다.
```

### 자료형

| 자료형 | 의미 | 이 레포의 예 |
| --- | --- | --- |
| `int` | 정수 | `answer`, `best_score`, `score` |
| `str` | 문자열 | `question`, 사용자 입력값 |
| `bool` | 참/거짓 | `record_score()`의 반환값 |
| `list` | 여러 값을 순서대로 저장 | `GameState.quizzes` |
| `tuple` | 변경하지 않을 여러 값 | `Quiz.choices` |
| `dict` | 키와 값의 묶음 | `Quiz.to_dict()` 반환값 |

### 조건문

조건문은 상황에 따라 다른 코드를 실행할 때 사용한다.

예시:

- 메뉴 번호가 `1`이면 퀴즈 풀기.
- 메뉴 번호가 `2`이면 퀴즈 추가.
- 저장 파일이 없으면 기본 퀴즈로 시작.
- 정답이면 `correct_count` 증가.

```python
if choice == 1:
    self._play_quizzes()
elif choice == 2:
    self._add_quiz()
else:
    ...
```

답변 템플릿:

```text
if/elif/else는 조건에 따라 실행할 코드를 고를 때 사용한다.
이 프로젝트에서는 메뉴 번호와 저장 파일 상태, 입력 오류를 구분하는 데 사용했다.
```

### 반복문

`while`은 조건이 참인 동안 계속 반복한다. 이 프로젝트에서는 사용자가 종료하기 전까지 메뉴를 계속 보여줄 때 쓴다.

```python
while self._running:
    self._print_menu()
```

`for`는 정해진 목록을 하나씩 처리할 때 쓴다. 이 프로젝트에서는 퀴즈 목록과 선택지를 출력할 때 쓴다.

```python
for index, quiz in enumerate(quizzes, start=1):
    print(quiz.question)
```

답변 템플릿:

```text
while은 종료 조건이 만족될 때까지 계속 반복할 때 쓰고,
for는 리스트처럼 정해진 묶음을 하나씩 순회할 때 쓴다.
```

### 함수와 메서드

함수는 특정 작업을 이름 붙여 재사용하기 위한 코드 묶음이다. 클래스 안에 정의된 함수는 메서드라고 부른다.

예시:

- `calculate_score(correct_count, total_count) -> int`
- `_read_number(prompt, minimum, maximum) -> int | None`
- `is_correct(answer) -> bool`

답변 템플릿:

```text
함수는 입력값을 받아 정해진 처리를 하고 결과를 반환할 수 있는 코드 묶음이다.
메서드는 클래스 안에 정의된 함수이며, 객체의 속성을 사용할 수 있다.
```

## 3. 파일 입출력과 JSON

### 나올 가능성

높다. 미션에서 `state.json` 저장과 불러오기를 직접 요구했다.

### 핵심 흐름

1. 프로그램 시작 시 `state.json`이 있는지 확인한다.
2. 파일이 있으면 UTF-8로 읽는다.
3. JSON 문자열을 Python 데이터로 바꾼다.
4. `Quiz`와 `GameState` 객체로 변환한다.
5. 저장할 때는 객체를 `dict`로 바꾼다.
6. `dict`를 JSON 문자열로 바꿔 파일에 쓴다.

### 중요한 함수

| 코드 | 의미 |
| --- | --- |
| `Path.read_text(encoding="utf-8")` | 파일을 문자열로 읽는다. |
| `Path.write_text(..., encoding="utf-8")` | 문자열을 파일에 쓴다. |
| `json.loads(text)` | JSON 문자열을 Python 데이터로 바꾼다. |
| `json.dumps(data)` | Python 데이터를 JSON 문자열로 바꾼다. |
| `Quiz.to_dict()` | `Quiz` 객체를 저장 가능한 `dict`로 바꾼다. |
| `Quiz.from_dict()` | `dict`를 다시 `Quiz` 객체로 바꾼다. |

### `state.json` 구조

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

답변 템플릿:

```text
JSON은 문자열 기반의 데이터 저장 형식이다.
Python 객체를 바로 파일에 저장하기 어렵기 때문에,
Quiz 객체를 dict로 바꾼 뒤 JSON 문자열로 저장한다.
다시 실행할 때는 JSON을 읽어 dict로 바꾸고 Quiz 객체로 복원한다.
```

## 4. 입력 검증과 예외 처리

### 입력 검증

사용자가 입력한 값은 항상 믿을 수 없다. 그래서 숫자 입력에서는 아래 처리가 필요하다.

- 앞뒤 공백 제거: `.strip()`
- 빈 입력 확인
- 숫자 변환: `int(raw_value)`
- 숫자가 아닌 입력 처리: `ValueError`
- 범위 확인: `number not in range(minimum, maximum + 1)`

예시:

```python
try:
    number = int(raw_value)
except ValueError:
    print("잘못된 입력입니다.")
```

### 예외 처리

`try/except`는 오류가 발생해도 프로그램이 바로 중단되지 않게 처리하기 위해 사용한다.

| 예외 | 발생 상황 | 처리 위치 |
| --- | --- | --- |
| `ValueError` | 숫자가 아닌 값을 `int()`로 바꾸려고 할 때 | `cli/app.py` |
| `OSError` | 파일 읽기/쓰기 실패 | `core/storage.py`, `main.py` |
| `JSONDecodeError` | 손상된 JSON 파일 읽기 실패 | `core/storage.py` |
| `KeyboardInterrupt` | 사용자가 `Ctrl+C`로 중단 | `cli/app.py`, `main.py` |
| `EOFError` | 입력 스트림이 끊김 | `cli/app.py` |

답변 템플릿:

```text
try/except는 오류가 발생해도 프로그램이 바로 종료되지 않게 하기 위해 사용한다.
이 프로젝트에서는 잘못된 숫자 입력, 손상된 JSON 파일, 저장 실패, Ctrl+C 중단을 처리한다.
```

## 5. 프로그램 실행 흐름

깊은 운영체제 수준의 생명주기보다는 아래 흐름을 설명할 수 있으면 충분하다.

```text
python3 main.py 실행
-> if __name__ == "__main__" 조건 확인
-> main() 호출
-> JsonStateRepository 생성
-> QuizGame 생성
-> QuizCli 생성
-> cli.run() 실행
-> while 반복으로 메뉴 출력과 입력 처리
-> 종료 선택 또는 입력 중단 시 state.json 저장
-> 종료 코드 반환
```

`main.py`는 실제 기능을 길게 구현하지 않고 객체를 조립하는 시작점으로만 둔다.

답변 템플릿:

```text
프로그램은 main.py에서 시작한다.
main()은 저장소, 게임, CLI 객체를 만들고 cli.run()을 실행한다.
CLI는 while 반복으로 메뉴를 보여주고, 사용자가 종료를 선택하면 현재 상태를 저장한 뒤 끝난다.
```

## 6. 구조와 책임 분리

이 레포는 `core`와 `cli`를 나눠서 작성했다.

| 패키지 | 역할 |
| --- | --- |
| `core` | 퀴즈 데이터, 게임 규칙, 저장소 경계 |
| `cli` | 콘솔 출력, 사용자 입력, 안내 메시지 |
| `main.py` | 객체 생성과 실행 시작 |

중요한 점은 `core`가 `cli`를 알지 않는다는 것이다. 즉, 콘솔 문구를 바꿔도 퀴즈 규칙과 저장 로직은 크게 흔들리지 않는다.

답변 템플릿:

```text
core와 cli를 분리한 이유는 게임 규칙과 사용자 입출력의 변경 이유가 다르기 때문이다.
core는 퀴즈와 점수 같은 핵심 규칙을 담당하고,
cli는 메뉴 출력과 입력 처리를 담당한다.
```

## 7. Git 기초

Python 시험이라면 Git 비중은 낮을 수 있지만, 미션에 포함되어 있으므로 기본 의미는 외워둔다.

| 명령어 | 의미 |
| --- | --- |
| `git init` | 현재 폴더를 Git 저장소로 만든다. |
| `git add` | 변경 파일을 커밋 준비 상태로 올린다. |
| `git commit` | 준비된 변경사항을 기록으로 남긴다. |
| `git push` | 로컬 커밋을 GitHub 같은 원격 저장소에 올린다. |
| `git pull` | 원격 저장소의 변경사항을 로컬로 가져와 반영한다. |
| `git checkout` | 브랜치를 이동하거나 특정 파일/커밋을 확인한다. |
| `git clone` | 원격 저장소를 새 로컬 폴더로 복제한다. |

답변 템플릿:

```text
Git은 코드 변경 이력을 기록하고 협업하기 위한 도구다.
commit은 변경사항을 로컬 기록으로 남기는 것이고,
push는 그 기록을 원격 저장소에 올리는 것이다.
```

## 8. 예상 질문과 짧은 답

### Q1. `self`는 무엇인가?

`self`는 현재 객체 자기 자신을 가리키는 이름이다. 객체의 속성이나 메서드에 접근할 때 사용한다.

### Q2. `Quiz`와 `QuizGame`의 차이는?

`Quiz`는 퀴즈 한 문제를 표현하고, `QuizGame`은 퀴즈 목록과 점수 같은 전체 게임 상태를 관리한다.

### Q3. 왜 모든 코드를 한 함수에 넣지 않았는가?

기능별 책임을 나누기 위해서다. 입력, 게임 규칙, 저장 로직을 분리하면 코드가 읽기 쉽고 수정하기 쉽다.

### Q4. `for`와 `while`의 차이는?

`for`는 정해진 목록을 순회할 때 쓰고, `while`은 조건이 참인 동안 계속 반복할 때 쓴다.

### Q5. JSON을 왜 사용하는가?

문자열 기반이라 파일로 저장하기 쉽고, `dict`, `list`, `str`, `int` 같은 기본 데이터 구조와 잘 맞기 때문이다.

### Q6. `try/except`를 왜 사용하는가?

입력 오류나 파일 오류가 발생해도 프로그램이 바로 멈추지 않고 안내하거나 복구하기 위해 사용한다.

### Q7. `if __name__ == "__main__"`은 왜 쓰는가?

이 파일이 직접 실행될 때만 `main()`을 호출하기 위해 사용한다. 다른 파일에서 import될 때 자동 실행되는 것을 막는다.

### Q8. `to_dict()`와 `from_dict()`는 왜 필요한가?

객체를 JSON에 저장하려면 `dict` 같은 기본 자료형으로 바꿔야 한다. `to_dict()`는 객체를 저장 가능한 형태로 바꾸고, `from_dict()`는 저장된 데이터를 다시 객체로 복원한다.

### Q9. `record_score()`가 `bool`을 반환하는 이유는?

최고 점수가 갱신되었는지 여부를 CLI가 알 수 있게 하기 위해서다. `True`면 새 최고 점수이고, `False`면 기존 최고 점수보다 낮거나 같다.

### Q10. 파일이 없거나 손상되면 어떻게 되는가?

파일이 없으면 기본 퀴즈로 시작하고, JSON이 손상되었거나 스키마가 맞지 않으면 안내 메시지를 출력한 뒤 기본 퀴즈로 복구한다.

## 9. 벼락치기 체크리스트

- [ ] 클래스, 객체, 속성, 메서드, `self`, `__init__`을 말로 설명할 수 있다.
- [ ] `Quiz`, `QuizGame`, `QuizCli`, `JsonStateRepository`의 역할을 구분할 수 있다.
- [ ] `if/elif/else`, `for`, `while`의 사용 위치를 코드에서 찾을 수 있다.
- [ ] `int`, `str`, `bool`, `list`, `tuple`, `dict`의 차이를 예시로 설명할 수 있다.
- [ ] `state.json`에 어떤 데이터가 저장되는지 설명할 수 있다.
- [ ] `json.loads()`와 `json.dumps()`의 차이를 설명할 수 있다.
- [ ] `try/except`가 필요한 이유를 설명할 수 있다.
- [ ] `main.py`에서 프로그램이 시작되는 흐름을 설명할 수 있다.
- [ ] Git 기본 명령어 7개의 뜻을 말할 수 있다.

## 10. 최종 암기 문장

```text
이 프로젝트는 Python 콘솔 퀴즈 게임이다.
main.py에서 저장소, 게임, CLI 객체를 만들고 실행한다.
Quiz는 한 문제의 데이터와 정답 판정을 담당하고,
QuizGame은 퀴즈 목록, 점수 계산, 최고 점수 갱신, 저장 호출을 담당한다.
QuizCli는 메뉴 출력과 사용자 입력을 담당한다.
state.json은 퀴즈 목록과 최고 점수를 저장하는 JSON 파일이다.
try/except는 잘못된 입력이나 파일 오류가 발생해도 프로그램이 안전하게 동작하도록 하기 위해 사용한다.
```
