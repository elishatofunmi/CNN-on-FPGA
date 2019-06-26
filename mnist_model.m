modelfile = 'model_cnn.h5';

classNames = {'0', '1','2','3','4','5','6','7','8','9'};

net = importKerasNetwork(modelfile, 'Classes', classNames);

% plot the CNN network architecture
figure
plot(net);
title('CNN network architecture on an MNIST dataset')



% change file path to access images to be predicted

cd test_images;

% import the test input data
data = sbionmimport('test_data.csv');