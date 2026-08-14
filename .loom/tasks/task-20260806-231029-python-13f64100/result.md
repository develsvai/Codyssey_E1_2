# 결과

`doc/python-exam-summary.md`를 추가해 Python 기초 시험 대비 내용을 총정리했다.

포함한 내용:

- 시험 직전 우선순위
- 클래스와 객체 핵심 개념
- 변수, 자료형, 조건문, 반복문, 함수/메서드
- `state.json` 기반 JSON 파일 입출력
- 입력 검증과 `try/except` 예외 처리
- `main.py`에서 시작되는 프로그램 실행 흐름
- `core`/`cli` 책임 분리
- Git 기초 명령어
- 예상 질문과 짧은 답변
- 벼락치기 체크리스트와 최종 암기 문장

README의 파일 구조와 설계 문서 섹션에도 `doc/python-exam-summary.md` 링크를 추가했다.

## 검증

- `rg -n "python-exam-summary|Python 시험 대비|클래스와 객체|파일 입출력|프로그램 실행 흐름|Git 기초" README.md doc/python-exam-summary.md`
- `git diff --check`
- `loom validate --strict`

모두 통과했다.

## 남은 위험

없음. 이번 Task는 문서 추가와 README 링크 반영만 포함하며, Python 코드 동작은 변경하지 않았다.
