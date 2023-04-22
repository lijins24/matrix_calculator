import unittest
from Matrix_Calculator import Matrix


class MyTestCase(unittest.TestCase):
    def test_init(self):
        test = Matrix(2, 2)
        self.assertEqual(test[0], [0, 0])
        self.assertEqual(test[1], [0, 0])
        test2 = Matrix(3, 3)
        self.assertEqual(test2[0], [0, 0, 0])
        self.assertEqual(test2[1], [0, 0, 0])

    def test_len(self):
        test = Matrix(2, 2)
        self.assertEqual(len(test), 2)
        test2 = Matrix(3, 3)
        self.assertEqual(len(test2), 3)

    def test__str__(self):
        test = Matrix(3, 3)
        self.assertEqual(test.__str__(), '0 | 0 | 0\n0 | 0 | 0\n0 | 0 | 0')
        test2 = Matrix(2, 2)
        self.assertEqual(test2.__str__(), '0 | 0\n0 | 0')

    def test_setdata(self):
        matrix1 = Matrix(2, 2)
        matrix2 = Matrix(3, 3)
        matrix1.setdata([[1, 2], [3, 4]])
        matrix2.setdata([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(matrix1[0][0], 1)
        self.assertEqual(matrix1[0][1], 2)
        self.assertEqual(matrix1[1][0], 3)
        self.assertEqual(matrix1[1][1], 4)

    def test_getitem(self):
        matrix1 = Matrix(2, 2)
        matrix2 = Matrix(3, 3)
        matrix1.setdata([[3, 6], [0, 10]])
        matrix2.setdata([[12, 3, 7], [0, 4, 6], [6, 0, 7]])
        result = matrix1[0]
        expected_result = [3, 6]
        self.assertEqual(result, expected_result)

    def test_addition(self):
        m1 = [[1, 2], [3, 4]]
        m2 = [[5, 6], [7, 8]]
        m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m4 = [[1, 2, 0], [4, 5, 2], [3, 8, 1]]
        expected_result = [[6, 8], [10, 12]]
        expected_result_2 = [[2, 4, 3], [8, 10, 8], [10, 16, 10]]
        matrix = Matrix(2, 2)
        matrix_2 = Matrix(3, 3)
        result = matrix.addition(m1, m2)
        result_2 = matrix_2.addition(m3, m4)
        self.assertEqual(result, expected_result)
        self.assertEqual(result_2, expected_result_2)

    def test_subtraction(self):
        m1 = [[5, 6], [7, 8]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m4 = [[1, 2, 0], [4, 5, 2], [3, 8, 1]]
        expected_result = [[4, 4], [4, 4]]
        expected_result_2 = [[0, 0, 3], [0, 0, 4], [4, 0, 8]]
        matrix = Matrix(2, 2)
        matrix_2 = Matrix(3, 3)
        result = matrix.subtraction(m1, m2)
        result_2 = matrix_2.subtraction(m3, m4)
        self.assertEqual(result, expected_result)
        self.assertEqual(result_2, expected_result_2)

    def test_multiplication(self):
        m = Matrix(2, 2)
        n = Matrix(3, 3)
        matrix1 = Matrix(2, 2)
        matrix1.setdata([[1, 2], [3, 4]])
        matrix2 = Matrix(2, 2)
        matrix2.setdata([[3, 4], [5, 6]])
        expected_result1 = [[13, 16], [29, 36]]
        result1 = m.multiplication(matrix1, matrix2)

        matrix3 = Matrix(3, 3)
        matrix3.setdata([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix4 = Matrix(3, 3)
        matrix4.setdata([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
        expected_result2 = [[48, 54, 60], [111, 126, 141], [174, 198, 222]]
        result2 = n.multiplication(matrix3, matrix4)

        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)

    def test_transpose(self):
        matrix1 = Matrix(2, 2)
        matrix1.setdata([[1, 2], [3, 4]])
        result = matrix1.transpose(matrix1)
        expected_result = [[1, 3], [2, 4]]
        self.assertEqual(result, expected_result)
        matrix2 = Matrix(3, 3)
        matrix2.setdata([[1, 2, 0], [3, 4, 5], [0, 4, 10]])
        result_2 = matrix2.transpose(matrix2)
        expected_result_2 = [[1, 3, 0], [2, 4, 4], [0, 5, 10]]
        self.assertEqual(result_2, expected_result_2)

    def test_inverse(self):
        test = Matrix(2, 2)
        test2 = Matrix(2, 2)
        test2.setdata([[1, 2], [3, 4]])
        self.assertEqual(test.inverse(test2), [[-2, 1], [3 / 2, -1 / 2]])
        test3 = Matrix(3, 3)
        test4 = Matrix(3, 3)
        test4.setdata([[1, 2, 2], [2, 2, 2], [2, 2, 4]])
        self.assertEqual(test3.inverse(test4), [[-1, 1, 0], [1, 0, -1 / 2], [0, -1 / 2, 1 / 2]])

    def test_rank(self):
        matrix1 = Matrix(2, 2)
        matrix1.setdata([[1, 2], [3, 4]])
        expected_result1 = 2
        result1 = matrix1.rank()
        self.assertEqual(result1, expected_result1)

        matrix2 = Matrix(2, 2)
        matrix2.setdata([[1, 0], [2, 0]])
        expected_result2 = 1
        result2 = matrix2.rank()
        self.assertEqual(result2, expected_result2)

        matrix3 = Matrix(2, 2)
        matrix3.setdata([[0, 0], [0, 0]])
        expected_result3 = 0
        result3 = matrix3.rank()
        self.assertEqual(result3, expected_result3)

        matrix4 = Matrix(3, 3)
        matrix4.setdata([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
        expected_result4 = 3
        result4 = matrix4.rank()
        self.assertEqual(result4, expected_result4)

        matrix5 = Matrix(3, 3)
        matrix5.setdata([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        expected_result5 = 0
        result5 = matrix5.rank()
        self.assertEqual(result5, expected_result5)

        matrix6 = Matrix(3, 3)
        matrix6.setdata([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        expected_result6 = 2
        result6 = matrix6.rank()
        self.assertEqual(result6, expected_result6)

        matrix7 = Matrix(3, 3)
        matrix7.setdata([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        expected_result7 = 1
        result7 = matrix7.rank()
        self.assertEqual(result7, expected_result7)

    def test_positive_definite(self):
        matrix1 = Matrix(2, 2)
        matrix2 = Matrix(2, 2)
        matrix3 = Matrix(3, 3)
        matrix4 = Matrix(3, 3)
        matrix1.setdata([[1, 2], [3, 4]])
        matrix2.setdata([[4, 2], [4, 4]])
        matrix3.setdata([[1, 2, 3], [2, 4, 5], [3, 5, 7]])
        matrix4.setdata([[1, 1, 1], [2, 3, 4], [4, 9, 17]])
        result1 = matrix1.positive_definite()
        result2 = matrix2.positive_definite()
        result3 = matrix3.positive_definite()
        result4 = matrix4.positive_definite()

        self.assertEqual(result1, False)
        self.assertEqual(result2, True)
        self.assertEqual(result3, False)
        self.assertEqual(result4, True)

    def test_row_echelon(self):
        test = Matrix(2, 2)
        test.setdata([[1, 2], [2, 3]])
        self.assertEqual(test.row_echelon(), [[1, 2], [0, -1]])
        test2 = Matrix(2, 2)
        test2.setdata([[6, 9], [5, 0]])
        self.assertEqual(test2.row_echelon(), [[6, 9], [0, -15 / 2]])
        test3 = Matrix(2, 2)
        test3.setdata([[0, 9], [5, 0]])
        self.assertEqual(test3.row_echelon(), [[5, 0], [0, 9]])
        test4 = Matrix(2, 2)
        test4.setdata([[100, 0], [100, 0]])
        self.assertEqual(test4.row_echelon(), [[100, 0], [0, 0]])

        test5 = Matrix(3, 3)
        test5.setdata([[1, 2, 3], [2, 3, 9], [1, 5, 2]])
        self.assertEqual(test5.row_echelon(), [[1, 2, 3], [0, -1, 3], [0, 0, 8]])

        test6 = Matrix(3, 3)
        test6.setdata([[0, 9, 1], [5, 0, 2], [4, 1, 0]])
        self.assertEqual(test6.row_echelon(), [[5, 0, 2], [0, 9, 1], [0, 0, -1.7111111111111112]])

        test7 = Matrix(3, 3)
        test7.setdata([[0, 9, 0], [0, 0, 1], [5, 0, 9]])
        self.assertEqual(test7.row_echelon(), [[5, 0, 9], [0, 9, 0], [0, 0, 1]])

        test8 = Matrix(3, 3)
        test8.setdata([[2, 0, 10], [1, 0, 0], [0, 1, 0]])
        self.assertEqual(test8.row_echelon(), [[2, 0, 10], [0, 1, 0], [0, 0, -5]])


def main():
    unittest.main(verbosity=3)


if __name__ == '__main__':
    unittest.main()
