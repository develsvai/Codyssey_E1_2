# Python 콘솔 퀴즈 게임

## 프로젝트 개요

입학 연수 미션을 위한 Python 콘솔 퀴즈 게임입니다. 사용자는 메뉴에서 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 점수 확인, 종료 기능을 선택할 수 있습니다.

현재 구조는 `core`와 `cli`를 분리해, 사용자 입출력은 CLI가 맡고 게임 규칙과 저장 경계는 core가 맡도록 구성했습니다.

## 퀴즈 주제와 선정 이유

초기 퀴즈 주제는 Python, Git, JSON 기초입니다. 이번 미션에서 직접 다루는 개념을 퀴즈로 복습할 수 있도록 선택했습니다.

## 실행 방법

```bash
python3 main.py
```

Python 3.10 이상을 사용합니다. 외부 라이브러리는 사용하지 않습니다.

## 기능 목록

- 메뉴 출력 및 입력 처리
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- JSON 파일 저장 및 불러오기

## 파일 구조

```text
main.py
core/
  interfaces.py
  models.py
  game.py
  storage.py
cli/
  app.py
state.json
```

## 데이터 파일

데이터 파일은 프로젝트 루트의 `state.json`입니다. 프로그램 실행 중 생성되며, 퀴즈 목록과 최고 점수를 저장합니다.

예상 스키마는 다음과 같습니다.

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
