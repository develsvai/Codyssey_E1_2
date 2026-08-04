from cli.app import QuizCli
from core.game import QuizGame
from core.storage import JsonStateRepository


def main() -> int:
    repository = JsonStateRepository("state.json")
    game = QuizGame(repository)
    cli = QuizCli(game)
    try:
        return cli.run()
    except KeyboardInterrupt:
        print()
        print("프로그램이 중단되어 현재 상태를 저장하고 종료합니다.")
        try:
            game.save()
        except OSError:
            print("상태 저장 중 오류가 발생했습니다.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
