from copy import deepcopy
import error


class Matrix:
    """"Класс матрицы"""

    def __init__(self, list_of_lists):
        """Создаёт объект класса Matrix принимая список списков, содержащих числа."""
        if not isinstance(list_of_lists, list):
            raise error.MatrixTypeError(1)
        for i in list_of_lists:
            if not isinstance(i, list):
                raise error.MatrixTypeError(1)
            if len(i) == len(list_of_lists[0]):
                if not all(isinstance(x, int | float) for x in i):
                    raise error.MatrixTypeError(2)
            else:
                raise error.SizeError(2)
        self.matrix = deepcopy(list_of_lists)
        self.rows = len(list_of_lists)
        self.columns = len(list_of_lists[0])

    def __str__(self):
        """Печать матрицы"""
        format_size = []
        for col in zip(*self.matrix):
            col_len = [len(str(x)) for x in col]
            format_size.append(max(col_len))
        res = '\n'
        for i in self.matrix:
            for n, e in enumerate(i):
                res += f'{e:>{format_size[n]}}  '
            res += '\n'
        return res

    def __eq__(self, other):
        """Сравнение матриц."""
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                return all([all([self.matrix[row][col] == other.matrix[row][col]
                                 for col in range(self.columns)]) for row in range(self.rows)])
            else:
                return False
        else:
            raise error.MatrixTypeError(3)

    def __add__(self, other):
        """Сложение матриц. Для матриц одной размерности"""
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                return Matrix([list(map(sum, zip(*i))) for i in zip(self.matrix, other.matrix)])
            else:
                raise error.SizeError(1)
        else:
            raise error.MatrixTypeError(3)

    def __mul__(self, other):
        """Умножение матриц. Для совместимых матриц."""
        if isinstance(other, Matrix):
            if self.rows == other.columns and self.columns == other.rows:
                return Matrix([[sum(a * b for a, b in zip(ra, cb)) for cb in zip(*other.matrix)] for ra in self.matrix])
            else:
                raise error.NotDefinedError('Матрицы не совместимы')
        elif isinstance(other, int | float):
            return Matrix([[self.matrix[row][col] * other for col in range(self.columns)] for row in range(self.rows)])
        else:
            raise error.MatrixTypeError(3)
