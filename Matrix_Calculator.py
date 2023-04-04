class Matrix2x2:
    def __init__(self, rows=2, columns=2):
        # set the default matrix size to 2x2
        self.matrix = []
        self.rows = rows
        self.columns = columns
        # if not, then raise error
        if self.rows != 2 or self.columns != 2:
            print("Please enter a 2x2 or 3x3 dimension matrix!")
            raise ValueError
        # construct the matrix structure
        self.matrix = [[0] * self.columns for _ in range(self.rows)]

    def get_matrix(self):
        return self.matrix

    def setdata(self, data):
        # set the values inside the matrix
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = data[i][j]
        return self.matrix





# class Matrix3x3:

def main():
    a = Matrix2x2()
    print(a.get_matrix())
    print(a.setdata([[1, 2], [3, 4]]))


main()


