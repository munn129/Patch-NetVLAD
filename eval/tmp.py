import numpy as np
import matplotlib.pyplot as plt

# 예시 데이터 생성 (에러 값)
N = 100

errors = np.random.normal(loc=0, scale=1, size=N)  # 정규분포를 따르는 예시 에러 데이터
a_errors = np.random.normal(loc=0, scale=1, size=N)

# 에러 값이 음수일 수 있으므로 0보다 작은 값은 제거
errors = errors[errors >= 0]

# 에러의 최대값을 얻음
max_error = np.max(errors)

# 히스토그램 그리기
plt.hist(errors, bins=N,
        #  range=(0, max_error),
        #  edgecolor='black',
         alpha=0.7,
         label = 'a')

plt.hist(a_errors, bins=N,
        #  range=(0, max_error),
        #  edgecolor='black',
         alpha=0.7,
         label = 'ab')

plt.title("Error Distribution Histogram")
plt.xlabel("Error Value")
plt.ylabel("Frequency")
plt.show()
