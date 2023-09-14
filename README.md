# SVD-image-compression
This project is an implementation of an image compression algorithm based on singularity value decomposition.

## Algorithm
1. Split image into 3 color channel matrices
2. For each matrix:
3. Perform a singularity value decomposition
4. Remove the k smallest singularity values from the diagonal matrix
5. Remove the last k columns of matrix U
6. Remove the last k rows of matrix V
