from tree import Node

finder = KnighPathFinder((0,0))

finder.find_path((2, 1))
finder.find_path((3, 3))

class KnighPathFinder:
    def __init__(self, start_position):
        self._root = Node(start_position)
        self._considered_positions = set(start_position)

    def get_valid_moves(self, pos):
        possible_moves = list(
            (1, 2),
            (2, 1),
            (1, 2),
        )
