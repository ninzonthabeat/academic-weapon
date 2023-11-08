import numpy as np

"""
There are 3 methods to find the derivative:
Symbolically (slow, requires equation)
Numerically (quick, no need for equation, approximation)
Automaitcally (quick, must have a "def f()", not an approximation) --> advanced
"""


def f(x):
    return x**2


# gradient = the derivative for a given variable
# f'(x) = (f(x+delta) - f(x-delta)) / (2*delta)
# f is the function to find the derivative of
# x is the point of derivation
# delta is the number in the approximation
def gradient(f, x, delta):
    return (f(x + delta) - f(x - delta))/(2*delta)


def g(x):
    return np.cos(x**4) * np.sin(x**2 + 4.0)**4


print("f'(4) =", gradient(f, 4, 0.001))
print("g'(5) =", gradient(g, 5.0, 0.0001))


delta = 0.0001
step = 0.01  # lambda
x = 3  # initial value
tolerance = 0.01  # done when error becomes less than tolerance
error = gradient(f, x, delta)
maxStep = 1000  # end after 1000 steps
stepCount = 1   # amount of steps so far

while abs(error) > tolerance and stepCount < maxStep:
    newGradient = gradient(f, x, delta)
    x = x - step*newGradient
    error = newGradient
    stepCount += 1

if stepCount >= maxStep:
    print("Algorithm ended because it took too long")
else:
    print("Algorithm used", stepCount, "steps")

print("For x =", x, "the function value is f(x)=", f(x))
print("with error =", abs(error))