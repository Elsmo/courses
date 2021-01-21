class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        help_lst = []
        for mini_lst in self.my_matrix:
            help_lst.append(' '.join(list(map(str, mini_lst))))
        return '\n'.join(list(map(str, help_lst)))

    def test(self, other):
        if len(self.my_matrix) == len(other.my_matrix):
            for mini_lst in self.my_matrix:
                for mini_lst2 in other.my_matrix:
                    if len(mini_lst) != len(mini_lst2):
                        return False
        else:
            return False

    def __add__(self, other):
        new_matrix, new = [], []
        i = 0
        if self.test(other):
            print('Такие матрицы не поддаются сложению')
        else:
            for mini_lst in range(len(self.my_matrix)):
                for j in range(len(self.my_matrix[0])):
                    new_matrix.append(self.my_matrix[mini_lst][j] + other.my_matrix[mini_lst][j])
            while i <= len(self.my_matrix[0]):
                new.append(new_matrix[:len(self.my_matrix[0])])
                new_matrix = new_matrix[len(self.my_matrix[0]):]
                i += 1
            print()
            print(Matrix(new))


a = Matrix([[31, 22], [37, 43], [51, 86]])
print(a)
b = Matrix([[9, 8], [3, 7], [9, 4]])
a + b
