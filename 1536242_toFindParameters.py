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

for u in range(8,11):
	for v in range(2,5):
		for k in range(1,15):
			for j in range(1,15):
	
				alfa1 = 10**(-u)
				alfa2 = 10**(-v)
				eps1 = 2.5*10**(-3)
				eps2 = 2.5*10**(-3)
				m = 0
				q = 0
				mp = 1
				qp = 1
				mptemp = 0
				qptemp = 0
				count = 0
				MSEtemp = 4245
				MSEcheck = 4245
				x = train['SAT']
				y = train['GPA']

				while(abs(mp - mptemp) >= eps1):
					while(abs(qp - qptemp) >= eps2):
					
						MSE = 0.5*(sum((m*x + q - y)**2))
						
						mp = m - alfa1*np.dot((m*x + q - y), x)
						
						#print 'm:', m
						#print 'I have subtracted to m:', alfa1*np.dot((m*x + q - y), x)
						#print 'new m:', mp
						
						qp = q - alfa2*np.dot((m*x + q - y), np.ones(y.size))
						
						#print 'q:', q
						#print 'I have subtracted to q:', alfa2*np.dot((m*x + q - y), np.ones(y.size))
						#print 'new q:', qp

						count = count + 1
						
						#print 'the error on m :', abs(mp - m)
						#print 'the error on m :', abs(mp - m)

						mptemp = m
						qptemp = q
						
						m = mp
						q = qp
						
						print 'new MSE :', MSE
						
						if((MSE - MSEtemp)<0):
							#print 'decrease of MSE :', (MSE - MSEtemp)
							alfa1 = (k/10.0)*alfa1
							alfa2 = (j/10.0)*alfa2
						if((MSE - MSEtemp)>0):
							#print 'increase of MSE :', (MSE - MSEtemp)
							alfa1 = (0.5)*alfa1
							alfa2 = (0.5)*alfa2
							
						MSEtemp = MSE
						print '---------'
						if count == 100 :
							#print 'count break'
							break
					if count == 100 :
						#print 'count break'
						break
					count = count + 1
					#print 'q is not changing anymore'
				#print 'm is not changing anymore'
				if(MSE < MSEcheck):
					MSEcheck = MSE
					mCheck = m
					qCheck = q
					alfa1Check = alfa1
					uCheck = u
					alfa2Check = alfa2
					vCheck = v
					eps1Check = eps1
					eps2Check = eps2
					percM = k/10.0
					percQ = j/10.0

uhm = train.plot(x = "SAT", y = "GPA", kind = "scatter")
uhm.set_xlabel('SAT')
uhm.set_ylabel('GPA')

plt.plot(range(0,1600),map((lambda i: mCheck*i+qCheck), range(0,1600)))
print 'the angular coefficient is:', mCheck
print 'the intercept is:', qCheck
print 'the alfa1 is:', alfa1Check, uCheck
print 'the alfa2 is:', alfa2Check, vCheck
print 'the eps1 is:', eps1Check
print 'the eps1 is:', eps2Check
print 'alfa1 was changing of', percM
print 'alfa1 was changing of', percQ
print 'the best MSE is:', MSEcheck
plt.show()
'''
test = pd.read_csv(
    "testfile.csv",
    delimiter = ',', )



idlol = test['ID']
s = test['SAT']

r = mCheck*s+qCheck


import csv


file = open('1536242_submissionConCicli.csv', 'w')
writer = csv.writer(file, delimiter=',',lineterminator='\n')
writer.writerow(['ID', 'GPA'])
for i in range(0,199):
    writer.writerow([idlol[i], float(r[i])])
file.close()
'''