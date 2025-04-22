class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def add(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                sum_product = 0
                for k in range(3):
                    sum_product += self.data[i][k] * other.data[k][j]
                row.append(sum_product)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        transposed = []
        for j in range(3):
            row = []
            for i in range(3):
                row.append(self.data[i][j])
            transposed.append(row)
        return Matrix(transposed)

A=Matrix([[1,2,3],[4,5,6],[7,8,9]])
B=Matrix([[9,8,7],[6,5,4],[3,2,1]]) 
print(A.add(B))
print()
print(A.multiply(B))
print()
print(A.transpose())
