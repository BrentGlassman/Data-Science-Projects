import numpy as np 
import sympy as sypy
import matplotlib.pyplot as plt
import scipy.io as sio
import math

if __name__ == '__main__':

	mat_contents = sio.loadmat('circles_32x32.mat')
	for key in mat_contents.keys():
  		print(key)

	b = mat_contents["circles"].shape #(32,32,1861)
	print b
	#print mat_contents["circles"][:][:][0]
	
	mean=np.zeros(1024)
	for i in range(1861):
		for j in range(32):
			for k in range(32):
				mean[32*j+k]+=mat_contents["circles"][j][k][i]
		
	mean/=1861
	
	cov_mat=np.zeros([1024,1024])
	#tempmat=np.zeros([4096,4096])
	for i in range(1861):
		temparr=np.zeros(1024)
		for j in range(32):
			for k in range(32):
				temparr[j*32+k]=mat_contents["circles"][j][k][i]-mean[j*32+k]
		
		cov_mat+=np.outer(temparr,temparr)
	cov_mat/=1860	
	
	eigenvals, eigenvecs = np.linalg.eig(cov_mat)
	#print eigenvals.shape
	#print eigenvecs.shape
	idx = eigenvals.argsort()[::-1]   
	#print("index size equals ", idx.shape)
	#print(eigenvals)
	eigenvals = eigenvals[idx]
	eigenvecs = eigenvecs[:,idx]
	eigenvals = eigenvals.real
	eigenvecs = eigenvecs.real
	#print(sum(eigenvals))
	
	temp=0
	ctr=0
	while(temp<(0.95*sum(eigenvals))):
		temp+=eigenvals[ctr]
		ctr+=1
	print "It takes ", ctr ," dimensions to yield 95% of the variance out of 1024"
		
	temp2=np.zeros(1024)
	for i in range(1024):
		temp2[i]=i
	plt.semilogy(temp2,eigenvals)
	plt.show()
	
	Pcomp1=np.zeros([32,32])
	Pcomp2=np.zeros([32,32])
	Pcomp3=np.zeros([32,32])
	Pcomp4=np.zeros([32,32])
	Pcomp5=np.zeros([32,32])
	Pcomp6=np.zeros([32,32])
	Pcomp7=np.zeros([32,32])
	Pcomp8=np.zeros([32,32])
	Pcomp9=np.zeros([32,32])
	Pcomp10=np.zeros([32,32])
	Pcomp11=np.zeros([32,32])
	Pcomp12=np.zeros([32,32])
	Pcomp13=np.zeros([32,32])
	Pcomp14=np.zeros([32,32])
	Pcomp15=np.zeros([32,32])
	Pcomp16=np.zeros([32,32])
	for i in range(32):
		for j in range(32):
			n=5
			k=0
			Pcomp1[j][i]=eigenvecs[i*32+j][0*n+k]
			Pcomp2[j][i]=eigenvecs[i*32+j][1*n+k]
			Pcomp3[j][i]=eigenvecs[i*32+j][2*n+k]
			Pcomp4[j][i]=eigenvecs[i*32+j][3*n+k]
			Pcomp5[j][i]=eigenvecs[i*32+j][4*n+k]
			Pcomp6[j][i]=eigenvecs[i*32+j][5*n+k]
			Pcomp7[j][i]=eigenvecs[i*32+j][6*n+k]
			Pcomp8[j][i]=eigenvecs[i*32+j][7*n+k]
			Pcomp9[j][i]=eigenvecs[i*32+j][8*n+k]
			Pcomp10[j][i]=eigenvecs[i*32+j][9*n+k]
			Pcomp11[j][i]=eigenvecs[i*32+j][10*n+k]
			Pcomp12[j][i]=eigenvecs[i*32+j][11*n+k]
			Pcomp13[j][i]=eigenvecs[i*32+j][12*n+k]
			Pcomp14[j][i]=eigenvecs[i*32+j][13*n+k]
			Pcomp15[j][i]=eigenvecs[i*32+j][14*n+k]
			Pcomp16[j][i]=eigenvecs[i*32+j][15*n+k]

	plt.subplot(4,4,1)
	plt.axis('off')
	plt.imshow(Pcomp1, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,2)
	plt.axis('off')
	plt.imshow(Pcomp2, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,3)
	plt.axis('off')
	plt.imshow(Pcomp3, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,4)
	plt.axis('off')
	plt.imshow(Pcomp4, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,5)
	plt.axis('off')
	plt.imshow(Pcomp5, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,6)
	plt.axis('off')
	plt.imshow(Pcomp6, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,7)
	plt.axis('off')
	plt.imshow(Pcomp7, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,8)
	plt.axis('off')
	plt.imshow(Pcomp8, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,9)
	plt.axis('off')
	plt.imshow(Pcomp9, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,10)
	plt.axis('off')
	plt.imshow(Pcomp10, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,11)
	plt.axis('off')
	plt.imshow(Pcomp11, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,12)
	plt.axis('off')
	plt.imshow(Pcomp12, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,13)
	plt.axis('off')
	plt.imshow(Pcomp13, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,14)
	plt.axis('off')
	plt.imshow(Pcomp14, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,15)
	plt.axis('off')
	plt.imshow(Pcomp15, cmap=plt.get_cmap('gray_r'))
	plt.subplot(4,4,16)
	plt.axis('off')
	plt.imshow(Pcomp16, cmap=plt.get_cmap('gray_r'))
	plt.show()
	
	

	
	
	
	
	
	
	
