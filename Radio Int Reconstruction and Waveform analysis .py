#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import zhaires
import numpy as np 
import matplotlib.pyplot as plt 


# In[11]:


filename = "R15.csv"
time, Ex, Ey, Ez = np.loadtxt(filename,unpack=True)
#100PeV Proton Shower
#Z=3.5km
#For the first antenna located at (0,0) 
fig = plt.figure(figsize=(8,5), dpi=80)
ax = plt.subplot(111)
plt.plot(time, Ex,linestyle=":",linewidth=1.5,color = "Red")
plt.plot(time, Ey,linestyle=":",linewidth=1.5,color = "Green")
plt.plot(time, Ez,linestyle=":",linewidth=1.5,color = "Blue")
plt.xlabel("Time (ns)")
plt.ylabel("E-Field")
plt.title ("Run15 Proton Induced Shower")
plt.xlim(-1,10)
plt.ylim(-0.002,0.02)

plt.show()


# In[3]:


print("Direct proton showers with varying heights of 3.5km, 5.25km, 7km. ")


# In[7]:


wv13 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run13_A/waveforms_A.npy") # z=7km
wv14 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run14_B/waveforms_B.npy") # z=5.25km
wv15 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run15_C/waveforms_C.npy") # z=3.5km
wv16 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run16_A/waveforms.npy") # z=7km
wv17 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run17_B/waveforms.npy") # z=5.25km
wv18 = np.load("/Users/herminiocarrillo42069/Desktop/showers/run18_C/waveforms.npy") # z=3.5km


# In[8]:


print(wv13.dtype)


# In[9]:


#Ey for Run_13A
#Z=7.0km

