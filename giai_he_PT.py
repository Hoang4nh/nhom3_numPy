#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn 
import numpy as np

# Ma trận hệ số A
A = np.array([[1, 2], [3, 4]])

# Véc-tơ b
B = np.array([5, 6])

# Tìm ma trận nghịch đảo của A
C = np.linalg.inv(A)

# Tìm nghiệm của hệ phương trình
X = np.dot(C, B)

print('Ma trận A:')
print(A)
print('Véc-tơ B:')
print(B)
print('Ma trận nghịch đảo của A:')
print(C)
print('Nghiệm của hệ phương trình:')
print(X)
