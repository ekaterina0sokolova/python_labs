import numpy as np

def function(temperature1, temperature2):
    temperature1_array = np.array(temperature1)
    temperature2_array = np.array(temperature2)

    t1_even = temperature1_array[::2]
    t2_even = temperature2_array[::2]

    combined_list = np.concatenate((t1_even, t2_even))

    return int(np.max(combined_list) + np.min(combined_list) + np.mean(combined_list))



print(function([12,24,36],[12,24,36])) # 72
print(function([12,24,36,44],[12,24,36,49])) # 72