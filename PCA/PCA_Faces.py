import numpy as np 
import sympy as sypy
import matplotlib.pyplot as plt
import scipy.io as sio
import math

if __name__ == '__main__':

	mat_contents = sio.loadmat('Yale_64x64.mat')
	for key in mat_contents.keys():
  		print(key)

	b = mat_contents["fea"].shape
	c = mat_contents["gnd"].shape 
	print b
	print c
	#print mat_contents["gnd"][:]
	mean = np.zeros([4096,1])
	for j in range(165):
		for i in range(4096):
			mean[i]+=mat_contents["fea"][i][j]
	mean[i]/=165
	#meanmat=np.zeros([64,64])
	#for i in range(64):
	#	for j in range(64):
	#		meanmat[j][i]=mean[i*64+j]
	cov_mat=np.zeros([4096,4096])
	#tempmat=np.zeros([4096,4096])
	for i in range(165):
		temparr=np.zeros(4096)
		for j in range(64):
			for k in range(64):
				temparr[j*64+k]=mat_contents["fea"][j*64+k][i]-mean[j*64+k]
		cov_mat+=np.outer(temparr,temparr)
	cov_mat/=164	
	
	eigenvals, eigenvecs = np.linalg.eig(cov_mat)
	print eigenvals.shape
	print eigenvecs.shape
	
	idx = eigenvals.argsort()[::-1]   
	print("index size equals ", idx.shape)
	print(eigenvals)
	eigenvals = eigenvals[idx]
	eigenvecs = eigenvecs[:,idx]
	eigenvals = eigenvals.real
	eigenvecs = eigenvecs.real
	
	
	temp=0
	ctr=1
	while(temp<(0.95*(sum(eigenvals)-eigenvals[0]))):
		temp+=eigenvals[ctr]
		ctr+=1
	print "It takes ", ctr-1 ," dimensions to yield 95% of the variance out of 4096"
		
	
	
	
	
	
	
	Pcomp1=np.zeros([64,64])
	Pcomp2=np.zeros([64,64])
	Pcomp3=np.zeros([64,64])
	Pcomp4=np.zeros([64,64])
	Pcomp5=np.zeros([64,64])
	Pcomp6=np.zeros([64,64])
	Pcomp7=np.zeros([64,64])
	Pcomp8=np.zeros([64,64])
	Pcomp9=np.zeros([64,64])
	for i in range(64):
		for j in range(64):
			Pcomp1[j][i]=eigenvecs[i*64+j][0]
			Pcomp2[j][i]=eigenvecs[i*64+j][1]
			Pcomp3[j][i]=eigenvecs[i*64+j][2]
			Pcomp4[j][i]=eigenvecs[i*64+j][3]
			Pcomp5[j][i]=eigenvecs[i*64+j][4]
			Pcomp6[j][i]=eigenvecs[i*64+j][5]
			Pcomp7[j][i]=eigenvecs[i*64+j][6]
			Pcomp8[j][i]=eigenvecs[i*64+j][7]
			Pcomp9[j][i]=eigenvecs[i*64+j][8]
	plt.subplot(3,3,1)
	plt.imshow(Pcomp1, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,2)
	plt.imshow(Pcomp2, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,3)
	plt.imshow(Pcomp3, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,4)
	plt.imshow(Pcomp4, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,5)
	plt.imshow(Pcomp5, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,6)
	plt.imshow(Pcomp6, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,7)
	plt.imshow(Pcomp7, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,8)
	plt.imshow(Pcomp8, cmap=plt.get_cmap('gray_r'))
	plt.subplot(3,3,9)
	plt.imshow(Pcomp9, cmap=plt.get_cmap('gray_r'))
	plt.show()
#	imgs1 = np.zeros([64,64])
#	imgs2 = np.zeros([64,64])
#	imgs3 = np.zeros([64,64])
#	imgs4 = np.zeros([64,64])
#	imgs5 = np.zeros([64,64])
#	imgs6 = np.zeros([64,64])
#	imgs7 = np.zeros([64,64])
#	imgs8 = np.zeros([64,64])
#	imgs9 = np.zeros([64,64])
#	imgs10 = np.zeros([64,64])
#	imgs11 = np.zeros([64,64])
#	imgs12 = np.zeros([64,64])
#	imgs13 = np.zeros([64,64])
#	imgs14 = np.zeros([64,64])
#	imgs15 = np.zeros([64,64])
#	
#	
#	for i in range(64):
#		for j in range(64):
#			k=0
#			imgs1[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs2[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs3[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs4[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs5[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs6[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs7[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs8[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs9[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs10[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs11[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs12[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs13[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs14[j][i]=mat_contents["fea"][i*64+j][k]
#			k+=11
#			imgs15[j][i]=mat_contents["fea"][i*64+j][k]
#			
	
#	plt.subplot(3,5,1)		
#	plt.imshow(imgs1, cmap=plt.get_cmap('gray'))	
#	plt.subplot(3,5,2)
#	plt.imshow(imgs2, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,3)
#	plt.imshow(imgs3, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,4)
#	plt.imshow(imgs4, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,5)
#	plt.imshow(imgs5, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,6)
#	plt.imshow(imgs6, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,7)
#	plt.imshow(imgs7, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,8)
#	plt.imshow(imgs8, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,9)
#	plt.imshow(imgs9, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,10)
#	plt.imshow(imgs10, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,11)
#	plt.imshow(imgs11, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,12)
#	plt.imshow(imgs12, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,13)
#	plt.imshow(imgs13, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,14)
#	plt.imshow(imgs14, cmap=plt.get_cmap('gray'))
#	plt.subplot(3,5,15)
#	plt.imshow(imgs15, cmap=plt.get_cmap('gray'))
#	plt.show()
	
	
	
	
	
	
	
	
	
	
	
	
	