for i in range(25):
    plt.plot(wv13['t'][i], wv13['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.001, 0.001)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[10]:


#Ey for Run14_B
#Z=5.25km

for i in range(25):
    plt.plot(wv16['t'][i], wv16['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.0001, 0.0001)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[11]:


#Ey for Run15_C
#Z=3.50km

for i in range(25):
    plt.plot(wv14['t'][i], wv14['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.001, 0.001)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[12]:


#Ey for Run16_A
#Z=7.0km

for i in range(25):
    plt.plot(wv17['t'][i], wv17['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.0002, 0.0002)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[13]:


#Ey for Run17_B
#z=5.25km

for i in range(25):
    plt.plot(wv17['t'][i], wv17['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.0002, 0.0002)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[14]:


#Ey for Run18_C
#z=3.5km

for i in range(25):
    plt.plot(wv18['t'][i], wv18['Ey'][i], label=i)
plt.xlim(-6,25)
plt.ylim(-0.0002, 0.0002)
plt.title("E-Field of all 25 Antennas")
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.show()


# In[15]:


for i in range(25):
    s = np.zeros(len(wv13['Ey'][i]))
    for j in range(len(wv13['Ey'][i])):
        s[j] = s[j] + wv13['Ey'][i][j]
    #print(s)


# In[16]:


def f(x):
    return x**2

nums = [1,1,1,1,1]

list = 0 
for i in range(6):
    list = list + f(i)
print(list)


# In[17]:


list = 0 
for i in range(25):
    list = list + wv17['Ey'][i]

print(list) # This is the sum of all antenna values without taking into account the light travel time for Ey. 
len(list)

plt.plot(time,list, linestyle='-', linewidth = 0.5, color = "red")
plt.ylim(-0.0001,0.0001)
plt.xlim(-100,1000)
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.title("Ey over Time")
plt.show()


# In[18]:


#atmospheric refractive index equation
a = 325*10**-6
b = 0.1218 #1/km
def n(z):
    # z corresponds to the height of the antenna array in km
    return 1+a*np.exp(-b*z)

height = np.linspace(0,10,11)
ARI = n(height)
plt.xlabel("Height (km)")
plt.ylabel("ARI")

plt.title("ARI as a Function of Height")
plt.plot(height, ARI, linestyle="-", color = "Blue")
plt.show()


# In[19]:


yref = np.linspace(-100,100,25)
xref = np.linspace(0,200,25)

ypts = wv17['y'] #x-coordinates of antenna array 
xpts = wv17['x'] #y-coordinates of antenna array 
time1 = wv17['t'][0] # time in terms of ns 

c = 3.00*10**8 #speed of light in m/s

def xdiff(i,j): #the difference between x-coordinates of location i and j 
    return xpts[i] - xref[j]

def ydiff(i,j): #the difference between y-coordinates of locations i and j 
    return ypts[i] - yref[j]

def dist_ij(i,j): # this is the distance between antenna point i and reference point j 
    return np.sqrt(xdiff(i,j)**2 + ydiff(i,j)**2 + 5250**2)

def delta_ij(i,j,z):
    # travel time of light between location i and j, in units of ns.
    return (dist_ij(i,j)*n(z)/c)*10**9

print(xref[12]) #point of max flux in schoorlemmer paper along x
print(yref[12]) #point of max flux in schoorlemmer paper along y

print("The time it takes light to reach the first antenna at position (0m,0m) from reference point (100m,0m) is", delta_ij(0,12,5.25)," ns")
print("The time interval per recorded data point is" ,wv17['t'][0][10101]-wv17['t'][0][10100], " ns") 
len(time1)


# In[20]:


print("Applying the reconstruction method to the y-component of the electric field for Run17_B.")


# In[65]:


A1_Ey = wv17['Ey'][0] # the measured electric field at antenna 1 
A2_Ey = wv17['Ey'][1] # the measured electric field at antenna 2
A3_Ey = wv17['Ey'][2] # the measured electric field at antenna 3 
A4_Ey = wv17['Ey'][3] # the measured electric field at antenna 4 
A5_Ey = wv17['Ey'][4] # the measured electric field at antenna 5 
A6_Ey = wv17['Ey'][5] # the measured electric field at antenna 6 
A7_Ey = wv17['Ey'][6] # the measured electric field at antenna 7 
A8_Ey = wv17['Ey'][7] # the measured electric field at antenna 8 
A9_Ey = wv17['Ey'][8] # the measured electric field at antenna 9 
A10_Ey = wv17['Ey'][9] # the measured electric field at antenna 10 
A11_Ey = wv17['Ey'][10] # the measured electric field at antenna 11 
A12_Ey = wv17['Ey'][11] # the measured electric field at antenna 12
A13_Ey = wv17['Ey'][12] # the measured electric field at antenna 13 
A14_Ey = wv17['Ey'][13] # the measured electric field at antenna 14
A15_Ey = wv17['Ey'][14] # the measured electric field at antenna 15
A16_Ey = wv17['Ey'][15] # the measured electric field at antenna 16
A17_Ey = wv17['Ey'][16] # the measured electric field at antenna 17
A18_Ey = wv17['Ey'][17] # the measured electric field at antenna 18
A19_Ey = wv17['Ey'][18] # the measured electric field at antenna 19
A20_Ey = wv17['Ey'][19] # the measured electric field at antenna 20
A21_Ey = wv17['Ey'][20] # the measured electric field at antenna 21
A22_Ey = wv17['Ey'][21] # the measured electric field at antenna 22 
A23_Ey = wv17['Ey'][22] # the measured electric field at antenna 23
A24_Ey = wv17['Ey'][23] # the measured electric field at antenna 24
A25_Ey = wv17['Ey'][24] # the measured electric field at antenna 25


# In[66]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta0 = delta_ij(0,0,5.25) # delta_ij for antenna 1
A2_delta0 = delta_ij(1,0,5.25) # delta_ij for antenna 2
A3_delta0 = delta_ij(2,0,5.25) # delta_ij for antenna 3
A4_delta0 = delta_ij(3,0,5.25) # delta_ij for antenna 4
A5_delta0 = delta_ij(4,0,5.25) # delta_ij for antenna 5
A6_delta0 = delta_ij(5,0,5.25) # delta_ij for antenna 6
A7_delta0 = delta_ij(6,0,5.25) # delta_ij for antenna 7
A8_delta0 = delta_ij(7,0,5.25) # delta_ij for antenna 8
A9_delta0 = delta_ij(8,0,5.25) # delta_ij for antenna 9
A10_delta0 = delta_ij(9,0,5.25) # delta_ij for antenna 10
A11_delta0 = delta_ij(10,0,5.25) # delta_ij for antenna 11
A12_delta0 = delta_ij(11,0,5.25) # delta_ij for antenna 12
A13_delta0 = delta_ij(12,0,5.25) # delta_ij for antenna 13
A14_delta0 = delta_ij(13,0,5.25) # delta_ij for antenna 14
A15_delta0 = delta_ij(14,0,5.25) # delta_ij for antenna 15
A16_delta0 = delta_ij(15,0,5.25) # delta_ij for antenna 16
A17_delta0 = delta_ij(16,0,5.25) # delta_ij for antenna 17
A18_delta0 = delta_ij(17,0,5.25) # delta_ij for antenna 18
A19_delta0 = delta_ij(18,0,5.25) # delta_ij for antenna 19
A20_delta0 = delta_ij(19,0,5.25) # delta_ij for antenna 20
A21_delta0 = delta_ij(20,0,5.25) # delta_ij for antenna 21
A22_delta0 = delta_ij(21,0,5.25) # delta_ij for antenna 22
A23_delta0 = delta_ij(22,0,5.25) # delta_ij for antenna 23
A24_delta0 = delta_ij(23,0,5.25) # delta_ij for antenna 24
A25_delta0 = delta_ij(24,0,5.25) # delta_ij for antenna 25

RecA1Ey1 = np.roll(A1_Ey,int(round(A1_delta0)),axis=None)    # shifted e-field at ant1
RecA2Ey1 = np.roll(A2_Ey,int(round(A2_delta0)),axis=None)    # shifted e-field at ant2
RecA3Ey1 = np.roll(A3_Ey,int(round(A3_delta0)),axis=None)    # shifted e-field at ant3
RecA4Ey1 = np.roll(A4_Ey,int(round(A4_delta0)),axis=None)    # shifted e-field at ant4
RecA5Ey1 = np.roll(A5_Ey,int(round(A5_delta0)),axis=None)    # shifted e-field at ant5
RecA6Ey1 = np.roll(A6_Ey,int(round(A6_delta0)),axis=None)    # shifted e-field at ant6
RecA7Ey1 = np.roll(A7_Ey,int(round(A7_delta0)),axis=None)    # shifted e-field at ant7
RecA8Ey1 = np.roll(A8_Ey,int(round(A8_delta0)),axis=None)    # shifted e-field at ant8
RecA9Ey1 = np.roll(A9_Ey,int(round(A9_delta0)),axis=None)    # shifted e-field at ant9
RecA10Ey1 = np.roll(A10_Ey,int(round(A10_delta0)),axis=None)  # shifted e-field at ant10
RecA11Ey1 = np.roll(A11_Ey,int(round(A11_delta0)),axis=None)  # shifted e-field at ant11
RecA12Ey1 = np.roll(A12_Ey,int(round(A12_delta0)),axis=None)  # shifted e-field at ant12
RecA13Ey1 = np.roll(A13_Ey,int(round(A13_delta0)),axis=None)  # shifted e-field at ant13
RecA14Ey1 = np.roll(A14_Ey,int(round(A14_delta0)),axis=None)  # shifted e-field at ant14
RecA15Ey1 = np.roll(A15_Ey,int(round(A15_delta0)),axis=None)  # shifted e-field at ant15
RecA16Ey1 = np.roll(A16_Ey,int(round(A16_delta0)),axis=None)  # shifted e-field at ant16
RecA17Ey1 = np.roll(A17_Ey,int(round(A17_delta0)),axis=None)  # shifted e-field at ant17
RecA18Ey1 = np.roll(A18_Ey,int(round(A18_delta0)),axis=None)  # shifted e-field at ant18
RecA19Ey1 = np.roll(A19_Ey,int(round(A19_delta0)),axis=None) # shifted e-field at ant19
RecA20Ey1 = np.roll(A20_Ey,int(round(A20_delta0)),axis=None) # shifted e-field at ant20
RecA21Ey1 = np.roll(A21_Ey,int(round(A21_delta0)),axis=None) # shifted e-field at ant21
RecA22Ey1 = np.roll(A22_Ey,int(round(A22_delta0)),axis=None) # shifted e-field at ant22
RecA23Ey1 = np.roll(A23_Ey,int(round(A23_delta0)),axis=None) # shifted e-field at ant23
RecA24Ey1 = np.roll(A24_Ey,int(round(A24_delta0)),axis=None) # shifted e-field at ant24
RecA25Ey1 = np.roll(A25_Ey,int(round(A25_delta0)),axis=None) # shifted e-field at ant25


# In[67]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta1 = delta_ij(0,1,5.25) # delta_ij for antenna 1
A2_delta1 = delta_ij(1,1,5.25) # delta_ij for antenna 2
A3_delta1 = delta_ij(2,1,5.25) # delta_ij for antenna 3
A4_delta1 = delta_ij(3,1,5.25) # delta_ij for antenna 4
A5_delta1 = delta_ij(4,1,5.25) # delta_ij for antenna 5
A6_delta1 = delta_ij(5,1,5.25) # delta_ij for antenna 6
A7_delta1 = delta_ij(6,1,5.25) # delta_ij for antenna 7
A8_delta1 = delta_ij(7,1,5.25) # delta_ij for antenna 8
A9_delta1 = delta_ij(8,1,5.25) # delta_ij for antenna 9
A10_delta1 = delta_ij(9,1,5.25) # delta_ij for antenna 10
A11_delta1 = delta_ij(10,1,5.25) # delta_ij for antenna 11
A12_delta1 = delta_ij(11,1,5.25) # delta_ij for antenna 12
A13_delta1 = delta_ij(12,1,5.25) # delta_ij for antenna 13
A14_delta1 = delta_ij(13,1,5.25) # delta_ij for antenna 14
A15_delta1 = delta_ij(14,1,5.25) # delta_ij for antenna 15
A16_delta1 = delta_ij(15,1,5.25) # delta_ij for antenna 16
A17_delta1 = delta_ij(16,1,5.25) # delta_ij for antenna 17
A18_delta1 = delta_ij(17,1,5.25) # delta_ij for antenna 18
A19_delta1 = delta_ij(18,1,5.25) # delta_ij for antenna 19
A20_delta1 = delta_ij(19,1,5.25) # delta_ij for antenna 20
A21_delta1 = delta_ij(20,1,5.25) # delta_ij for antenna 21
A22_delta1 = delta_ij(21,1,5.25) # delta_ij for antenna 22
A23_delta1 = delta_ij(22,1,5.25) # delta_ij for antenna 23
A24_delta1 = delta_ij(23,1,5.25) # delta_ij for antenna 24
A25_delta1 = delta_ij(24,1,5.25) # delta_ij for antenna 25

RecA1Ey2 = np.roll(A1_Ey,int(round(A1_delta1)),axis=None)    # shifted e-field at ant1
RecA2Ey2 = np.roll(A2_Ey,int(round(A2_delta1)),axis=None)    # shifted e-field at ant2
RecA3Ey2 = np.roll(A3_Ey,int(round(A3_delta1)),axis=None)    # shifted e-field at ant3
RecA4Ey2 = np.roll(A4_Ey,int(round(A4_delta1)),axis=None)    # shifted e-field at ant4
RecA5Ey2 = np.roll(A5_Ey,int(round(A5_delta1)),axis=None)    # shifted e-field at ant5
RecA6Ey2 = np.roll(A6_Ey,int(round(A6_delta1)),axis=None)    # shifted e-field at ant6
RecA7Ey2 = np.roll(A7_Ey,int(round(A7_delta1)),axis=None)    # shifted e-field at ant7
RecA8Ey2 = np.roll(A8_Ey,int(round(A8_delta1)),axis=None)    # shifted e-field at ant8
RecA9Ey2 = np.roll(A9_Ey,int(round(A9_delta1)),axis=None)    # shifted e-field at ant9
RecA10Ey2 = np.roll(A10_Ey,int(round(A10_delta1)),axis=None)  # shifted e-field at ant10
RecA11Ey2 = np.roll(A11_Ey,int(round(A11_delta1)),axis=None)  # shifted e-field at ant11
RecA12Ey2 = np.roll(A12_Ey,int(round(A12_delta1)),axis=None)  # shifted e-field at ant12
RecA13Ey2 = np.roll(A13_Ey,int(round(A13_delta1)),axis=None)  # shifted e-field at ant13
RecA14Ey2 = np.roll(A14_Ey,int(round(A14_delta1)),axis=None)  # shifted e-field at ant14
RecA15Ey2 = np.roll(A15_Ey,int(round(A15_delta1)),axis=None)  # shifted e-field at ant15
RecA16Ey2 = np.roll(A16_Ey,int(round(A16_delta1)),axis=None)  # shifted e-field at ant16
RecA17Ey2 = np.roll(A17_Ey,int(round(A17_delta1)),axis=None)  # shifted e-field at ant17
RecA18Ey2 = np.roll(A18_Ey,int(round(A18_delta1)),axis=None)  # shifted e-field at ant18
RecA19Ey2 = np.roll(A19_Ey,int(round(A19_delta1)),axis=None) # shifted e-field at ant19
RecA20Ey2 = np.roll(A20_Ey,int(round(A20_delta1)),axis=None) # shifted e-field at ant20
RecA21Ey2 = np.roll(A21_Ey,int(round(A21_delta1)),axis=None) # shifted e-field at ant21
RecA22Ey2 = np.roll(A22_Ey,int(round(A22_delta1)),axis=None) # shifted e-field at ant22
RecA23Ey2 = np.roll(A23_Ey,int(round(A23_delta1)),axis=None) # shifted e-field at ant23
RecA24Ey2 = np.roll(A24_Ey,int(round(A24_delta1)),axis=None) # shifted e-field at ant24
RecA25Ey2 = np.roll(A25_Ey,int(round(A25_delta1)),axis=None) # shifted e-field at ant25


# In[68]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta2 = delta_ij(0,2,5.25) # delta_ij for antenna 1
A2_delta2 = delta_ij(1,2,5.25) # delta_ij for antenna 2
A3_delta2 = delta_ij(2,2,5.25) # delta_ij for antenna 3
A4_delta2 = delta_ij(3,2,5.25) # delta_ij for antenna 4
A5_delta2 = delta_ij(4,2,5.25) # delta_ij for antenna 5
A6_delta2 = delta_ij(5,2,5.25) # delta_ij for antenna 6
A7_delta2 = delta_ij(6,2,5.25) # delta_ij for antenna 7
A8_delta2 = delta_ij(7,2,5.25) # delta_ij for antenna 8
A9_delta2 = delta_ij(8,2,5.25) # delta_ij for antenna 9
A10_delta2 = delta_ij(9,2,5.25) # delta_ij for antenna 10
A11_delta2 = delta_ij(10,2,5.25) # delta_ij for antenna 11
A12_delta2 = delta_ij(11,2,5.25) # delta_ij for antenna 12
A13_delta2 = delta_ij(12,2,5.25) # delta_ij for antenna 13
A14_delta2 = delta_ij(13,2,5.25) # delta_ij for antenna 14
A15_delta2 = delta_ij(14,2,5.25) # delta_ij for antenna 15
A16_delta2 = delta_ij(15,2,5.25) # delta_ij for antenna 16
A17_delta2 = delta_ij(16,2,5.25) # delta_ij for antenna 17
A18_delta2 = delta_ij(17,2,5.25) # delta_ij for antenna 18
A19_delta2 = delta_ij(18,2,5.25) # delta_ij for antenna 19
A20_delta2 = delta_ij(19,2,5.25) # delta_ij for antenna 20
A21_delta2 = delta_ij(20,2,5.25) # delta_ij for antenna 21
A22_delta2 = delta_ij(21,2,5.25) # delta_ij for antenna 22
A23_delta2 = delta_ij(22,2,5.25) # delta_ij for antenna 23
A24_delta2 = delta_ij(23,2,5.25) # delta_ij for antenna 24
A25_delta2 = delta_ij(24,2,5.25) # delta_ij for antenna 25

RecA1Ey3 = np.roll(A1_Ey,int(round(A1_delta2)),axis=None)    # shifted e-field at ant1
RecA2Ey3 = np.roll(A2_Ey,int(round(A2_delta2)),axis=None)    # shifted e-field at ant2
RecA3Ey3 = np.roll(A3_Ey,int(round(A3_delta2)),axis=None)    # shifted e-field at ant3
RecA4Ey3 = np.roll(A4_Ey,int(round(A4_delta2)),axis=None)    # shifted e-field at ant4
RecA5Ey3 = np.roll(A5_Ey,int(round(A5_delta2)),axis=None)    # shifted e-field at ant5
RecA6Ey3 = np.roll(A6_Ey,int(round(A6_delta2)),axis=None)    # shifted e-field at ant6
RecA7Ey3 = np.roll(A7_Ey,int(round(A7_delta2)),axis=None)    # shifted e-field at ant7
RecA8Ey3 = np.roll(A8_Ey,int(round(A8_delta2)),axis=None)    # shifted e-field at ant8
RecA9Ey3 = np.roll(A9_Ey,int(round(A9_delta2)),axis=None)    # shifted e-field at ant9
RecA10Ey3 = np.roll(A10_Ey,int(round(A10_delta2)),axis=None)  # shifted e-field at ant10
RecA11Ey3 = np.roll(A11_Ey,int(round(A11_delta2)),axis=None)  # shifted e-field at ant11
RecA12Ey3 = np.roll(A12_Ey,int(round(A12_delta2)),axis=None)  # shifted e-field at ant12
RecA13Ey3 = np.roll(A13_Ey,int(round(A13_delta2)),axis=None)  # shifted e-field at ant13
RecA14Ey3 = np.roll(A14_Ey,int(round(A14_delta2)),axis=None)  # shifted e-field at ant14
RecA15Ey3 = np.roll(A15_Ey,int(round(A15_delta2)),axis=None)  # shifted e-field at ant15
RecA16Ey3 = np.roll(A16_Ey,int(round(A16_delta2)),axis=None)  # shifted e-field at ant16
RecA17Ey3 = np.roll(A17_Ey,int(round(A17_delta2)),axis=None)  # shifted e-field at ant17
RecA18Ey3 = np.roll(A18_Ey,int(round(A18_delta2)),axis=None)  # shifted e-field at ant18
RecA19Ey3 = np.roll(A19_Ey,int(round(A19_delta2)),axis=None) # shifted e-field at ant19
RecA20Ey3 = np.roll(A20_Ey,int(round(A20_delta2)),axis=None) # shifted e-field at ant20
RecA21Ey3 = np.roll(A21_Ey,int(round(A21_delta2)),axis=None) # shifted e-field at ant21
RecA22Ey3 = np.roll(A22_Ey,int(round(A22_delta2)),axis=None) # shifted e-field at ant22
RecA23Ey3 = np.roll(A23_Ey,int(round(A23_delta2)),axis=None) # shifted e-field at ant23
RecA24Ey3 = np.roll(A24_Ey,int(round(A24_delta2)),axis=None) # shifted e-field at ant24
RecA25Ey3 = np.roll(A25_Ey,int(round(A25_delta2)),axis=None) # shifted e-field at ant25


# In[69]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta3 = delta_ij(0,3,5.25) # delta_ij for antenna 1
A2_delta3 = delta_ij(1,3,5.25) # delta_ij for antenna 2
A3_delta3 = delta_ij(2,3,5.25) # delta_ij for antenna 3
A4_delta3 = delta_ij(3,3,5.25) # delta_ij for antenna 4
A5_delta3 = delta_ij(4,3,5.25) # delta_ij for antenna 5
A6_delta3 = delta_ij(5,3,5.25) # delta_ij for antenna 6
A7_delta3 = delta_ij(6,3,5.25) # delta_ij for antenna 7
A8_delta3 = delta_ij(7,3,5.25) # delta_ij for antenna 8
A9_delta3 = delta_ij(8,3,5.25) # delta_ij for antenna 9
A10_delta3 = delta_ij(9,3,5.25) # delta_ij for antenna 10
A11_delta3 = delta_ij(10,3,5.25) # delta_ij for antenna 11
A12_delta3 = delta_ij(11,3,5.25) # delta_ij for antenna 12
A13_delta3 = delta_ij(12,3,5.25) # delta_ij for antenna 13
A14_delta3 = delta_ij(13,3,5.25) # delta_ij for antenna 14
A15_delta3 = delta_ij(14,3,5.25) # delta_ij for antenna 15
A16_delta3 = delta_ij(15,3,5.25) # delta_ij for antenna 16
A17_delta3 = delta_ij(16,3,5.25) # delta_ij for antenna 17
A18_delta3 = delta_ij(17,3,5.25) # delta_ij for antenna 18
A19_delta3 = delta_ij(18,3,5.25) # delta_ij for antenna 19
A20_delta3 = delta_ij(19,3,5.25) # delta_ij for antenna 20
A21_delta3 = delta_ij(20,3,5.25) # delta_ij for antenna 21
A22_delta3 = delta_ij(21,3,5.25) # delta_ij for antenna 22
A23_delta3 = delta_ij(22,3,5.25) # delta_ij for antenna 23
A24_delta3 = delta_ij(23,3,5.25) # delta_ij for antenna 24
A25_delta3 = delta_ij(24,3,5.25) # delta_ij for antenna 25

RecA1Ey4 = np.roll(A1_Ey,int(round(A1_delta3)),axis=None)    # shifted e-field at ant1
RecA2Ey4 = np.roll(A2_Ey,int(round(A2_delta3)),axis=None)    # shifted e-field at ant2
RecA3Ey4 = np.roll(A3_Ey,int(round(A3_delta3)),axis=None)    # shifted e-field at ant3
RecA4Ey4 = np.roll(A4_Ey,int(round(A4_delta3)),axis=None)    # shifted e-field at ant4
RecA5Ey4 = np.roll(A5_Ey,int(round(A5_delta3)),axis=None)    # shifted e-field at ant5
RecA6Ey4 = np.roll(A6_Ey,int(round(A6_delta3)),axis=None)    # shifted e-field at ant6
RecA7Ey4 = np.roll(A7_Ey,int(round(A7_delta3)),axis=None)    # shifted e-field at ant7
RecA8Ey4 = np.roll(A8_Ey,int(round(A8_delta3)),axis=None)    # shifted e-field at ant8
RecA9Ey4 = np.roll(A9_Ey,int(round(A9_delta3)),axis=None)    # shifted e-field at ant9
RecA10Ey4 = np.roll(A10_Ey,int(round(A10_delta3)),axis=None)  # shifted e-field at ant10
RecA11Ey4 = np.roll(A11_Ey,int(round(A11_delta3)),axis=None)  # shifted e-field at ant11
RecA12Ey4 = np.roll(A12_Ey,int(round(A12_delta3)),axis=None)  # shifted e-field at ant12
RecA13Ey4 = np.roll(A13_Ey,int(round(A13_delta3)),axis=None)  # shifted e-field at ant13
RecA14Ey4 = np.roll(A14_Ey,int(round(A14_delta3)),axis=None)  # shifted e-field at ant14
RecA15Ey4 = np.roll(A15_Ey,int(round(A15_delta3)),axis=None)  # shifted e-field at ant15
RecA16Ey4 = np.roll(A16_Ey,int(round(A16_delta3)),axis=None)  # shifted e-field at ant16
RecA17Ey4 = np.roll(A17_Ey,int(round(A17_delta3)),axis=None)  # shifted e-field at ant17
RecA18Ey4 = np.roll(A18_Ey,int(round(A18_delta3)),axis=None)  # shifted e-field at ant18
RecA19Ey4 = np.roll(A19_Ey,int(round(A19_delta3)),axis=None) # shifted e-field at ant19
RecA20Ey4 = np.roll(A20_Ey,int(round(A20_delta3)),axis=None) # shifted e-field at ant20
RecA21Ey4 = np.roll(A21_Ey,int(round(A21_delta3)),axis=None) # shifted e-field at ant21
RecA22Ey4 = np.roll(A22_Ey,int(round(A22_delta3)),axis=None) # shifted e-field at ant22
RecA23Ey4 = np.roll(A23_Ey,int(round(A23_delta3)),axis=None) # shifted e-field at ant23
RecA24Ey4 = np.roll(A24_Ey,int(round(A24_delta3)),axis=None) # shifted e-field at ant24
RecA25Ey4 = np.roll(A25_Ey,int(round(A25_delta3)),axis=None) # shifted e-field at ant25


# In[101]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta4 = delta_ij(0,4,5.25) # delta_ij for antenna 1
A2_delta4 = delta_ij(1,4,5.25) # delta_ij for antenna 2
A3_delta4 = delta_ij(2,4,5.25) # delta_ij for antenna 3
A4_delta4 = delta_ij(3,4,5.25) # delta_ij for antenna 4
A5_delta4 = delta_ij(4,4,5.25) # delta_ij for antenna 5
A6_delta4 = delta_ij(5,4,5.25) # delta_ij for antenna 6
A7_delta4 = delta_ij(6,4,5.25) # delta_ij for antenna 7
A8_delta4 = delta_ij(7,4,5.25) # delta_ij for antenna 8
A9_delta4 = delta_ij(8,4,5.25) # delta_ij for antenna 9
A10_delta4 = delta_ij(9,4,5.25) # delta_ij for antenna 10
A11_delta4 = delta_ij(10,4,5.25) # delta_ij for antenna 11
A12_delta4 = delta_ij(11,4,5.25) # delta_ij for antenna 12
A13_delta4 = delta_ij(12,4,5.25) # delta_ij for antenna 13
A14_delta4 = delta_ij(13,4,5.25) # delta_ij for antenna 14
A15_delta4 = delta_ij(14,4,5.25) # delta_ij for antenna 15
A16_delta4 = delta_ij(15,4,5.25) # delta_ij for antenna 16
A17_delta4 = delta_ij(16,4,5.25) # delta_ij for antenna 17
A18_delta4 = delta_ij(17,4,5.25) # delta_ij for antenna 18
A19_delta4 = delta_ij(18,4,5.25) # delta_ij for antenna 19
A20_delta4 = delta_ij(19,4,5.25) # delta_ij for antenna 20
A21_delta4 = delta_ij(20,4,5.25) # delta_ij for antenna 21
A22_delta4 = delta_ij(21,4,5.25) # delta_ij for antenna 22
A23_delta4 = delta_ij(22,4,5.25) # delta_ij for antenna 23
A24_delta4 = delta_ij(23,4,5.25) # delta_ij for antenna 24
A25_delta4 = delta_ij(24,4,5.25) # delta_ij for antenna 25

RecA1Ey5 = np.roll(A1_Ey,int(round(A1_delta4)),axis=None)    # shifted e-field at ant1
RecA2Ey5 = np.roll(A2_Ey,int(round(A2_delta4)),axis=None)    # shifted e-field at ant2
RecA3Ey5 = np.roll(A3_Ey,int(round(A3_delta4)),axis=None)    # shifted e-field at ant3
RecA4Ey5 = np.roll(A4_Ey,int(round(A4_delta4)),axis=None)    # shifted e-field at ant4
RecA5Ey5 = np.roll(A5_Ey,int(round(A5_delta4)),axis=None)    # shifted e-field at ant5
RecA6Ey5 = np.roll(A6_Ey,int(round(A6_delta4)),axis=None)    # shifted e-field at ant6
RecA7Ey5 = np.roll(A7_Ey,int(round(A7_delta4)),axis=None)    # shifted e-field at ant7
RecA8Ey5 = np.roll(A8_Ey,int(round(A8_delta4)),axis=None)    # shifted e-field at ant8
RecA9Ey5 = np.roll(A9_Ey,int(round(A9_delta4)), axis=None)    # shifted e-field at ant9
RecA10Ey5 = np.roll(A10_Ey,int(round(A10_delta4)),axis=None)  # shifted e-field at ant11
RecA11Ey5 = np.roll(A11_Ey,int(round(A11_delta4)),axis=None)  # shifted e-field at ant11
RecA12Ey5 = np.roll(A12_Ey,int(round(A12_delta4)),axis=None)  # shifted e-field at ant12
RecA13Ey5 = np.roll(A13_Ey,int(round(A13_delta4)),axis=None)  # shifted e-field at ant13
RecA14Ey5 = np.roll(A14_Ey,int(round(A14_delta4)),axis=None)  # shifted e-field at ant14
RecA15Ey5 = np.roll(A15_Ey,int(round(A15_delta4)),axis=None)  # shifted e-field at ant15
RecA16Ey5 = np.roll(A16_Ey,int(round(A16_delta4)),axis=None)  # shifted e-field at ant16
RecA17Ey5 = np.roll(A17_Ey,int(round(A17_delta4)),axis=None)  # shifted e-field at ant17
RecA18Ey5 = np.roll(A18_Ey,int(round(A18_delta4)),axis=None)  # shifted e-field at ant18
RecA19Ey5 = np.roll(A19_Ey,int(round(A19_delta4)),axis=None) # shifted e-field at ant19
RecA20Ey5 = np.roll(A20_Ey,int(round(A20_delta4)),axis=None) # shifted e-field at ant20
RecA21Ey5 = np.roll(A21_Ey,int(round(A21_delta4)),axis=None) # shifted e-field at ant21
RecA22Ey5 = np.roll(A22_Ey,int(round(A22_delta4)),axis=None) # shifted e-field at ant22
RecA23Ey5 = np.roll(A23_Ey,int(round(A23_delta4)),axis=None) # shifted e-field at ant23
RecA24Ey5 = np.roll(A24_Ey,int(round(A24_delta4)),axis=None) # shifted e-field at ant24
RecA25Ey5 = np.roll(A25_Ey,int(round(A25_delta4)),axis=None) # shifted e-field at ant25


# In[102]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta5 = delta_ij(0,5,5.25) # delta_ij for antenna 1
A2_delta5 = delta_ij(1,5,5.25) # delta_ij for antenna 2
A3_delta5 = delta_ij(2,5,5.25) # delta_ij for antenna 3
A4_delta5 = delta_ij(3,5,5.25) # delta_ij for antenna 4
A5_delta5 = delta_ij(4,5,5.25) # delta_ij for antenna 5
A6_delta5 = delta_ij(5,5,5.25) # delta_ij for antenna 6
A7_delta5 = delta_ij(6,5,5.25) # delta_ij for antenna 7
A8_delta5 = delta_ij(7,5,5.25) # delta_ij for antenna 8
A9_delta5 = delta_ij(8,5,5.25) # delta_ij for antenna 9
A10_delta5 = delta_ij(9,5,5.25) # delta_ij for antenna 10
A11_delta5 = delta_ij(10,5,5.25) # delta_ij for antenna 11
A12_delta5 = delta_ij(11,5,5.25) # delta_ij for antenna 12
A13_delta5 = delta_ij(12,5,5.25) # delta_ij for antenna 13
A14_delta5 = delta_ij(13,5,5.25) # delta_ij for antenna 14
A15_delta5 = delta_ij(14,5,5.25) # delta_ij for antenna 15
A16_delta5 = delta_ij(15,5,5.25) # delta_ij for antenna 16
A17_delta5 = delta_ij(16,5,5.25) # delta_ij for antenna 17
A18_delta5 = delta_ij(17,5,5.25) # delta_ij for antenna 18
A19_delta5 = delta_ij(18,5,5.25) # delta_ij for antenna 19
A20_delta5 = delta_ij(19,5,5.25) # delta_ij for antenna 20
A21_delta5 = delta_ij(20,5,5.25) # delta_ij for antenna 21
A22_delta5 = delta_ij(21,5,5.25) # delta_ij for antenna 22
A23_delta5 = delta_ij(22,5,5.25) # delta_ij for antenna 23
A24_delta5 = delta_ij(23,5,5.25) # delta_ij for antenna 24
A25_delta5 = delta_ij(24,5,5.25) # delta_ij for antenna 25

RecA1Ey6 = np.roll(A1_Ey,int(round(A1_delta5)),axis=None)    # shifted e-field at ant1
RecA2Ey6 = np.roll(A2_Ey,int(round(A2_delta5)),axis=None)    # shifted e-field at ant2
RecA3Ey6 = np.roll(A3_Ey,int(round(A3_delta5)),axis=None)    # shifted e-field at ant3
RecA4Ey6 = np.roll(A4_Ey,int(round(A4_delta5)),axis=None)    # shifted e-field at ant4
RecA5Ey6 = np.roll(A5_Ey,int(round(A5_delta5)),axis=None)    # shifted e-field at ant5
RecA6Ey6 = np.roll(A6_Ey,int(round(A6_delta5)),axis=None)    # shifted e-field at ant6
RecA7Ey6 = np.roll(A7_Ey,int(round(A7_delta5)),axis=None)    # shifted e-field at ant7
RecA8Ey6 = np.roll(A8_Ey,int(round(A8_delta5)),axis=None)    # shifted e-field at ant8
RecA9Ey6 = np.roll(A9_Ey,int(round(A9_delta5)),axis=None)    # shifted e-field at ant9
RecA10Ey6 = np.roll(A10_Ey,int(round(A10_delta5)),axis=None)  # shifted e-field at ant10
RecA11Ey6 = np.roll(A11_Ey,int(round(A11_delta5)),axis=None)  # shifted e-field at ant11
RecA12Ey6 = np.roll(A12_Ey,int(round(A12_delta5)),axis=None)  # shifted e-field at ant12
RecA13Ey6 = np.roll(A13_Ey,int(round(A13_delta5)),axis=None)  # shifted e-field at ant13
RecA14Ey6 = np.roll(A14_Ey,int(round(A14_delta5)),axis=None)  # shifted e-field at ant14
RecA15Ey6 = np.roll(A15_Ey,int(round(A15_delta5)),axis=None)  # shifted e-field at ant15
RecA16Ey6 = np.roll(A16_Ey,int(round(A16_delta5)),axis=None)  # shifted e-field at ant16
RecA17Ey6 = np.roll(A17_Ey,int(round(A17_delta5)),axis=None)  # shifted e-field at ant17
RecA18Ey6 = np.roll(A18_Ey,int(round(A18_delta5)),axis=None)  # shifted e-field at ant18
RecA19Ey6 = np.roll(A19_Ey,int(round(A19_delta5)),axis=None) # shifted e-field at ant19
RecA20Ey6 = np.roll(A20_Ey,int(round(A20_delta5)),axis=None) # shifted e-field at ant20
RecA21Ey6 = np.roll(A21_Ey,int(round(A21_delta5)),axis=None) # shifted e-field at ant21
RecA22Ey6 = np.roll(A22_Ey,int(round(A22_delta5)),axis=None) # shifted e-field at ant22
RecA23Ey6 = np.roll(A23_Ey,int(round(A23_delta5)),axis=None) # shifted e-field at ant23
RecA24Ey6 = np.roll(A24_Ey,int(round(A24_delta5)),axis=None) # shifted e-field at ant24
RecA25Ey6 = np.roll(A25_Ey,int(round(A25_delta5)),axis=None) # shifted e-field at ant25


# In[103]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta6 = delta_ij(0,6,5.25) # delta_ij for antenna 1
A2_delta6 = delta_ij(1,6,5.25) # delta_ij for antenna 2
A3_delta6 = delta_ij(2,6,5.25) # delta_ij for antenna 3
A4_delta6 = delta_ij(3,6,5.25) # delta_ij for antenna 4
A5_delta6 = delta_ij(4,6,5.25) # delta_ij for antenna 5
A6_delta6 = delta_ij(5,6,5.25) # delta_ij for antenna 6
A7_delta6 = delta_ij(6,6,5.25) # delta_ij for antenna 7
A8_delta6 = delta_ij(7,6,5.25) # delta_ij for antenna 8
A9_delta6 = delta_ij(8,6,5.25) # delta_ij for antenna 9
A10_delta6 = delta_ij(9,6,5.25) # delta_ij for antenna 10
A11_delta6 = delta_ij(10,6,5.25) # delta_ij for antenna 11
A12_delta6 = delta_ij(11,6,5.25) # delta_ij for antenna 12
A13_delta6 = delta_ij(12,6,5.25) # delta_ij for antenna 13
A14_delta6 = delta_ij(13,6,5.25) # delta_ij for antenna 14
A15_delta6 = delta_ij(14,6,5.25) # delta_ij for antenna 15
A16_delta6 = delta_ij(15,6,5.25) # delta_ij for antenna 16
A17_delta6 = delta_ij(16,6,5.25) # delta_ij for antenna 17
A18_delta6 = delta_ij(17,6,5.25) # delta_ij for antenna 18
A19_delta6 = delta_ij(18,6,5.25) # delta_ij for antenna 19
A20_delta6 = delta_ij(19,6,5.25) # delta_ij for antenna 20
A21_delta6 = delta_ij(20,6,5.25) # delta_ij for antenna 21
A22_delta6 = delta_ij(21,6,5.25) # delta_ij for antenna 22
A23_delta6 = delta_ij(22,6,5.25) # delta_ij for antenna 23
A24_delta6 = delta_ij(23,6,5.25) # delta_ij for antenna 24
A25_delta6 = delta_ij(24,6,5.25) # delta_ij for antenna 25

RecA1Ey7 = np.roll(A1_Ey,int(round(A1_delta6)),axis=None)    # shifted e-field at ant1
RecA2Ey7 = np.roll(A2_Ey,int(round(A2_delta6)),axis=None)    # shifted e-field at ant2
RecA3Ey7 = np.roll(A3_Ey,int(round(A3_delta6)),axis=None)    # shifted e-field at ant3
RecA4Ey7 = np.roll(A4_Ey,int(round(A4_delta6)),axis=None)    # shifted e-field at ant4
RecA5Ey7 = np.roll(A5_Ey,int(round(A5_delta6)),axis=None)    # shifted e-field at ant5
RecA6Ey7 = np.roll(A6_Ey,int(round(A6_delta6)),axis=None)    # shifted e-field at ant6
RecA7Ey7 = np.roll(A7_Ey,int(round(A7_delta6)),axis=None)    # shifted e-field at ant7
RecA8Ey7 = np.roll(A8_Ey,int(round(A8_delta6)),axis=None)    # shifted e-field at ant8
RecA9Ey7 = np.roll(A9_Ey,int(round(A9_delta6)),axis=None)    # shifted e-field at ant9
RecA10Ey7 = np.roll(A10_Ey,int(round(A10_delta6)),axis=None)  # shifted e-field at ant10
RecA11Ey7 = np.roll(A11_Ey,int(round(A11_delta6)),axis=None)  # shifted e-field at ant11
RecA12Ey7 = np.roll(A12_Ey,int(round(A12_delta6)),axis=None)  # shifted e-field at ant12
RecA13Ey7 = np.roll(A13_Ey,int(round(A13_delta6)),axis=None)  # shifted e-field at ant13
RecA14Ey7 = np.roll(A14_Ey,int(round(A14_delta6)),axis=None)  # shifted e-field at ant14
RecA15Ey7 = np.roll(A15_Ey,int(round(A15_delta6)),axis=None)  # shifted e-field at ant15
RecA16Ey7 = np.roll(A16_Ey,int(round(A16_delta6)),axis=None)  # shifted e-field at ant16
RecA17Ey7 = np.roll(A17_Ey,int(round(A17_delta6)),axis=None)  # shifted e-field at ant17
RecA18Ey7 = np.roll(A18_Ey,int(round(A18_delta6)),axis=None)  # shifted e-field at ant18
RecA19Ey7 = np.roll(A19_Ey,int(round(A19_delta6)),axis=None) # shifted e-field at ant19
RecA20Ey7 = np.roll(A20_Ey,int(round(A20_delta6)),axis=None) # shifted e-field at ant20
RecA21Ey7 = np.roll(A21_Ey,int(round(A21_delta6)),axis=None) # shifted e-field at ant21
RecA22Ey7 = np.roll(A22_Ey,int(round(A22_delta6)),axis=None) # shifted e-field at ant22
RecA23Ey7 = np.roll(A23_Ey,int(round(A23_delta6)),axis=None) # shifted e-field at ant23
RecA24Ey7 = np.roll(A24_Ey,int(round(A24_delta6)),axis=None) # shifted e-field at ant24
RecA25Ey7 = np.roll(A25_Ey,int(round(A25_delta6)),axis=None) # shifted e-field at ant25


# In[104]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta7 = delta_ij(0,7,5.25) # delta_ij for antenna 1
A2_delta7 = delta_ij(1,7,5.25) # delta_ij for antenna 2
A3_delta7 = delta_ij(2,7,5.25) # delta_ij for antenna 3
A4_delta7 = delta_ij(3,7,5.25) # delta_ij for antenna 4
A5_delta7 = delta_ij(4,7,5.25) # delta_ij for antenna 5
A6_delta7 = delta_ij(5,7,5.25) # delta_ij for antenna 6
A7_delta7 = delta_ij(6,7,5.25) # delta_ij for antenna 7
A8_delta7 = delta_ij(7,7,5.25) # delta_ij for antenna 8
A9_delta7 = delta_ij(8,7,5.25) # delta_ij for antenna 9
A10_delta7 = delta_ij(9,7,5.25) # delta_ij for antenna 10
A11_delta7 = delta_ij(10,7,5.25) # delta_ij for antenna 11
A12_delta7 = delta_ij(11,7,5.25) # delta_ij for antenna 12
A13_delta7 = delta_ij(12,7,5.25) # delta_ij for antenna 13
A14_delta7 = delta_ij(13,7,5.25) # delta_ij for antenna 14
A15_delta7 = delta_ij(14,7,5.25) # delta_ij for antenna 15
A16_delta7 = delta_ij(15,7,5.25) # delta_ij for antenna 16
A17_delta7 = delta_ij(16,7,5.25) # delta_ij for antenna 17
A18_delta7 = delta_ij(17,7,5.25) # delta_ij for antenna 18
A19_delta7 = delta_ij(18,7,5.25) # delta_ij for antenna 19
A20_delta7 = delta_ij(19,7,5.25) # delta_ij for antenna 20
A21_delta7 = delta_ij(20,7,5.25) # delta_ij for antenna 21
A22_delta7 = delta_ij(21,7,5.25) # delta_ij for antenna 22
A23_delta7 = delta_ij(22,7,5.25) # delta_ij for antenna 23
A24_delta7 = delta_ij(23,7,5.25) # delta_ij for antenna 24
A25_delta7 = delta_ij(24,7,5.25) # delta_ij for antenna 25

RecA1Ey8 = np.roll(A1_Ey,int(round(A1_delta7)),axis=None)    # shifted e-field at ant1
RecA2Ey8 = np.roll(A2_Ey,int(round(A2_delta7)),axis=None)    # shifted e-field at ant2
RecA3Ey8 = np.roll(A3_Ey,int(round(A3_delta7)),axis=None)    # shifted e-field at ant3
RecA4Ey8 = np.roll(A4_Ey,int(round(A4_delta7)),axis=None)    # shifted e-field at ant4
RecA5Ey8 = np.roll(A5_Ey,int(round(A5_delta7)),axis=None)    # shifted e-field at ant5
RecA6Ey8 = np.roll(A6_Ey,int(round(A6_delta7)),axis=None)    # shifted e-field at ant6
RecA7Ey8 = np.roll(A7_Ey,int(round(A7_delta7)),axis=None)    # shifted e-field at ant7
RecA8Ey8 = np.roll(A8_Ey,int(round(A8_delta7)),axis=None)    # shifted e-field at ant8
RecA9Ey8 = np.roll(A9_Ey,int(round(A9_delta7)),axis=None)    # shifted e-field at ant9
RecA10Ey8 = np.roll(A10_Ey,int(round(A10_delta7)),axis=None)  # shifted e-field at ant10
RecA11Ey8 = np.roll(A11_Ey,int(round(A11_delta7)),axis=None)  # shifted e-field at ant11
RecA12Ey8 = np.roll(A12_Ey,int(round(A12_delta7)),axis=None)  # shifted e-field at ant12
RecA13Ey8 = np.roll(A13_Ey,int(round(A13_delta7)),axis=None)  # shifted e-field at ant13
RecA14Ey8 = np.roll(A14_Ey,int(round(A14_delta7)),axis=None)  # shifted e-field at ant14
RecA15Ey8 = np.roll(A15_Ey,int(round(A15_delta7)),axis=None)  # shifted e-field at ant15
RecA16Ey8 = np.roll(A16_Ey,int(round(A16_delta7)),axis=None)  # shifted e-field at ant16
RecA17Ey8 = np.roll(A17_Ey,int(round(A17_delta7)),axis=None)  # shifted e-field at ant17
RecA18Ey8 = np.roll(A18_Ey,int(round(A18_delta7)),axis=None)  # shifted e-field at ant18
RecA19Ey8 = np.roll(A19_Ey,int(round(A19_delta7)),axis=None) # shifted e-field at ant19
RecA20Ey8 = np.roll(A20_Ey,int(round(A20_delta7)),axis=None) # shifted e-field at ant20
RecA21Ey8 = np.roll(A21_Ey,int(round(A21_delta7)),axis=None) # shifted e-field at ant21
RecA22Ey8 = np.roll(A22_Ey,int(round(A22_delta7)),axis=None) # shifted e-field at ant22
RecA23Ey8 = np.roll(A23_Ey,int(round(A23_delta7)),axis=None) # shifted e-field at ant23
RecA24Ey8 = np.roll(A24_Ey,int(round(A24_delta7)),axis=None) # shifted e-field at ant24
RecA25Ey8 = np.roll(A25_Ey,int(round(A25_delta7)),axis=None) # shifted e-field at ant25


# In[105]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta8 = delta_ij(0,8,5.25) # delta_ij for antenna 1
A2_delta8 = delta_ij(1,8,5.25) # delta_ij for antenna 2
A3_delta8 = delta_ij(2,8,5.25) # delta_ij for antenna 3
A4_delta8 = delta_ij(3,8,5.25) # delta_ij for antenna 4
A5_delta8 = delta_ij(4,8,5.25) # delta_ij for antenna 5
A6_delta8 = delta_ij(5,8,5.25) # delta_ij for antenna 6
A7_delta8 = delta_ij(6,8,5.25) # delta_ij for antenna 7
A8_delta8 = delta_ij(7,8,5.25) # delta_ij for antenna 8
A9_delta8 = delta_ij(8,8,5.25) # delta_ij for antenna 9
A10_delta8 = delta_ij(9,8,5.25) # delta_ij for antenna 10
A11_delta8 = delta_ij(10,8,5.25) # delta_ij for antenna 11
A12_delta8 = delta_ij(11,8,5.25) # delta_ij for antenna 12
A13_delta8 = delta_ij(12,8,5.25) # delta_ij for antenna 13
A14_delta8 = delta_ij(13,8,5.25) # delta_ij for antenna 14
A15_delta8 = delta_ij(14,8,5.25) # delta_ij for antenna 15
A16_delta8 = delta_ij(15,8,5.25) # delta_ij for antenna 16
A17_delta8 = delta_ij(16,8,5.25) # delta_ij for antenna 17
A18_delta8 = delta_ij(17,8,5.25) # delta_ij for antenna 18
A19_delta8 = delta_ij(18,8,5.25) # delta_ij for antenna 19
A20_delta8 = delta_ij(19,8,5.25) # delta_ij for antenna 20
A21_delta8 = delta_ij(20,8,5.25) # delta_ij for antenna 21
A22_delta8 = delta_ij(21,8,5.25) # delta_ij for antenna 22
A23_delta8 = delta_ij(22,8,5.25) # delta_ij for antenna 23
A24_delta8 = delta_ij(23,8,5.25) # delta_ij for antenna 24
A25_delta8 = delta_ij(24,8,5.25) # delta_ij for antenna 25

RecA1Ey9 = np.roll(A1_Ey,int(round(A1_delta8)),axis=None)    # shifted e-field at ant1
RecA2Ey9 = np.roll(A2_Ey,int(round(A2_delta8)),axis=None)    # shifted e-field at ant2
RecA3Ey9 = np.roll(A3_Ey,int(round(A3_delta8)),axis=None)    # shifted e-field at ant3
RecA4Ey9 = np.roll(A4_Ey,int(round(A4_delta8)),axis=None)    # shifted e-field at ant4
RecA5Ey9 = np.roll(A5_Ey,int(round(A5_delta8)),axis=None)    # shifted e-field at ant5
RecA6Ey9 = np.roll(A6_Ey,int(round(A6_delta8)),axis=None)    # shifted e-field at ant6
RecA7Ey9 = np.roll(A7_Ey,int(round(A7_delta8)),axis=None)    # shifted e-field at ant7
RecA8Ey9 = np.roll(A8_Ey,int(round(A8_delta8)),axis=None)    # shifted e-field at ant8
RecA9Ey9 = np.roll(A9_Ey,int(round(A9_delta8)),axis=None)    # shifted e-field at ant9
RecA10Ey9 = np.roll(A10_Ey,int(round(A10_delta8)),axis=None)  # shifted e-field at ant10
RecA11Ey9 = np.roll(A11_Ey,int(round(A11_delta8)),axis=None)  # shifted e-field at ant11
RecA12Ey9 = np.roll(A12_Ey,int(round(A12_delta8)),axis=None)  # shifted e-field at ant12
RecA13Ey9 = np.roll(A13_Ey,int(round(A13_delta8)),axis=None)  # shifted e-field at ant13
RecA14Ey9 = np.roll(A14_Ey,int(round(A14_delta8)),axis=None)  # shifted e-field at ant14
RecA15Ey9 = np.roll(A15_Ey,int(round(A15_delta8)),axis=None)  # shifted e-field at ant15
RecA16Ey9 = np.roll(A16_Ey,int(round(A16_delta8)),axis=None)  # shifted e-field at ant16
RecA17Ey9 = np.roll(A17_Ey,int(round(A17_delta8)),axis=None)  # shifted e-field at ant17
RecA18Ey9 = np.roll(A18_Ey,int(round(A18_delta8)),axis=None)  # shifted e-field at ant18
RecA19Ey9 = np.roll(A19_Ey,int(round(A19_delta8)),axis=None) # shifted e-field at ant19
RecA20Ey9 = np.roll(A20_Ey,int(round(A20_delta8)),axis=None) # shifted e-field at ant20
RecA21Ey9 = np.roll(A21_Ey,int(round(A21_delta8)),axis=None) # shifted e-field at ant21
RecA22Ey9 = np.roll(A22_Ey,int(round(A22_delta8)),axis=None) # shifted e-field at ant22
RecA23Ey9 = np.roll(A23_Ey,int(round(A23_delta8)),axis=None) # shifted e-field at ant23
RecA24Ey9 = np.roll(A24_Ey,int(round(A24_delta8)),axis=None) # shifted e-field at ant24
RecA25Ey9 = np.roll(A25_Ey,int(round(A25_delta8)),axis=None) # shifted e-field at ant25


# In[106]:


# With respect to position (0m,-50m) in the xy plane.
A1_delta9 = delta_ij(0,9,5.25) # delta_ij for antenna 1
A2_delta9 = delta_ij(1,9,5.25) # delta_ij for antenna 2
A3_delta9 = delta_ij(2,9,5.25) # delta_ij for antenna 3
A4_delta9 = delta_ij(3,9,5.25) # delta_ij for antenna 4
A5_delta9 = delta_ij(4,9,5.25) # delta_ij for antenna 5
A6_delta9 = delta_ij(5,9,5.25) # delta_ij for antenna 6
A7_delta9 = delta_ij(6,9,5.25) # delta_ij for antenna 7
A8_delta9 = delta_ij(7,9,5.25) # delta_ij for antenna 8
A9_delta9 = delta_ij(8,9,5.25) # delta_ij for antenna 9
A10_delta9 = delta_ij(9,9,5.25) # delta_ij for antenna 10
A11_delta9 = delta_ij(10,9,5.25) # delta_ij for antenna 11
A12_delta9 = delta_ij(11,9,5.25) # delta_ij for antenna 12
A13_delta9 = delta_ij(12,9,5.25) # delta_ij for antenna 13
A14_delta9 = delta_ij(13,9,5.25) # delta_ij for antenna 14
A15_delta9 = delta_ij(14,9,5.25) # delta_ij for antenna 15
A16_delta9 = delta_ij(15,9,5.25) # delta_ij for antenna 16
A17_delta9 = delta_ij(16,9,5.25) # delta_ij for antenna 17
A18_delta9 = delta_ij(17,9,5.25) # delta_ij for antenna 18
A19_delta9 = delta_ij(18,9,5.25) # delta_ij for antenna 19
A20_delta9 = delta_ij(19,9,5.25) # delta_ij for antenna 20
A21_delta9 = delta_ij(20,9,5.25) # delta_ij for antenna 21
A22_delta9 = delta_ij(21,9,5.25) # delta_ij for antenna 22
A23_delta9 = delta_ij(22,9,5.25) # delta_ij for antenna 23
A24_delta9 = delta_ij(23,9,5.25) # delta_ij for antenna 24
A25_delta9 = delta_ij(24,9,5.25) # delta_ij for antenna 25

RecA1Ey10 = np.roll(A1_Ey,int(round(A1_delta9)),axis=None)    # shifted e-field at ant1
RecA2Ey10 = np.roll(A2_Ey,int(round(A2_delta9)),axis=None)    # shifted e-field at ant2
RecA3Ey10 = np.roll(A3_Ey,int(round(A3_delta9)),axis=None)    # shifted e-field at ant3
RecA4Ey10 = np.roll(A4_Ey,int(round(A4_delta9)),axis=None)    # shifted e-field at ant4
RecA5Ey10 = np.roll(A5_Ey,int(round(A5_delta9)),axis=None)    # shifted e-field at ant5
RecA6Ey10 = np.roll(A6_Ey,int(round(A6_delta9)),axis=None)    # shifted e-field at ant6
RecA7Ey10 = np.roll(A7_Ey,int(round(A7_delta9)),axis=None)    # shifted e-field at ant7
RecA8Ey10 = np.roll(A8_Ey,int(round(A8_delta9)),axis=None)    # shifted e-field at ant8
RecA9Ey10 = np.roll(A9_Ey,int(round(A9_delta9)),axis=None)    # shifted e-field at ant9
RecA10Ey10 = np.roll(A10_Ey,int(round(A10_delta9)),axis=None)  # shifted e-field at ant10
RecA11Ey10 = np.roll(A11_Ey,int(round(A11_delta9)),axis=None)  # shifted e-field at ant11
RecA12Ey10 = np.roll(A12_Ey,int(round(A12_delta9)),axis=None)  # shifted e-field at ant12
RecA13Ey10 = np.roll(A13_Ey,int(round(A13_delta9)),axis=None)  # shifted e-field at ant13
RecA14Ey10 = np.roll(A14_Ey,int(round(A14_delta9)),axis=None)  # shifted e-field at ant14
RecA15Ey10 = np.roll(A15_Ey,int(round(A15_delta9)),axis=None)  # shifted e-field at ant15
RecA16Ey10 = np.roll(A16_Ey,int(round(A16_delta9)),axis=None)  # shifted e-field at ant16
RecA17Ey10 = np.roll(A17_Ey,int(round(A17_delta9)),axis=None)  # shifted e-field at ant17
RecA18Ey10 = np.roll(A18_Ey,int(round(A18_delta9)),axis=None)  # shifted e-field at ant18
RecA19Ey10 = np.roll(A19_Ey,int(round(A19_delta9)),axis=None) # shifted e-field at ant19
RecA20Ey10 = np.roll(A20_Ey,int(round(A20_delta9)),axis=None) # shifted e-field at ant20
RecA21Ey10 = np.roll(A21_Ey,int(round(A21_delta9)),axis=None) # shifted e-field at ant21
RecA22Ey10 = np.roll(A22_Ey,int(round(A22_delta9)),axis=None) # shifted e-field at ant22
RecA23Ey10 = np.roll(A23_Ey,int(round(A23_delta9)),axis=None) # shifted e-field at ant23
RecA24Ey10 = np.roll(A24_Ey,int(round(A24_delta9)),axis=None) # shifted e-field at ant24
RecA25Ey10 = np.roll(A25_Ey,int(round(A25_delta9)),axis=None) # shifted e-field at ant25


# In[107]:


# With respect to position (100m,0m) in the xy plane.
A1_delta10 = delta_ij(0,10,5.25) # delta_ij for antenna 1
A2_delta10 = delta_ij(1,10,5.25) # delta_ij for antenna 2
A3_delta10 = delta_ij(2,10,5.25) # delta_ij for antenna 3
A4_delta10 = delta_ij(3,10,5.25) # delta_ij for antenna 4
A5_delta10 = delta_ij(4,10,5.25) # delta_ij for antenna 5
A6_delta10 = delta_ij(5,10,5.25) # delta_ij for antenna 6
A7_delta10 = delta_ij(6,10,5.25) # delta_ij for antenna 7
A8_delta10 = delta_ij(7,10,5.25) # delta_ij for antenna 8
A9_delta10 = delta_ij(8,10,5.25) # delta_ij for antenna 9
A10_delta10 = delta_ij(9,10,5.25) # delta_ij for antenna 10
A11_delta10 = delta_ij(10,10,5.25) # delta_ij for antenna 11
A12_delta10 = delta_ij(11,10,5.25) # delta_ij for antenna 12
A13_delta10 = delta_ij(12,10,5.25) # delta_ij for antenna 13
A14_delta10 = delta_ij(13,10,5.25) # delta_ij for antenna 14
A15_delta10 = delta_ij(14,10,5.25) # delta_ij for antenna 15
A16_delta10 = delta_ij(15,10,5.25) # delta_ij for antenna 16
A17_delta10 = delta_ij(16,10,5.25) # delta_ij for antenna 17
A18_delta10 = delta_ij(17,10,5.25) # delta_ij for antenna 18
A19_delta10 = delta_ij(18,10,5.25) # delta_ij for antenna 19
A20_delta10 = delta_ij(19,10,5.25) # delta_ij for antenna 20
A21_delta10 = delta_ij(20,10,5.25) # delta_ij for antenna 21
A22_delta10 = delta_ij(21,10,5.25) # delta_ij for antenna 22
A23_delta10 = delta_ij(22,10,5.25) # delta_ij for antenna 23
A24_delta10 = delta_ij(23,10,5.25) # delta_ij for antenna 24
A25_delta10 = delta_ij(24,10,5.25) # delta_ij for antenna 25

RecA1Ey11 = np.roll(A1_Ey,int(round(A1_delta10)),axis=None)    # shifted e-field at ant1
RecA2Ey11 = np.roll(A2_Ey,int(round(A2_delta10)),axis=None)    # shifted e-field at ant2
RecA3Ey11 = np.roll(A3_Ey,int(round(A3_delta10)),axis=None)    # shifted e-field at ant3
RecA4Ey11 = np.roll(A4_Ey,int(round(A4_delta10)),axis=None)    # shifted e-field at ant4
RecA5Ey11 = np.roll(A5_Ey,int(round(A5_delta10)),axis=None)    # shifted e-field at ant5
RecA6Ey11 = np.roll(A6_Ey,int(round(A6_delta10)),axis=None)    # shifted e-field at ant6
RecA7Ey11 = np.roll(A7_Ey,int(round(A7_delta10)),axis=None)    # shifted e-field at ant7
RecA8Ey11 = np.roll(A8_Ey,int(round(A8_delta10)),axis=None)    # shifted e-field at ant8
RecA9Ey11 = np.roll(A9_Ey,int(round(A9_delta10)),axis=None)    # shifted e-field at ant9
RecA10Ey11 = np.roll(A10_Ey,int(round(A10_delta10)),axis=None)  # shifted e-field at ant10
RecA11Ey11 = np.roll(A11_Ey,int(round(A11_delta10)),axis=None)  # shifted e-field at ant11
RecA12Ey11 = np.roll(A12_Ey,int(round(A12_delta10)),axis=None)  # shifted e-field at ant12
RecA13Ey11 = np.roll(A13_Ey,int(round(A13_delta10)),axis=None)  # shifted e-field at ant13
RecA14Ey11 = np.roll(A14_Ey,int(round(A14_delta10)),axis=None)  # shifted e-field at ant14
RecA15Ey11 = np.roll(A15_Ey,int(round(A15_delta10)),axis=None)  # shifted e-field at ant15
RecA16Ey11 = np.roll(A16_Ey,int(round(A16_delta10)),axis=None)  # shifted e-field at ant16
RecA17Ey11 = np.roll(A17_Ey,int(round(A17_delta10)),axis=None)  # shifted e-field at ant17
RecA18Ey11 = np.roll(A18_Ey,int(round(A18_delta10)),axis=None)  # shifted e-field at ant18
RecA19Ey11 = np.roll(A19_Ey,int(round(A19_delta10)),axis=None) # shifted e-field at ant19
RecA20Ey11 = np.roll(A20_Ey,int(round(A20_delta10)),axis=None) # shifted e-field at ant20
RecA21Ey11 = np.roll(A21_Ey,int(round(A21_delta10)),axis=None) # shifted e-field at ant21
RecA22Ey11 = np.roll(A22_Ey,int(round(A22_delta10)),axis=None) # shifted e-field at ant22
RecA23Ey11 = np.roll(A23_Ey,int(round(A23_delta10)),axis=None) # shifted e-field at ant23
RecA24Ey11 = np.roll(A24_Ey,int(round(A24_delta10)),axis=None) # shifted e-field at ant24
RecA25Ey11 = np.roll(A25_Ey,int(round(A25_delta10)),axis=None) # shifted e-field at ant2


# In[108]:


# With respect to position (100m,0m) in the xy plane.
A1_delta11 = delta_ij(0,11,5.25) # delta_ij for antenna 1
A2_delta11 = delta_ij(1,11,5.25) # delta_ij for antenna 2
A3_delta11 = delta_ij(2,11,5.25) # delta_ij for antenna 3
A4_delta11 = delta_ij(3,11,5.25) # delta_ij for antenna 4
A5_delta11 = delta_ij(4,11,5.25) # delta_ij for antenna 5
A6_delta11 = delta_ij(5,11,5.25) # delta_ij for antenna 6
A7_delta11 = delta_ij(6,11,5.25) # delta_ij for antenna 7
A8_delta11 = delta_ij(7,11,5.25) # delta_ij for antenna 8
A9_delta11 = delta_ij(8,11,5.25) # delta_ij for antenna 9
A10_delta11 = delta_ij(9,11,5.25) # delta_ij for antenna 10
A11_delta11 = delta_ij(10,11,5.25) # delta_ij for antenna 11
A12_delta11 = delta_ij(11,11,5.25) # delta_ij for antenna 12
A13_delta11 = delta_ij(12,11,5.25) # delta_ij for antenna 13
A14_delta11 = delta_ij(13,11,5.25) # delta_ij for antenna 14
A15_delta11 = delta_ij(14,11,5.25) # delta_ij for antenna 15
A16_delta11 = delta_ij(15,11,5.25) # delta_ij for antenna 16
A17_delta11 = delta_ij(16,11,5.25) # delta_ij for antenna 17
A18_delta11 = delta_ij(17,11,5.25) # delta_ij for antenna 18
A19_delta11 = delta_ij(18,11,5.25) # delta_ij for antenna 19
A20_delta11 = delta_ij(19,11,5.25) # delta_ij for antenna 20
A21_delta11 = delta_ij(20,11,5.25) # delta_ij for antenna 21
A22_delta11 = delta_ij(21,11,5.25) # delta_ij for antenna 22
A23_delta11 = delta_ij(22,11,5.25) # delta_ij for antenna 23
A24_delta11 = delta_ij(23,11,5.25) # delta_ij for antenna 24
A25_delta11 = delta_ij(24,11,5.25) # delta_ij for antenna 25

RecA1Ey12 = np.roll(A1_Ey,int(round(A1_delta11)),axis=None)    # shifted e-field at ant1
RecA2Ey12 = np.roll(A2_Ey,int(round(A2_delta11)),axis=None)    # shifted e-field at ant2
RecA3Ey12 = np.roll(A3_Ey,int(round(A3_delta11)),axis=None)    # shifted e-field at ant3
RecA4Ey12 = np.roll(A4_Ey,int(round(A4_delta11)),axis=None)    # shifted e-field at ant4
RecA5Ey12 = np.roll(A5_Ey,int(round(A5_delta11)),axis=None)    # shifted e-field at ant5
RecA6Ey12 = np.roll(A6_Ey,int(round(A6_delta11)),axis=None)    # shifted e-field at ant6
RecA7Ey12 = np.roll(A7_Ey,int(round(A7_delta11)),axis=None)    # shifted e-field at ant7
RecA8Ey12 = np.roll(A8_Ey,int(round(A8_delta11)),axis=None)    # shifted e-field at ant8
RecA9Ey12 = np.roll(A9_Ey,int(round(A9_delta11)),axis=None)    # shifted e-field at ant9
RecA10Ey12 = np.roll(A10_Ey,int(round(A10_delta11)),axis=None)  # shifted e-field at ant10
RecA11Ey12 = np.roll(A11_Ey,int(round(A11_delta11)),axis=None)  # shifted e-field at ant11
RecA12Ey12 = np.roll(A12_Ey,int(round(A12_delta11)),axis=None)  # shifted e-field at ant12
RecA13Ey12 = np.roll(A13_Ey,int(round(A13_delta11)),axis=None)  # shifted e-field at ant13
RecA14Ey12 = np.roll(A14_Ey,int(round(A14_delta11)),axis=None)  # shifted e-field at ant14
RecA15Ey12 = np.roll(A15_Ey,int(round(A15_delta11)),axis=None)  # shifted e-field at ant15
RecA16Ey12 = np.roll(A16_Ey,int(round(A16_delta11)),axis=None)  # shifted e-field at ant16
RecA17Ey12 = np.roll(A17_Ey,int(round(A17_delta11)),axis=None)  # shifted e-field at ant17
RecA18Ey12 = np.roll(A18_Ey,int(round(A18_delta11)),axis=None)  # shifted e-field at ant18
RecA19Ey12 = np.roll(A19_Ey,int(round(A19_delta11)),axis=None) # shifted e-field at ant19
RecA20Ey12 = np.roll(A20_Ey,int(round(A20_delta11)),axis=None) # shifted e-field at ant20
RecA21Ey12 = np.roll(A21_Ey,int(round(A21_delta11)),axis=None) # shifted e-field at ant21
RecA22Ey12 = np.roll(A22_Ey,int(round(A22_delta11)),axis=None) # shifted e-field at ant22
RecA23Ey12 = np.roll(A23_Ey,int(round(A23_delta11)),axis=None) # shifted e-field at ant23
RecA24Ey12 = np.roll(A24_Ey,int(round(A24_delta11)),axis=None) # shifted e-field at ant24
RecA25Ey12 = np.roll(A25_Ey,int(round(A25_delta11)),axis=None) # shifted e-field at ant25


# In[109]:


# With respect to position (100m,0m) in the xy plane.
A1_delta12 = delta_ij(0,12,5.25) # delta_ij for antenna 1
A2_delta12 = delta_ij(1,12,5.25) # delta_ij for antenna 2
A3_delta12 = delta_ij(2,12,5.25) # delta_ij for antenna 3
A4_delta12 = delta_ij(3,12,5.25) # delta_ij for antenna 4
A5_delta12 = delta_ij(4,12,5.25) # delta_ij for antenna 5
A6_delta12 = delta_ij(5,12,5.25) # delta_ij for antenna 6
A7_delta12 = delta_ij(6,12,5.25) # delta_ij for antenna 7
A8_delta12 = delta_ij(7,12,5.25) # delta_ij for antenna 8
A9_delta12 = delta_ij(8,12,5.25) # delta_ij for antenna 9
A10_delta12 = delta_ij(9,12,5.25) # delta_ij for antenna 10
A11_delta12 = delta_ij(10,12,5.25) # delta_ij for antenna 11
A12_delta12 = delta_ij(11,12,5.25) # delta_ij for antenna 12
A13_delta12 = delta_ij(12,12,5.25) # delta_ij for antenna 13
A14_delta12 = delta_ij(13,12,5.25) # delta_ij for antenna 14
A15_delta12 = delta_ij(14,12,5.25) # delta_ij for antenna 15
A16_delta12 = delta_ij(15,12,5.25) # delta_ij for antenna 16
A17_delta12 = delta_ij(16,12,5.25) # delta_ij for antenna 17
A18_delta12 = delta_ij(17,12,5.25) # delta_ij for antenna 18
A19_delta12 = delta_ij(18,12,5.25) # delta_ij for antenna 19
A20_delta12 = delta_ij(19,12,5.25) # delta_ij for antenna 20
A21_delta12 = delta_ij(20,12,5.25) # delta_ij for antenna 21
A22_delta12 = delta_ij(21,12,5.25) # delta_ij for antenna 22
A23_delta12 = delta_ij(22,12,5.25) # delta_ij for antenna 23
A24_delta12 = delta_ij(23,12,5.25) # delta_ij for antenna 24
A25_delta12 = delta_ij(24,12,5.25) # delta_ij for antenna 25

RecA1Ey13 = np.roll(A1_Ey,int(round(A1_delta12)),axis=None)    # shifted e-field at ant1
RecA2Ey13 = np.roll(A2_Ey,int(round(A2_delta12)),axis=None)    # shifted e-field at ant2
RecA3Ey13 = np.roll(A3_Ey,int(round(A3_delta12)),axis=None)    # shifted e-field at ant3
RecA4Ey13 = np.roll(A4_Ey,int(round(A4_delta12)),axis=None)    # shifted e-field at ant4
RecA5Ey13 = np.roll(A5_Ey,int(round(A5_delta12)),axis=None)    # shifted e-field at ant5
RecA6Ey13 = np.roll(A6_Ey,int(round(A6_delta12)),axis=None)    # shifted e-field at ant6
RecA7Ey13 = np.roll(A7_Ey,int(round(A7_delta12)),axis=None)    # shifted e-field at ant7
RecA8Ey13 = np.roll(A8_Ey,int(round(A8_delta12)),axis=None)    # shifted e-field at ant8
RecA9Ey13 = np.roll(A9_Ey,int(round(A9_delta12)),axis=None)    # shifted e-field at ant9
RecA10Ey13 = np.roll(A10_Ey,int(round(A10_delta12)),axis=None)  # shifted e-field at ant10
RecA11Ey13 = np.roll(A11_Ey,int(round(A11_delta12)),axis=None)  # shifted e-field at ant11
RecA12Ey13 = np.roll(A12_Ey,int(round(A12_delta12)),axis=None)  # shifted e-field at ant12
RecA13Ey13 = np.roll(A13_Ey,int(round(A13_delta12)),axis=None)  # shifted e-field at ant13
RecA14Ey13 = np.roll(A14_Ey,int(round(A14_delta12)),axis=None)  # shifted e-field at ant14
RecA15Ey13 = np.roll(A15_Ey,int(round(A15_delta12)),axis=None)  # shifted e-field at ant15
RecA16Ey13 = np.roll(A16_Ey,int(round(A16_delta12)),axis=None)  # shifted e-field at ant16
RecA17Ey13 = np.roll(A17_Ey,int(round(A17_delta12)),axis=None)  # shifted e-field at ant17
RecA18Ey13 = np.roll(A18_Ey,int(round(A18_delta12)),axis=None)  # shifted e-field at ant18
RecA19Ey13 = np.roll(A19_Ey,int(round(A19_delta12)),axis=None) # shifted e-field at ant19
RecA20Ey13 = np.roll(A20_Ey,int(round(A20_delta12)),axis=None) # shifted e-field at ant20
RecA21Ey13 = np.roll(A21_Ey,int(round(A21_delta12)),axis=None) # shifted e-field at ant21
RecA22Ey13 = np.roll(A22_Ey,int(round(A22_delta12)),axis=None) # shifted e-field at ant22
RecA23Ey13 = np.roll(A23_Ey,int(round(A23_delta12)),axis=None) # shifted e-field at ant23
RecA24Ey13 = np.roll(A24_Ey,int(round(A24_delta12)),axis=None) # shifted e-field at ant24
RecA25Ey13 = np.roll(A25_Ey,int(round(A25_delta12)),axis=None) # shifted e-field at ant25


# In[110]:


# With respect to position (100m,0m) in the xy plane.
A1_delta13 = delta_ij(0,13,5.25) # delta_ij for antenna 1
A2_delta13 = delta_ij(1,13,5.25) # delta_ij for antenna 2
A3_delta13 = delta_ij(2,13,5.25) # delta_ij for antenna 3
A4_delta13 = delta_ij(3,13,5.25) # delta_ij for antenna 4
A5_delta13 = delta_ij(4,13,5.25) # delta_ij for antenna 5
A6_delta13 = delta_ij(5,13,5.25) # delta_ij for antenna 6
A7_delta13 = delta_ij(6,13,5.25) # delta_ij for antenna 7
A8_delta13 = delta_ij(7,13,5.25) # delta_ij for antenna 8
A9_delta13 = delta_ij(8,13,5.25) # delta_ij for antenna 9
A10_delta13 = delta_ij(9,13,5.25) # delta_ij for antenna 10
A11_delta13 = delta_ij(10,13,5.25) # delta_ij for antenna 11
A12_delta13 = delta_ij(11,13,5.25) # delta_ij for antenna 12
A13_delta13 = delta_ij(12,13,5.25) # delta_ij for antenna 13
A14_delta13 = delta_ij(13,13,5.25) # delta_ij for antenna 14
A15_delta13 = delta_ij(14,13,5.25) # delta_ij for antenna 15
A16_delta13 = delta_ij(15,13,5.25) # delta_ij for antenna 16
A17_delta13 = delta_ij(16,13,5.25) # delta_ij for antenna 17
A18_delta13 = delta_ij(17,13,5.25) # delta_ij for antenna 18
A19_delta13 = delta_ij(18,13,5.25) # delta_ij for antenna 19
A20_delta13 = delta_ij(19,13,5.25) # delta_ij for antenna 20
A21_delta13 = delta_ij(20,13,5.25) # delta_ij for antenna 21
A22_delta13 = delta_ij(21,13,5.25) # delta_ij for antenna 22
A23_delta13 = delta_ij(22,13,5.25) # delta_ij for antenna 23
A24_delta13 = delta_ij(23,13,5.25) # delta_ij for antenna 24
A25_delta13 = delta_ij(24,13,5.25) # delta_ij for antenna 25

RecA1Ey14 = np.roll(A1_Ey,int(round(A1_delta13)),axis=None)    # shifted e-field at ant1
RecA2Ey14 = np.roll(A2_Ey,int(round(A2_delta13)),axis=None)    # shifted e-field at ant2
RecA3Ey14 = np.roll(A3_Ey,int(round(A3_delta13)),axis=None)    # shifted e-field at ant3
RecA4Ey14 = np.roll(A4_Ey,int(round(A4_delta13)),axis=None)    # shifted e-field at ant4
RecA5Ey14 = np.roll(A5_Ey,int(round(A5_delta13)),axis=None)    # shifted e-field at ant5
RecA6Ey14 = np.roll(A6_Ey,int(round(A6_delta13)),axis=None)    # shifted e-field at ant6
RecA7Ey14 = np.roll(A7_Ey,int(round(A7_delta13)),axis=None)    # shifted e-field at ant7
RecA8Ey14 = np.roll(A8_Ey,int(round(A8_delta13)),axis=None)    # shifted e-field at ant8
RecA9Ey14 = np.roll(A9_Ey,int(round(A9_delta13)),axis=None)    # shifted e-field at ant9
RecA10Ey14 = np.roll(A10_Ey,int(round(A10_delta13)),axis=None)  # shifted e-field at ant10
RecA11Ey14 = np.roll(A11_Ey,int(round(A11_delta13)),axis=None)  # shifted e-field at ant11
RecA12Ey14 = np.roll(A12_Ey,int(round(A12_delta13)),axis=None)  # shifted e-field at ant12
RecA13Ey14 = np.roll(A13_Ey,int(round(A13_delta13)),axis=None)  # shifted e-field at ant13
RecA14Ey14 = np.roll(A14_Ey,int(round(A14_delta13)),axis=None)  # shifted e-field at ant14
RecA15Ey14 = np.roll(A15_Ey,int(round(A15_delta13)),axis=None)  # shifted e-field at ant15
RecA16Ey14 = np.roll(A16_Ey,int(round(A16_delta13)),axis=None)  # shifted e-field at ant16
RecA17Ey14 = np.roll(A17_Ey,int(round(A17_delta13)),axis=None)  # shifted e-field at ant17
RecA18Ey14 = np.roll(A18_Ey,int(round(A18_delta13)),axis=None)  # shifted e-field at ant18
RecA19Ey14 = np.roll(A19_Ey,int(round(A19_delta13)),axis=None) # shifted e-field at ant19
RecA20Ey14 = np.roll(A20_Ey,int(round(A20_delta13)),axis=None) # shifted e-field at ant20
RecA21Ey14 = np.roll(A21_Ey,int(round(A21_delta13)),axis=None) # shifted e-field at ant21
RecA22Ey14 = np.roll(A22_Ey,int(round(A22_delta13)),axis=None) # shifted e-field at ant22
RecA23Ey14 = np.roll(A23_Ey,int(round(A23_delta13)),axis=None) # shifted e-field at ant23
RecA24Ey14 = np.roll(A24_Ey,int(round(A24_delta13)),axis=None) # shifted e-field at ant24
RecA25Ey14 = np.roll(A25_Ey,int(round(A25_delta13)),axis=None) # shifted e-field at ant25


# In[111]:


# With respect to position (100m,0m) in the xy plane.
A1_delta14 = delta_ij(0,14,5.25) # delta_ij for antenna 1
A2_delta14 = delta_ij(1,14,5.25) # delta_ij for antenna 2
A3_delta14 = delta_ij(2,14,5.25) # delta_ij for antenna 3
A4_delta14 = delta_ij(3,14,5.25) # delta_ij for antenna 4
A5_delta14 = delta_ij(4,14,5.25) # delta_ij for antenna 5
A6_delta14 = delta_ij(5,14,5.25) # delta_ij for antenna 6
A7_delta14 = delta_ij(6,14,5.25) # delta_ij for antenna 7
A8_delta14 = delta_ij(7,14,5.25) # delta_ij for antenna 8
A9_delta14 = delta_ij(8,14,5.25) # delta_ij for antenna 9
A10_delta14 = delta_ij(9,14,5.25) # delta_ij for antenna 10
A11_delta14 = delta_ij(10,14,5.25) # delta_ij for antenna 11
A12_delta14 = delta_ij(11,14,5.25) # delta_ij for antenna 12
A13_delta14 = delta_ij(12,14,5.25) # delta_ij for antenna 13
A14_delta14 = delta_ij(13,14,5.25) # delta_ij for antenna 14
A15_delta14 = delta_ij(14,14,5.25) # delta_ij for antenna 15
A16_delta14 = delta_ij(15,14,5.25) # delta_ij for antenna 16
A17_delta14 = delta_ij(16,14,5.25) # delta_ij for antenna 17
A18_delta14 = delta_ij(17,14,5.25) # delta_ij for antenna 18
A19_delta14 = delta_ij(18,14,5.25) # delta_ij for antenna 19
A20_delta14 = delta_ij(19,14,5.25) # delta_ij for antenna 20
A21_delta14 = delta_ij(20,14,5.25) # delta_ij for antenna 21
A22_delta14 = delta_ij(21,14,5.25) # delta_ij for antenna 22
A23_delta14 = delta_ij(22,14,5.25) # delta_ij for antenna 23
A24_delta14 = delta_ij(23,14,5.25) # delta_ij for antenna 24
A25_delta14 = delta_ij(24,14,5.25) # delta_ij for antenna 25

RecA1Ey15 = np.roll(A1_Ey,int(round(A1_delta14)),axis=None)    # shifted e-field at ant1
RecA2Ey15 = np.roll(A2_Ey,int(round(A2_delta14)),axis=None)    # shifted e-field at ant2
RecA3Ey15 = np.roll(A3_Ey,int(round(A3_delta14)),axis=None)    # shifted e-field at ant3
RecA4Ey15 = np.roll(A4_Ey,int(round(A4_delta14)),axis=None)    # shifted e-field at ant4
RecA5Ey15 = np.roll(A5_Ey,int(round(A5_delta14)),axis=None)    # shifted e-field at ant5
RecA6Ey15 = np.roll(A6_Ey,int(round(A6_delta14)),axis=None)    # shifted e-field at ant6
RecA7Ey15 = np.roll(A7_Ey,int(round(A7_delta14)),axis=None)    # shifted e-field at ant7
RecA8Ey15 = np.roll(A8_Ey,int(round(A8_delta14)),axis=None)    # shifted e-field at ant8
RecA9Ey15 = np.roll(A9_Ey,int(round(A9_delta14)),axis=None)    # shifted e-field at ant9
RecA10Ey15 = np.roll(A10_Ey,int(round(A10_delta14)),axis=None)  # shifted e-field at ant10
RecA11Ey15 = np.roll(A11_Ey,int(round(A11_delta14)),axis=None)  # shifted e-field at ant11
RecA12Ey15 = np.roll(A12_Ey,int(round(A12_delta14)),axis=None)  # shifted e-field at ant12
RecA13Ey15 = np.roll(A13_Ey,int(round(A13_delta14)),axis=None)  # shifted e-field at ant13
RecA14Ey15 = np.roll(A14_Ey,int(round(A14_delta14)),axis=None)  # shifted e-field at ant14
RecA15Ey15 = np.roll(A15_Ey,int(round(A15_delta14)),axis=None)  # shifted e-field at ant15
RecA16Ey15 = np.roll(A16_Ey,int(round(A16_delta14)),axis=None)  # shifted e-field at ant16
RecA17Ey15 = np.roll(A17_Ey,int(round(A17_delta14)),axis=None)  # shifted e-field at ant17
RecA18Ey15 = np.roll(A18_Ey,int(round(A18_delta14)),axis=None)  # shifted e-field at ant18
RecA19Ey15 = np.roll(A19_Ey,int(round(A19_delta14)),axis=None) # shifted e-field at ant19
RecA20Ey15 = np.roll(A20_Ey,int(round(A20_delta14)),axis=None) # shifted e-field at ant20
RecA21Ey15 = np.roll(A21_Ey,int(round(A21_delta14)),axis=None) # shifted e-field at ant21
RecA22Ey15 = np.roll(A22_Ey,int(round(A22_delta14)),axis=None) # shifted e-field at ant22
RecA23Ey15 = np.roll(A23_Ey,int(round(A23_delta14)),axis=None) # shifted e-field at ant23
RecA24Ey15 = np.roll(A24_Ey,int(round(A24_delta14)),axis=None) # shifted e-field at ant24
RecA25Ey15 = np.roll(A25_Ey,int(round(A25_delta14)),axis=None) # shifted e-field at ant25


# In[112]:


# With respect to position (100m,0m) in the xy plane.
A1_delta15 = delta_ij(0,15,5.25) # delta_ij for antenna 1
A2_delta15 = delta_ij(1,15,5.25) # delta_ij for antenna 2
A3_delta15 = delta_ij(2,15,5.25) # delta_ij for antenna 3
A4_delta15 = delta_ij(3,15,5.25) # delta_ij for antenna 4
A5_delta15 = delta_ij(4,15,5.25) # delta_ij for antenna 5
A6_delta15 = delta_ij(5,15,5.25) # delta_ij for antenna 6
A7_delta15 = delta_ij(6,15,5.25) # delta_ij for antenna 7
A8_delta15 = delta_ij(7,15,5.25) # delta_ij for antenna 8
A9_delta15 = delta_ij(8,15,5.25) # delta_ij for antenna 9
A10_delta15 = delta_ij(9,15,5.25) # delta_ij for antenna 10
A11_delta15 = delta_ij(10,15,5.25) # delta_ij for antenna 11
A12_delta15 = delta_ij(11,15,5.25) # delta_ij for antenna 12
A13_delta15 = delta_ij(12,15,5.25) # delta_ij for antenna 13
A14_delta15 = delta_ij(13,15,5.25) # delta_ij for antenna 14
A15_delta15 = delta_ij(14,15,5.25) # delta_ij for antenna 15
A16_delta15 = delta_ij(15,15,5.25) # delta_ij for antenna 16
A17_delta15 = delta_ij(16,15,5.25) # delta_ij for antenna 17
A18_delta15 = delta_ij(17,15,5.25) # delta_ij for antenna 18
A19_delta15 = delta_ij(18,15,5.25) # delta_ij for antenna 19
A20_delta15 = delta_ij(19,15,5.25) # delta_ij for antenna 20
A21_delta15 = delta_ij(20,15,5.25) # delta_ij for antenna 21
A22_delta15 = delta_ij(21,15,5.25) # delta_ij for antenna 22
A23_delta15 = delta_ij(22,15,5.25) # delta_ij for antenna 23
A24_delta15 = delta_ij(23,15,5.25) # delta_ij for antenna 24
A25_delta15 = delta_ij(24,15,5.25) # delta_ij for antenna 25

RecA1Ey16 = np.roll(A1_Ey,int(round(A1_delta15)),axis=None)    # shifted e-field at ant1
RecA2Ey16 = np.roll(A2_Ey,int(round(A2_delta15)),axis=None)    # shifted e-field at ant2
RecA3Ey16 = np.roll(A3_Ey,int(round(A3_delta15)),axis=None)    # shifted e-field at ant3
RecA4Ey16 = np.roll(A4_Ey,int(round(A4_delta15)),axis=None)    # shifted e-field at ant4
RecA5Ey16 = np.roll(A5_Ey,int(round(A5_delta15)),axis=None)    # shifted e-field at ant5
RecA6Ey16 = np.roll(A6_Ey,int(round(A6_delta15)),axis=None)    # shifted e-field at ant6
RecA7Ey16 = np.roll(A7_Ey,int(round(A7_delta15)),axis=None)    # shifted e-field at ant7
RecA8Ey16 = np.roll(A8_Ey,int(round(A8_delta15)),axis=None)    # shifted e-field at ant8
RecA9Ey16 = np.roll(A9_Ey,int(round(A9_delta15)),axis=None)    # shifted e-field at ant9
RecA10Ey16 = np.roll(A10_Ey,int(round(A10_delta15)),axis=None)  # shifted e-field at ant10
RecA11Ey16 = np.roll(A11_Ey,int(round(A11_delta15)),axis=None)  # shifted e-field at ant11
RecA12Ey16 = np.roll(A12_Ey,int(round(A12_delta15)),axis=None)  # shifted e-field at ant12
RecA13Ey16 = np.roll(A13_Ey,int(round(A13_delta15)),axis=None)  # shifted e-field at ant13
RecA14Ey16 = np.roll(A14_Ey,int(round(A14_delta15)),axis=None)  # shifted e-field at ant14
RecA15Ey16 = np.roll(A15_Ey,int(round(A15_delta15)),axis=None)  # shifted e-field at ant15
RecA16Ey16 = np.roll(A16_Ey,int(round(A16_delta15)),axis=None)  # shifted e-field at ant16
RecA17Ey16 = np.roll(A17_Ey,int(round(A17_delta15)),axis=None)  # shifted e-field at ant17
RecA18Ey16 = np.roll(A18_Ey,int(round(A18_delta15)),axis=None)  # shifted e-field at ant18
RecA19Ey16 = np.roll(A19_Ey,int(round(A19_delta15)),axis=None) # shifted e-field at ant19
RecA20Ey16 = np.roll(A20_Ey,int(round(A20_delta15)),axis=None) # shifted e-field at ant20
RecA21Ey16 = np.roll(A21_Ey,int(round(A21_delta15)),axis=None) # shifted e-field at ant21
RecA22Ey16 = np.roll(A22_Ey,int(round(A22_delta15)),axis=None) # shifted e-field at ant22
RecA23Ey16 = np.roll(A23_Ey,int(round(A23_delta15)),axis=None) # shifted e-field at ant23
RecA24Ey16 = np.roll(A24_Ey,int(round(A24_delta15)),axis=None) # shifted e-field at ant24
RecA25Ey16 = np.roll(A25_Ey,int(round(A25_delta15)),axis=None) # shifted e-field at ant25


# In[113]:


# With respect to position (100m,0m) in the xy plane.
A1_delta16 = delta_ij(0,16,5.25) # delta_ij for antenna 1
A2_delta16 = delta_ij(1,16,5.25) # delta_ij for antenna 2
A3_delta16 = delta_ij(2,16,5.25) # delta_ij for antenna 3
A4_delta16 = delta_ij(3,16,5.25) # delta_ij for antenna 4
A5_delta16 = delta_ij(4,16,5.25) # delta_ij for antenna 5
A6_delta16 = delta_ij(5,16,5.25) # delta_ij for antenna 6
A7_delta16 = delta_ij(6,16,5.25) # delta_ij for antenna 7
A8_delta16 = delta_ij(7,16,5.25) # delta_ij for antenna 8
A9_delta16 = delta_ij(8,16,5.25) # delta_ij for antenna 9
A10_delta16 = delta_ij(9,16,5.25) # delta_ij for antenna 10
A11_delta16 = delta_ij(10,16,5.25) # delta_ij for antenna 11
A12_delta16 = delta_ij(11,16,5.25) # delta_ij for antenna 12
A13_delta16 = delta_ij(12,16,5.25) # delta_ij for antenna 13
A14_delta16 = delta_ij(13,16,5.25) # delta_ij for antenna 14
A15_delta16 = delta_ij(14,16,5.25) # delta_ij for antenna 15
A16_delta16 = delta_ij(15,16,5.25) # delta_ij for antenna 16
A17_delta16 = delta_ij(16,16,5.25) # delta_ij for antenna 17
A18_delta16 = delta_ij(17,16,5.25) # delta_ij for antenna 18
A19_delta16 = delta_ij(18,16,5.25) # delta_ij for antenna 19
A20_delta16 = delta_ij(19,16,5.25) # delta_ij for antenna 20
A21_delta16 = delta_ij(20,16,5.25) # delta_ij for antenna 21
A22_delta16 = delta_ij(21,16,5.25) # delta_ij for antenna 22
A23_delta16 = delta_ij(22,16,5.25) # delta_ij for antenna 23
A24_delta16 = delta_ij(23,16,5.25) # delta_ij for antenna 24
A25_delta16 = delta_ij(24,16,5.25) # delta_ij for antenna 25

RecA1Ey17 = np.roll(A1_Ey,int(round(A1_delta16)),axis=None)    # shifted e-field at ant1
RecA2Ey17 = np.roll(A2_Ey,int(round(A2_delta16)),axis=None)    # shifted e-field at ant2
RecA3Ey17 = np.roll(A3_Ey,int(round(A3_delta16)),axis=None)    # shifted e-field at ant3
RecA4Ey17 = np.roll(A4_Ey,int(round(A4_delta16)),axis=None)    # shifted e-field at ant4
RecA5Ey17 = np.roll(A5_Ey,int(round(A5_delta16)),axis=None)    # shifted e-field at ant5
RecA6Ey17 = np.roll(A6_Ey,int(round(A6_delta16)),axis=None)    # shifted e-field at ant6
RecA7Ey17 = np.roll(A7_Ey,int(round(A7_delta16)),axis=None)    # shifted e-field at ant7
RecA8Ey17 = np.roll(A8_Ey,int(round(A8_delta16)),axis=None)    # shifted e-field at ant8
RecA9Ey17 = np.roll(A9_Ey,int(round(A9_delta16)),axis=None)    # shifted e-field at ant9
RecA10Ey17 = np.roll(A10_Ey,int(round(A10_delta16)),axis=None)  # shifted e-field at ant10
RecA11Ey17 = np.roll(A11_Ey,int(round(A11_delta16)),axis=None)  # shifted e-field at ant11
RecA12Ey17 = np.roll(A12_Ey,int(round(A12_delta16)),axis=None)  # shifted e-field at ant12
RecA13Ey17 = np.roll(A13_Ey,int(round(A13_delta16)),axis=None)  # shifted e-field at ant13
RecA14Ey17 = np.roll(A14_Ey,int(round(A14_delta16)),axis=None)  # shifted e-field at ant14
RecA15Ey17 = np.roll(A15_Ey,int(round(A15_delta16)),axis=None)  # shifted e-field at ant15
RecA16Ey17 = np.roll(A16_Ey,int(round(A16_delta16)),axis=None)  # shifted e-field at ant16
RecA17Ey17 = np.roll(A17_Ey,int(round(A17_delta16)),axis=None)  # shifted e-field at ant17
RecA18Ey17 = np.roll(A18_Ey,int(round(A18_delta16)),axis=None)  # shifted e-field at ant18
RecA19Ey17 = np.roll(A19_Ey,int(round(A19_delta16)),axis=None) # shifted e-field at ant19
RecA20Ey17 = np.roll(A20_Ey,int(round(A20_delta16)),axis=None) # shifted e-field at ant20
RecA21Ey17 = np.roll(A21_Ey,int(round(A21_delta16)),axis=None) # shifted e-field at ant21
RecA22Ey17 = np.roll(A22_Ey,int(round(A22_delta16)),axis=None) # shifted e-field at ant22
RecA23Ey17 = np.roll(A23_Ey,int(round(A23_delta16)),axis=None) # shifted e-field at ant23
RecA24Ey17 = np.roll(A24_Ey,int(round(A24_delta16)),axis=None) # shifted e-field at ant24
RecA25Ey17 = np.roll(A25_Ey,int(round(A25_delta16)),axis=None) # shifted e-field at ant25


# In[114]:


# With respect to position (100m,0m) in the xy plane.
A1_delta17 = delta_ij(0,17,5.25) # delta_ij for antenna 1
A2_delta17 = delta_ij(1,17,5.25) # delta_ij for antenna 2
A3_delta17 = delta_ij(2,17,5.25) # delta_ij for antenna 3
A4_delta17 = delta_ij(3,17,5.25) # delta_ij for antenna 4
A5_delta17 = delta_ij(4,17,5.25) # delta_ij for antenna 5
A6_delta17 = delta_ij(5,17,5.25) # delta_ij for antenna 6
A7_delta17 = delta_ij(6,17,5.25) # delta_ij for antenna 7
A8_delta17 = delta_ij(7,17,5.25) # delta_ij for antenna 8
A9_delta17 = delta_ij(8,17,5.25) # delta_ij for antenna 9
A10_delta17 = delta_ij(9,17,5.25) # delta_ij for antenna 10
A11_delta17 = delta_ij(10,17,5.25) # delta_ij for antenna 11
A12_delta17 = delta_ij(11,17,5.25) # delta_ij for antenna 12
A13_delta17 = delta_ij(12,17,5.25) # delta_ij for antenna 13
A14_delta17 = delta_ij(13,17,5.25) # delta_ij for antenna 14
A15_delta17 = delta_ij(14,17,5.25) # delta_ij for antenna 15
A16_delta17 = delta_ij(15,17,5.25) # delta_ij for antenna 16
A17_delta17 = delta_ij(16,17,5.25) # delta_ij for antenna 17
A18_delta17 = delta_ij(17,17,5.25) # delta_ij for antenna 18
A19_delta17 = delta_ij(18,17,5.25) # delta_ij for antenna 19
A20_delta17 = delta_ij(19,17,5.25) # delta_ij for antenna 20
A21_delta17 = delta_ij(20,17,5.25) # delta_ij for antenna 21
A22_delta17 = delta_ij(21,17,5.25) # delta_ij for antenna 22
A23_delta17 = delta_ij(22,17,5.25) # delta_ij for antenna 23
A24_delta17 = delta_ij(23,17,5.25) # delta_ij for antenna 24
A25_delta17 = delta_ij(24,17,5.25) # delta_ij for antenna 25

RecA1Ey18 = np.roll(A1_Ey,int(round(A1_delta17)),axis=None)    # shifted e-field at ant1
RecA2Ey18 = np.roll(A2_Ey,int(round(A2_delta17)),axis=None)    # shifted e-field at ant2
RecA3Ey18 = np.roll(A3_Ey,int(round(A3_delta17)),axis=None)    # shifted e-field at ant3
RecA4Ey18 = np.roll(A4_Ey,int(round(A4_delta17)),axis=None)    # shifted e-field at ant4
RecA5Ey18 = np.roll(A5_Ey,int(round(A5_delta17)),axis=None)    # shifted e-field at ant5
RecA6Ey18 = np.roll(A6_Ey,int(round(A6_delta17)),axis=None)    # shifted e-field at ant6
RecA7Ey18 = np.roll(A7_Ey,int(round(A7_delta17)),axis=None)    # shifted e-field at ant7
RecA8Ey18 = np.roll(A8_Ey,int(round(A8_delta17)),axis=None)    # shifted e-field at ant8
RecA9Ey18 = np.roll(A9_Ey,int(round(A9_delta17)),axis=None)    # shifted e-field at ant9
RecA10Ey18 = np.roll(A10_Ey,int(round(A10_delta17)),axis=None)  # shifted e-field at ant10
RecA11Ey18 = np.roll(A11_Ey,int(round(A11_delta17)),axis=None)  # shifted e-field at ant11
RecA12Ey18 = np.roll(A12_Ey,int(round(A12_delta17)),axis=None)  # shifted e-field at ant12
RecA13Ey18 = np.roll(A13_Ey,int(round(A13_delta17)),axis=None)  # shifted e-field at ant13
RecA14Ey18 = np.roll(A14_Ey,int(round(A14_delta17)),axis=None)  # shifted e-field at ant14
RecA15Ey18 = np.roll(A15_Ey,int(round(A15_delta17)),axis=None)  # shifted e-field at ant15
RecA16Ey18 = np.roll(A16_Ey,int(round(A16_delta17)),axis=None)  # shifted e-field at ant16
RecA17Ey18 = np.roll(A17_Ey,int(round(A17_delta17)),axis=None)  # shifted e-field at ant17
RecA18Ey18 = np.roll(A18_Ey,int(round(A18_delta17)),axis=None)  # shifted e-field at ant18
RecA19Ey18 = np.roll(A19_Ey,int(round(A19_delta17)),axis=None) # shifted e-field at ant19
RecA20Ey18 = np.roll(A20_Ey,int(round(A20_delta17)),axis=None) # shifted e-field at ant20
RecA21Ey18 = np.roll(A21_Ey,int(round(A21_delta17)),axis=None) # shifted e-field at ant21
RecA22Ey18 = np.roll(A22_Ey,int(round(A22_delta17)),axis=None) # shifted e-field at ant22
RecA23Ey18 = np.roll(A23_Ey,int(round(A23_delta17)),axis=None) # shifted e-field at ant23
RecA24Ey18 = np.roll(A24_Ey,int(round(A24_delta17)),axis=None) # shifted e-field at ant24
RecA25Ey18 = np.roll(A25_Ey,int(round(A25_delta17)),axis=None) # shifted e-field at ant25


# In[115]:


# With respect to position (100m,0m) in the xy plane.
A1_delta18 = delta_ij(0,18,5.25) # delta_ij for antenna 1
A2_delta18 = delta_ij(1,18,5.25) # delta_ij for antenna 2
A3_delta18 = delta_ij(2,18,5.25) # delta_ij for antenna 3
A4_delta18 = delta_ij(3,18,5.25) # delta_ij for antenna 4
A5_delta18 = delta_ij(4,18,5.25) # delta_ij for antenna 5
A6_delta18 = delta_ij(5,18,5.25) # delta_ij for antenna 6
A7_delta18 = delta_ij(6,18,5.25) # delta_ij for antenna 7
A8_delta18 = delta_ij(7,18,5.25) # delta_ij for antenna 8
A9_delta18 = delta_ij(8,18,5.25) # delta_ij for antenna 9
A10_delta18 = delta_ij(9,18,5.25) # delta_ij for antenna 10
A11_delta18 = delta_ij(10,18,5.25) # delta_ij for antenna 11
A12_delta18 = delta_ij(11,18,5.25) # delta_ij for antenna 12
A13_delta18 = delta_ij(12,18,5.25) # delta_ij for antenna 13
A14_delta18 = delta_ij(13,18,5.25) # delta_ij for antenna 14
A15_delta18 = delta_ij(14,18,5.25) # delta_ij for antenna 15
A16_delta18 = delta_ij(15,18,5.25) # delta_ij for antenna 16
A17_delta18 = delta_ij(16,18,5.25) # delta_ij for antenna 17
A18_delta18 = delta_ij(17,18,5.25) # delta_ij for antenna 18
A19_delta18 = delta_ij(18,18,5.25) # delta_ij for antenna 19
A20_delta18 = delta_ij(19,18,5.25) # delta_ij for antenna 20
A21_delta18 = delta_ij(20,18,5.25) # delta_ij for antenna 21
A22_delta18 = delta_ij(21,18,5.25) # delta_ij for antenna 22
A23_delta18 = delta_ij(22,18,5.25) # delta_ij for antenna 23
A24_delta18 = delta_ij(23,18,5.25) # delta_ij for antenna 24
A25_delta18 = delta_ij(24,18,5.25) # delta_ij for antenna 25

RecA1Ey19 = np.roll(A1_Ey,int(round(A1_delta18)),axis=None)    # shifted e-field at ant1
RecA2Ey19 = np.roll(A2_Ey,int(round(A2_delta18)),axis=None)    # shifted e-field at ant2
RecA3Ey19 = np.roll(A3_Ey,int(round(A3_delta18)),axis=None)    # shifted e-field at ant3
RecA4Ey19 = np.roll(A4_Ey,int(round(A4_delta18)),axis=None)    # shifted e-field at ant4
RecA5Ey19 = np.roll(A5_Ey,int(round(A5_delta18)),axis=None)    # shifted e-field at ant5
RecA6Ey19 = np.roll(A6_Ey,int(round(A6_delta18)),axis=None)    # shifted e-field at ant6
RecA7Ey19 = np.roll(A7_Ey,int(round(A7_delta18)),axis=None)    # shifted e-field at ant7
RecA8Ey19 = np.roll(A8_Ey,int(round(A8_delta18)),axis=None)    # shifted e-field at ant8
RecA9Ey19 = np.roll(A9_Ey,int(round(A9_delta18)),axis=None)    # shifted e-field at ant9
RecA10Ey19 = np.roll(A10_Ey,int(round(A10_delta18)),axis=None)  # shifted e-field at ant10
RecA11Ey19 = np.roll(A11_Ey,int(round(A11_delta18)),axis=None)  # shifted e-field at ant11
RecA12Ey19 = np.roll(A12_Ey,int(round(A12_delta18)),axis=None)  # shifted e-field at ant12
RecA13Ey19 = np.roll(A13_Ey,int(round(A13_delta18)),axis=None)  # shifted e-field at ant13
RecA14Ey19 = np.roll(A14_Ey,int(round(A14_delta18)),axis=None)  # shifted e-field at ant14
RecA15Ey19 = np.roll(A15_Ey,int(round(A15_delta18)),axis=None)  # shifted e-field at ant15
RecA16Ey19 = np.roll(A16_Ey,int(round(A16_delta18)),axis=None)  # shifted e-field at ant16
RecA17Ey19 = np.roll(A17_Ey,int(round(A17_delta18)),axis=None)  # shifted e-field at ant17
RecA18Ey19 = np.roll(A18_Ey,int(round(A18_delta18)),axis=None)  # shifted e-field at ant18
RecA19Ey19 = np.roll(A19_Ey,int(round(A19_delta18)),axis=None) # shifted e-field at ant19
RecA20Ey19 = np.roll(A20_Ey,int(round(A20_delta18)),axis=None) # shifted e-field at ant20
RecA21Ey19 = np.roll(A21_Ey,int(round(A21_delta18)),axis=None) # shifted e-field at ant21
RecA22Ey19 = np.roll(A22_Ey,int(round(A22_delta18)),axis=None) # shifted e-field at ant22
RecA23Ey19 = np.roll(A23_Ey,int(round(A23_delta18)),axis=None) # shifted e-field at ant23
RecA24Ey19 = np.roll(A24_Ey,int(round(A24_delta18)),axis=None) # shifted e-field at ant24
RecA25Ey19 = np.roll(A25_Ey,int(round(A25_delta18)),axis=None) # shifted e-field at ant25


# In[116]:


# With respect to position (100m,0m) in the xy plane.
A1_delta19 = delta_ij(0,19,5.25) # delta_ij for antenna 1
A2_delta19 = delta_ij(1,19,5.25) # delta_ij for antenna 2
A3_delta19 = delta_ij(2,19,5.25) # delta_ij for antenna 3
A4_delta19 = delta_ij(3,19,5.25) # delta_ij for antenna 4
A5_delta19 = delta_ij(4,19,5.25) # delta_ij for antenna 5
A6_delta19 = delta_ij(5,19,5.25) # delta_ij for antenna 6
A7_delta19 = delta_ij(6,19,5.25) # delta_ij for antenna 7
A8_delta19 = delta_ij(7,19,5.25) # delta_ij for antenna 8
A9_delta19 = delta_ij(8,19,5.25) # delta_ij for antenna 9
A10_delta19 = delta_ij(9,19,5.25) # delta_ij for antenna 10
A11_delta19 = delta_ij(10,19,5.25) # delta_ij for antenna 11
A12_delta19 = delta_ij(11,19,5.25) # delta_ij for antenna 12
A13_delta19 = delta_ij(12,19,5.25) # delta_ij for antenna 13
A14_delta19 = delta_ij(13,19,5.25) # delta_ij for antenna 14
A15_delta19 = delta_ij(14,19,5.25) # delta_ij for antenna 15
A16_delta19 = delta_ij(15,19,5.25) # delta_ij for antenna 16
A17_delta19 = delta_ij(16,19,5.25) # delta_ij for antenna 17
A18_delta19 = delta_ij(17,19,5.25) # delta_ij for antenna 18
A19_delta19 = delta_ij(18,19,5.25) # delta_ij for antenna 19
A20_delta19 = delta_ij(19,19,5.25) # delta_ij for antenna 20
A21_delta19 = delta_ij(20,19,5.25) # delta_ij for antenna 21
A22_delta19 = delta_ij(21,19,5.25) # delta_ij for antenna 22
A23_delta19 = delta_ij(22,19,5.25) # delta_ij for antenna 23
A24_delta19 = delta_ij(23,19,5.25) # delta_ij for antenna 24
A25_delta19 = delta_ij(24,19,5.25) # delta_ij for antenna 25

RecA1Ey20 = np.roll(A1_Ey,int(round(A1_delta19)),axis=None)    # shifted e-field at ant1
RecA2Ey20 = np.roll(A2_Ey,int(round(A2_delta19)),axis=None)    # shifted e-field at ant2
RecA3Ey20 = np.roll(A3_Ey,int(round(A3_delta19)),axis=None)    # shifted e-field at ant3
RecA4Ey20 = np.roll(A4_Ey,int(round(A4_delta19)),axis=None)    # shifted e-field at ant4
RecA5Ey20 = np.roll(A5_Ey,int(round(A5_delta19)),axis=None)    # shifted e-field at ant5
RecA6Ey20 = np.roll(A6_Ey,int(round(A6_delta19)),axis=None)    # shifted e-field at ant6
RecA7Ey20 = np.roll(A7_Ey,int(round(A7_delta19)),axis=None)    # shifted e-field at ant7
RecA8Ey20 = np.roll(A8_Ey,int(round(A8_delta19)),axis=None)    # shifted e-field at ant8
RecA9Ey20 = np.roll(A9_Ey,int(round(A9_delta19)),axis=None)    # shifted e-field at ant9
RecA10Ey20 = np.roll(A10_Ey,int(round(A10_delta19)),axis=None)  # shifted e-field at ant10
RecA11Ey20 = np.roll(A11_Ey,int(round(A11_delta19)),axis=None)  # shifted e-field at ant11
RecA12Ey20 = np.roll(A12_Ey,int(round(A12_delta19)),axis=None)  # shifted e-field at ant12
RecA13Ey20 = np.roll(A13_Ey,int(round(A13_delta19)),axis=None)  # shifted e-field at ant13
RecA14Ey20 = np.roll(A14_Ey,int(round(A14_delta19)),axis=None)  # shifted e-field at ant14
RecA15Ey20 = np.roll(A15_Ey,int(round(A15_delta19)),axis=None)  # shifted e-field at ant15
RecA16Ey20 = np.roll(A16_Ey,int(round(A16_delta19)),axis=None)  # shifted e-field at ant16
RecA17Ey20 = np.roll(A17_Ey,int(round(A17_delta19)),axis=None)  # shifted e-field at ant17
RecA18Ey20 = np.roll(A18_Ey,int(round(A18_delta19)),axis=None)  # shifted e-field at ant18
RecA19Ey20 = np.roll(A19_Ey,int(round(A19_delta19)),axis=None) # shifted e-field at ant19
RecA20Ey20 = np.roll(A20_Ey,int(round(A20_delta19)),axis=None) # shifted e-field at ant20
RecA21Ey20 = np.roll(A21_Ey,int(round(A21_delta19)),axis=None) # shifted e-field at ant21
RecA22Ey20 = np.roll(A22_Ey,int(round(A22_delta19)),axis=None) # shifted e-field at ant22
RecA23Ey20 = np.roll(A23_Ey,int(round(A23_delta19)),axis=None) # shifted e-field at ant23
RecA24Ey20 = np.roll(A24_Ey,int(round(A24_delta19)),axis=None) # shifted e-field at ant24
RecA25Ey20 = np.roll(A25_Ey,int(round(A25_delta19)),axis=None) # shifted e-field at ant25


# In[117]:


# With respect to position (100m,0m) in the xy plane.
A1_delta20 = delta_ij(0,20,5.25) # delta_ij for antenna 1
A2_delta20 = delta_ij(1,20,5.25) # delta_ij for antenna 2
A3_delta20 = delta_ij(2,20,5.25) # delta_ij for antenna 3
A4_delta20 = delta_ij(3,20,5.25) # delta_ij for antenna 4
A5_delta20 = delta_ij(4,20,5.25) # delta_ij for antenna 5
A6_delta20 = delta_ij(5,20,5.25) # delta_ij for antenna 6
A7_delta20 = delta_ij(6,20,5.25) # delta_ij for antenna 7
A8_delta20 = delta_ij(7,20,5.25) # delta_ij for antenna 8
A9_delta20 = delta_ij(8,20,5.25) # delta_ij for antenna 9
A10_delta20 = delta_ij(9,20,5.25) # delta_ij for antenna 10
A11_delta20 = delta_ij(10,20,5.25) # delta_ij for antenna 11
A12_delta20 = delta_ij(11,20,5.25) # delta_ij for antenna 12
A13_delta20 = delta_ij(12,20,5.25) # delta_ij for antenna 13
A14_delta20 = delta_ij(13,20,5.25) # delta_ij for antenna 14
A15_delta20 = delta_ij(14,20,5.25) # delta_ij for antenna 15
A16_delta20 = delta_ij(15,20,5.25) # delta_ij for antenna 16
A17_delta20 = delta_ij(16,20,5.25) # delta_ij for antenna 17
A18_delta20 = delta_ij(17,20,5.25) # delta_ij for antenna 18
A19_delta20 = delta_ij(18,20,5.25) # delta_ij for antenna 19
A20_delta20 = delta_ij(19,20,5.25) # delta_ij for antenna 20
A21_delta20 = delta_ij(20,20,5.25) # delta_ij for antenna 21
A22_delta20 = delta_ij(21,20,5.25) # delta_ij for antenna 22
A23_delta20 = delta_ij(22,20,5.25) # delta_ij for antenna 23
A24_delta20 = delta_ij(23,20,5.25) # delta_ij for antenna 24
A25_delta20 = delta_ij(24,20,5.25) # delta_ij for antenna 25

RecA1Ey21 = np.roll(A1_Ey,int(round(A1_delta20)),axis=None)    # shifted e-field at ant1
RecA2Ey21 = np.roll(A2_Ey,int(round(A2_delta20)),axis=None)    # shifted e-field at ant2
RecA3Ey21 = np.roll(A3_Ey,int(round(A3_delta20)),axis=None)    # shifted e-field at ant3
RecA4Ey21 = np.roll(A4_Ey,int(round(A4_delta20)),axis=None)    # shifted e-field at ant4
RecA5Ey21 = np.roll(A5_Ey,int(round(A5_delta20)),axis=None)    # shifted e-field at ant5
RecA6Ey21 = np.roll(A6_Ey,int(round(A6_delta20)),axis=None)    # shifted e-field at ant6
RecA7Ey21 = np.roll(A7_Ey,int(round(A7_delta20)),axis=None)    # shifted e-field at ant7
RecA8Ey21 = np.roll(A8_Ey,int(round(A8_delta20)),axis=None)    # shifted e-field at ant8
RecA9Ey21 = np.roll(A9_Ey,int(round(A9_delta20)),axis=None)    # shifted e-field at ant9
RecA10Ey21 = np.roll(A10_Ey,int(round(A10_delta20)),axis=None)  # shifted e-field at ant10
RecA11Ey21 = np.roll(A11_Ey,int(round(A11_delta20)),axis=None)  # shifted e-field at ant11
RecA12Ey21 = np.roll(A12_Ey,int(round(A12_delta20)),axis=None)  # shifted e-field at ant12
RecA13Ey21 = np.roll(A13_Ey,int(round(A13_delta20)),axis=None)  # shifted e-field at ant13
RecA14Ey21 = np.roll(A14_Ey,int(round(A14_delta20)),axis=None)  # shifted e-field at ant14
RecA15Ey21 = np.roll(A15_Ey,int(round(A15_delta20)),axis=None)  # shifted e-field at ant15
RecA16Ey21 = np.roll(A16_Ey,int(round(A16_delta20)),axis=None)  # shifted e-field at ant16
RecA17Ey21 = np.roll(A17_Ey,int(round(A17_delta20)),axis=None)  # shifted e-field at ant17
RecA18Ey21 = np.roll(A18_Ey,int(round(A18_delta20)),axis=None)  # shifted e-field at ant18
RecA19Ey21 = np.roll(A19_Ey,int(round(A19_delta20)),axis=None) # shifted e-field at ant19
RecA20Ey21 = np.roll(A20_Ey,int(round(A20_delta20)),axis=None) # shifted e-field at ant20
RecA21Ey21 = np.roll(A21_Ey,int(round(A21_delta20)),axis=None) # shifted e-field at ant21
RecA22Ey21 = np.roll(A22_Ey,int(round(A22_delta20)),axis=None) # shifted e-field at ant22
RecA23Ey21 = np.roll(A23_Ey,int(round(A23_delta20)),axis=None) # shifted e-field at ant23
RecA24Ey21 = np.roll(A24_Ey,int(round(A24_delta20)),axis=None) # shifted e-field at ant24
RecA25Ey21 = np.roll(A25_Ey,int(round(A25_delta20)),axis=None) # shifted e-field at ant25


# In[118]:


# With respect to position (100m,0m) in the xy plane.
A1_delta21 = delta_ij(0,21,5.25) # delta_ij for antenna 1
A2_delta21 = delta_ij(1,21,5.25) # delta_ij for antenna 2
A3_delta21 = delta_ij(2,21,5.25) # delta_ij for antenna 3
A4_delta21 = delta_ij(3,21,5.25) # delta_ij for antenna 4
A5_delta21 = delta_ij(4,21,5.25) # delta_ij for antenna 5
A6_delta21 = delta_ij(5,21,5.25) # delta_ij for antenna 6
A7_delta21 = delta_ij(6,21,5.25) # delta_ij for antenna 7
A8_delta21 = delta_ij(7,21,5.25) # delta_ij for antenna 8
A9_delta21 = delta_ij(8,21,5.25) # delta_ij for antenna 9
A10_delta21 = delta_ij(9,21,5.25) # delta_ij for antenna 10
A11_delta21 = delta_ij(10,21,5.25) # delta_ij for antenna 11
A12_delta21 = delta_ij(11,21,5.25) # delta_ij for antenna 12
A13_delta21 = delta_ij(12,21,5.25) # delta_ij for antenna 13
A14_delta21 = delta_ij(13,21,5.25) # delta_ij for antenna 14
A15_delta21 = delta_ij(14,21,5.25) # delta_ij for antenna 15
A16_delta21 = delta_ij(15,21,5.25) # delta_ij for antenna 16
A17_delta21 = delta_ij(16,21,5.25) # delta_ij for antenna 17
A18_delta21 = delta_ij(17,21,5.25) # delta_ij for antenna 18
A19_delta21 = delta_ij(18,21,5.25) # delta_ij for antenna 19
A20_delta21 = delta_ij(19,21,5.25) # delta_ij for antenna 20
A21_delta21 = delta_ij(20,21,5.25) # delta_ij for antenna 21
A22_delta21 = delta_ij(21,21,5.25) # delta_ij for antenna 22
A23_delta21 = delta_ij(22,21,5.25) # delta_ij for antenna 23
A24_delta21 = delta_ij(23,21,5.25) # delta_ij for antenna 24
A25_delta21 = delta_ij(24,21,5.25) # delta_ij for antenna 25

RecA1Ey22 = np.roll(A1_Ey,int(round(A1_delta21)),axis=None)    # shifted e-field at ant1
RecA2Ey22 = np.roll(A2_Ey,int(round(A2_delta21)),axis=None)    # shifted e-field at ant2
RecA3Ey22 = np.roll(A3_Ey,int(round(A3_delta21)),axis=None)    # shifted e-field at ant3
RecA4Ey22 = np.roll(A4_Ey,int(round(A4_delta21)),axis=None)    # shifted e-field at ant4
RecA5Ey22 = np.roll(A5_Ey,int(round(A5_delta21)),axis=None)    # shifted e-field at ant5
RecA6Ey22 = np.roll(A6_Ey,int(round(A6_delta21)),axis=None)    # shifted e-field at ant6
RecA7Ey22 = np.roll(A7_Ey,int(round(A7_delta21)),axis=None)    # shifted e-field at ant7
RecA8Ey22 = np.roll(A8_Ey,int(round(A8_delta21)),axis=None)    # shifted e-field at ant8
RecA9Ey22 = np.roll(A9_Ey,int(round(A9_delta21)),axis=None)    # shifted e-field at ant9
RecA10Ey22 = np.roll(A10_Ey,int(round(A10_delta21)),axis=None)  # shifted e-field at ant10
RecA11Ey22 = np.roll(A11_Ey,int(round(A11_delta21)),axis=None)  # shifted e-field at ant11
RecA12Ey22 = np.roll(A12_Ey,int(round(A12_delta21)),axis=None)  # shifted e-field at ant12
RecA13Ey22 = np.roll(A13_Ey,int(round(A13_delta21)),axis=None)  # shifted e-field at ant13
RecA14Ey22 = np.roll(A14_Ey,int(round(A14_delta21)),axis=None)  # shifted e-field at ant14
RecA15Ey22 = np.roll(A15_Ey,int(round(A15_delta21)),axis=None)  # shifted e-field at ant15
RecA16Ey22 = np.roll(A16_Ey,int(round(A16_delta21)),axis=None)  # shifted e-field at ant16
RecA17Ey22 = np.roll(A17_Ey,int(round(A17_delta21)),axis=None)  # shifted e-field at ant17
RecA18Ey22 = np.roll(A18_Ey,int(round(A18_delta21)),axis=None)  # shifted e-field at ant18
RecA19Ey22 = np.roll(A19_Ey,int(round(A19_delta21)),axis=None) # shifted e-field at ant19
RecA20Ey22 = np.roll(A20_Ey,int(round(A20_delta21)),axis=None) # shifted e-field at ant20
RecA21Ey22 = np.roll(A21_Ey,int(round(A21_delta21)),axis=None) # shifted e-field at ant21
RecA22Ey22 = np.roll(A22_Ey,int(round(A22_delta21)),axis=None) # shifted e-field at ant22
RecA23Ey22 = np.roll(A23_Ey,int(round(A23_delta21)),axis=None) # shifted e-field at ant23
RecA24Ey22 = np.roll(A24_Ey,int(round(A24_delta21)),axis=None) # shifted e-field at ant24
RecA25Ey22 = np.roll(A25_Ey,int(round(A25_delta21)),axis=None) # shifted e-field at ant25


# In[119]:


# With respect to position (100m,0m) in the xy plane.
A1_delta22 = delta_ij(0,22,5.25) # delta_ij for antenna 1
A2_delta22 = delta_ij(1,22,5.25) # delta_ij for antenna 2
A3_delta22 = delta_ij(2,22,5.25) # delta_ij for antenna 3
A4_delta22 = delta_ij(3,22,5.25) # delta_ij for antenna 4
A5_delta22 = delta_ij(4,22,5.25) # delta_ij for antenna 5
A6_delta22 = delta_ij(5,22,5.25) # delta_ij for antenna 6
A7_delta22 = delta_ij(6,22,5.25) # delta_ij for antenna 7
A8_delta22 = delta_ij(7,22,5.25) # delta_ij for antenna 8
A9_delta22 = delta_ij(8,22,5.25) # delta_ij for antenna 9
A10_delta22 = delta_ij(9,22,5.25) # delta_ij for antenna 10
A11_delta22 = delta_ij(10,22,5.25) # delta_ij for antenna 11
A12_delta22 = delta_ij(11,22,5.25) # delta_ij for antenna 12
A13_delta22 = delta_ij(12,22,5.25) # delta_ij for antenna 13
A14_delta22 = delta_ij(13,22,5.25) # delta_ij for antenna 14
A15_delta22 = delta_ij(14,22,5.25) # delta_ij for antenna 15
A16_delta22 = delta_ij(15,22,5.25) # delta_ij for antenna 16
A17_delta22 = delta_ij(16,22,5.25) # delta_ij for antenna 17
A18_delta22 = delta_ij(17,22,5.25) # delta_ij for antenna 18
A19_delta22 = delta_ij(18,22,5.25) # delta_ij for antenna 19
A20_delta22 = delta_ij(19,22,5.25) # delta_ij for antenna 20
A21_delta22 = delta_ij(20,22,5.25) # delta_ij for antenna 21
A22_delta22 = delta_ij(21,22,5.25) # delta_ij for antenna 22
A23_delta22 = delta_ij(22,22,5.25) # delta_ij for antenna 23
A24_delta22 = delta_ij(23,22,5.25) # delta_ij for antenna 24
A25_delta22 = delta_ij(24,22,5.25) # delta_ij for antenna 25

RecA1Ey23 = np.roll(A1_Ey,int(round(A1_delta22)),axis=None)    # shifted e-field at ant1
RecA2Ey23 = np.roll(A2_Ey,int(round(A2_delta22)),axis=None)    # shifted e-field at ant2
RecA3Ey23 = np.roll(A3_Ey,int(round(A3_delta22)),axis=None)    # shifted e-field at ant3
RecA4Ey23 = np.roll(A4_Ey,int(round(A4_delta22)),axis=None)    # shifted e-field at ant4
RecA5Ey23 = np.roll(A5_Ey,int(round(A5_delta22)),axis=None)    # shifted e-field at ant5
RecA6Ey23 = np.roll(A6_Ey,int(round(A6_delta22)),axis=None)    # shifted e-field at ant6
RecA7Ey23 = np.roll(A7_Ey,int(round(A7_delta22)),axis=None)    # shifted e-field at ant7
RecA8Ey23 = np.roll(A8_Ey,int(round(A8_delta22)),axis=None)    # shifted e-field at ant8
RecA9Ey23 = np.roll(A9_Ey,int(round(A9_delta22)),axis=None)    # shifted e-field at ant9
RecA10Ey23 = np.roll(A10_Ey,int(round(A10_delta22)),axis=None)  # shifted e-field at ant10
RecA11Ey23 = np.roll(A11_Ey,int(round(A11_delta22)),axis=None)  # shifted e-field at ant11
RecA12Ey23 = np.roll(A12_Ey,int(round(A12_delta22)),axis=None)  # shifted e-field at ant12
RecA13Ey23 = np.roll(A13_Ey,int(round(A13_delta22)),axis=None)  # shifted e-field at ant13
RecA14Ey23 = np.roll(A14_Ey,int(round(A14_delta22)),axis=None)  # shifted e-field at ant14
RecA15Ey23 = np.roll(A15_Ey,int(round(A15_delta22)),axis=None)  # shifted e-field at ant15
RecA16Ey23 = np.roll(A16_Ey,int(round(A16_delta22)),axis=None)  # shifted e-field at ant16
RecA17Ey23 = np.roll(A17_Ey,int(round(A17_delta22)),axis=None)  # shifted e-field at ant17
RecA18Ey23 = np.roll(A18_Ey,int(round(A18_delta22)),axis=None)  # shifted e-field at ant18
RecA19Ey23 = np.roll(A19_Ey,int(round(A19_delta22)),axis=None) # shifted e-field at ant19
RecA20Ey23 = np.roll(A20_Ey,int(round(A20_delta22)),axis=None) # shifted e-field at ant20
RecA21Ey23 = np.roll(A21_Ey,int(round(A21_delta22)),axis=None) # shifted e-field at ant21
RecA22Ey23 = np.roll(A22_Ey,int(round(A22_delta22)),axis=None) # shifted e-field at ant22
RecA23Ey23 = np.roll(A23_Ey,int(round(A23_delta22)),axis=None) # shifted e-field at ant23
RecA24Ey23 = np.roll(A24_Ey,int(round(A24_delta22)),axis=None) # shifted e-field at ant24
RecA25Ey23 = np.roll(A25_Ey,int(round(A25_delta22)),axis=None) # shifted e-field at ant25


# In[120]:


# With respect to position (100m,0m) in the xy plane.
A1_delta23 = delta_ij(0,23,5.25) # delta_ij for antenna 1
A2_delta23 = delta_ij(1,23,5.25) # delta_ij for antenna 2
A3_delta23 = delta_ij(2,23,5.25) # delta_ij for antenna 3
A4_delta23 = delta_ij(3,23,5.25) # delta_ij for antenna 4
A5_delta23 = delta_ij(4,23,5.25) # delta_ij for antenna 5
A6_delta23 = delta_ij(5,23,5.25) # delta_ij for antenna 6
A7_delta23 = delta_ij(6,23,5.25) # delta_ij for antenna 7
A8_delta23 = delta_ij(7,23,5.25) # delta_ij for antenna 8
A9_delta23 = delta_ij(8,23,5.25) # delta_ij for antenna 9
A10_delta23 = delta_ij(9,23,5.25) # delta_ij for antenna 10
A11_delta23 = delta_ij(10,23,5.25) # delta_ij for antenna 11
A12_delta23 = delta_ij(11,23,5.25) # delta_ij for antenna 12
A13_delta23 = delta_ij(12,23,5.25) # delta_ij for antenna 13
A14_delta23 = delta_ij(13,23,5.25) # delta_ij for antenna 14
A15_delta23 = delta_ij(14,23,5.25) # delta_ij for antenna 15
A16_delta23 = delta_ij(15,23,5.25) # delta_ij for antenna 16
A17_delta23 = delta_ij(16,23,5.25) # delta_ij for antenna 17
A18_delta23 = delta_ij(17,23,5.25) # delta_ij for antenna 18
A19_delta23 = delta_ij(18,23,5.25) # delta_ij for antenna 19
A20_delta23 = delta_ij(19,23,5.25) # delta_ij for antenna 20
A21_delta23 = delta_ij(20,23,5.25) # delta_ij for antenna 21
A22_delta23 = delta_ij(21,23,5.25) # delta_ij for antenna 22
A23_delta23 = delta_ij(22,23,5.25) # delta_ij for antenna 23
A24_delta23 = delta_ij(23,23,5.25) # delta_ij for antenna 24
A25_delta23 = delta_ij(24,23,5.25) # delta_ij for antenna 25

RecA1Ey24 = np.roll(A1_Ey,int(round(A1_delta23)),axis=None)    # shifted e-field at ant1
RecA2Ey24 = np.roll(A2_Ey,int(round(A2_delta23)),axis=None)    # shifted e-field at ant2
RecA3Ey24 = np.roll(A3_Ey,int(round(A3_delta23)),axis=None)    # shifted e-field at ant3
RecA4Ey24 = np.roll(A4_Ey,int(round(A4_delta23)),axis=None)    # shifted e-field at ant4
RecA5Ey24 = np.roll(A5_Ey,int(round(A5_delta23)),axis=None)    # shifted e-field at ant5
RecA6Ey24 = np.roll(A6_Ey,int(round(A6_delta23)),axis=None)    # shifted e-field at ant6
RecA7Ey24 = np.roll(A7_Ey,int(round(A7_delta23)),axis=None)    # shifted e-field at ant7
RecA8Ey24 = np.roll(A8_Ey,int(round(A8_delta23)),axis=None)    # shifted e-field at ant8
RecA9Ey24 = np.roll(A9_Ey,int(round(A9_delta23)),axis=None)    # shifted e-field at ant9
RecA10Ey24 = np.roll(A10_Ey,int(round(A10_delta23)),axis=None)  # shifted e-field at ant10
RecA11Ey24 = np.roll(A11_Ey,int(round(A11_delta23)),axis=None)  # shifted e-field at ant11
RecA12Ey24 = np.roll(A12_Ey,int(round(A12_delta23)),axis=None)  # shifted e-field at ant12
RecA13Ey24 = np.roll(A13_Ey,int(round(A13_delta23)),axis=None)  # shifted e-field at ant13
RecA14Ey24 = np.roll(A14_Ey,int(round(A14_delta23)),axis=None)  # shifted e-field at ant14
RecA15Ey24 = np.roll(A15_Ey,int(round(A15_delta23)),axis=None)  # shifted e-field at ant15
RecA16Ey24 = np.roll(A16_Ey,int(round(A16_delta23)),axis=None)  # shifted e-field at ant16
RecA17Ey24 = np.roll(A17_Ey,int(round(A17_delta23)),axis=None)  # shifted e-field at ant17
RecA18Ey24 = np.roll(A18_Ey,int(round(A18_delta23)),axis=None)  # shifted e-field at ant18
RecA19Ey24 = np.roll(A19_Ey,int(round(A19_delta23)),axis=None) # shifted e-field at ant19
RecA20Ey24 = np.roll(A20_Ey,int(round(A20_delta23)),axis=None) # shifted e-field at ant20
RecA21Ey24 = np.roll(A21_Ey,int(round(A21_delta23)),axis=None) # shifted e-field at ant21
RecA22Ey24 = np.roll(A22_Ey,int(round(A22_delta23)),axis=None) # shifted e-field at ant22
RecA23Ey24 = np.roll(A23_Ey,int(round(A23_delta23)),axis=None) # shifted e-field at ant23
RecA24Ey24 = np.roll(A24_Ey,int(round(A24_delta23)),axis=None) # shifted e-field at ant24
RecA25Ey24 = np.roll(A25_Ey,int(round(A25_delta23)),axis=None) # shifted e-field at ant25


# In[121]:


# With respect to position (100m,0m) in the xy plane.
A1_delta24 = delta_ij(0,24,5.25) # delta_ij for antenna 1
A2_delta24 = delta_ij(1,24,5.25) # delta_ij for antenna 2
A3_delta24 = delta_ij(2,24,5.25) # delta_ij for antenna 3
A4_delta24 = delta_ij(3,24,5.25) # delta_ij for antenna 4
A5_delta24 = delta_ij(4,24,5.25) # delta_ij for antenna 5
A6_delta24 = delta_ij(5,24,5.25) # delta_ij for antenna 6
A7_delta24 = delta_ij(6,24,5.25) # delta_ij for antenna 7
A8_delta24 = delta_ij(7,24,5.25) # delta_ij for antenna 8
A9_delta24 = delta_ij(8,24,5.25) # delta_ij for antenna 9
A10_delta24 = delta_ij(9,24,5.25) # delta_ij for antenna 10
A11_delta24 = delta_ij(10,24,5.25) # delta_ij for antenna 11
A12_delta24 = delta_ij(11,24,5.25) # delta_ij for antenna 12
A13_delta24 = delta_ij(12,24,5.25) # delta_ij for antenna 13
A14_delta24 = delta_ij(13,24,5.25) # delta_ij for antenna 14
A15_delta24 = delta_ij(14,24,5.25) # delta_ij for antenna 15
A16_delta24 = delta_ij(15,24,5.25) # delta_ij for antenna 16
A17_delta24 = delta_ij(16,24,5.25) # delta_ij for antenna 17
A18_delta24 = delta_ij(17,24,5.25) # delta_ij for antenna 18
A19_delta24 = delta_ij(18,24,5.25) # delta_ij for antenna 19
A20_delta24 = delta_ij(19,24,5.25) # delta_ij for antenna 20
A21_delta24 = delta_ij(20,24,5.25) # delta_ij for antenna 21
A22_delta24 = delta_ij(21,24,5.25) # delta_ij for antenna 22
A23_delta24 = delta_ij(22,24,5.25) # delta_ij for antenna 23
A24_delta24 = delta_ij(23,24,5.25) # delta_ij for antenna 24
A25_delta24 = delta_ij(24,24,5.25) # delta_ij for antenna 25

RecA1Ey25 = np.roll(A1_Ey,int(round(A1_delta24)),axis=None)    # shifted e-field at ant1
RecA2Ey25 = np.roll(A2_Ey,int(round(A2_delta24)),axis=None)    # shifted e-field at ant2
RecA3Ey25 = np.roll(A3_Ey,int(round(A3_delta24)),axis=None)    # shifted e-field at ant3
RecA4Ey25 = np.roll(A4_Ey,int(round(A4_delta24)),axis=None)    # shifted e-field at ant4
RecA5Ey25 = np.roll(A5_Ey,int(round(A5_delta24)),axis=None)    # shifted e-field at ant5
RecA6Ey25 = np.roll(A6_Ey,int(round(A6_delta24)),axis=None)    # shifted e-field at ant6
RecA7Ey25 = np.roll(A7_Ey,int(round(A7_delta24)),axis=None)    # shifted e-field at ant7
RecA8Ey25 = np.roll(A8_Ey,int(round(A8_delta24)),axis=None)    # shifted e-field at ant8
RecA9Ey25 = np.roll(A9_Ey,int(round(A9_delta24)),axis=None)    # shifted e-field at ant9
RecA10Ey25 = np.roll(A10_Ey,int(round(A10_delta24)),axis=None)  # shifted e-field at ant10
RecA11Ey25 = np.roll(A11_Ey,int(round(A11_delta24)),axis=None)  # shifted e-field at ant11
RecA12Ey25 = np.roll(A12_Ey,int(round(A12_delta24)),axis=None)  # shifted e-field at ant12
RecA13Ey25 = np.roll(A13_Ey,int(round(A13_delta24)),axis=None)  # shifted e-field at ant13
RecA14Ey25 = np.roll(A14_Ey,int(round(A14_delta24)),axis=None)  # shifted e-field at ant14
RecA15Ey25 = np.roll(A15_Ey,int(round(A15_delta24)),axis=None)  # shifted e-field at ant15
RecA16Ey25 = np.roll(A16_Ey,int(round(A16_delta24)),axis=None)  # shifted e-field at ant16
RecA17Ey25 = np.roll(A17_Ey,int(round(A17_delta24)),axis=None)  # shifted e-field at ant17
RecA18Ey25 = np.roll(A18_Ey,int(round(A18_delta24)),axis=None)  # shifted e-field at ant18
RecA19Ey25 = np.roll(A19_Ey,int(round(A19_delta24)),axis=None) # shifted e-field at ant19
RecA20Ey25 = np.roll(A20_Ey,int(round(A20_delta24)),axis=None) # shifted e-field at ant20
RecA21Ey25 = np.roll(A21_Ey,int(round(A21_delta24)),axis=None) # shifted e-field at ant21
RecA22Ey25 = np.roll(A22_Ey,int(round(A22_delta24)),axis=None) # shifted e-field at ant22
RecA23Ey25 = np.roll(A23_Ey,int(round(A23_delta24)),axis=None) # shifted e-field at ant23
RecA24Ey25 = np.roll(A24_Ey,int(round(A24_delta24)),axis=None) # shifted e-field at ant24
RecA25Ey25 = np.roll(A25_Ey,int(round(A25_delta24)),axis=None) # shifted e-field at ant25


# In[127]:


# the normalized values of power for each reference point, where the number next to j corresponds to the 
# reference point in question
Sj1n = (RecA1Ey1 + RecA2Ey1 + RecA3Ey1 + RecA4Ey1 + RecA5Ey1 + RecA6Ey1 + RecA7Ey1 + RecA8Ey1 + RecA9Ey1 + RecA10Ey1 + RecA11Ey1 + RecA12Ey1 + RecA13Ey1 + RecA14Ey1 + RecA15Ey1 + RecA16Ey1 + RecA17Ey1 + RecA18Ey1 + RecA19Ey1 + RecA20Ey1 + RecA21Ey1 + RecA22Ey1 + RecA23Ey1 + RecA24Ey1+ RecA25Ey1)**2  
Sj2n = (RecA1Ey2 + RecA2Ey2 + RecA3Ey2 + RecA4Ey2 + RecA5Ey2 + RecA6Ey2 + RecA7Ey12 + RecA8Ey2 + RecA9Ey2 + RecA10Ey2 + RecA11Ey2 + RecA12Ey2 + RecA13Ey2 + RecA14Ey2 + RecA15Ey2 + RecA16Ey2 + RecA17Ey2 + RecA18Ey2 + RecA19Ey2 + RecA20Ey2 + RecA21Ey2 + RecA22Ey2 + RecA23Ey2 + RecA24Ey2 + RecA25Ey2)**2  
Sj3n = (RecA1Ey3 + RecA2Ey3 + RecA3Ey3 + RecA4Ey3 + RecA5Ey3 + RecA6Ey3 + RecA7Ey12 + RecA8Ey3 + RecA9Ey3 + RecA10Ey3 + RecA11Ey3 + RecA12Ey3 + RecA13Ey3 + RecA14Ey3 + RecA15Ey3 + RecA16Ey3 + RecA17Ey3 + RecA18Ey3 + RecA19Ey3 + RecA20Ey3 + RecA21Ey3 + RecA22Ey3 + RecA23Ey3 + RecA24Ey3 + RecA25Ey3)**2
Sj4n = (RecA1Ey4 + RecA2Ey4 + RecA3Ey4 + RecA4Ey4 + RecA5Ey4 + RecA6Ey4 + RecA7Ey12 + RecA8Ey4 + RecA9Ey4 + RecA10Ey4 + RecA11Ey4 + RecA12Ey4 + RecA13Ey4 + RecA14Ey4 + RecA15Ey4 + RecA16Ey4 + RecA17Ey4 + RecA18Ey4 + RecA19Ey4 + RecA20Ey4 + RecA21Ey4 + RecA22Ey4 + RecA23Ey4 + RecA24Ey4 + RecA25Ey4)**2
Sj5n = (RecA1Ey5 + RecA2Ey5 + RecA3Ey5 + RecA4Ey5 + RecA5Ey5 + RecA6Ey5 + RecA7Ey12 + RecA8Ey5 + RecA9Ey5 + RecA10Ey5 + RecA11Ey5 + RecA12Ey5 + RecA13Ey5 + RecA14Ey5 + RecA15Ey5 + RecA16Ey5 + RecA17Ey5 + RecA18Ey5 + RecA19Ey5 + RecA20Ey5 + RecA21Ey5 + RecA22Ey5 + RecA23Ey5 + RecA24Ey5 + RecA25Ey5)**2
Sj6n = (RecA1Ey6 + RecA2Ey6 + RecA3Ey6 + RecA4Ey6 + RecA5Ey6 + RecA6Ey6 + RecA7Ey12 + RecA8Ey6 + RecA9Ey6 + RecA10Ey6 + RecA11Ey6 + RecA12Ey6 + RecA13Ey6 + RecA14Ey6 + RecA15Ey6 + RecA16Ey6 + RecA17Ey6 + RecA18Ey6 + RecA19Ey6 + RecA20Ey6 + RecA21Ey6 + RecA22Ey6 + RecA23Ey6 + RecA24Ey6 + RecA25Ey6)**2
Sj7n = (RecA1Ey7 + RecA2Ey7 + RecA3Ey7 + RecA4Ey7 + RecA5Ey7 + RecA6Ey7 + RecA7Ey12 + RecA8Ey7 + RecA9Ey7 + RecA10Ey7 + RecA11Ey7 + RecA12Ey7 + RecA13Ey7 + RecA14Ey7 + RecA15Ey7 + RecA16Ey7 + RecA17Ey7 + RecA18Ey7 + RecA19Ey7 + RecA20Ey7 + RecA21Ey7 + RecA22Ey7 + RecA23Ey7 + RecA24Ey7 + RecA25Ey7)**2
Sj8n = (RecA1Ey8 + RecA2Ey8 + RecA3Ey8 + RecA4Ey8 + RecA5Ey8 + RecA6Ey8 + RecA7Ey12 + RecA8Ey8 + RecA9Ey8 + RecA10Ey8+ RecA11Ey8 + RecA12Ey8 + RecA13Ey8 + RecA14Ey8 + RecA15Ey8 + RecA16Ey8 + RecA17Ey8 + RecA18Ey8 + RecA19Ey8 + RecA20Ey8 + RecA21Ey8 + RecA22Ey8 + RecA23Ey8 + RecA24Ey8 + RecA25Ey8)**2
Sj9n = (RecA1Ey9 + RecA2Ey9 + RecA3Ey9 + RecA4Ey9 + RecA5Ey9 + RecA6Ey9 + RecA7Ey9 + RecA8Ey9 + RecA9Ey9 + RecA10Ey9 + RecA11Ey9 + RecA12Ey9 + RecA13Ey9 + RecA14Ey9 + RecA15Ey9 + RecA16Ey9 + RecA17Ey9 + RecA18Ey9 + RecA19Ey9 + RecA20Ey9 + RecA21Ey9 + RecA22Ey9 + RecA23Ey9 + RecA24Ey9 + RecA25Ey9)**2
Sj10n = (RecA1Ey10 + RecA2Ey10 + RecA3Ey10 + RecA4Ey10 + RecA5Ey10 + RecA6Ey10 + RecA7Ey10 + RecA8Ey10 + RecA9Ey10 + RecA10Ey10 + RecA11Ey10 + RecA12Ey10 + RecA13Ey10 + RecA14Ey10 + RecA15Ey10 + RecA16Ey10 + RecA17Ey10 + RecA18Ey10 + RecA19Ey10 + RecA20Ey10 + RecA21Ey10 + RecA22Ey10 + RecA23Ey10 + RecA24Ey10 + RecA25Ey10)**2  
Sj11n = (RecA1Ey11 + RecA2Ey11 + RecA3Ey11 + RecA4Ey11 + RecA5Ey11 + RecA6Ey11 + RecA7Ey11 + RecA8Ey11 + RecA9Ey11 + RecA10Ey11 + RecA11Ey11 + RecA12Ey11 + RecA13Ey11 + RecA14Ey11 + RecA15Ey11 + RecA16Ey11 + RecA17Ey11 + RecA18Ey11 + RecA19Ey11 + RecA20Ey11 + RecA21Ey11 + RecA22Ey11 + RecA23Ey11 + RecA24Ey11 + RecA25Ey11)**2 
Sj12n = (RecA1Ey12 + RecA2Ey12 + RecA3Ey12 + RecA4Ey12 + RecA5Ey12 + RecA6Ey12 + RecA7Ey12 + RecA8Ey12 + RecA9Ey12 + RecA10Ey12 + RecA11Ey12 + RecA12Ey12 + RecA13Ey12 + RecA14Ey12 + RecA15Ey12 + RecA16Ey12 + RecA17Ey12 + RecA18Ey12 + RecA19Ey12 + RecA20Ey12 + RecA21Ey12 + RecA22Ey12 + RecA23Ey12 + RecA24Ey12 + RecA25Ey12)**2 
Sj13n = (RecA1Ey13 + RecA2Ey13 + RecA3Ey13 + RecA4Ey13 + RecA5Ey13 + RecA6Ey13 + RecA7Ey13 + RecA8Ey13 + RecA9Ey13 + RecA10Ey13 + RecA11Ey13 + RecA12Ey13 + RecA13Ey13 + RecA14Ey13 + RecA15Ey13 + RecA16Ey13 + RecA17Ey13 + RecA18Ey13 + RecA19Ey13 + RecA20Ey13 + RecA21Ey13 + RecA22Ey13 + RecA23Ey13 + RecA24Ey13 + RecA25Ey13)**2 
Sj14n = (RecA1Ey14 + RecA2Ey14 + RecA3Ey14 + RecA4Ey14 + RecA5Ey14 + RecA6Ey14 + RecA7Ey14 + RecA8Ey14 + RecA9Ey14 + RecA10Ey14 + RecA11Ey14 + RecA12Ey14 + RecA13Ey14 + RecA14Ey14 + RecA15Ey14 + RecA16Ey14 + RecA17Ey14 + RecA18Ey14 + RecA19Ey14 + RecA20Ey14 + RecA21Ey14 + RecA22Ey14 + RecA23Ey14 + RecA24Ey14 + RecA25Ey14)**2 
Sj15n = (RecA1Ey15 + RecA2Ey15 + RecA3Ey15 + RecA4Ey15 + RecA5Ey15 + RecA6Ey16 + RecA7Ey15 + RecA8Ey15 + RecA9Ey15 + RecA10Ey15 + RecA11Ey15 + RecA12Ey15 + RecA13Ey15 + RecA14Ey15 + RecA15Ey15 + RecA16Ey15 + RecA17Ey15 + RecA18Ey15 + RecA19Ey15 + RecA20Ey15 + RecA21Ey15 + RecA22Ey15 + RecA23Ey15 + RecA24Ey15 + RecA25Ey15)**2 
Sj16n = (RecA1Ey16 + RecA2Ey16 + RecA3Ey16 + RecA4Ey16 + RecA5Ey16 + RecA6Ey16 + RecA7Ey16 + RecA8Ey16 + RecA9Ey16 + RecA10Ey16 + RecA11Ey16 + RecA12Ey16 + RecA13Ey16 + RecA14Ey16 + RecA15Ey16 + RecA16Ey16 + RecA17Ey16 + RecA18Ey16 + RecA19Ey16 + RecA20Ey16 + RecA21Ey16 + RecA22Ey16 + RecA23Ey16 + RecA24Ey16 + RecA25Ey16)**2
Sj17n = (RecA1Ey17 + RecA2Ey17 + RecA3Ey17 + RecA4Ey17 + RecA5Ey17 + RecA6Ey17 + RecA7Ey17 + RecA8Ey17 + RecA9Ey17 + RecA10Ey17 + RecA11Ey17 + RecA12Ey17 + RecA13Ey17 + RecA14Ey17 + RecA15Ey17 + RecA16Ey17 + RecA17Ey17 + RecA18Ey17 + RecA19Ey17 + RecA20Ey17 + RecA21Ey17 + RecA22Ey17 + RecA23Ey17 + RecA24Ey17 + RecA25Ey17)**2
Sj18n = (RecA1Ey18 + RecA2Ey18 + RecA3Ey18 + RecA4Ey18 + RecA5Ey18 + RecA6Ey18 + RecA7Ey18 + RecA8Ey18 + RecA9Ey18 + RecA10Ey18 + RecA11Ey18 + RecA12Ey18 + RecA13Ey18 + RecA14Ey18 + RecA15Ey18 + RecA16Ey18 + RecA17Ey18 + RecA18Ey18 + RecA19Ey18 + RecA20Ey18 + RecA21Ey18 + RecA22Ey18 + RecA23Ey18 + RecA24Ey18 + RecA25Ey18)**2
Sj19n = (RecA1Ey19 + RecA2Ey19 + RecA3Ey19 + RecA4Ey19 + RecA5Ey19 + RecA6Ey19 + RecA7Ey19 + RecA8Ey19 + RecA9Ey19 + RecA10Ey19 + RecA11Ey19 + RecA12Ey19 + RecA13Ey19 + RecA14Ey19 + RecA15Ey19 + RecA16Ey19 + RecA17Ey19 + RecA18Ey19 + RecA19Ey19 + RecA20Ey19 + RecA21Ey19 + RecA22Ey19 + RecA23Ey19 + RecA24Ey19 + RecA25Ey19)**2
Sj20n = (RecA1Ey20 + RecA2Ey20 + RecA3Ey20 + RecA4Ey20 + RecA5Ey20 + RecA6Ey20 + RecA7Ey20 + RecA8Ey20 + RecA9Ey20 + RecA10Ey20 + RecA11Ey20 + RecA12Ey20 + RecA13Ey20 + RecA14Ey20 + RecA15Ey20 + RecA16Ey20 + RecA17Ey20 + RecA18Ey20 + RecA19Ey20 + RecA20Ey20 + RecA21Ey20 + RecA22Ey20 + RecA23Ey20 + RecA24Ey20 + RecA25Ey20)**2
Sj21n = (RecA1Ey21 + RecA2Ey21 + RecA3Ey21 + RecA4Ey21 + RecA5Ey21 + RecA6Ey21 + RecA7Ey21 + RecA8Ey21 + RecA9Ey21 + RecA10Ey21 + RecA11Ey21 + RecA12Ey21 + RecA13Ey21 + RecA14Ey21 + RecA15Ey21 + RecA16Ey21 + RecA17Ey21 + RecA18Ey21 + RecA19Ey21 + RecA20Ey21 + RecA21Ey21 + RecA22Ey21 + RecA23Ey21 + RecA24Ey21 + RecA25Ey21)**2
Sj22n = (RecA1Ey22 + RecA2Ey22 + RecA3Ey22 + RecA4Ey22 + RecA5Ey22 + RecA6Ey22 + RecA7Ey22 + RecA8Ey22 + RecA9Ey22 + RecA10Ey22 + RecA11Ey22 + RecA12Ey22 + RecA13Ey22 + RecA14Ey22 + RecA15Ey22 + RecA16Ey22 + RecA17Ey22 + RecA18Ey22 + RecA19Ey22 + RecA20Ey22 + RecA21Ey22 + RecA22Ey22 + RecA23Ey22 + RecA24Ey22 + RecA25Ey22)**2
Sj23n = (RecA1Ey23 + RecA2Ey23 + RecA3Ey23 + RecA4Ey23 + RecA5Ey23 + RecA6Ey23 + RecA7Ey23 + RecA8Ey23 + RecA9Ey23 + RecA10Ey23 + RecA11Ey23 + RecA12Ey23 + RecA13Ey23 + RecA14Ey23 + RecA15Ey23 + RecA16Ey23 + RecA17Ey23 + RecA18Ey23 + RecA19Ey23 + RecA20Ey23 + RecA21Ey23 + RecA22Ey23 + RecA23Ey23 + RecA24Ey23 + RecA25Ey23)**2
Sj24n = (RecA1Ey24 + RecA2Ey24 + RecA3Ey24 + RecA4Ey24 + RecA5Ey24 + RecA6Ey24 + RecA7Ey24 + RecA8Ey24 + RecA9Ey24 + RecA10Ey24 + RecA11Ey24 + RecA12Ey24 + RecA13Ey24 + RecA14Ey24 + RecA15Ey24 + RecA16Ey24 + RecA17Ey24 + RecA18Ey24 + RecA19Ey24 + RecA20Ey24 + RecA21Ey24 + RecA22Ey24 + RecA23Ey24 + RecA24Ey24 + RecA25Ey24)**2
Sj25n = (RecA1Ey25 + RecA2Ey25 + RecA3Ey25 + RecA4Ey25 + RecA5Ey25 + RecA6Ey25 + RecA7Ey25 + RecA8Ey25 + RecA9Ey25 + RecA10Ey25 + RecA11Ey25 + RecA12Ey25 + RecA13Ey25 + RecA14Ey25 + RecA15Ey25 + RecA16Ey25 + RecA17Ey25 + RecA18Ey25 + RecA19Ey25 + RecA20Ey25 + RecA21Ey25 + RecA22Ey25 + RecA23Ey25 + RecA24Ey25 + RecA25Ey25)**2


# In[128]:


max(Sj1n)


# In[133]:


Sjlist = [max(Sj1n),max(Sj2n),max(Sj3n),max(Sj4n),max(Sj5n),max(Sj6n),max(Sj7n),max(Sj8n),max(Sj9n),max(Sj10n),max(Sj11n),max(Sj12n),max(Sj13n),max(Sj14n),max(Sj15n),max(Sj16n),max(Sj17n),max(Sj18n),max(Sj19n),max(Sj20n),max(Sj21n),max(Sj22n),max(Sj23n),max(Sj24n),max(Sj25n)]
print(len(Sjlist))
print(len(xref))
print(len(yref))


# In[134]:


X, Y = np.meshgrid(xref, yref)
Z = Sjlist

plt.contour(X, Y, Z, colors='black');


# In[130]:


fig = plt.figure(figsize=(12,8), dpi=80)
ax = plt.subplot(111)
for i in range(25):
    plt.plot(wv17['t'][i], wv17['Ey'][i], label="A%d"%(i+1))

#plt.plot(time,S_jsum, label = "Sj")
plt.ylim(-0.0001,0.0001)
plt.xlim(-100,2000)
plt.xlabel("Time (ns)", fontsize=16)
plt.ylabel("Ey", fontsize=16)
plt.title("Ey over Time", fontsize = 20)
plt.legend(loc="lower right", frameon=True)
plt.show()


# In[129]:


fig = plt.figure(figsize=(12,8), dpi=80)
ax = plt.subplot(111)
plt.plot(time1,RecA1Ey, label = "A1")
plt.plot(time1,RecA2Ey, label = "A2")
plt.plot(time1,RecA3Ey, label = "A3")
plt.plot(time1,RecA4Ey, label = "A4")
plt.plot(time1,RecA5Ey, label = "A5")
plt.plot(time1,RecA6Ey, label = "A6")
plt.plot(time1,RecA7Ey, label = "A7")
plt.plot(time1,RecA8Ey, label = "A8")
plt.plot(time1,RecA9Ey, label = "A9")
plt.plot(time1,RecA10Ey, label = "A10")
plt.plot(time1,RecA11Ey, label = "A11")
plt.plot(time1,RecA12Ey, label = "A12")
plt.plot(time1,RecA13Ey, label = "A13")
plt.plot(time1,RecA14Ey, label = "A14")
plt.plot(time1,RecA15Ey, label = "A15")
plt.plot(time1,RecA16Ey, label = "A16")
plt.plot(time1,RecA17Ey, label = "A17")
plt.plot(time1,RecA18Ey, label = "A18")
plt.plot(time1,RecA19Ey, label = "A19")
plt.plot(time1,RecA20Ey, label = "A20")
plt.plot(time1,RecA21Ey, label = "A21")
plt.plot(time1,RecA22Ey, label = "A22")
plt.plot(time1,RecA23Ey, label = "A23")
plt.plot(time1,RecA24Ey, label = "A24")
plt.plot(time1,RecA25Ey, label = "A25")
#plt.plot(time,S_jsum, label = "Sj")
#plt.ylim(-0.0002,0.0002)
plt.xlim(5250,5800)
plt.xlabel("Time (ns)",fontsize=16)
plt.ylabel("Ey",fontsize=16)
plt.title("Shifted Ey over Time",fontsize=20)
plt.legend(loc="lower right", frameon=True, fontsize=10)
plt.show()


# In[28]:


fig = plt.figure(figsize=(12,8), dpi=80)
ax = plt.subplot(111)
plt.plot(time1,S_jsum**2, label = "Sj", linestyle=':',linewidth=1)
plt.ylim(0,0.0000020)
plt.xlim(5250,5500)
plt.xlabel("Time (ns)")
plt.ylabel("Ey")
plt.title("Sum shifted Ey over Time")
plt.legend(loc="lower right", frameon=True)
plt.show()


# In[ ]:




