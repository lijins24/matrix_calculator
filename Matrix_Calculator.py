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
        self.matrix = matrix1
        #print(f"matrix[0][1]:{matrix2[0][1]}")
        #if matrix1.dim == 2:
            #print(matrix2[0][1])
            #print(matrix2[1][0])
        tem = []
        for i in range(matrix1.dim):
            for j in range(matrix1.dim):
                tem.append([i][j])
            # tem = self.matrix[0][1]
            # self.matrix[0][1] = self.matrix[1][0]
            # self.matrix[1][0] = tem
        #print(matrix2)
        #elif matrix1.dim == 3:

        return self.matrix

    def multiplication(self, matrix1, matrix2):
        if matrix1.dim == matrix2.dim:
            for i in range(self.dim):
                for j in range(self.dim):
                    for k in range(self.dim):
                        self.matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return self.matrix

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

    print()
    print("+"*10)
    matrix9 = Matrix(2,2)
    matrix9.transpose(matrix1)
    print(matrix9)
    print("+" * 10)
    print()

    # 3x3 checking
    matrix5 = Matrix(3, 3)
    print("matrix5 is")
    matrix5.setdata([[1, 2,3], [3, 4,5],[5,6,7]])
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


main()
