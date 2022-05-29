#!/usr/bin/env python
# coding: utf-8

# # David Brookes
# # May 2022

# # Code developed to solve the probability problem:

# ## Coupons in cereal boxes are numbered 1 to 5, and a set of one each is required for a prize. With one coupon per box, how many boxes on average are required to make a complete set.

# In[8]:


# Code from the internet.
# Calculates integer partitions in lexicographic and reverse lexicographic order.
# Note: Yield is used here. Apparently this is a good idea!


# def revlex_partitions(n):
#     """
#     Generate all integer partitions of n
#     in reverse lexicographic order
#     """
#     if n == 0:
#         yield []
#         return
#     for p in revlex_partitions(n - 1):
#         if len(p) == 1 or (len(p) > 1 and p[-1] < p[-2]):
#             p[-1] += 1
#             yield p
#             p[-1] -= 1
#         p.append(1)
#         yield p
#         p.pop()
        
        
# def lex_partitions(n):
#     """
#     Generate all integer partitions of n
#     in lexicographic order
#     """
#     if n == 0:
#         yield []
#         return
#     for p in lex_partitions(n - 1):
#         p.append(1)
#         yield p
#         p.pop()
#         if len(p) == 1 or (len(p) > 1 and p[-1] < p[-2]):
#             p[-1] += 1
#             yield p
#             p[-1] -= 1

# def main():
#     for p in revlex_partitions(6):
#         print(p)
#     print()
#     for p in revlex_partitions(5):
#         print(p)
#     print()    
    
# #    for p in lex_partitions(5):
# #        print(p)
        
# if __name__ == '__main__':
#     main()


# In[21]:



import numpy as np 

def partitions(n, k):
    """
    Generate all integer partitions of n
    that can be summed in k terms or less.
    """
    if n == 0:
        return([[]])
    else:
        newlist=[]
        for p in partitions(n-1, k):
            if len(p)<k:
                p_copy = p.copy()
                p_copy.append(1)
                newlist.append(p_copy)
            if len(p) == 1 or (len(p)>1 and p[-1] < p[-2]):
                p[-1] += 1
                newlist.append(p)      
        return(newlist)
    
def filtered_partitions(parts, k):
    """
    This returns all integer partitions of n
    that can be summed in exactly k terms.
    """
    filtered_list = []
    for p in parts:
        if len(p) == k:
            filtered_list.append(p)
    return(filtered_list)
    
def repetitions(part):
    reps = []
    unique_vals = list(set(part))
    for v in unique_vals:
        reps.append(part.count(v))       
    return(reps)
    
def calc_prob(num_c, b, f_parts):
    perms = 0
    for f_part in f_parts:
        f_lenpart = len(f_part)
        perm = np.math.factorial(b-1)
        for i in range(f_lenpart):
            perm = perm/np.math.factorial(f_part[i])
        perm = perm * np.math.factorial(num_c-1)

        reps = repetitions(f_part) 
        for j in range(len(reps)):
            perm = perm/np.math.factorial(reps[j])
        
        perm = perm*num_c            
        perms += perm
        
    totalperms = (num_c)**(b) 

    return(perms/totalperms)

def theo_exp_b(n):
    harmonic = 0.0
    for i in range(1,n+1):
        harmonic += 1/i
    return(n*harmonic)
        
def main():

    # Number of distinct coupons.
    num_c = 5

    # Maximum number of boxes to consider (i.e. less than infinity!).
    num_b = 70

    # Probability of getting a full set of coupons after opening b boxes.
    prob = 0.0
    # Expected number of boxes.
    exp_b = 0.0

    for b in range(1,num_b+1):
        if b > num_c:
            parts = partitions(b-1, num_c-1)
            f_parts = filtered_partitions(parts, num_c-1)
            pr = calc_prob(num_c, b, f_parts)
        elif b == num_c:
            pr = np.math.factorial(num_c)/(num_c**num_c)
        else:
            pr = 0.0
        prob += pr
        exp_b += b*pr

    # Approximate solution.
    print('Compuational solution')
    print('prob=', prob)
    print('exp_b=', exp_b)
    print()
    
    #Exact solution.
    print('Theoretical solution')
    theoretical_exp_b = theo_exp_b(num_c)
    print('exp_b=', theoretical_exp_b)
       
if __name__ == '__main__':
    main()


# In[ ]:




