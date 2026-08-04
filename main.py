from cli.app import QuizCli
from core.game import QuizGame
from core.storage import JsonStateRepository


def main() -> int:
    repository = JsonStateRepository("state.json")
    game = QuizGame(repository)
    cli = QuizCli(game)
    return cli.run()


if __name__ == "__main__":
    raise SystemExit(main())
