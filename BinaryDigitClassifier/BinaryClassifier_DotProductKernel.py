import numpy as np 
import sympy as sypy
import matplotlib.pyplot as plt
import scipy.io as sio
import math
import time

if __name__ == '__main__':

	mat_contents = sio.loadmat('MNIST_20x20.mat')
	#This file can be found in the Data-Science-Projects directory
	t0 = time.clock()
	#for key in mat_contents.keys():
  		#print(key)
  	#print mat_contents["imgs"][1]	
  	# a will access the 2nd 20x20 image [(2-1)th image] and find the value of gray in the 20th row 1st column 
	a = mat_contents["imgs"][1][19][0] # access 20x20 imgs with "imgs" key then [ROWS][COLUMNS][image N]
	c = mat_contents["labels"][1]
	d = mat_contents["labels"].shape
	b = mat_contents["imgs"].shape # Represents the size of the 3-d array
	print b
	print d
	
	reforMAT=np.zeros([400,70000])
	for i in range(70000):
		for j in range(20):
			for k in range(20):
				reforMAT[j*20+k][i]=mat_contents["imgs"][k][j][i]
	print ("Reformatted matrix   ",time.clock() - t0)
	a0=[]
	a1=[]
	a2=[]
	a3=[]
	a4=[]
	a5=[]
	a6=[]
	a7=[]
	a8=[]
	a9=[]
	temp1=[]
	lengths=[]
	Tlengths=[]
	# Separates the images #s into arrays
	for i in range(70000):
		if mat_contents["labels"][i]==0:
			a0.append(i)
		if mat_contents["labels"][i]==1:
			a1.append(i)
		if mat_contents["labels"][i]==2:
			a2.append(i)
		if mat_contents["labels"][i]==3:
			a3.append(i)
		if mat_contents["labels"][i]==4:
			a4.append(i)
		if mat_contents["labels"][i]==5:
			a5.append(i)
		if mat_contents["labels"][i]==6:
			a6.append(i)
		if mat_contents["labels"][i]==7:
			a7.append(i)
		if mat_contents["labels"][i]==8:
			a8.append(i)
		if mat_contents["labels"][i]==9:
			a9.append(i)
			
	#print(len(a0),len(a1),len(a2),len(a3),len(a4),len(a5),len(a6),len(a7),len(a8),len(a9))	
	#print(mat_contents["imgs"][0][0][20000])
	
	Data_Percent = 0.5
	lengths.append( int(math.ceil(Data_Percent*len(a0))))	
	lengths.append( int(math.ceil(Data_Percent*len(a1))))
	lengths.append( int(math.ceil(Data_Percent*len(a2))))
	lengths.append( int(math.ceil(Data_Percent*len(a3))))
	lengths.append( int(math.ceil(Data_Percent*len(a4))))
	lengths.append( int(math.ceil(Data_Percent*len(a5))))
	lengths.append( int(math.ceil(Data_Percent*len(a6))))
	lengths.append( int(math.ceil(Data_Percent*len(a7))))
	lengths.append( int(math.ceil(Data_Percent*len(a8))))
	lengths.append( int(math.ceil(Data_Percent*len(a9))))
	
	Tlengths.append(len(a0))	
	Tlengths.append(len(a1))
	Tlengths.append(len(a2))
	Tlengths.append(len(a3))
	Tlengths.append(len(a4))
	Tlengths.append(len(a5))
	Tlengths.append(len(a6))
	Tlengths.append(len(a7))
	Tlengths.append(len(a8))
	Tlengths.append(len(a9))
	
	largestA=Tlengths[0]
	for i in range(10):
		if(Tlengths[i]>largestA):
			largestA=Tlengths[i]	
		
	aMatrix = np.zeros([10,largestA])
	diff=np.zeros(10)
	for i in range(10):
		diff[i]=largestA-Tlengths[i]
	for i in range(int(diff[0])):
		a0.append(0)
	for i in range(int(diff[1])):
		a1.append(0)
	for i in range(int(diff[2])):
		a2.append(0)
	for i in range(int(diff[3])):
		a3.append(0)
	for i in range(int(diff[4])):
		a4.append(0)
	for i in range(int(diff[5])):
		a5.append(0)
	for i in range(int(diff[6])):
		a6.append(0)
	for i in range(int(diff[7])):
		a7.append(0)
	for i in range(int(diff[8])):
		a8.append(0)
	for i in range(int(diff[9])):
		a9.append(0)									
	
	aMatrix[0]=a0
	aMatrix[1]=a1
	aMatrix[2]=a2
	aMatrix[3]=a3
	aMatrix[4]=a4
	aMatrix[5]=a5
	aMatrix[6]=a6
	aMatrix[7]=a7
	aMatrix[8]=a8
	aMatrix[9]=a9
				

	
	MeanDist = np.zeros([10,400])

	for j in range(10):
		for i in range(lengths[j]):
			for k in range(400):
				MeanDist[j,k]+=reforMAT[k,aMatrix[j,i]]
	for i in range(10):
		MeanDist[i,:]/=lengths[i]
					


	rangebig=10
	for indx1 in range(rangebig):
		print("So Far So Good!!", time.clock()-t0)
		Nindx1 = Tlengths[indx1]-lengths[indx1]
		temparray=[]
		for i in range(lengths[indx1],Tlengths[indx1]):
			temparray.append(aMatrix[indx1,i])	

		counter=np.zeros(10)
		for i in range(Nindx1):
			tempTot=np.zeros(10)
			for n in range(10):
				for k in range(400):	
					tempTot[n]+=(MeanDist[n,k]-reforMAT[k,temparray[i]])**2
			for x in range(10):		
				if tempTot[indx1]>tempTot[x]:	
					counter[x]+=1
		for i in range(10):
			if counter[i]>0:
				counter[i]=(Nindx1-counter[i])/Nindx1			
		print(counter,Nindx1)						
		
		
		
		
		
		
		
		
		
		
		
		
		
			
