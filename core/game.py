from core.interfaces import LoadResult, LoadStatus, StateRepository
from core.models import GameState, Quiz


DEFAULT_QUIZZES = [
    Quiz(
        question="Python에서 리스트의 길이를 구하는 함수는?",
        choices=("len", "count", "size", "length"),
        answer=1,
    ),
    Quiz(
        question="Git에서 변경사항을 기록으로 남기는 명령은?",
        choices=("git push", "git add", "git commit", "git pull"),
        answer=3,
    ),
    Quiz(
        question="JSON에서 객체를 표현할 때 사용하는 기본 기호는?",
        choices=("()", "[]", "{}", "<>"),
        answer=3,
    ),
    Quiz(
        question="Python 조건문에서 여러 조건을 이어서 검사할 때 쓰는 키워드는?",
        choices=("else if", "elif", "case", "when"),
        answer=2,
    ),
    Quiz(
        question="GitHub 원격 저장소의 변경사항을 로컬로 가져오는 명령은?",
        choices=("git pull", "git clone", "git checkout", "git init"),
        answer=1,
    ),
]


class QuizGame:
    def __init__(self, repository: StateRepository) -> None:
        self._repository = repository
        self._load_result = LoadResult(None, LoadStatus.MISSING)
        self._state = self._load_initial_state()

    @property
    def load_result(self) -> LoadResult:
        return self._load_result

    @property
    def quizzes(self) -> list[Quiz]:
        return self._state.quizzes

    @property
    def best_score(self) -> int:
        return self._state.best_score

    def quiz_count(self) -> int:
        return len(self._state.quizzes)

    def quiz_titles(self) -> list[str]:
        return [quiz.question for quiz in self._state.quizzes]

    def add_quiz(self, quiz: Quiz) -> None:
        self._state.quizzes.append(quiz)
        try:
            self.save()
        except OSError:
            self._state.quizzes.pop()
            raise

    def record_score(self, score: int) -> bool:
        if score <= self._state.best_score:
            return False
        self._state.best_score = score
        self.save()
        return True

    def calculate_score(self, correct_count: int, total_count: int) -> int:
        if total_count <= 0:
            return 0
        return round((correct_count / total_count) * 100)

    def save(self) -> None:
        self._repository.save(self._state)

    def _load_initial_state(self) -> GameState:
        self._load_result = self._repository.load()
        if self._load_result.state is not None:
            return self._load_result.state
        return GameState(quizzes=list(DEFAULT_QUIZZES), best_score=0)
