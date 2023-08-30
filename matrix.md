Документация к классу матриц
===

```__eq__```
---

>>> from matrix import Matrix
>>> import error

>>> Matrix([[1, 2], [3, 4], [5, 6]]) == Matrix([[1, 2], [3, 4], [5, 6]])
True

>>> Matrix([[1, 2], [3, 4], [5, 6]]) == Matrix([[1, 2], [3, 4], [5, 7]])
False

>>> Matrix([[1, 2], [3, 4], [5, 6]]) == Matrix([[1, 2, 3], [4, 5, 6]])
False

>>> Matrix([[1, 2], [3, 4], [5, 6]]) == 2
Traceback (most recent call last):
...
error.MatrixTypeError: Неверный тип данных.
