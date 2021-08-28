import numpy as np
from scipy.linalg import lu,lu_factor,lu_solve
n=3
m=3
A= np.array([[1,1,-1],[2,-1,1],[-1,2,2]],dtype=float)
x= np.empty(3,dtype=float);x.shape=[3,1]
B= np.array([-2,5,1],dtype=float); B.shape = [3,1]

def Gaussian_Elimination():
    print("original matrix\n",A,'\n')
    for j in range(0,n-1):
        for i in range(1,m):
            if  j == 0 :
                print("i=",i,"j=",j)
                K_1 = A[i,j]/A[m-m,m-m]
                A[i] = A[i]-(K_1*A[m-m])
                B[i] = B[i]-(K_1*B[m-m])
                print("cofficien_1\n",K_1,'\n')       
                print("step 1 matrix\n",A,'\n')
                print("B Matrix\n",B,'\n',"**********END STEP 1**************")
        for j in range (1,n-1):
            for i in range(1,m-1):
                K_2 = A[i+1,j]/A[i,j]
                A[i+1] = A[i+1]-(K_2*A[j])
                B[i+1] = B[i+1]-(K_2*B[j])
                print("cofficien_2\n",K_2,'\n') 
                print("step 2 matrix\n",A,'\n')
                print("B Matrix\n",B,"\n","**********END STEP 2**************","\n")
                #find x metrix
                #find x[3]
                #x[n-1]=B[n-1]/A[n-1,n-1]   
                #find x[k]
    print("********************Liner Equation********************")
    x[n-1]=B[n-1]/A[n-1,n-1]
    print("x[2]=",x[n-1],"\n")
    for i in range (0,m-1):
        for j in range(1,m):
            k=n-j-1
            if i<j and k != 0 :
                print("k=",k)
                print("i=",i,"j=",j,"k=",k)
                x[k]=1/A[k,k]*(B[k]-(A[k,k+1]*x[k+1]))
                print(">>>>>>>>>>>>>>>>>>>>>>> x[1]",x[k],"\n")
                P1=0
            if i ==0 and k == 0:
                for j in range (1,m):
                    print("i=",i,"j=",j,"k=",k)
                    P=((A[k,j]*x[j]))
                    P1=P1+P
                    print("P = ",P)
                    print("SUM_P1 = ",P1,"\n")

                x[k]=(1/A[k,k])*(B[k]-P1)
                print("CHECK B-SUM = ",B[k]-P1)
                print("CHECK 1/A = ",1/A[k,j-1])
                print("x[0] =",x[k],"\n")
                print(x,"\n","\n","***********END***************")

if __name__ == '__main__':
    Gaussian_Elimination()

