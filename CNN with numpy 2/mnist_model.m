modelfile = 'model_cnn.h5';

classNames = {'0', '1','2','3','4','5','6','7','8','9'};

net = importKerasNetwork(modelfile, 'Classes', classNames);

% plot the CNN network architecture
%figure
%plot(net);
%title('CNN network architecture on an MNIST dataset')



% change file path to access images to be predicted

%cd test_images;

% import the test input data
%data = sbionmimport('test_data.csv');



copyfile(fullfile(fxpnn_demo_dir, [model,'.slx']), fullfile(fxpnn_temp_dir, [model '_toconvert.slx']));


% Open and Inspect model
model = [model '_toconvert'];
system_under_design = [model '/Function Fitting Neural Network'];
baseline_output = [model '/yarr'];
open_system(model);

% Set up model for HDL code generation
hdlsetup(model);

% You can run the following command to check for HDL code generation
% compatibility.
%
% |checkhdl(systemname,'TargetDirectory',workingdir);|
%
%
%
% Run the following command to generate HDL code.
%
% |makehdl(systemname,'TargetDirectory',workingdir);|
%
% Run the following command to generate the test bench.
%
% |makehdltb(systemname,'TargetDirectory',workingdir);|
%
close all;
Simulink.sdi.close;
clear engineInputs engineTargets net x t
clear h1 h2 h3 
clear sim_out logsout nn_out yarr_out ypred actual
clear solution opts p
close_system(model, 0);
close_system(sysName, 0);
clear system_under_design model block_path
clear netName sysName
clear best_solution baseline_output
cd(current_dir);
status = rmdir(fxpnn_temp_dir, 's'); %#ok
clear fxpnn_demo_dir fxpnn_temp_dir current_dir status
displayEndOfDemoMessage(mfilename)

% Create a function to plot regression data
function plotRegression(sim_out, baseline_path, neural_network_output_path, plotTitle)
    
    nn_out = find(sim_out.logsout, 'BlockPath', neural_network_output_path);
    yarr_out = find(sim_out.logsout, 'BlockPath', baseline_path);

    ypred = nn_out{1}.Values.Data;
    actual = yarr_out{1}.Values.Data;

    figure;
    plotregression(double(ypred), actual, plotTitle);
end