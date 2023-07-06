#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#odi.csv file converted into array
arr1= np.loadtxt("odi.csv",delimiter=",",dtype=str,skiprows=1)
print("Odi data of Player:-\n",arr1,"\n")

#Creating array of specific columns with datatype as integer
mat1=arr1[:,1].astype(int)#Matches played in odi 
print("Total Number of Matches played by each Player in Odi:-\n",mat1,"\n" )
run1=arr1[:,2].astype(int)#Runs in ODI Matches
print("Total Number Of Runs of Each Player in Odi:-\n",run1,"\n")
wckt1=arr1[:,3].astype(int)#Wickets in ODI Matches
print("Total Number Of Wicket Taken by each player in Odi:-\n",wckt1,"\n")
cen1=arr1[:,4].astype(int)#Century in ODI Matches
print("Total Number of Century did by each player in odi:-\n",cen1,"\n")
ha_cen1=arr1[:,5].astype(int)#Half-Century in ODI Matches
print("Total Number of Half-Century did by each player in odi:-\n",ha_cen1,"\n")
print("*************OPERATIONS*************")

#Arithmetic and Statistical Operations, Mathematical Operations, Bitwise Operators
result_odi=np.add(mat1,run1)
print("Sum of Total Matches and Total Runs:-\n",result_odi,"\n")

result1_odi=np.subtract(run1,mat1)
print("Subtarction of Total Matches and Total Runs:-\n",result1_odi,"\n")

result2_odi=np.matmul(mat1,run1)
print("Matrix Multiplication Of Total Matches And Total Runs -\n",result2_odi,"\n")

result3_odi=np.hstack((mat1,run1))
print("Stack Along Rows -\n",result3_odi,"\n")

result4_odi=np.vstack((mat1,run1))
print("Stack Along Columns -\n",result4_odi,"\n")

result5_odi=np.multiply(mat1,run1)
print("Multiplication of Total Matches and Total Runs -\n", result5_odi,"\n")

result6_odi=np.divide(run1,mat1)
print("Division of Total Runs and Total Matches -\n", result6_odi,"\n")

result7_odi=np.bitwise_and(mat1,run1)
print("Bitwise Operator for Total Runs -\n",result7_odi,"\n")


mean_odi=np.mean(run1)
median_odi=np.median(run1)
std_odi=np.std(run1)
var_odi=np.var(run1)

print("Mean of Total Runs of ODI:-\n",mean_odi,"\n")
print("Median of Total Runs of ODI:-\n",median_odi,"\n")
print("Standard Deviation of Total Runs of ODI:-\n",std_odi,"\n")
print("Variance of Total Runs of ODI:-\n",var_odi,"\n")

#Copying Of an Array
c=run1.copy()
print("Copied Array of Total Runs -\n",c,"\n")

#View an Array
d=run1.view()
run1[0]=10000
print("View Array of Total Runs After Changing Runs Of Virat Kohli -\n",d,"\n")

#Searching
maxruns= np.max(run1)
minruns = np.min(run1)
z= np.where(run1 > 5000)
print("Searching:")
print("Maximum Total Runs -", maxruns)
print("Minimum Total Runs -", minruns)
print("Indices where Total Runs are Greater than 5000 Runs -",z,"\n")

#Sorting
sorted_a = np.sort(run1)
print("Sorting:")
print("Sorted Total Runs Array -\n", sorted_a,"\n")

#Counting
nonzero_count = np.count_nonzero(run1)
print("Counting:")
print("Non-zero Count of Total Runs -", nonzero_count)
count_odi=wckt1[np.where(wckt1==0)]
print("How many Player has taken zero wickets in Odi :-", {count_odi.size})
count1_odi=cen1[np.where(cen1==0)]
print("How many player not did century in Odi :-",{count1_odi.size})
count2_odi=ha_cen1[np.where(ha_cen1==0)]
print("How many player did Half-century in Odi :-",{count2_odi.size},"\n")

#Broadcasting
arr4 = np.array([1, 2, 3])
arr5 = np.array([[1], [2], [3]])
broadcasted = arr4 + arr5
print("Broadcasting:")
print("Broadcasted Array -\n",broadcasted,"\n")

#Generate a Custom Sequence
sequence = np.arange(0,12,1)
print("Customize Range -\n",sequence,"\n")


# In[ ]:




