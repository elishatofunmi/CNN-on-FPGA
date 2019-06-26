% text files
cd 
data = uiimport('train.csv');

% array indexing

%row_3 = data(3,:); % row 3, all columns

%col_4 = data(10:14,4); % row 10 to 14, 4 columns

layers = [imageInputLayer([28 28 1])
          convolution2dLayer(5,20)
          reluLayer
          maxPooling2dLayer(2,'Stride',2)
          fullyConnectedLayer(10)
          softmaxLayer
          classificationLayer];
      
options = trainingOptions('sgdm');

convnet = trainNetwork(data,layers,options);

