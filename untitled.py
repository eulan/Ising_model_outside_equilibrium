# -*- coding: utf-8 -*-
"""Untitled.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EMTFu5oj8L9zqgv0MRbU_P34fESLnNtX
"""

from google.colab import drive
drive.mount('/content/drive/')

!sudo apt-get install libmp3-dev cmake automake libtool
!pip3 install torch torchvision
!pip install pycuda
!pip install pillow
import sys
sys.version
!nvcc --version

# importing the data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import ListedColormap
N=100
NR=100
tmax=800
csv_path = '/content/drive/My Drive/Colab Notebooks/ising/lte_g1_N100_Nr_100_tmax_800.csv'
df=pd.read_csv(csv_path, header = None)
df.head()
time = df[10]
lattice = df.drop(10, axis = 1)
df.shape[0]

import torch
import torch.nn as nn
import torch.nn.functional as F
import pycuda.driver as cuda
from torch.utils.data import Dataset, DataLoader

torch.cuda.is_available()


cuda.init()## Get Id of default device
print(torch.cuda.current_device())
print(cuda.Device(0).name())
print(torch.cuda.memory_allocated())
print(torch.cuda.memory_cached())

X = np.asarray(df)
Y = np.zeros((df.shape[0], 4),dtype = float)
#Y[:,0]=lattice.mean(axis=1)    

def Measurer(Y,X,N):
    gmen1=0
    gmen2=0
    gmen3=0
    mag = 0
    for i in range(0,X.shape[0]):
        
        gmen1=0
        gmen2=0
        gmen3=0
        mag = 0
        
        for j in range(0,N):
            mag += X[i,j]
            gmen1+=X[i,j]*X[i,(j+1)%N]
            gmen2+=X[i,j]*X[i,(j+2)%N]
            gmen3+=X[i,j]*X[i,(j+3)%N]
            
        gmen1/=N
        gmen2/=N
        gmen3/=N
        mag /= N
        
        Y[i,0] = mag
        Y[i,1] = 0.5*(1-gmen1)
        Y[i,2] = 0.25*(1-2*gmen1+gmen2)
        Y[i,3] = 0.25*(1-3*gmen1+2*gmen2-gmen3+gmen1**2+gmen1*gmen3-gmen2**2)
    return Y

Y = Measurer(Y,X,N)
    
class Net(nn.Module):
    
    # Constructor
    def __init__(self, in_size, n_hidden1,n_hidden2, out_size, p = 0, m = 0.9):
        super(Net, self).__init__()
        self.drop = nn.Dropout(p=p)
        self.linear1 = nn.Linear(in_size, n_hidden1)
        self.linear2 = nn.Linear(n_hidden1, n_hidden2)
        self.linear3 = nn.Linear(n_hidden2, out_size)
        self.bn1 = nn.BatchNorm1d(n_hidden1, momentum = m)
        self.bn2 = nn.BatchNorm1d(n_hidden2, momentum = m)
    
    # Prediction function
    def forward(self, x):
        x = F.relu(self.bn1(self.drop(self.linear1(x))))
        x = F.relu(self.bn2(self.drop(self.linear2(x))))
        x = self.linear3(x)
        return x
      
def init_weights(m):
    if type(m) == nn.Linear:
        torch.nn.init.xavier_uniform_(m.weight)
        m.bias.data.fill_(0.01)
