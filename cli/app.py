from core.game import QuizGame


class QuizCli:
    def __init__(self, game: QuizGame) -> None:
        self._game = game
        self._running = True

    def run(self) -> int:
        print("저장된 데이터 또는 기본 퀴즈를 불러왔습니다.")
        while self._running:
            self._print_menu()
            choice = self._read_menu_choice()
            if choice is None:
                continue
            self._handle_choice(choice)
        return 0

    def _print_menu(self) -> None:
        print()
        print("=" * 40)
        print("나만의 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def _read_menu_choice(self) -> int | None:
        try:
            raw_value = input("선택: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            print("입력이 중단되어 현재 상태를 저장하고 종료합니다.")
            self._save_before_exit()
            self._running = False
            return None

        if not raw_value:
            print("빈 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            return None

        try:
            choice = int(raw_value)
        except ValueError:
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            return None

        if choice not in range(1, 6):
            print("범위 밖 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            return None

        return choice

    def _handle_choice(self, choice: int) -> None:
        if choice == 1:
            print("퀴즈 풀기 기능은 다음 단계에서 구현합니다.")
        elif choice == 2:
            print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")
        elif choice == 3:
            self._print_quiz_titles()
        elif choice == 4:
            print(f"최고 점수: {self._game.best_score}점")
        elif choice == 5:
            self._save_before_exit()
            print("프로그램을 종료합니다.")
            self._running = False

    def _print_quiz_titles(self) -> None:
        titles = self._game.quiz_titles()
        if not titles:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록: 총 {len(titles)}개")
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title}")

    def _save_before_exit(self) -> None:
        try:
            self._game.save()
        except OSError:
            print("상태 저장 중 오류가 발생했습니다.")
