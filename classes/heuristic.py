from abc import ABC, abstractmethod
 
class Heuristic(ABC):

    
    @abstractmethod
    def get_heuristic(self, current):
        pass
