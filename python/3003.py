chess = {
    "king" : 1,
    "queen" : 1,
    "rook" : 2,
    "bishop" : 2,
    "knight" : 2,
    "pawn" : 8
}

chess_list = list(chess.values())
current_chess = list(map(int,input().split()))
for i in range(len(current_chess)) :
    print(chess_list[i] - current_chess[i], end=' ')