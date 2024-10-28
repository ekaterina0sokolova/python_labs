import numpy as np


def function(a, b, c, d):
    matrix = np.array(
        [[1, 0, 1, 0],
        [4, 0, 1, -2],
        [-4, 4, 0, 1],
        [a, b, c, d],]
    )
    vector = np.array([2, 0, 5, -2])
    solution = np.linalg.solve(matrix, vector)

    return int(np.sum(solution))





print(function(12,12,1,1)) # 2
print(function(102,12,33,1)) # 1
