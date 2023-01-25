class Piece:
    def __init__(self, left, top, right, bottom, number):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.number = number

class Tetravex:
    def __init__(self, size, pieces):
        self.size = size
        self.pieces = pieces
        self.board = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.unused_pieces = pieces.copy()

    def solve(self):
            for i in range(self.size[0]*self.size[1]):
                self.afficher()  # Affiche le plateau de jeu
                print("Pieces disponibles: ")
                for j, piece in enumerate(self.unused_pieces):
                    print(j, f"({piece.left} {piece.top} {piece.right} {piece.bottom})")
                piece_index = int(input("Choisir une piece: "))
                if piece_index < 0 or piece_index >= len(self.unused_pieces):
                    print("Piece non disponible. Choisir une autre piece.")
                    continue
                piece = self.unused_pieces[piece_index]
                self.unused_pieces.remove(piece)
                coordinates = input("Choisir les coordonnees (x y): ")
                x, y = map(int, coordinates.split())
                if self.is_valid_move(x, y, piece):
                    self.board[x][y] = piece
                else:
                    print("Deplacement non valide. Choisir une autre piece ou coordonnees.")
                    self.unused_pieces.append(piece)
                    continue
    def afficher(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    print("_", end=" ")
                else:
                    print(piece.number, end=" ")
            print()

    def is_valid_move(self, x, y, piece):
        if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
            return False
        if self.board[x][y] is not None:
            return False
        if x > 0 and self.board[x-1][y] is not None and self.board[x-1][y].right != piece.left:
            return False
        if x < self.size[0]-1 and self.board[x+1][y] is not None and self.board[x+1][y].left != piece.right:
            return False
        if y > 0 and self.board[x][y-1] is not None and self.board[x][y-1].bottom != piece.top:
            return False
        if y < self.size[1]-1 and self.board[x][y+1] is not None and self.board[x][y+1].top != piece.bottom:
            return False
        return True


def main():
    with open("5x5.txt", "r") as f:
        size = list(f.readline().split())
        size[0],size[1] = int(size[0]),int(size[1])
        pieces = []
        for i in range(size[0]*size[1]):
            piece_data = f.readline().split()
            piece_data = [int(chiffre) for chiffre in piece_data ]
            piece = Piece(piece_data[0], piece_data[1], piece_data[2], piece_data[3], i)
            pieces.append(piece)
    game = Tetravex(size, pieces)
    game.solve()

if __name__ == "__main__":
    main()
