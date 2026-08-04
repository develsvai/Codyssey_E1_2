from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from core.models import GameState


class LoadStatus(Enum):
    LOADED = "loaded"
    MISSING = "missing"
    RECOVERED = "recovered"
    ERROR = "error"


@dataclass(frozen=True)
class LoadResult:
    state: GameState | None
    status: LoadStatus
    detail: str = ""


class StateRepository(ABC):
    """Persistence boundary used by the game core."""

    @abstractmethod
    def load(self) -> LoadResult:
        """Return the saved game state and load status."""

    @abstractmethod
    def save(self, state: GameState) -> None:
        """Persist the current game state."""
