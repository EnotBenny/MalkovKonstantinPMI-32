"""Безопасный ввод чисел и матриц с консоли"""

from __future__ import annotations

import math

from logic import Matrix


def read_int(prompt: str, *, minimum: int | None = None) -> int:
    """Считать целое число, при необходимости — не меньше minimum,
    повторяет запрос,пока пользователь не введёт корректное значение"""
    while True:
        raw: str = input(prompt).strip()
        try:
            value: int = int(raw)
        except ValueError:
            print("Ошибка: введите целое число")
            continue

        if minimum is not None and value < minimum:
            print(f"Ошибка: число должно быть не меньше {minimum}.")
            continue

        return value


def parse_number(token: str) -> float:
    """Распарсить один токен как конечное вещественное число"""
    try:
        value: float = float(token)
    except ValueError as error:
        raise ValueError(f"«{token}» — не число") from error

    if math.isnan(value) or math.isinf(value):
        raise ValueError(f"«{token}» — недопустимое значение")
    return value


def read_row(length: int) -> list[float]:
    """Считать строку из ровно n чисел"""
    while True:
        raw: str = input().strip()
        if not raw:
            print("Ошибка: строка пуста, введите числа через пробел")
            continue

        parts: list[str] = raw.split()
        if len(parts) != length:
            err = f"Ошибка: нужно ровно {length}, получено {len(parts)}."
            print(err)
            continue

        try:
            row: list[float] = [parse_number(part) for part in parts]
        except ValueError as error:
            print(f"Ошибка: {error}. Все элементы должны быть числами")
            continue

        return row


def read_matrix_from_console() -> Matrix:
    """Считать матрицу с консоли, размеры, затем строки"""
    rows: int = read_int("Введите количество строк: ", minimum=1)
    cols: int = read_int("Введите количество столбцов: ", minimum=1)

    matrix: Matrix = []
    for row_index in range(rows):
        print(f"Строка {row_index + 1}: введите {cols} чисел через пробел")
        matrix.append(read_row(cols))

    return matrix
