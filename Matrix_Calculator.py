class Matrix:
    def __init__(self, rows, columns,dim):
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
        self.matrix = [[0] * self.columns for _ in range(self.rows)]

    def get_value(self, rows, columns):
         return self.matrix[rows][columns]

    def get_matrix(self):
        print("-" * 10)
        for i in self.matrix:
            print(i)
        print("-" * 10)

    def setdata(self, data):
        if self.dim == len(data[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] = data[i][j]
            return self.matrix
        else:
            print("Please enter the values that matches the size of the matrix!")

    def addition(self, matrix1, matrix2):
        if matrix1.dim == matrix2.dim == 2:
            for i in range(2):
                for j in range(2):
                    self.matrix[i][j] = matrix1.get_value(i,j) + matrix2.get_value(i,j)
            return self.matrix
        if matrix1.dim == matrix2.dim == 3:
            for i in range(3):
                for j in range(3):
                    self.matrix[i][j] = matrix1.get_value(i, j) + matrix2.get_value(i, j)
            return self.matrix



# class Matrix3x3:

def main():
    matrix1 = Matrix(2, 2)

    # print(a.get_matrix())
    matrix1.setdata([[1, 1], [2, 2]])
    matrix2 = Matrix(2, 2)
    matrix2.setdata([[2, 2], [3, 3]])
    #print(matrix1.get_value(0,0))

    # print(matrix1.get_matrix())


    matrix3 = Matrix(2,2)
    matrix3.addition(matrix1, matrix2)
    print(matrix3.get_matrix())


main()
