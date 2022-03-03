import math
import numpy as np

matrix = np.array([[3,-2,1,0],
                   [8,4,2,1],
                   [1,0,2,1],
                   [1,1,5,9]],float)

m, n = np.shape(matrix)

def check_diag_dominance(X):
    if np.all(((abs(np.diag(X)))) >= (np.sum(abs(X),axis=1) - abs(np.diag(X)))):
        print ('Matrix is diagonally dominant')
    else:
        r: int = findStepsForDDM(X)
        print ('Matrix is NOT diagonally dominant but can be made into that form thru ', round(r), ' steps')
    return

def findStepsForDDM(arr):
 
    result = 0
    m,n = np.shape(arr)
 
    # For each row
    for i in range(m):
 
        # To store the sum of the current row
        sum = 0
        for j in range(n):
            sum += abs(arr[i][j])
 
        # Remove the element of the current row
        # which lies on the main diagonal
        sum -= abs(arr[i][i])
 
        # Checking if the diagonal element is less
        # than the sum of non-diagonal element
        # then add their difference to the result
        if (abs(arr[i][i]) < abs(sum)):
            result += abs(abs(arr[i][i]) - abs(sum))
 
    return result

check_diag_dominance(matrix)