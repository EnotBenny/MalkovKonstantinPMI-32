"""Запуск алгоритма"""

# Правила: в матрицу вводятся только числа цыфрами
# (е pi и т.д не подходят) при вводе числа с точностью выше 6 знаков
# вывод округлиться до 6 знаков послк запятой.
# Дробные числа вводятся через ".". Если максимальных или минимальных чисел
# больше 1 то местами мкняются первые встреченые макс/мин числа
# при члении матрицы слева направо сверху вниз.

from __future__ import annotations

from input import read_matrix_from_console
from logic import (
    Matrix,
    copy_matrix,
    find_max_min_positions,
    format_matrix,
    swap_max_min,
)

TEST_MATRIX: Matrix = [
    [11, 32, 13, 44, 55],
    [31, 42, 53, 66, 75],
    [12, 26, 33, 45, 52],
    [15, 22, 35, 64, 57],
    [21, 52, 32, 44, 38],
]


def choose_matrix() -> Matrix:
    """Спросить у пользователя источник матрицы и вернуть её"""
    print("Выберите способ задания матрицы:")
    print("  1 — ввести вручную")
    print("  2 — использовать тестовую матрицу из кода")

    while True:
        choice: str = input("Ваш выбор (1/2): ").strip()
        if choice == "1":
            return read_matrix_from_console()
        if choice == "2":
            return copy_matrix(TEST_MATRIX)
        print("Ошибка: введите 1 или 2")


def main() -> None:
    """Запустить программу"""
    try:
        matrix: Matrix = choose_matrix()
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван пользователем")
        return

    print("\nИсходная матрица:")
    print(format_matrix(matrix))

    max_pos, min_pos = find_max_min_positions(matrix)
    max_val: float = matrix[max_pos[0]][max_pos[1]]
    min_val: float = matrix[min_pos[0]][min_pos[1]]
    print(f"\nМаксимум: {max_val:g}")
    print(f"Минимум:  {min_val:g}")

    swap_max_min(matrix)
    print("\nМатрица после обмена max и min:")
    print(format_matrix(matrix))


main()
