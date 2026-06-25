def RELU(x):
  return max(0, x)

y_true = [1, -1, 3]
for i in range(len(y_true)):
  y_true[i] = RELU(y_true[i])
print(y_true)

import numpy as np

# x la vector
def RELU_numpy(v):
  np_v = np.array(v)
  return np.maximum(np_v, 0)

print(RELU_numpy(y_true))


