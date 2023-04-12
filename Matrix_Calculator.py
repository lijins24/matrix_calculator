class Matrix:
    def __init__(self, rows, columns):
        # set the default matrix size to 2x2
        self.matrix = []
        self.rows = rows
        self.columns = columns
        self.dim = 0
        # if not, then raise error
        if self.rows == 2 and self.columns == 2:
            self.dim = 2
        elif self.rows == 3 and self.columns == 3:
            self.dim = 3
        else:
            print("Please enter a 2x2 or 3x3 dimension matrix!")
            raise ValueError
        for _ in range(self.rows):
            self.matrix.append([0] * self.columns)
        #self.matrix = [[0] * self.columns for _ in range(self.rows)]

    def __getitem__(self, i):
        return self.matrix[i]
    # def get_value(self, rows, columns):
    #      return self.matrix[rows][columns]

    def __str__(self):
        return '\n'.join(' | '.join(map(str, rows)) for rows in self.matrix)

    # def get_matrix(self):
    #     print("-" * 10)
    #     for i in self.matrix:
    #         print(i)
    #     print("-" * 10)

    def setdata(self, data):
        if self.dim == len(data[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] = data[i][j]
            return self.matrix
        else:
            print("Please enter the values that matches the size of the matrix!")

    def addition(self, matrix1, matrix2):
        if matrix1.dim == matrix2.dim:
            for i in range(matrix1.dim):
                for j in range(matrix1.dim):
                    self.matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            return self.matrix
        else:
            print("Please make sure two matrices have same dimension!")

    def subtraction(self, matrix1, matrix2):
        if matrix1.dim == matrix2.dim:
            for i in range(matrix1.dim):
                for j in range(matrix1.dim):
                    self.matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            return self.matrix
        else:
            print("Please make sure two matrices have same dimension!")

    def transpose(self, matrix1):
        tem = []
        for i in range(matrix1.dim):
            for j in range(matrix1.dim):
                tem=[[matrix1[j][i] for j in range(matrix1.dim)] for i in range(matrix1.dim)]
        for k in range(len(tem)):
            for l in range(len(tem)):
                self.matrix[k][l] = tem[k][l]
        return self.matrix

    def multiplication(self, matrix1, matrix2):
        if matrix1.dim == matrix2.dim:
            for i in range(self.dim):
                for j in range(self.dim):
                    for k in range(self.dim):
                        self.matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return self.matrix

    def inverse(self, matrix1):
        if self.dim == 2:
            a, b = matrix1[0]
            c, d = matrix1[1]
            determinant = (a * d) - (b * c)
            if determinant == 0:
                return None
            else:
                self.matrix = [[d, -b], [-c, a]]
                base = 1 / determinant
                self.matrix = [[base * i for i in row] for row in self.matrix]
                return self.matrix
        if self.dim == 3:
            a, b, c = matrix1[0]
            d, e, f = matrix1[1]
            g, h, i = matrix1[2]

            deter_plus = (a * e * i) + (b * f * g) + (c * d * h)
            deter_minus = (c * e * g) + (b * d * i) + (a * f * h)
            deter_3x3 = deter_plus - deter_minus
            print(deter_3x3)
            if deter_3x3 == 0:
                return None
            else:
                self.matrix = [[(e * i - f * h), (c * h - b * i), (b * f - c * e)],
                           [(f * g - d * i), (a * i - c * g), (c * d - a * f)],
                           [(d * h - e * g), (g * b - a * h), (a * e - b * d)]]
                base = 1 / deter_3x3
                self.matrix = [[base * i for i in row] for row in self.matrix]
                return self.matrix

    #def reduced_row_echelon_form(self):

def main():
    # 2x2 checking
    matrix1 = Matrix(2, 2)
    print("matrix1 is")
    matrix1.setdata([[1, 2], [3, 4]])
    #print(matrix1.get_matrix())
    print(matrix1)

    print("matrix2 is")
    matrix2 = Matrix(2, 2)
    matrix2.setdata([[2, 3], [4, 5]])
    print(matrix2)

    matrix3 = Matrix(2,2)
    matrix3.addition(matrix1, matrix2)
    print("matrix1 + matrix2 = matrix3")
    print(matrix3)

    matrix4 = Matrix(2, 2)
    matrix4.subtraction(matrix1, matrix2)
    print("matrix1 - matrix2 = matrix4")
    print(matrix4)

    matrix9 = Matrix(2,2)
    matrix9.transpose(matrix1)
    print("transpose of matrix1 = matrix9")
    print(matrix9)

    matrix11= Matrix(2,2)
    matrix11.inverse(matrix1)
    print("inverse of matrix1 = matrix11")
    print(matrix11)

    matrix13=Matrix(2,2)
    matrix13.multiplication(matrix1,matrix2)
    print("matrix1 * matrix2 = matrix13")
    print(matrix13)

    # 3x3 checking
    matrix5 = Matrix(3, 3)
    print("matrix5 is")
    matrix5.setdata([[1, 2,3], [2, 3,4],[2,2,1]])
    print(matrix5)

    print("matrix6 is")
    matrix6 = Matrix(3, 3)
    matrix6.setdata([[2, 3,4], [4, 5,6],[6,7,8]])
    print(matrix6)

    matrix7 = Matrix(3, 3)
    matrix7.addition(matrix5, matrix6)
    print("matrix5 + matrix6 = matrix7")
    print(matrix7)

    matrix8 = Matrix(3, 3)
    matrix8.subtraction(matrix5, matrix6)
    print("matrix5 - matrix6 = matrix8")
    print(matrix8)

    print()
    print("+" * 10)
    matrix10 = Matrix(3, 3)
    matrix10.transpose(matrix5)
    print(matrix10)
    print("+" * 10)
    print()

    matrix12 = Matrix(3, 3)
    matrix12.inverse(matrix5)
    print("inverse of matrix5 = matrix12")
    print(matrix12)

    matrix14 = Matrix(3, 3)
    matrix14.multiplication(matrix5, matrix6)
    print("matrix5 * matrix6 = matrix14")
    print(matrix14)



main()
