import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

import SVD_compression

# Load image
image = Image.open('data/test.jpg')
img_matrix = np.array(image)

# Split image into 3 color channels
R = img_matrix[:, :, 0]
G = img_matrix[:, :, 1]
B = img_matrix[:, :, 2]

U, Sigma, V, eval_string = SVD_compression.compress(R)
R_compressed = U @ Sigma @ V

U, Sigma, V, eval_string = SVD_compression.compress(G)
G_compressed = U @ Sigma @ V

U, Sigma, V, eval_string = SVD_compression.compress(B)
B_compressed = U @ Sigma @ V

img_matrix_compressed = np.dstack((R_compressed, G_compressed, B_compressed))

print(eval_string)

plt.figure()
plt.imshow(img_matrix.astype('uint8'))
plt.title("original")
plt.axis('off')

plt.figure()
plt.imshow(img_matrix_compressed.astype('uint8'))
plt.title("compressed")
plt.axis('off')

plt.show()
