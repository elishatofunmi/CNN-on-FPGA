import numpy as np
import tensorflow as tf
import keras



class write_to_disk:
    def __init__(self):
        from keras.datasets import mnist

        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()

        self.x_train_list = self.conv_list(self.X_train)
        self.x_test_list = self.conv_list(self.X_test)
        self.y_train_list = self.conv_y_list(self.y_train)
        self.y_test_list = self.conv_y_list(self.y_test)

        fob = open('x_train.txt', 'w')
        fob.write(str(self.x_train_list))
        fob.close()

        fob_test = open('x_test.txt', 'w')
        fob_test.write(str(self.x_test_list))
        fob_test.close()


        fob_y_train = open('y_train.txt', 'w')
        fob_y_train.write(str(self.y_train_list))
        fob_y_train.close()


        fob_y_test = open('y_test.txt', 'w')
        fob_y_test.write(str(self.y_test_list))
        fob_y_test.close()
        return


    def shape(self,two_dimensional):
        no_of_rows, no_of_cols = len(two_dimensional), len(two_dimensional[0])
        return no_of_rows, no_of_cols


    def conv_list(self, matrix):
        x = []
        x = matrix.tolist()
        return x

    def conv_y_list(self,matrix):        
        return matrix.tolist()



if __name__ == '__main__':
    todisk = write_to_disk()