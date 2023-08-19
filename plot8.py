from pylab import *
import pylab as pl
import matplotlib.pyplot as plt

ft8test = np.loadtxt('ft8.txt', skiprows=1)
ft8gas = np.loadtxt('ft8gas.txt',skiprows=1)
ft8ph = np.loadtxt('ft8pH.txt',skiprows=1)

plt.figure()
plt.subplot(241)
plt.plot(ft8gas[:,0],ft8gas[:,1],'rs',ft8test[:,0],ft8test[:,3],'g')
plt.title('CO2')

plt.subplot(242)
plt.plot(ft8gas[:,0],ft8gas[:,2],'rs',ft8test[:,0],ft8test[:,4],'g')
plt.title('CH4')

plt.subplot(243)
plt.plot(ft8ph[:,0],ft8ph[:,1],'rs',ft8test[:,0],ft8test[:,13],'g')
plt.title('Fe(II)')
plt.subplot(244)
plt.plot(ft8ph[:,0],ft8ph[:,2],'rs',ft8test[:,0],ft8test[:,1],'g')
plt.title('pH')



plt.subplot(245)
plt.plot(ft8test[:,0],ft8test[:,9],'g')
plt.title('Acetate')

plt.subplot(246)
plt.plot(ft8test[:,0],ft8test[:,10],'g')
plt.title('Glucose')

plt.subplot(247)
plt.plot(ft8test[:,0],ft8test[:,12],'g')
plt.title('WEOC')

plt.subplot(248)
plt.plot(ft8test[:,0],ft8test[:,19],'g')
plt.title('SOM1')


plt.show()
