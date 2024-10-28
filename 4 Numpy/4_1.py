import numpy as np

def function(int_list):
    n_list = np.array(int_list)
    n_list[n_list < 0] += 3
    n_list[n_list > 0] *= 2
    n_list = np.sort(n_list)
    req_summ = n_list[-1] + n_list[-2]
    return req_summ


print(function([1,2,3,-3, 0])) # 10
print(function([1,2,3,-3, 13, 0])) # 32
