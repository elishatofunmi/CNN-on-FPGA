
import myhdl
import migen
import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
from dl2hdl.model import MyHdlModel
from dl2hdl.basic.fixed_def import FixedDef
import os


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == '__main__':
    PATH = os.getcwd() + '//pytorch_model.pt'
    model = Net()
    model.load_state_dict(torch.load(PATH))
    model.eval()
    
    hdl_model = MyHdlModel(torch_model=model, fxp=FixedDef(4, 4))
    hdl_model.convert(path='', name='my_net')
    print(os.getcwd())
