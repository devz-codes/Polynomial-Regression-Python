import numpy as np
from numpy.linalg import inv
from statistics import mean

class Polynomial_Regression:

    def __init__(self,x_val,y_val,degree):
        self.x_val=x_val
        self.y_val=y_val
        self.degree=degree

    def coefficients(self):

        np.set_printoptions(suppress=True)

        mt1=np.empty((0,0))
        mt2=np.empty((0,0))

        for i in range(1,self.degree+2):
            lst1=[pow(k,i-1) for k in self.x_val]
            prod=list(map(lambda x,y:x*y,lst1,self.y_val))
            mt1=np.append(mt1,np.matrix(sum(prod)))

            a=[]

            for j in range(0,self.degree+1):
                lst2=[pow(k,i+j-1) for k in self.x_val]
                a.append(sum(lst2))
            
            mt2=np.append(mt2,np.matrix([a]))
        
        mt2=mt2.reshape(self.degree+1,self.degree+1)
        mt1=mt1.reshape(self.degree+1,1)
        
        mt2=inv(mt2)
        coef=np.dot(mt2,mt1)

        return coef.astype(np.float64)
    
    
    def predict(self,inp):
        i=0
        sum=0
        for x in Polynomial_Regression.coefficients(self):
            sum+=x[0]*pow(inp,i)
            i+=1
        return sum
    
    
    def r_square(self):

        mean_y=mean(self.y_val)
        sst=0
        sse=0

        for i in range(len(self.x_val)):
            sst+=pow(self.y_val[i]-mean_y,2)
            sse+=pow(self.y_val[i]-Polynomial_Regression.predict(self,self.x_val[i]),2)
        
        return (sst-sse)/sst


x=[x for x in range(1,6)]
y=[5,4,3,2,1]

obj=Polynomial_Regression(x,y,1)

print(obj.r_square())

