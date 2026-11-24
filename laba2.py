INF = 999999

def print_matrix(matrix, name):
    print(f"\n--- {name} ---")
    for row in matrix:
        for x in row:
            if x >= INF:
                print("INF", end="  ")
            else:
                print(x, end="    ")
        print()

def print_path(u, v, next_node):
    # якщо шляху немає
    if next_node[u][v] == -1:
        print(f"шляху немає між {u+1} і {v+1}")
        return
    path = [u]
    cur = u
    # йдемо по наступних вершинах поки не дійдемо до кінця
    while cur != v:
        cur = next_node[cur][v]
        path.append(cur)
    # виводимо з 1 а не з 0
    print("шлях:", " -> ".join(str(x+1) for x in path))

def floyd_warshall(graph):
    n = len(graph)
    # копіюємо граф щоб не змінювати оригінал
    dist = [row[:] for row in graph]

    # заповнюємо таблицю наступних вершин
    next_node = []
    for i in range(n):
        row = []
        for j in range(n):
            # якщо ребра немає або це та сама вершина
            if graph[i][j] == INF or i == j:
                row.append(-1)
            else:
                row.append(j)
        next_node.append(row)

    # основний цикл алгоритму флойда-уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # перевіряємо чи є коротший шлях через вершину k
                if dist[i][k] != INF and dist[k][j] != INF:
                    new_dist = dist[i][k] + dist[k][j]
                    if new_dist < dist[i][j]:
                        dist[i][j] = new_dist
                        next_node[i][j] = next_node[i][k]

    # перевірка на від'ємний цикл
    neg_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            neg_cycle = True
            break

    if neg_cycle:
        print("є від'ємний цикл!")

    print_matrix(dist, "мінімальні відстані")
    next_for_print = [[x + 1 if x != -1 else -1 for x in row] for row in next_node]
    print_matrix(next_for_print, "найкоротші шляхи")

    if neg_cycle:
        return

    print("\nвведи пару вершин для пошуку шляху")
    while True:
        u_input = input(f"початкова (1-{n}) або exit: ")
        if u_input.lower() == 'exit':
            break
        v_input = input(f"кінцева (1-{n}) або exit: ")
        if v_input.lower() == 'exit':
            break

        try:
            # користувач вводить з 1, переводимо в 0 для масиву
            u = int(u_input) - 1
            v = int(v_input) - 1
            # перевірка що вершина існує
            if 0 <= u < n and 0 <= v < n:
                # якщо відстань залишилась INF - шляху немає
                if dist[u][v] >= INF:
                    print("шляху немає")
                else:
                    print(f"відстань: {dist[u][v]}")
                    print_path(u, v, next_node)
            else:
                print(f"невірні вершини, введи від 1 до {n}")
        except ValueError:
            print("введи число!")


