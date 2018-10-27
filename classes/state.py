class State:
    def __init__(self, current, parent, heuristic=None, move_cost=1):
        """
            State object that contains the current configuration of the game state.
        :param current: the current shape of the 8-puzzle game.
        :param parent: the previous state of the 8-puzzle game.
        :param heuristic: Heuristic cost Object to calculate heuristic cost in case of using A* Algorithm.
        :param move_cost: the step cost which is the payload that was taken to move from parent game state to current game state.
        """
        self.__current = current
        self.__parent = parent
        if parent is None:
            self.__cost = 0
        else:
            self.__cost = parent.cost + move_cost
        if heuristic is None:
            self.__heuristic = 0
        else:
            tmpHeurisitc = heuristic()
            self.__heuristic = tmpHeurisitc.get_heuristic(self)
        self.__move_cost = move_cost

    @property
    def current(self):
        return self.__current

    @property
    def parent(self):
        return self.__parent

    @property
    def cost(self):
        return self.__cost

    @property
    def move_cost(self):
        return self.__move_cost
 
    @property
    def heuristic(self):
        return self.__heuristic

    def get_total_cost(self):
        return self.cost + self.heuristic

    @parent.setter
    def parent(self, parent):
        self.__parent = parent
    
    @current.setter
    def current(self, current):
        self.__current = current

    def __hash__(self):
        return hash(str(self.__current))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.current == other.current

    def is_goal(self):
        """
            Checks if we the current game state is the final state.
        :return: True if we reached the final state; False otherwise.
        """
        return self.current == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __lt__(self, other):
        """
        :param other: other state to be compared with
        :return: True if current state has total cost less than the other. False otherwise.
        """
        return self.get_total_cost() < other.get_total_cost()