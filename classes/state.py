class State:

    def __init__(self, current, parent, heuristic, move_cost=1):
        self.__current = current
        self.__parent = parent
        if parent is None:
            self.__cost = 0
        else:
            self.__cost = parent.cost + move_cost
        self.__heuristic = heuristic(current)
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
        
    @parent.setter
    def parent(self, parent):
        self.__parent = parent
    
    @current.setter
    def current(self, current):
        self.__current = current
