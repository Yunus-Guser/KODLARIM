import random

# Oyun tahtası boyutları
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Mayın sayısı
NUM_MINES = 10

# Mayın tarlası tahtası
board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

# Mayınları yerleştirme
for i in range(NUM_MINES):
    x = random.randint(0, BOARD_WIDTH - 1)
    y = random.randint(0, BOARD_HEIGHT - 1)
    board[y][x] = "X"

# Kullanıcının tahmin ettiği koordinatları alır
def get_guess():
    while True:
        try:
            x, y = map(int, input("Tahmin etmek istediğiniz koordinatları girin (örneğin: 2,3): ").split(","))
            if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
                print("Girdiğiniz koordinatlar tahtanın dışında kaldı. Lütfen tekrar deneyin.")
                continue
            return x, y
        except ValueError:
            print("Geçersiz koordinat. Lütfen tekrar deneyin.")

# Tahtayı ekrana basar
def print_board(board, show_mines=False):
    print(" " + " ".join(str(x) for x in range(BOARD_WIDTH)))
    for i in range(BOARD_HEIGHT):
        row = ""
        for j in range(BOARD_WIDTH):
            if board[i][j] == "X" and show_mines:
                row += "X"
            elif board[i][j] == 0:
                row += "-"
            else:
                row += str(board[i][j])
        print(str(i) + " " + row)

# Oyunu başlatır
def play_game():
    print("Mayın Tarlası oyununa hoş geldiniz!")
    print_board(board)
    while True:
        x, y = get_guess()
        if board[y][x] == "X":
            print("Oyun bitti! Mayına bastınız.")
            print_board(board, show_mines=True)
            break
        else:
            adjacent_mines = count_adjacent_mines(x, y)
            board[y][x] = adjacent_mines
            print_board(board)
            if check_win():
                print("Tebrikler, oyunu kazandınız!")
                break

# Verilen koordinatlardaki hücrenin komşu mayınlarını sayar
def count_adjacent_mines(x, y):
    count = 0
    for i in range(max(0, y - 1), min(BOARD_HEIGHT, y + 2)):
        for j in range(max(0, x - 1), min(BOARD_WIDTH, x + 2)):
            if board[i][j] == "X":
                count += 1
    return count

# Oyunun kazanılıp kazanılmadığını kontrol eder
def check_win():
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if board[i][j] == 0:
                return False
            elif board[i][j] != "X":
                if count_adjacent_mines(j, i) != board[i][j]:
                    return False
    return True

# Oyunu başlat
play_game()