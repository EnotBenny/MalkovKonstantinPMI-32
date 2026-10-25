"""Операции над двумерными списками чисел"""

from __future__ import annotations

Position = tuple[int, int]
Matrix = list[list[float]]


def validate_matrix(matrix: Matrix) -> None:
    """Проверить, что матрица не пустая"""
    if not matrix:
        raise ValueError("Матрица не должна быть пустой")
    for index, row in enumerate(matrix):
        if not row:
            raise ValueError(f"Строка {index} не должна быть пустой")


def find_max_min_positions(matrix: Matrix) -> tuple[Position, Position]:
    """Найти позиции максимума и минимума, при нескольких одинаковых значениях
    возвращается первое найденное при обходе слева-направо, сверху-вниз."""
    validate_matrix(matrix)

    max_pos: Position = (0, 0)
    min_pos: Position = (0, 0)
    max_val: float = matrix[0][0]
    min_val: float = matrix[0][0]

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value > max_val:
                max_val = value
                max_pos = (row_index, col_index)
            if value < min_val:
                min_val = value
                min_pos = (row_index, col_index)

    return max_pos, min_pos


def swap_max_min(matrix: Matrix) -> Matrix:
    """Поменять местами максимальный и минимальный элементы матрицы,
    изменяет переданную матрицу на месте и возвращает её же"""
    max_pos, min_pos = find_max_min_positions(matrix)
    (max_i, max_j), (min_i, min_j) = max_pos, min_pos

    matrix[max_i][max_j], matrix[min_i][min_j] = (
        matrix[min_i][min_j],
        matrix[max_i][max_j],
    )
    return matrix


def copy_matrix(matrix: Matrix) -> Matrix:
    """Создать глубокую копию матрицы"""
    return [row[:] for row in matrix]


def _format_value(value: float) -> str:
    """Отформатировать число"""
    if value.is_integer():
        return f"{int(value):>10d}"
    text = f"{value:.6f}".rstrip("0").rstrip(".")
    return f"{text:>10}"


def format_matrix(matrix: Matrix) -> str:
    """Вернуть строковое представление матрицы"""
    lines: list[str] = []
    for row in matrix:
        lines.append(" ".join(_format_value(value) for value in row))
    return "\n".join(lines)
