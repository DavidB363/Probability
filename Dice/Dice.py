#!/usr/bin/env python
# coding: utf-8

# 
# # David Brookes
# # May 2022

# # Probabilty Problem:
# # On average, how many times must a die be thrown until one gets a 4?

# In[1]:


# Note that no programming knowledge is assumed, but some mathematics and probability
# theory is assumed.


# In[2]:


# Determine the expected number of throws of a 6 sided fair die to produce 
# a preselected outcome for the first time (e.g. 4, say - it doesn't matter which number is chosen
# when a fair die is used).


# ## Theoretical Solution

# In[3]:


# Theoretical result (obtained by summing an infinite series, for example).
# (This is the exact result).


# In[2]:


# p represents the probability of getting a 4 for each throw of the die.
p = 1/6

theoretical_number_of_throws = 1/p

print('Theoretical Solution')
print('Expected number of throws ', theoretical_number_of_throws)


# ## Computational Solution (Truncated Series)

# In[5]:


# Approximate result using computation (summing a truncated series).
# Need to calculate the probability of first throwing a 4 on either...
# the first throw or...
# the second or...
# the third throw or...
# ...etc


# In[1]:


expected_throws = 0.0
max_num_throws = 100 # i.e. Less than infinity!
p = 1/6 # The probability of throwing a 4.
q = 1-p # The probability of not throwing a 4.

for throw in range(1,max_num_throws+1):
    #print(throw)
    probability = (q**(throw-1))*p 
    #print(probability)
    
    expected_throws = expected_throws + probability*throw
    
print('Computational Solution')
print('Expected number of throws ', expected_throws)   


# ## Solution by Simulation

# In[7]:


# Approximate solution using simulation (generation of random numbers - Monte carlo simulation).
# The computer generates a series of random numbers that represent the rolls of a die.
# e.g. 6, 5, 2, 6, 2, 4 - here 4 appears on the sixth roll in this trial (i.e. success!).
# Many trials are run, and the average of the number of rolls to success is calculated. 


# In[3]:


import numpy as np

number_of_trials = 1000

preselected_number = 4

total_throws_to_success = 0
for trial in range(number_of_trials):
    success = False
    #print('trial ', trial)
    throw_count = 0
    while not success:
        throw_count += 1
        #print('throw count:', throw_count)
        result_of_throw = np.random.randint(1, 6+1)
        #print(random_int)
        if (result_of_throw == preselected_number):
            success = True
            #print('success')
        else:
            pass
            #print('failure')
    total_throws_to_success += throw_count
    
average_throws_to_success = total_throws_to_success/number_of_trials

print('Simulation Solution')
print('Expected number of throws ', average_throws_to_success)  
print()