def plotter(X,y,y_hat):
  T=X[:,N]
  t_real = np.zeros(tmax, dtype = float)
  counter = np.zeros(tmax, dtype = int)
  Op_real = np.zeros((tmax,4), dtype = float)
  Op_real_model = np.zeros((tmax,4), dtype = float)
  for i in range(0,len(T)):
    if int(N*T[i]) < tmax :
      t_real[int(N*T[i])]+=T[i]
      Op_real[int(N*T[i]),:] += y[i,:]
      Op_real_model[int(N*T[i]),:] += y_hat[i,:]
      counter[int(N*T[i])]+=1
  for i in range(0,tmax):
    t_real[i]/=counter[i]
    Op_real[i,:] /= counter[i]
    Op_real_model[i,:]/= counter[i]
    
  plt.figure()
  plt.figure(figsize=(8,7))
  plt.subplot(221)
  plt.scatter(t_real,Op_real[:,0])
  plt.scatter(t_real,Op_real_model[:,0])
  red_patch = mpatches.Patch(color='black', label='0')
  red_patch1 = mpatches.Patch(color='orange', label='DL')
  red_patch2 = mpatches.Patch(color='blue', label='KMC')
  plt.legend(handles=[red_patch,red_patch1,red_patch2])
  plt.yscale('linear')
  plt.ylim(Op_real[:,0].min(),Op_real[:,0].max())
  plt.title('Magnetization')
  plt.grid(True)

  plt.subplot(222)
  x = np.linspace(t_real.min(),t_real.max(),500)
  plt.plot(x, 0.28*x**(-0.5), color = 'black')
  red_patch = mpatches.Patch(color='black', label='0.28*x**(-0.5)')
  red_patch1 = mpatches.Patch(color='orange', label='DL')
  red_patch2 = mpatches.Patch(color='blue', label='KMC')
  plt.legend(handles=[red_patch,red_patch1,red_patch2]) 
  plt.scatter(t_real,Op_real[:,1])
  plt.scatter(t_real,Op_real_model[:,1])
  plt.ylim(Op_real_model[:,1].min(),Op_real_model[:,1].max())
  #plt.yscale('log')
  plt.title('G_0')
  plt.grid(True)

  plt.subplot(223)
  plt.scatter(t_real,Op_real[:,2])
  plt.scatter(t_real,Op_real_model[:,2])
  plt.plot(x, 0.07*x**(-1.5), color = 'black')
  red_patch = mpatches.Patch(color='black', label='0.07*x**(-1.5)')
  red_patch1 = mpatches.Patch(color='orange', label='DL')
  red_patch2 = mpatches.Patch(color='blue', label='KMC')
  plt.legend(handles=[red_patch,red_patch1,red_patch2]) 
  plt.ylim(Op_real_model[:,2].min(),Op_real_model[:,2].max())
  #plt.yscale('log')
  plt.title('G_1')
  plt.grid(True)

  plt.subplot(224)
  plt.scatter(t_real,Op_real[:,3])
  plt.scatter(t_real,Op_real_model[:,3])
  plt.plot(x, 0.039*x**(-3), color = 'black')
  red_patch = mpatches.Patch(color='black', label='0.039*x**(-3)')
  red_patch1 = mpatches.Patch(color='orange', label='DL')
  red_patch2 = mpatches.Patch(color='blue', label='KMC')
  plt.legend(handles=[red_patch,red_patch1,red_patch2]) 
  plt.ylim(Op_real_model[:,3].min(),Op_real_model[:,3].max())
  #plt.yscale('log')
  plt.title('G_2')
  plt.grid(True)

  #plt.gca().yaxis.set_minor_formatter(NullFormatter())
  plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
  plt.savefig("result.jpg", dpi=150)
  plt.show()
  
  
def trainer(epochs):
  for t in range(epochs):
    prediction = model(X_train.cuda()).cuda()     # input x and predict based on x

    loss = loss_func(prediction, y_train.cuda())     # must be (1. nn output, 2. target)
    if t%200 == 0:
      LOSS.append(loss.item())
    if t%500 == 0:
      print(loss)
    optimizer.zero_grad()   # clear gradients for next train
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients
  if t==(epochs-1):
    plt.plot(range(len(LOSS)), LOSS)
    plt.yscale('log')
    plt.show()

m = 0.95
net = Net(N+1,2*N,2*N,4,p=0, m = m)
net.apply(init_weights)
y_train = torch.from_numpy(Y).type(torch.FloatTensor)
X_train =  torch.from_numpy(X).type(torch.FloatTensor)
model = net.cuda()
print(model)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum = m)
loss_func = torch.nn.MSELoss()
LOSS = []
epochs = 2000

torch.cuda.empty_cache() #in the final or the applications for clear the cache.
next(model.parameters()).is_cuda

trainer(epochs)
torch.cuda.empty_cache()

y_hat = np.zeros((y_train.shape[0], 4),dtype = float) 
y_hat = torch.from_numpy(y_hat).type(torch.FloatTensor)
y_hat = model(X_train.cuda()).cpu()
y_hat = y_hat.detach().numpy()
y = y_train.numpy()
X = X_train.numpy()
plotter(X,y,y_hat)

