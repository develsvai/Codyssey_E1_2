# 결과

- 실제 이미지 경로가 `doc/image/`임을 확인했다.
- `README.md` 파일 구조에 `doc/learning-objectives-rationale.md`와 `doc/image/` 제출 증빙 캡처 디렉터리를 추가했다.
- `doc/submission-checklist.md`에 첨부된 제출 캡처 섹션을 추가했다.
- 캡처 3장을 Git 이력 그래프, `develop` push 성공, GitHub 병합 기록 위치에 맞춰 연결했다.

## 검증

- `git ls-files --error-unmatch`로 이미지 3개가 Git 추적 대상임을 확인했다.
- `rg -n "첨부된 제출 캡처|!\\[|doc/image|image/" README.md doc/submission-checklist.md`
- `git diff --check`
- `loom validate --strict`
