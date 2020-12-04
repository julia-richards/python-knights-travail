from tree import Node

# test = Node((2, 1))
# print(test.value)


class KnightPathFinder:
    def __init__(self, start_position):
        self._root = Node(start_position)
        self._considered_positions = set(start_position)

    def get_valid_moves(self, pos):
        possible_moves = [
            (1, 2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (2, -1),
            (-1, -2),
            (-2, -1),
            (1, -2)
        ]

        moves = []
        current_x, current_y = pos
        for x_move, y_move in possible_moves:
            new_set_x, new_set_y = (current_x + x_move, current_y + y_move)
            # keep from going off the board, cannot exceed 8
            if new_set_x in range(0, 8) and new_set_y in range(0, 8):
                new_pos = new_set_x, new_set_y
            moves.append(new_pos)
        return moves

    def new_move_positions(self, pos):
        # call get valid moves with pos as param
        # filter valid moves with the considered postions
        # add result to considered postions
        possible_moves = set(self.get_valid_moves(pos)).difference(self._considered_positions)
        self._considered_positions = self._considered_positions.union(possible_moves)

        return possible_moves


finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
