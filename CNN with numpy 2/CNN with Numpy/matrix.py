"""
1. convert image arrays to list arrays.
2. A function that gets a particular convolution of size (k by k) from the image array 
which is now being represented as a list.
3. generate random values of integers or floats between 0 and 1.
4. Flatten layer
5. neurons initialization
6. activation function.
7. wrap up feed forward and backpropagation.
"""



class matrix:
    def __init__(self):
        """
        m: is the number of rows.
        n: is the number of columns.
       
        """

        return
    
    def initialize_matrix(self, m, n):
        matrix = []
        for k in range(m):
            matrix.append([])
        return matrix


    def zero_matrix(self,m,n):
        row =  []
        zero_matrix =[]
        for k in range(m):
            row.append(0)
        
        for l in range(n): 
            zero_matrix.append(row)

        return zero_matrix

    def shape(self,matrix):
        no_of_rows = len(matrix)
        no_of_columns = len(matrix[0])
        return no_of_rows, no_of_columns


    def multiply(self, a, b):
        list_mul = []
        for i, j in zip(a,b):
            list_mul.append(i*j)
        return sum(list_mul)

    def matmul(self, a,b):
        l,k = self.shape(a)
        c,d = self.shape(b)

        output_multiplication = self.zero_matrix(l,d)
        if k == c:
            "output mulitplication will be of shape l by d"
            for z in range(l):
                for k in range(d):
                    find_row = a[l]
                    find_col = [b[l][z] for h in range(l)]
                    output_multiplication[z][k] = self.multiply(find_row, find_col)

        else:
            raise('Invalid dimension')


        return output_multiplication





class random:
    def __init__(self):
        """
        generates random values or type int or float
        """
        return

    def random_int(self):
        return

    