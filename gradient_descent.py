import numpy as np
import matplotlib.pyplot as plt

# Objective function
def Objective(a):
    return (a + 5)**2

# Plot
a_values = np.linspace(-15, 4, 400)
plt.plot(a_values, Objective(a_values), label='Objective Function')
plt.xlabel('a')
plt.ylabel('Objective Function Value')
plt.title('Gradient Descent Optimization')
plt.grid(True)
plt.legend()

# Initialization
x = [2]  # random parameter
tol = 0.001  # epsilon
error = 1
h = 0.01  # h of numerical derivate calculation
step = 0.05  # t_k
k = 0  # count

# Gradient Descent
while error > tol:
    grad_n1 = (Objective(x[k]) - Objective(x[k] - h)) / h
    x.append(x[k] - step * grad_n1)
    grand_n = (Objective(x[k + 1])- Objective(x[k + 1]- h)) / h
    error = abs(x[k + 1] - x[k])  # to stop algorithm
    step = abs(((x[k + 1])- x[k])*(grand_n-grad_n1)) / (abs((grand_n - grad_n1))**2)
    k += 1

    # Plot
    plt.plot(x[k], Objective(x[k]), 'ro')
    plt.xlim(-15, 4)
    plt.ylim(-50, 230)
    plt.pause(0.1)

plt.show()