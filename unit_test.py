import unittest
import error
from matrix import Matrix


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mat1 = Matrix([[1, 2], [3, 4], [5, 6]])
        self.mat2 = Matrix([[1, 2], [3, 4], [5, 6]])
        self.mat3 = Matrix([[1, 2], [3, 4], [5, 7]])
        self.mat4 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.num1 = 2

    def test_matrix_exist(self):
        with self.assertRaises(error.MatrixTypeError):
            Matrix([[1, 2], ['a', 4]])
        with self.assertRaises(error.MatrixTypeError):
            Matrix([1, 2])
        with self.assertRaises(error.MatrixTypeError):
            Matrix(1)
        with self.assertRaises(error.SizeError):
            Matrix([[1, 2], [3, 4], [5, 6, 7]])
        self.assertTrue(Matrix([[1, 2], [3, 4], [5, 6]]))

    def test_eq(self):
        self.assertTrue(self.mat1 == self.mat2)
        self.assertFalse(self.mat1 == self.mat3)
        self.assertFalse(self.mat1 == self.mat4)
        with self.assertRaises(error.MatrixTypeError):
            self.mat1 == self.num1

    def test_add(self):
        self.assertEqual(self.mat1 + self.mat2, Matrix([[2, 4], [6, 8], [10, 12]]))
        with self.assertRaises(error.MatrixTypeError):
            self.mat1 + self.num1
        with self.assertRaises(error.SizeError):
            self.mat1 + self.mat4


    def test_mul(self):
        self.assertEqual(self.mat1*self.mat4, Matrix([[9, 12, 15], [19, 26, 33], [29, 40, 51]]))
        self.assertEqual(self.mat1*self.num1, Matrix([[2, 4], [6, 8], [10, 12]]))
        with self.assertRaises(error.NotDefinedError):
            self.mat1 * self.mat2
        with self.assertRaises(error.MatrixTypeError):
            self.mat1 * 'a'


if __name__ == '__main__':
    unittest.main(verbosity=2)