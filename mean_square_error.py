# y_true, y_pred la vector
def mse_pure(y_true, y_pred):
  mse = 0
  if len(y_true) == len(y_pred):
    for i in range(len(y_true)):
      mse += (y_true[i] - y_pred[i])**2
  else: 
    return
  return mse / len(y_true)

import numpy as np
import pandas as pd

def mse_numpy(y_true, y_pred):
  np_true = np.array(y_true)
  np_pred = np.array(y_pred)
  return np.mean((np_true - np_pred) ** 2)

# y_true_1 = [1.0, 2.0, 3.0, 4.0]
# y_pred_1 = [1.0, 2.0, 3.0, 4.0]
# print("Test 1 (Hoàn hảo):", mse_pure(y_true_1, y_pred_1)) 
