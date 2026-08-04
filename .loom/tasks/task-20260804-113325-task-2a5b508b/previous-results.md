# Previous Results

5 older recorded result(s) were omitted. Promote durable context to Job Notes or explicit Context References.

## 6. 제출 문서 커밋 수 최신화

# 결과

- `doc/architecture.md`의 최소 10개 이상 커밋 조건 근거를 `12개`에서 `14개 이상`으로 갱신했다.
- `doc/submission-checklist.md`의 현재 로컬 커밋 수를 `14개 이상`으로 갱신하고, 최신 값 확인 명령 `git rev-list --count HEAD`를 함께 적었다.
- `git rev-list --count HEAD` 실행 결과 현재 커밋 수가 14개임을 확인했다.

## 검증

- `git rev-list --count HEAD` 결과: `14`
- `rg -n "12개|14개 이상|git rev-list --count HEAD|커밋 수" doc/architecture.md doc/submission-checklist.md`로 문서 표기 확인.
- `git diff --check -- doc/architecture.md doc/submission-checklist.md` 통과.
- `loom validate --strict` 통과.

## 남은 항목

- 이후 이 Task 커밋과 Loom 완료 커밋까지 추가되면 실제 커밋 수는 더 증가한다. 문서에는 `14개 이상`과 확인 명령을 함께 남겨 제출 직전에도 다시 확인할 수 있게 했다.

## 7. README 실행 방법 상세화

# 결과

- `README.md`의 `실행 방법` 섹션을 단계별 안내로 상세화했다.
- Python 버전 확인, 프로젝트 루트 이동, 실행 명령, 메뉴 화면 예시, 메뉴별 사용 방법을 추가했다.
- 첫 실행 시 `state.json`이 없을 때의 동작과 재실행 시 저장 데이터를 불러오는 흐름을 설명했다.
- 정답 번호 입력 범위와 잘못된 입력 처리 기준도 실행 안내에 포함했다.

## 검증

- `sed -n '1,170p' README.md`로 수정된 실행 방법 내용을 확인했다.
- `git diff --check -- README.md` 통과.
- `loom validate --strict` 통과.

## 남은 항목

- 기능 코드 변경은 없다.
- GitHub push, clone/pull 실습, 제출 스크린샷 촬영은 이 Task 범위 밖이다.
