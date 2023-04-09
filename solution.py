import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 1374771107

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
  p1 = x_success / x_cnt
  p2 = y_success / y_cnt
  p_pool = (x_success + y_success) / (x_cnt + y_cnt)

  z = (p2 - p1) / np.sqrt(p_pool * (1 - p_pool) * (1/x_cnt + 1/y_cnt))

# Find the corresponding p-value and compare to alpha level
  p_value = 1 - norm.cdf(z)
  alpha = 0.02
  reject_null = p_value < alpha

return reject_null
