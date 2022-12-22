from scipy import *
import numpy as np
import matplotlib.pyplot as plt


# fig=plt.figure()
# data1= np.loadtxt('/home/fardous/Desktop/Talys/talys/Summercourse-ex/Task-3(03_12)/Data/Finlay')
# data2 = np.loadtxt('/home/fardous/Desktop/Talys/talys/Summercourse-ex/Task-3(03_12)/Data/Rapaport')
# plt.plot(data1[:,0], data1[:,1]*1000, 'o',  label='R.W.Finlay')
# plt.legend(loc='lower right')
# plt.plot(data2[:,0], data2[:,1]*1000, '+', label='J.Rapaport')
# plt.legend(loc='lower right')


data_a= np.loadtxt('/home/shailendra/Task-5(04_12)/ex5/talys/gammastrength/Photoabsorption')
plt.semilogy(data_a[0:,0], (data_a[0:,1]+data_a[0:,2]), 'o',  label='GLO:gnorm=1')
plt.legend(loc='upper right')

data_a= np.loadtxt('/home/shailendra/Task-5(04_12)/ex5/talys/gammastrength/photo2')
plt.semilogy(data_a[0:,0], (data_a[0:,1]+data_a[0:,2]), '+',  label='GLO:gnorm=8')
plt.legend(loc='upper right')

#data_a= np.loadtxt('/home/shailendra/Task-5(04_12)/ex5/talys/gammastrength/Photo')

#plt.semilogy(data_a[0:,0], (data_a[0:,1]+data_a[0:,2]), '*',  label='GLO:gnorm=5.9')
#plt.legend(loc='upper right')

data_a= np.loadtxt('/home/shailendra/Task-5(04_12)/ex5/talys/gammastrength/totalxs.tot')
plt.loglog(data_a[5:,0], data_a[5:,1],  label='Strength:1')
plt.legend(loc='upper right')




#plt.plot(1e-6*data1[:,0], data1[:,1], 'b')
axes = plt.gca()
axes.set_xlim([0,30])
axes.set_ylim([10e-10,10e-6])
#axes.set_yscale('log')
axes.set_xlabel('Energy MeV')
axes.set_ylabel('gammastrength [E1+M1]')

plt.show()
