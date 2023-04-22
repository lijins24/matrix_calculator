class Matrix:
    def __init__(self, rows, columns):
        self.matrix = []
        self.rows = rows
        self.columns = columns
        self.dim = 0
        if self.rows == 2 and self.columns == 2:
            self.dim = 2
        elif self.rows == 3 and self.columns == 3:
            self.dim = 3
        else:
            print("Please enter a 2x2 or 3x3 dimension matrix!")
            raise ValueError
        for _ in range(self.rows):
            self.matrix.append([0] * self.columns)
        if self.dim == 3:
            self.pivot_variable = [None, None, None]
        if self.dim == 2:
            self.pivot_variable = [None, None]

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, i):
        return self.matrix[i]

    def __str__(self):
        return '\n'.join(' | '.join(map(str, rows)) for rows in self.matrix)

    def setdata(self, data):
        """
        This function is used to set data in the matrix
        :param data: data inserted in the matrix
        :return: the matrix is formed
        """
        if self.dim == len(data[0]):
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] = data[i][j]
            return self.matrix
        else:
            print("Please enter the values that matches the size of the matrix!")

    def addition(self, matrix1, matrix2):
        """
        This function is used to add up two matrices
        :param matrix1: the first matrix used
        :param matrix2: the second matrix used
        :return: the matrix is modified with the sum of two matrices
        """
        if len(matrix1) == len(matrix2):
            for i in range(len(matrix1)):
                for j in range(len(matrix1)):
                    self.matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            return self.matrix
        else:
            print("Please make sure two matrices have same dimension!")

    def subtraction(self, matrix1, matrix2):
        """
        This function is used to subtract a matrix from another matrix
        :param matrix1: the matrix that is subtracted
        :param matrix2: the matrix used to subtract from another matrix
        :return: the matrix is modified with the subtraction of two matrices
        """
        if len(matrix1) == len(matrix2):
            for i in range(len(matrix1)):
                for j in range(len(matrix1)):
                    self.matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            return self.matrix
        else:
            print("Please make sure two matrices have same dimension!")

    def transpose(self, matrix1):
        """
        This function is used to get the transpose of the given matrix
        : param matrix1: the matrix input to get transpose form
        :return: modify the given matrix into its transpose form
        """
        tem = []
        for i in range(matrix1.dim):
            for j in range(matrix1.dim):
                tem = [[matrix1[j][i] for j in range(matrix1.dim)] for i in range(matrix1.dim)]
        for k in range(len(tem)):
            for l in range(len(tem)):
                self.matrix[k][l] = tem[k][l]
        return self.matrix

    def multiplication(self, matrix1, matrix2):
        """
        This function is used to multiply two matrices
        :param matrix1: the first matrix used
        :param matrix2: the second matrix used
        :return: the matrix is modified with the multiplication result of two matrices
        """
        if len(matrix1) == len(matrix2):
            for i in range(len(matrix1)):
                for j in range(len(matrix1)):
                    for k in range(self.dim):
                        self.matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return self.matrix

    def inverse(self, matrix1):
        """
        This function is used to get the inverse result of the given matrix
        : param matrix1: the matrix input to get inverse form
        :return: the matrix is modified with the inverse result of the given matrix
        """
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
            if deter_3x3 == 0:
                return None
            else:
                self.matrix = [[(e * i - f * h), (c * h - b * i), (b * f - c * e)],
                               [(f * g - d * i), (a * i - c * g), (c * d - a * f)],
                               [(d * h - e * g), (g * b - a * h), (a * e - b * d)]]
                base = 1 / deter_3x3
                self.matrix = [[base * i for i in row] for row in self.matrix]
                return self.matrix

    def rank(self):
        """
        This function is used to determine the rank for 2x2 matrix and 3x3 matrix
        : param: input a matrix
        :return: the rank of the matrix in integers
        """
        if self.dim == 2:
            a, b = self.matrix[0]
            c, d = self.matrix[1]
            if (a, b) == (0, 0):
                return 0
            elif (c, d) == (0, 0):
                return 0
            elif (a * d) - (b * c) != 0:
                return 2
            else:
                return 1
        elif self.dim == 3:
            det = self.matrix[0][0] * (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]) \
                  - self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0]) \
                  + self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])
            if det != 0:
                return 3
            elif self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] != 0:
                return 2
            elif any(self.matrix[0]) or any(self.matrix[1]) or any(self.matrix[2]):
                return 1
            else:
                return 0

    def positive_definite(self):
        """
        This function is used to determine whether the matrix is a positive definite
        : param: input a matrix
        :return: return true if it is a positive definite, return false if it is not a posistive definite
        """
        if self.dim == 2:
            det = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            if self.matrix[0][0] > 0 and det > 0:
                return True
            else:
                return False
        elif self.dim == 3:
            det = self.matrix[0][0] * (self.matrix[1][1] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][1]) \
                  - self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0]) \
                  + self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])
            if self.matrix[0][0] < 0:
                return False
            else:
                if self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0] < 0:
                    return False
                elif det < 0:
                    return False
                elif self.matrix[0][0] > 0 and self.matrix[1][1] > 0 and self.matrix[2][2] > 0 \
                        and self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0] > 0 \
                        and (self.matrix[0][0], self.matrix[0][1], self.matrix[1][0], self.matrix[1][1]) > (0, 0, 0, 0):
                    return True
                else:
                    return False

    def helper_add_multiply(self, row1, row2, multiple=1.0):
        """
        This function is used as a helper function to help row_echelon function. It can reduce the desired value to zero
        :param row1: the base row that will not be changed
        :param row2: the row that will be reduced
        :param multiple: the multiplier that will make the desired value equals corresponding index value,
        so it can be reduced to zero
        :return: modify the matrix so the desired index value can become zero
        """
        if row1 <= 0 or row2 <= 0 or row1 > self.dim or row2 > self.dim:
            print("Error! Please enter an existing row index!")
            raise IndexError
        else:
            for i in range(self.dim):
                self.matrix[row2 - 1][i] += multiple * self.matrix[row1 - 1][i]

    def helper_row_exchange(self, row1, row2):
        """
        This function is used as a helper function to help row_echelon function. It can exchange the position of
        the input two rows
        :param row1: first row user picks to change
        :param row2: second row user picks to change
        :return: modify the matrix so the two rows' position will be exchanged
        """
        if row1 <= 0 or row2 <= 0 or row1 > self.dim or row2 > self.dim:
            print("Error! Please enter an existing row index!")
            raise IndexError
        else:
            temp = self.matrix[row1 - 1]
            self.matrix[row1 - 1] = self.matrix[row2 - 1]
            self.matrix[row2 - 1] = temp
        return self.matrix

    def row_echelon(self):
        """
        This function is used to perform row reduction for the matrix, reduce it to upper triangular form
        : param: input a matrix
        :return: modify the input matrix into its upper triangular form
        """
        if self.dim == 3:
            if self.matrix[0][0] == 0 and self.matrix[1][0] == 0 and self.matrix[2][0] == 0:
                print("This is a 3x2 matrix! Please enter a 3x3 matrix!")
                raise ValueError
            elif self.matrix[0][1] == 0 and self.matrix[1][1] == 0 and self.matrix[2][1] == 0:
                print("This is a 3x2 matrix! Please enter a 3x3 matrix!")
                raise ValueError
            elif self.matrix[0][2] == 0 and self.matrix[1][2] == 0 and self.matrix[2][2] == 0:
                print("This is a 3x2 matrix! Please enter a 3x3 matrix!")
                raise ValueError
            elif self.matrix[0][0] == 0 and self.matrix[0][1] == 0 and self.matrix[0][2] == 0:
                print("This is a 2x3 matrix! Please enter a 3x3 matrix!")
                raise ValueError
            elif self.matrix[1][0] == 0 and self.matrix[1][1] == 0 and self.matrix[1][2] == 0:
                print("This is a 2x3 matrix! Please enter a 3x3 matrix!")
                raise ValueError
            elif self.matrix[2][0] == 0 and self.matrix[2][1] == 0 and self.matrix[2][2] == 0:
                print("This is a 2x3 matrix! Please enter a 3x3 matrix!")
                raise ValueError

            if self.matrix[0][0] == 0:
                if self.matrix[1][0] == 0:
                    self.helper_row_exchange(1, 3)
                    if self.matrix[1][1] == 0:
                        if self.matrix[2][1] == 0:
                            self.helper_add_multiply(2, 3, -(self.matrix[2][2] / self.matrix[1][2]))
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][2]
                        else:
                            self.helper_row_exchange(2, 3)
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][1]
                            self.pivot_variable[2] = self.matrix[2][2]
                    else:
                        if self.matrix[2][1] == 0:
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][1]
                            self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                            if self.matrix[2][2] != 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                            else:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][2]
                else:
                    self.helper_row_exchange(1, 2)
                    if self.matrix[2][0] == 0:
                        if self.matrix[1][1] == 0:
                            if self.matrix[2][1] == 0:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][2] / self.matrix[1][2]))
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][2]
                            else:
                                self.helper_row_exchange(2, 3)
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            if self.matrix[2][1] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                            else:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                                if self.matrix[2][2] != 0:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][1]
                                    self.pivot_variable[2] = self.matrix[2][2]
                                else:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][2]
                    else:
                        self.helper_add_multiply(1, 3, -(self.matrix[2][0] / self.matrix[0][0]))
                        if self.matrix[2][1] == 0:
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][1]
                            self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                            if self.matrix[2][2] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                            else:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
            else:
                if self.matrix[1][0] == 0:
                    if self.matrix[2][0] == 0:
                        if self.matrix[1][1] == 0:
                            if self.matrix[2][1] == 0:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][2] / self.matrix[1][2]))
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][2]
                            else:
                                self.helper_row_exchange(2, 3)
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            if self.matrix[2][1] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                            else:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                                if self.matrix[2][2] != 0:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][1]
                                    self.pivot_variable[2] = self.matrix[2][2]
                                else:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][2]
                    else:
                        self.helper_add_multiply(1, 3, -(self.matrix[2][0] / self.matrix[0][0]))
                        if self.matrix[2][1] == 0:
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][1]
                            self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                            if self.matrix[2][2] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                            else:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                else:
                    self.helper_add_multiply(1, 2, -(self.matrix[1][0] / self.matrix[0][0]))
                    if self.matrix[2][0] == 0:
                        if self.matrix[1][1] == 0:
                            if self.matrix[2][1] == 0:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][2] / self.matrix[1][2]))
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][2]
                            else:
                                self.helper_row_exchange(2, 3)
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            if self.matrix[2][1] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]
                            else:
                                self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                                if self.matrix[2][2] != 0:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][1]
                                    self.pivot_variable[2] = self.matrix[2][2]
                                else:
                                    self.pivot_variable[0] = self.matrix[0][0]
                                    self.pivot_variable[1] = self.matrix[1][2]
                    else:
                        self.helper_add_multiply(1, 3, -(self.matrix[2][0] / self.matrix[0][0]))
                        if self.matrix[2][1] == 0:
                            self.pivot_variable[0] = self.matrix[0][0]
                            self.pivot_variable[1] = self.matrix[1][1]
                            self.pivot_variable[2] = self.matrix[2][2]
                        else:
                            self.helper_add_multiply(2, 3, -(self.matrix[2][1] / self.matrix[1][1]))
                            if self.matrix[2][2] == 0:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                            else:
                                self.pivot_variable[0] = self.matrix[0][0]
                                self.pivot_variable[1] = self.matrix[1][1]
                                self.pivot_variable[2] = self.matrix[2][2]

        elif self.dim == 2:
            if self.matrix[0][0] == 0:
                if self.matrix[0][1] == 0:
                    if self.matrix[1][0] != 0:
                        pivot_one = self.matrix[1][0]
                        self.helper_row_exchange(1, 2)
                        self.pivot_variable = [pivot_one, None]
                        return self.matrix
                    elif self.matrix[1][0] == 0:
                        if self.matrix[1][1] == 0:
                            self.pivot_variable = [None, None]
                            return self.matrix
                        else:
                            pivot_one = self.matrix[1][1]
                            self.helper_row_exchange(1, 2)
                            self.pivot_variable = [pivot_one, None]
                            return self.matrix
                else:
                    if self.matrix[1][0] == 0:
                        pivot_one = self.matrix[0][1]
                        pivot_two = None
                        self.matrix[1][1] = 0
                        self.matrix[1][0] = 0
                        self.pivot_variable = [pivot_one, pivot_two]
                        return self.matrix
                    else:
                        self.helper_row_exchange(1, 2)
                        pivot_one = self.matrix[0][0]
                        pivot_two = self.matrix[1][1]
                        self.pivot_variable = [pivot_one, pivot_two]
                        return self.matrix
            else:
                if self.matrix[1][0] == 0:
                    pivot_one = self.matrix[0][0]
                    if self.matrix[1][1] == 0:
                        pivot_two = None
                    else:
                        pivot_two = self.matrix[1][1]
                    self.pivot_variable = [pivot_one, pivot_two]
                    return self.matrix
                else:
                    self.helper_add_multiply(1, 2, -(self.matrix[1][0] / self.matrix[0][0]))
                    pivot_one = self.matrix[0][0]
                    if self.matrix[1][1] == 0:
                        pivot_two = None
                    else:
                        pivot_two = self.matrix[1][1]
                    self.pivot_variable = [pivot_one, pivot_two]
                    return self.matrix
        return self.matrix
