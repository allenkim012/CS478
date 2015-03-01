import numpy as np
import matplotlib.pyplot as plt

fileTS = open('MSE_TS')
fileVS = open('MSE_VS')

TS = fileTS.readlines()

print TS

x = np.arange(-2, 2, 0.04)
y = (0.0964157711667416 - x * 0.7081355968336767) / 0.20097459091935868
# y = ( - x * 0.2699547499466077) / 0.06854811049799374


# a = [0.1, 0.2, -0.5, -0.2]
# b = [0.8, 0.2, -0.5, 0.5]

# c = [0.9, 0.7, -0.6, -0.9]
# d = [0.9, 0.9, 0.96, -0.8]

# a = [0.8, 0.6, 0.4, 0.9]
# b = [0.6, 0.4, 0.8, 0.5]

# c = [-0.4, -0.8, -0.2, -0.9]
# d = [-0.2, -0.6, 0.1, -0.8]


plt.figure('graph')
# plt.scatter(a, b, color='blue')
# plt.scatter(c, d, color='red')

plt.plot(x, y, color='green')
plt.xlabel('epochs')
plt.ylabel('MSE')
# # plt.xlim(-1,1)
# # plt.ylim(-1,1)         # restricts range of y axis from -8 to +8
# plt.axhline(color="gray", zorder=-1)

plt.show()
