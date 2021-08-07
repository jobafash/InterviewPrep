#This script is for visualizing loops
n = 3
# for i in range(n):
#     for j in range(n):
#         print(i, "        ", j)
# 0          0
# 0          1
# 0          2
# 1          0
# 1          1
# 1          2
# 2          0
# 2          1
# 2          2

# for i in range(n):
#     for j in range(i + 1, n):
#         print(i, "        ", j)
# 0          1
# 0          2
# 1          2

# for i in range(n):
#     for j in range(n - i - 1):
#         print(i, "        ", j)
# 0          0
# 0          1
# 1          0

# for i in range(n):
#     for j in range(1, n):
#         print(i, "        ", j)
# 0          1
# 0          2
# 1          1
# 1          2
# 2          1
# 2          2

# for i in range(n//2):
#     for j in range(1, n):
#         print(i, "        ", j)
# 0          1
# 0          2

# for i in range(n//2):
#     for j in range(n):
#         print(i, "        ", j)
# 0          0
# 0          1
# 0          2