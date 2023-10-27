from scipy import sparse
import numpy as np



# create a 2d numpy array (identity matrix) with a diagonal of ones, ands zeros everywhere else


eye = np.eye(4)

print(eye)

print("Numpy Array : \n%s" %eye)


# convert the numpy array to a scipy sparse matrix in CSR format only he nonzero entries are stored

sparseMatrix = sparse.csr_matrix(eye)

print("\nScipy sparse CSR matrix : \n%s" %sparseMatrix)

