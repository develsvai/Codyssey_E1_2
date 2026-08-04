from __future__ import annotations

import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any

from core.interfaces import StateRepository
from core.models import GameState, Quiz


class JsonStateRepository(StateRepository):
    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    def load(self) -> GameState | None:
        if not self._path.exists():
            return None

        try:
            data = json.loads(self._path.read_text(encoding="utf-8"))
            return self._state_from_dict(data)
        except (OSError, JSONDecodeError, KeyError, TypeError, ValueError):
            return None

    def save(self, state: GameState) -> None:
        payload = {
            "quizzes": [quiz.to_dict() for quiz in state.quizzes],
            "best_score": state.best_score,
        }
        self._path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _state_from_dict(self, data: dict[str, Any]) -> GameState:
        quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
        return GameState(
            quizzes=quizzes,
            best_score=int(data.get("best_score", 0)),
        )
