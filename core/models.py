from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Quiz:
    question: str
    choices: tuple[str, str, str, str]
    answer: int

    def __post_init__(self) -> None:
        if not self.question.strip():
            raise ValueError("question must not be empty")
        if len(self.choices) != 4:
            raise ValueError("quiz must have exactly 4 choices")
        if any(not choice.strip() for choice in self.choices):
            raise ValueError("choices must not be empty")
        if self.answer not in range(1, 5):
            raise ValueError("answer must be between 1 and 4")

    def is_correct(self, answer: int) -> bool:
        return self.answer == answer

    def to_dict(self) -> dict[str, Any]:
        return {
            "question": self.question,
            "choices": list(self.choices),
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Quiz:
        choices = data["choices"]
        if not isinstance(choices, list):
            raise ValueError("choices must be a list")
        return cls(
            question=str(data["question"]),
            choices=tuple(str(choice) for choice in choices),  # type: ignore[arg-type]
            answer=int(data["answer"]),
        )


@dataclass
class GameState:
    quizzes: list[Quiz]
    best_score: int = 0
