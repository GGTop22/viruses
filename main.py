import tkinter as tk


def infect_area(n, m, k, initial_infected, sizeOfCell, canvas):
    grid = [[0] * m for i in range(n)]  # Создаем пустую сетку размера n x m
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Соседние ячейки

    # Заполняем начальные заражённые ячейки
    for i in range(0, 2 * k, 2):
        y, x = initial_infected[i] - 1, initial_infected[i + 1] - 1
        grid[y][x] = 1
    freeCount = n * m - k
    draw_grid(canvas, grid, n, m, sizeOfCell)
    move = 1
    while freeCount > 0:
        next_infected = []
        # найти клетки со значением move и заразить соседние с ними ,новые заражённые клетки будут move+1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == move:
                    # Проверяем соседей и заражаем их
                    for dx, dy in directions:
                        nx, ny = j + dx, i + dy
                        if valid(ny, nx) and grid[ny][nx] == 0:
                            grid[ny][nx] = move + 1
                            next_infected.append((ny, nx))
                            freeCount -= 1
        # print(move, next_infected)
        move += 1
    # print(grid)
    draw_grid(canvas, grid, n, m, sizeOfCell)
    return move - 1
    # текущая клетка это grid[i][j]
    # нужно проверить пустая ли она (0 ли в ней) а также проверить её соседей,если они заразные то записать в текушую клетку move+1


def matrixHasNum(matrix, num) -> bool:
    for row in matrix:
        if num in row:
            return True
    return False


def valid(y, x):
    return 0 <= y < n and 0 <= x < m


# def create_grid(n, m, k):
#  grid = [[0] * m for _ in range(n)]
# for i in range(k):
# x, y =
# grid[y][x] = 1
# return grid


def draw_grid(canvas, grid, n, m, sizeOfCell):
    canvas.delete("all")
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                color = "red"
            elif grid[i][j] == 2:
                color = "orange"
            elif grid[i][j] == 3:
                color = "yellow"
            elif grid[i][j] == 4:
                color = "lime"
            elif grid[i][j] == 5:
                color = "black"
            else:
                color = "white"
            canvas.create_rectangle(j * sizeOfCell, i * sizeOfCell, (j + 1) * sizeOfCell, (i + 1) * sizeOfCell,
                                    fill=color, outline="black")

    # canvas.update()


root = tk.Tk()
sizeOfCell = 20
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
# Считываем входные данные
with open("INPUT.TXT", "r") as file:
    n, m = map(int, file.readline().split())
    s = file.readline().split()
    k = int(s[0])
    del s[0]
    initial_infected = list(map(int, s))

# print(initial_infected)
x = infect_area(n, m, k, initial_infected, sizeOfCell, canvas)
with open("OUTPUT.TXT", "w") as file:
    file.write(str(x))
print(x)
root.mainloop()
