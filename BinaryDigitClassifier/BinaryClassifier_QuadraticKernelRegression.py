import numpy as np 
import sympy as sypy
import matplotlib.pyplot as plt
import scipy.io as sio
import math
import time
import sys

if __name__ == '__main__':

	np.set_printoptions(threshold='nan')
	orig_stdout = sys.stdout
	f = open('outFIN.txt', 'w')
	sys.stdout = f

	
	t0 = time.clock()
	mat_contents = sio.loadmat('MNIST_20x20.mat')
	#for key in mat_contents.keys():
  		#print(key)
  	#print mat_contents["imgs"][1]	
  	# a will access the 2nd 20x20 image [(2-1)th image] and find the value of gray in the 20th row 1st column 
	a = mat_contents["imgs"][:][:][0] # access 20x20 imgs with "imgs" key then [ROWS][COLUMNS][image N]
	c = mat_contents["labels"][1]
	d = mat_contents["labels"].shape
	b = mat_contents["imgs"].shape # Represents the size of the 3-d array
	bla = -9239.2
	#print b
	#print d
	reforMAT=np.zeros([400,70000])
	for i in range(70000):
		for j in range(20):
			for k in range(20):
				reforMAT[j*20+k][i]=mat_contents["imgs"][k][j][i]
	print ("Reformatted matrix   ",time.clock() - t0)
	#x=reforMAT[:,500]
	#y=reforMAT[:,501]	
	#print(x.shape, y.shape)			
	#test1=np.dot(reforMAT[:,500],reforMAT[:,501])
	#print(test1)			
	
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
	temp1=np.zeros([45,])
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
	print ("Length Arrays Complete   ",time.clock() - t0)		
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
				
	rangesmall=9
	rangebig=10
	for indx1 in range(rangesmall):
		for indx2 in range(indx1+1,rangebig):
			Gram01=np.zeros([lengths[indx1]+lengths[indx2],lengths[indx1]+lengths[indx2]])	
			Ntrain = lengths[indx1]+lengths[indx2]
			Nsamples = Tlengths[indx1]+Tlengths[indx2]-Ntrain
			Nindx1 = Tlengths[indx1]-lengths[indx1]
			Nindx2 = Tlengths[indx2]-lengths[indx2]	
			temparray=[]
			temparray2=[]
			#RENAME a0 and a1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!******************!!!!!!!!!!!!!
			#xxx1=a0
			#xxx2
			for i in range(lengths[indx1]):
				temparray.append(aMatrix[indx1,i])
			for i in range(lengths[indx2]):
				temparray.append(aMatrix[indx2,i])
		
			for i in range(lengths[indx1],Tlengths[indx1]):
				temparray2.append(aMatrix[indx1,i])
			for i in range(lengths[indx2],Tlengths[indx2]):
				temparray2.append(aMatrix[indx2,i])
			
			#temparray=temparray1+temparray2
			#print (lengths[indx1],lengths[indx2],Tlengths[indx1],Tlengths[indx2],len(temparray),len(temparray2))
			Y=np.zeros(Ntrain)
			alpha01=np.zeros(Ntrain)
			ctr=0
			#print ("Beginning Gram Matrix   ",time.clock() - t0)
			for i in range(Ntrain):
				if(i<lengths[indx1]):
					Y[i]=1
				else:
					Y[i]=-1
			for i in range(Ntrain):
				#if i==(tempmin+tempmax)%math.floor((tempmin+tempmax)/10):
					#print ("Gram Matrix   ", ctr*10+10,"% complete   ",time.clock() - t0)
				for j in range(Ntrain):
					Gram01[j,i]=Gram01[i,j]=(np.dot(reforMAT[:,temparray[i]],reforMAT[:,temparray[j]])+1.0)**2
	
			
			Gram01inv=np.linalg.inv(Gram01)
			#print(alpha01.shape)
			for i in range(Ntrain):
				for j in range(Ntrain):
					alpha01[i]+=Gram01inv[i,j]*Y[j]
			#print("1 alpha calculation complete   ", time.clock()-t0)
			#print (Y.shape,alpha01.shape,Gram01inv.shape)
			counter=0
			for j in range(Nindx1):
				bla=0.0
				for i in range(Ntrain):
					bla+=alpha01[i]*(np.dot(reforMAT[:,temparray[i]],reforMAT[:,temparray2[j]])+1.0)**2
				if bla>0:
					counter+=1
			
			counter2=0
			for j in range(Nindx1,Nsamples):
				bla=0.0
				for i in range(Ntrain):
					bla+=alpha01[i]*(np.dot(reforMAT[:,temparray[i]],reforMAT[:,temparray2[j]])+1.0)**2
				if bla<0:
					counter2+=1
					
			print(indx1,indx2, "% 0's were correctly assigned ", time.clock()-t0,counter,Nindx1)		
			print(indx2,indx1, "% 1's were correctly assigned ", time.clock()-t0,counter2,Nindx2)		

		del Gram01
	
	sys.stdout = orig_stdout
	f.close()















	# Matrix average for 1's
