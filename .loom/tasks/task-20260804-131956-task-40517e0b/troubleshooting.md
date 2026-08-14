# 트러블슈팅

- 사용자는 `/docs/image`라고 표현했지만 실제 저장소 경로는 `doc/image/`였고 `docs/` 디렉터리는 없었다.
- 한글 파일명은 macOS에서 분해형으로 보일 수 있어 `git ls-files --error-unmatch`로 링크 대상이 Git에서 확인되는지 검증했다.
- 이미지 내용은 `view_image`로 확인한 뒤 Git log, push 성공, GitHub 병합 기록으로 분류했다.
