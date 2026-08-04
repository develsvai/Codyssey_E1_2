from abc import ABC, abstractmethod

from core.models import GameState


class StateRepository(ABC):
    """Persistence boundary used by the game core."""

    @abstractmethod
    def load(self) -> GameState | None:
        """Return a saved game state, or None when no usable state exists."""

    @abstractmethod
    def save(self, state: GameState) -> None:
        """Persist the current game state."""
