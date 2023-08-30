import pytest
from matrix import Matrix
import error


mat1 = Matrix([[1, 2], [3, 4], [5, 6]])
mat2 = Matrix([[1, 2], [3, 4], [5, 6]])
mat3 = Matrix([[1, 2], [3, 4], [5, 7]])
mat4 = Matrix([[1, 2, 3], [4, 5, 6]])
num1 = 2


def test_matrix_exist():
    with pytest.raises(error.MatrixTypeError):
        Matrix([[1, 2], ['a', 4]])
    with pytest.raises(error.MatrixTypeError):
        Matrix([1, 2])
    with pytest.raises(error.MatrixTypeError):
        Matrix(1)
    with pytest.raises(error.SizeError):
        Matrix([[1, 2], [3, 4], [5, 6, 7]])
    assert Matrix([[1, 2], [3, 4], [5, 6]])


def test_eq():
    assert mat1 == mat2
    assert not (mat1 == mat3)
    assert not (mat1 == mat4)
    with pytest.raises(error.MatrixTypeError):
        mat1 == num1


def test_add():
    assert mat1 + mat2 == Matrix([[2, 4], [6, 8], [10, 12]])
    with pytest.raises(error.MatrixTypeError):
        mat1 + num1
    with pytest.raises(error.SizeError):
        mat1 + mat4


def test_mul():
    assert mat1 * mat4 == Matrix([[9, 12, 15], [19, 26, 33], [29, 40, 51]])
    assert mat1 * num1 == Matrix([[2, 4], [6, 8], [10, 12]])
    with pytest.raises(error.NotDefinedError):
        mat1 * mat2
    with pytest.raises(error.MatrixTypeError):
        mat1 * 'a'


if __name__ == '__main__':
    pytest.main()