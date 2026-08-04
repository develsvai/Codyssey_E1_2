# 제출 체크리스트

이 문서는 미션 제출 전에 확인해야 할 Git workflow와 스크린샷 항목을 정리한다. 사용자 인증이 필요한 GitHub 작업과 실제 화면 캡처는 로컬 환경에서 직접 수행해야 한다.

## 현재 확인된 상태

- 작업 브랜치: `develop`
- 원격 저장소: `https://github.com/develsvai/Codyssey_E1_2.git`
- 현재 로컬 커밋 수: 12개
- `state.json`: 실행 중 생성되는 로컬 데이터 파일이며 `.gitignore`에 포함되어 있다.
- 기본 기능: 퀴즈 풀기, 퀴즈 추가, 목록, 최고 점수, 저장/불러오기 구현 완료

## Git workflow 제출 전 확인

```bash
git status --short --branch
git log --oneline --graph --decorate -n 20
```

- 최소 10개 이상의 의미 있는 커밋: 현재 충족
- `develop` 브랜치 작업 기록: 현재 충족
- 원격 저장소 업로드: 제출 전 `git push origin develop` 필요
- 최종 제출 브랜치 병합: GitHub에서 `develop`을 `master` 또는 제출 기준 브랜치로 병합 필요
- `clone`/`pull` 실습: 별도 디렉터리에서 수행 필요

## Git 기초 명령어 7종 체크

- `init`: 현재 저장소가 이미 Git 저장소로 준비되어 있으므로, 제출 기준상 직접 사용 증빙이 필요하면 별도 연습 디렉터리에서 확인한다.
- `add`: 문서/기능 변경 스테이징에 사용한다.
- `commit`: 기능 단위 커밋과 문서 커밋에 사용한다.
- `push`: 제출 전 `git push origin develop`로 수행한다.
- `pull`: clone 실습 뒤 기존 작업 디렉터리에서 `git pull origin develop`로 수행한다.
- `checkout`: `develop` 브랜치 이동 또는 확인에 사용한다.
- `clone`: 별도 디렉터리 복제 실습에서 사용한다.

## `clone`/`pull` 실습 절차

아래 절차는 퀴즈 게임 개발이 완료된 뒤 별도 로컬 디렉터리에서 수행한다.

```bash
git clone https://github.com/develsvai/Codyssey_E1_2.git Codyssey_E1_2_clone
cd Codyssey_E1_2_clone
git checkout develop
```

복제된 저장소에서 README에 간단한 확인 문구를 추가한 뒤 커밋하고 push한다.

```bash
git add README.md
git commit -m "Docs: clone 실습 확인 문구 추가"
git push origin develop
```

기존 작업 디렉터리로 돌아와 변경사항을 가져온다.

```bash
git pull origin develop
```

## 제출 스크린샷

- 개발 환경 설정: VSCode 또는 사용 IDE, `python3 --version`, `git config --list` 중 필요한 화면
- 프로그램 실행 결과: 메뉴, 퀴즈 풀이, 퀴즈 추가, 퀴즈 목록, 최고 점수 화면
- 데이터 유지 확인: 재실행 후 저장 데이터 로드 메시지와 추가 퀴즈 유지 화면
- Git 이력: `git log --oneline --graph --decorate` 실행 결과
