#!/usr/bin/env python
# coding: utf-8

# # Reverse 5 digit number

# In[1]:


My_Number = int(input("Please write the number to be : "))
Reverse_Number = 0
while(My_Number > 0):
    Reverse_Number = (Reverse_Number *10) + My_Number % 10
    My_Number = My_Number //10

    print("Reverse of the provided number is = %d" %Reverse_Number)


# # Getting 3 number then adding,substracting and multiplying

# In[2]:


m1 = int(input("Write number : " ))
m2 = int(input("Write number : " ))
m3 = int(input("Write number : " ))
add = m1+m2+m3
sub = m1-m2-m3
multiply = m1*m2*m3
print(add,sub,multiply)


# # Getting 20 numbers and calculating sum,average,max and min

# In[3]:


num_list = [10, 20.5, 30, 45.5, 50, 65, 85, 10, 12, 16, 24, 33, 12, 18, 18, 20, 33, 12, 85, 12]
numbers = sum(num_list)
avg = numbers / len(num_list)
print("sum is: ", numbers, "Average is: ", avg)
print("Minimum value is : ", min(num_list))
print("Maximum value is : ", max(num_list))


# # list of 12 grades-using for loop

# In[4]:


def all_grade(num):
    sum_num = 0
    for j in num:
        sum_num = sum_num + j

    avg = sum_num / len(num)
    return avg
print("The average is", all_grade([3,4,3,4,3.5,4,2,2,3,3,3,4]))


# # list of 12 grades-using for sum function

# In[5]:


number_list = [3,4,3,4,3.5,4,2,2,3,3,3,4]
avg = sum(number_list)/len(number_list)
print("The average is ",avg)


# # list of 12 grades-using mean function

# In[6]:


from numpy import mean
number_list = [3,4,3,4,3.5,4,2,2,3,3,3,4]
avg = mean(number_list)
print("The average is ", round(avg,2))


# # Calculating median with median function

# In[8]:


import statistics
number_list = [3,4,3,4,3.5,4,2,2,3,3,3,4]
medium_num =statistics.median(number_list)
print(medium_num)


# # Calculating median without median function

# In[11]:


number_list = [3,4,3,4,3.5,4,2,2,3,3,3,4]
abc = len(number_list)
number_list.sort()
  
if abc % 2 == 0:
    median1 = number_list[abc//2]
    median2 = number_list[abc//2 - 1]
    median = (median1 + median2)/2
else:
    median = number_list[abc//2]
print("Median is: " + str(median))


# # Calculating mode with mode function

# In[12]:


import statistics
number_list = [3,4,3,4,3.5,4,2,2,3,3,3,4]
print("Mode is :", statistics.mode(number_list))


# # Get 6 digit number from user and putinto array
# 

# In[ ]:


Working on .....

