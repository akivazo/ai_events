from abc import ABC, abstractmethod


class ToolProduct(ABC):
    @abstractmethod
    def act(self):
        pass