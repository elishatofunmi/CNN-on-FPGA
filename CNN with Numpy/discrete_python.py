import random



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


    def transpose(self, matrix):
        x, y = self.shape(matrix)
        zeros_of_transposed_matrix = self.zero_matrix(y,x)

        for i in matrix:
            for j in i:
                zeros_of_transposed_matrix[j][i] = matrix[i][j]
        return zeros_of_transposed_matrix


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

    

    def argmax(self,data):
        max_arg = data.index(max(data))
        return max_arg


def sigmoid(z):
    return 1.0/(1.0+(1/pow(2.718,z)))

def sigmoid_prime(z):
    return sigmoid(z) * (1-sigmoid(z))


class Network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = out = [[[random.random()] for k in range(i)] for i in sizes[1:]]
        self.weights = [rand(y,x) for x,y in zip(sizes[:-1], sizes[1:])]
        self.mat = matrix()

    def rand(y,x):
        return [[random.random() for k in range(x)] for i in range(y)]


    def feedforward(self,a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(self.mat.matmul(w,a)+b)
        return a
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            " Attention Attention Attention "
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, mini_batch_size)]
        for mini_batch in mini_batches:
            self.update_mini_batch(mini_batch, eta)
        if test_data:
            print('Epoch {0}: {1}/{2}'.fomat(j, self.evaluate(test_data), n_test)
        else:
            print('epoch {0} complete'.format(j))
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [self.mat.zero_matrix(self.mat.shape(b)) for b in self.biases]
        nabla_w = [self.mat.zero_matrix(self.mat.shape(w)) for b in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x,y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        self.weights = [w-(eta/len(mini_batch)) *nw for w , nw in zip(self.weights, nabla_w)]

        self.biases = [b - (eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]


    def backprop(self, x, y):
        nabla_b = [self.mat.zero_matrix(self.mat.shape(b)) for b in self.biases]
        nabla_w = [self.mat.zero_matrix(self.mat.shape(b)) for w in self.weights]
        activation = x    #feedforward
        activation,zs = [x], []
        for b, w in zip(self.biases, self.weights):
            z = self.mat.matmul(w,activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activation[-1], y)* sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = self.mat.transpose(self.mat.matmul(delta, activation[-2]))
        for l in range(2, self.num_layers):
            z = zs[-1]
            sp = sigmoid_prime(z)
            delta = self.mat.matmul(delta, self.mat.transpose(self.weights[-l+1]))
        return (nabla_b, nabla_w)




    def evaluate(self, test_data):
        test_results = (np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)


    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return (output_activations-y)

