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
        return self._read_number("선택: ", 1, 5)

    def _handle_choice(self, choice: int) -> None:
        if choice == 1:
            self._play_quizzes()
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

    def _play_quizzes(self) -> None:
        quizzes = self._game.quizzes
        total_count = len(quizzes)
        if total_count == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print()
        print(f"퀴즈를 시작합니다. 총 {total_count}문제입니다.")
        correct_count = 0

        for index, quiz in enumerate(quizzes, start=1):
            print()
            print("-" * 40)
            print(f"[문제 {index}]")
            print(quiz.question)
            for choice_index, choice in enumerate(quiz.choices, start=1):
                print(f"{choice_index}. {choice}")

            answer = self._read_number("정답 입력: ", 1, 4)
            if answer is None:
                return

            if quiz.is_correct(answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = self._game.calculate_score(correct_count, total_count)
        is_new_best = self._game.record_score(score)

        print()
        print("=" * 40)
        print(f"결과: {total_count}문제 중 {correct_count}문제 정답 ({score}점)")
        if is_new_best:
            print("새로운 최고 점수입니다!")
        else:
            print(f"현재 최고 점수: {self._game.best_score}점")
        print("=" * 40)

    def _read_number(self, prompt: str, minimum: int, maximum: int) -> int | None:
        while self._running:
            try:
                raw_value = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print()
                print("입력이 중단되어 현재 상태를 저장하고 종료합니다.")
                self._save_before_exit()
                self._running = False
                return None

            if not raw_value:
                print(f"빈 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
                continue

            try:
                number = int(raw_value)
            except ValueError:
                print(f"잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
                continue

            if number not in range(minimum, maximum + 1):
                print(f"범위 밖 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
                continue

            return number

        return None

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
