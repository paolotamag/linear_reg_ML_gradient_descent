import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv(
    "training.csv",
    delimiter = ',',
    usecols   = [1, 2] )
	
#removing far away points from training data set
train = train[train.GPA != 4.5]
#train = train[train.GPA > 2]


alfa1 = 10**(-10)
#alfa1 = 1.24939011*10**(-4)
alfa2 = 10**(-4)
#alfa2 = 1.012391292**(-3)
#eps1 = 10**(-5.5)
eps1 = 0.0025
eps2 = 0.0025
#eps2 = 10**(-5.5)
m = 0
q = 0
mp = 1
qp = 1
mptemp = 0
qptemp = 0
count = 0
MSEtemp = 4245
x = train['SAT']
y = train['GPA']

while(abs(mp - mptemp) >= eps1):
    while(abs(qp - qptemp) >= eps2):
	
        MSE = 0.5*(sum((m*x + q - y)**2))
		
        mp = m - alfa1*np.dot((m*x + q - y), x)
		
        print 'm:', m
        print 'I have subtracted to m:', alfa1*np.dot((m*x + q - y), x)
        print 'new m:', mp
		
        qp = q - alfa2*np.dot((m*x + q - y), np.ones(y.size))
		
        print 'q:', q
        print 'I have subtracted to q:', alfa2*np.dot((m*x + q - y), np.ones(y.size))
        print 'new q:', qp

        count = count + 1
		
        print 'the error on m :', abs(mp - m)
        print 'the error on q :', abs(qp - q)

        mptemp = m
        qptemp = q
		
        m = mp
        q = qp
		
        print 'new MSE :', MSE
		
        if((MSE - MSEtemp)<0):
            print 'decrease of MSE :', (MSE - MSEtemp)
            alfa1 = 1.4*alfa1
			#era 1.1 in entrambi
            alfa2 = 1.4*alfa2
        if((MSE - MSEtemp)>0):
            print 'increase of MSE :', (MSE - MSEtemp)
            alfa1 = 0.5*alfa1
            alfa2 = 0.5*alfa2
			
        MSEtemp = MSE
        print '---------'
        if count == 10000 :
            print 'count break'
            break
    if count == 10000 :
        print 'count break'
        break
    count = count + 1
    print 'q is not changing anymore'
print 'm is not changing anymore'

uhm = train.plot(x = "SAT", y = "GPA", kind = "scatter")
uhm.set_xlabel('SAT')
uhm.set_ylabel('GPA')

plt.plot(range(0,1600),map((lambda i: m*i+q), range(0,1600)))
print 'the angular coefficient is:', m
print 'the intercept is:', q
plt.show()

test = pd.read_csv(
    "testfile.csv",
    delimiter = ',', )



idlol = test['ID']
s = test['SAT']

r = m*s+q


import csv


file = open('1536242_submission.csv', 'w')
writer = csv.writer(file, delimiter=',',lineterminator='\n')
writer.writerow(['ID', 'GPA'])
for i in range(0,199):
    writer.writerow([idlol[i], float(r[i])])
file.close()