import numpy as np    
import random
xy=0
def create_dataset(rows,columns):
    X_list=[]
    y_list=[]
    for i in range(columns):
        l=[random.randint(0,1) for i in range(rows)]
        X_list.append(l)
        if(l[4]==1):
            output=[l[0]^l[2],l[1]^l[3]]
            y_list.append(output)
        else:
            p=[l[0]^l[2],l[1]^l[3]]
            out=[]
            for i in range(2):
                x_comp=~p[i]
                output=int(bin(x_comp)[-1])
                out.append(output)
            y_list.append(out)
          
    X=np.array(X_list).T   
    Y=np.array(y_list).T
    return X,Y
def initialise_parameters(n_x,n_y,n_h):
    w1=np.random.randn(n_h,n_x)*0.01
    b1=np.zeros((n_h,1))
    w2=np.random.randn(n_y,n_h)*0.01
    b2=np.zeros((n_y,1))
    return w1,b1,w2,b2
def sigmoid(x):
    return(1/(1+np.exp(-x)))
def forward_prop(X,w1,w2,predict):
    z1=np.dot(w1,X)+b1
    a1=np.tanh(z1)
    z2=np.dot(w2,a1)+b2
    a2=sigmoid(z2)   # prediction.
    if predict:
        return a2
    else:    
        return z1,a1,z2,a2
def back_prop(a1,a2,Y,m):
    """
    noice.
    """
    dz2= a2 - Y
    dw2 = (1 / m) * np.dot(dz2, a1.T)
    db2 = (1 / m) * np.sum(dz2, axis=1, keepdims=True)
    dz1 = np.multiply(np.dot(w2.T, dz2), 1 - np.power(a1, 2))
    dw1 = (1 / m) * np.dot(dz1, X.T)
    db1 = (1 / m) * np.sum(dz1, axis=1, keepdims=True)
    return dw1,db1,dw2,db2
def accuracy(prediction,Y,m,s):
    h=prediction-Y
    a=np.array([0,0], dtype=float)
    acc=0
    test=np.array([True,True],dtype=str)
    for i in range(m):
        
        l= h[:,i]==a
        xy=0
        for i in l:
            if i==False:
                xy=1
                break
        if(xy==0):
            acc+=1
    perc=(acc/m)*100     
    if(s=='train'):  
        print('Train Accuracy = {} percent'.format(perc)) 
    if(s=='test'):
        print('Test Accuracy = {} percent'.format(perc))     


#####################################################################
X_o,Y_o=create_dataset(5,50)   
X=X_o[:,:40]
# print(X.shape)
Y=Y_o[:,:40]
X_test=X_o[:,40:]
# print(X_test.shape)
Y_test=Y_o[:,40:]

m=X.shape[1]
m_test=X_test.shape[1]
n_x=X.shape[0]
print(n_x)
n_y=Y.shape[0]
n_h=5
epochs=3000
alpha=0.1

w1,b1,w2,b2=initialise_parameters(n_x,n_y,n_h)  

for i in range(epochs):
   
    z1,a1,z2,a2=forward_prop(X,w1,w2,False)
    
    dw1,db1,dw2,db2=back_prop(a1,a2,Y,m)

    w1 -= alpha*dw1
    w2 -= alpha*dw2
    b1 -= alpha*db1
    b2 -= alpha*db2
    
prediction=a2
prediction[prediction<0.5]=0
prediction[prediction>=0.5]=1
accuracy(prediction,Y,m,'train')

#test.
output=forward_prop(X_test,w1,w2,True) 
output[output<0.5]=0
output[output>=0.5]=1
# print(output)
accuracy(output,Y_test,m_test,'test')      

    
    

    

 


     