#	for j in range(total1):
#		for x in range(20):
#			for y in range(20):
#				imgs1[x][y]+=mat_contents["imgs"][x][y][a1[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs1[x][y] /= math.ceil(total1)
#			
#	# Matrix average for 2's			
#	for j in range(total2):
#		for x in range(20):
#			for y in range(20):
#				imgs2[x][y]+=mat_contents["imgs"][x][y][a2[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs2[x][y] /= math.ceil(total2)
#			
#	for j in range(total3):
#		for x in range(20):
#			for y in range(20):
#				imgs3[x][y]+=mat_contents["imgs"][x][y][a3[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs3[x][y] /= math.ceil(total3)
#			
#	for j in range(total4):
#		for x in range(20):
#			for y in range(20):
#				imgs4[x][y]+=mat_contents["imgs"][x][y][a4[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs4[x][y] /= math.ceil(total4)
#			
#	for j in range(total5):
#		for x in range(20):
#			for y in range(20):
#				imgs5[x][y]+=mat_contents["imgs"][x][y][a5[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs5[x][y] /= math.ceil(total5)
#		
#	for j in range(total6):
#		for x in range(20):
#			for y in range(20):
#				imgs6[x][y]+=mat_contents["imgs"][x][y][a6[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs6[x][y] /= math.ceil(total6)
#		
#	for j in range(total7):
#		for x in range(20):
#			for y in range(20):
#				imgs7[x][y]+=mat_contents["imgs"][x][y][a7[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs7[x][y] /= math.ceil(total7)
#		
#	for j in range(total8):
#		for x in range(20):
#			for y in range(20):
#				imgs8[x][y]+=mat_contents["imgs"][x][y][a8[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs8[x][y] /= math.ceil(total8)
#		
#	for j in range(total9):
#		for x in range(20):
#			for y in range(20):
#				imgs9[x][y]+=mat_contents["imgs"][x][y][a9[j]]
#				#print(a1[j],x,y)
#	for x in range(20):
#		for y in range(20):			
#			imgs9[x][y] /= math.ceil(total9)
#		
#																
#	plt.figure[1]
#	plt.subplot(331)		
#	plt.imshow(imgs1, cmap=plt.get_cmap('gray_r'))	
#	plt.subplot(332)		
#	plt.imshow(imgs2, cmap=plt.get_cmap('gray_r'))	
#	plt.subplot(333)		
#	plt.imshow(imgs3, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(334)		
#	plt.imshow(imgs4, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(335)		
#	plt.imshow(imgs5, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(336)		
#	plt.imshow(imgs6, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(337)		
#	plt.imshow(imgs7, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(338)		
#	plt.imshow(imgs8, cmap=plt.get_cmap('gray_r'))
#	plt.subplot(339)		
#	plt.imshow(imgs9, cmap=plt.get_cmap('gray_r'))
#	plt.show()
#	temp=0	
#	counter1=0
#	counter2=0
#	ctrx=0
#	test1 = len(a1)-total1
#	test2 = len(a2)-total2
#	for i in range(total1,len(a1)):	
#		Mean1dist=0
#		Mean2dist=0
#		for x in range(20):
#			for y in range(20):
#				Mean1dist += (imgs1[x][y] - mat_contents["imgs"][x][y][a1[i]])**2 #Computes the distance of the 1 to the average 1
#				Mean2dist += (imgs2[x][y] - mat_contents["imgs"][x][y][a1[i]])**2 #Computes the distance of the 1 to the average 2
#				
#		if Mean1dist<Mean2dist: #Which Does the image of a 1 look more like?
#			counter1+=1
#		else:
#			temp1.append(i)	
#			
#	for i in range(total2,len(a2)):	
#		Mean1dist=0
#		Mean2dist=0
#		for x in range(20):
#			for y in range(20):
#				Mean1dist += (imgs1[x][y] - mat_contents["imgs"][x][y][a2[i]])**2 #Computes the distance of the 2 to the average 1
#				Mean2dist += (imgs2[x][y] - mat_contents["imgs"][x][y][a2[i]])**2 #Computes the distance of the 2 to the average 2
#				
#		if Mean2dist<Mean1dist: #Which Does the image of a 2 look more like?
#			counter2+=1		
#			
#	Efficiency1 = float(counter1)/float(test1)
#	Efficiency2 = float(counter2)/float(test2)	
#	print('\n\nPART B: (Comparing 1s and 2s) \n')	
#	print('The Efficiency of a 1-image being classified as a 1 = ', Efficiency1)
#	print('The Efficiency of a 2-image being classified as a 2 = ', Efficiency2)
#	print('\nThe images note some of the ones that have been missclassified as twos')
#	
#	print('\n\n	Exit Figure to end program')	
#	plt.figure[2]
#	for k in range[9]:
#		bla = np.zeros([20,20])	
#		for x in range(20):
#			for y in range(20):	
#				bla[x][y]=mat_contents["imgs"][x][y][a1[temp1[k]]]
#	
#	
#		plt.subplot(331+k)		
#		plt.imshow(bla, cmap=plt.get_cmap('gray_r'))	
#	plt.show() #outputs 1s that the program computes as 2s
#		
#		
#		
