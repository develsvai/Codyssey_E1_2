# Python 콘솔 퀴즈 게임

## 프로젝트 개요

입학 연수 미션을 위한 Python 콘솔 퀴즈 게임입니다. 사용자는 콘솔 메뉴에서 퀴즈 풀기, 퀴즈 추가, 퀴즈 목록, 최고 점수 확인, 종료 기능을 사용할 수 있습니다.

구조는 `core`와 `cli`를 분리했습니다. 사용자 입출력은 `cli`가 담당하고, 퀴즈 모델과 게임 규칙, 저장소 경계는 `core`가 담당합니다.

## 퀴즈 주제와 선정 이유

초기 퀴즈 주제는 Python, Git, JSON 기초입니다. 이번 미션을 진행하면서 직접 다루는 개념을 복습할 수 있도록, 기본 문법과 저장 형식, Git 명령어를 중심으로 5개의 기본 퀴즈를 구성했습니다.

## 실행 방법

Python 3.10 이상에서 실행합니다. 외부 라이브러리는 사용하지 않고 표준 라이브러리만 사용합니다.

```bash
python3 main.py
```

첫 실행 시 `state.json`이 없으면 기본 퀴즈 5개로 시작합니다. 퀴즈를 추가하거나 최고 점수가 갱신되면 프로젝트 루트의 `state.json`에 저장됩니다.

## 기능 목록

- 메뉴 출력 및 1-5번 숫자 입력 처리
- 퀴즈 풀기와 문제별 정답/오답 안내
- 전체 문제 수 기준 100점 환산 점수 계산
- 최고 점수 갱신 및 저장
- 새 퀴즈 추가
- 등록된 퀴즈 목록 확인
- `state.json` 저장 및 불러오기
- 저장 파일 없음, 손상 파일, 읽기 오류 안내
- 빈 입력, 숫자 변환 실패, 범위 밖 숫자 재입력 처리
- `KeyboardInterrupt`, `EOFError` 발생 시 현재 상태 저장 후 안전 종료

## 파일 구조

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
doc/
  architecture.md
  submission-checklist.md
README.md
.gitignore
state.json  # 실행 중 생성되는 로컬 데이터 파일, Git에는 포함하지 않음
```

## 데이터 파일

데이터 파일은 프로젝트 루트의 `state.json`입니다. UTF-8 인코딩으로 저장하며, 프로그램 실행 중 생성되는 로컬 상태 파일이므로 `.gitignore`에 포함되어 있습니다.

저장 파일이 없으면 기본 퀴즈로 시작합니다. 저장 파일이 손상되었거나 스키마가 맞지 않으면 기본 퀴즈로 복구해 실행합니다.

스키마는 다음과 같습니다.

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

- `quizzes`: 퀴즈 목록
- `question`: 문제 문자열
- `choices`: 선택지 4개
- `answer`: 1부터 4 사이의 정답 번호
- `best_score`: 최고 점수, 0부터 100 사이의 정수

## 설계 문서

현재 패키지 책임과 의존 방향은 [doc/architecture.md](doc/architecture.md)에 정리되어 있습니다. 제출 전 Git workflow와 스크린샷 준비 항목은 [doc/submission-checklist.md](doc/submission-checklist.md)를 참고합니다.