if __name__ == "__main__":
    # Додаток 1 - Варіант 10
    variant10 = [
        [0,   INF, 1,   1,   1],
        [INF, 0,   INF, 1,   1],
        [1,   INF, 0,   INF, 1],
        [1,   1,   INF, 0,   INF],
        [1,   1,   1,   INF, 0]
    ]

    # Додаток 2 - всі тести
    test1 = [
        [0,   INF, INF, INF, INF, INF, INF],
        [1,   0,   -1,  5,   INF, INF, INF],
        [2,   4,   0,   3,   INF, -2,  6],
        [7,   8,   -4,  0,   INF, INF, INF],
        [INF, INF, INF, 11,  0,   INF, 9],
        [12,  INF, 13,  INF, 14,  0,   INF],
        [-5,  15,  INF, -6,  INF, 16,  0]
    ]

    test2 = [
        [0,   INF, 1,   INF, 3,   INF, 4],
        [INF, 0,   INF, 5,   INF, INF, INF],
        [2,   INF, 0,   INF, INF, -2,  6],
        [7,   8,   INF, 0,   INF, INF, INF],
        [INF, 10,  INF, 11,  0,   INF, 9],
        [12,  INF, 13,  INF, INF, 0,   INF],
        [-3,  14,  INF, -1,  INF, INF, 0]
    ]

    test3 = [
        [0,   INF, 1,   INF, 15,  INF, INF],
        [INF, 0,   -1,  3,   INF, 4,   INF],
        [2,   INF, 0,   -2,  INF, INF, 6],
        [7,   8,   5,   0,   INF, INF, INF],
        [INF, 10,  INF, 11,  0,   INF, 9],
        [12,  INF, 13,  INF, 14,  0,   INF],
        [15,  INF, INF, -6,  INF, -3,  0]
    ]

    test4 = [
        [0,   INF, 1,   INF, 3,   INF, 4],
        [2,   0,   INF, 5,   INF, INF, INF],
        [-2,  INF, 0,   INF, INF, -2,  6],
        [INF, 8,   INF, 0,   INF, INF, INF],
        [INF, INF, INF, 7,   0,   INF, 9],
        [11,  INF, 12,  INF, INF, 0,   INF],
        [INF, -4,  INF, -1,  INF, 10,  0]
    ]

    test5 = [
        [0,   1,   2,   7,   INF, 12,  INF],
        [INF, 0,   -1,  5,   INF, INF, INF],
        [INF, INF, 0,   3,   INF, 4,   6],
        [INF, 8,   -4,  0,   INF, INF, INF],
        [INF, 10,  INF, 11,  0,   INF, 9],
        [INF, INF, INF, INF, INF, 0,   INF],
        [INF, INF, INF, INF, INF, INF, 0]
    ]

    test6 = [
        [0,   2,   -5,  INF, INF, INF, 4],
        [1,   0,   INF, 5,   INF, INF, INF],
        [3,   INF, 0,   INF, INF, -2,  6],
        [7,   8,   INF, 0,   INF, INF, -4],
        [INF, -1,  INF, 11,  0,   INF, 9],
        [INF, INF, 13,  INF, 14,  0,   INF],
        [-5,  15,  INF, -6,  INF, 16,  0]
    ]

    test7 = [
        [0,   INF, INF, INF, INF, INF, INF],
        [INF, 0,   5,   INF, INF, INF, INF],
        [2,   INF, 0,   INF, INF, -2,  6],
        [7,   8,   INF, 0,   INF, INF, INF],
        [INF, 10,  INF, INF, 0,   INF, 9],
        [12,  INF, 13,  INF, INF, 0,   INF],
        [-5,  15,  INF, -6,  INF, INF, 0]
    ]

    test8 = [
        [0,   INF, 1,   INF, 3,   INF, 4],
        [INF, 0,   INF, INF, INF, INF, INF],
        [2,   INF, 0,   INF, INF, -2,  6],
        [7,   8,   INF, 0,   INF, INF, INF],
        [INF, 10,  INF, 11,  0,   INF, 9],
        [INF, INF, INF, INF, INF, 0,   INF],
        [-3,  14,  INF, -1,  INF, INF, 0]
    ]

    test9 = [
        [0,   INF, 1,   INF, 3,   INF, 4],
        [INF, 0,   2,   5,   INF, 7,   INF],
        [INF, 12,  0,   INF, INF, -2,  6],
        [INF, 8,   INF, 0,   13,  INF, INF],
        [INF, 10,  INF, 11,  0,   -3,  9],
        [INF, INF, INF, INF, INF, 0,   INF],
        [INF, 14,  INF, -1,  INF, INF, 0]
    ]

    test10 = [
        [0,   INF, INF, INF, 3,   INF, 4],
        [INF, 0,   -1,  INF, INF, INF, INF],
        [2,   5,   0,   INF, 8,   -2,  6],
        [7,   INF, 12,  0,   INF, 11,  INF],
        [INF, 1,   INF, 10,  0,   INF, 9],
        [INF, INF, INF, -4,  INF, 0,   INF],
        [8,   INF, -3,  10,  INF, INF, 0]
    ]

    while True:
        print("\n=========================================")
        print("0  - вихід")
        print("1  - варіант 10 (Додаток 1)")
        print("--- тести (Додаток 2) ---")
        print("2  - тест 1")
        print("3  - тест 2")
        print("4  - тест 3")
        print("5  - тест 4")
        print("6  - тест 5")
        print("7  - тест 6")
        print("8  - тест 7")
        print("9  - тест 8")
        print("10 - тест 9")
        print("11 - тест 10")
        print("=========================================")

        choice = input("вибір: ").strip()

        tests = {
            '1':  variant10,
            '2':  test1,
            '3':  test2,
            '4':  test3,
            '5':  test4,
            '6':  test5,
            '7':  test6,
            '8':  test7,
            '9':  test8,
            '10': test9,
            '11': test10
        }

        if choice == '0':
            break
        elif choice in tests:
            floyd_warshall(tests[choice])
        else:
            print("не те")