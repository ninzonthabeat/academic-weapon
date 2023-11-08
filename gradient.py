import numpy as np

# np.array([x, y]): 2D vector


# f(x,y) = x**2 + y**2
def f(p):
    return p[0]**2 + p[1]**2


# gradient is a vector [fx, fy]
def gradient(f, p, delta):
    # calculate partial derivative in x-direction
    rx = np.array([1, 0])
    fx = (f(p + delta*rx) - f(p - delta*rx)) / (2.0*delta)

    # calculate partial derivative in y-direction
    ry = np.array([0, 1])
    fy = (f(p + delta*ry) - f(p - delta*ry)) / (2.0*delta)
    return np.array([fx, fy])


p = [1, 2]
print("The gradient to f in point [1, 2] is equal to", gradient[f, p, 0.0001])

delta = 0.0001
step = 0.01  # lambda
p = np.array([1, 3])  # initial value
tolerance = 0.01  # done when error becomes less than tolerance
error = gradient(f, p, delta)
maxStep = 1000  # end after 1000 steps
stepCount = 1   # amount of steps so far

# lazy girl hack in order to use abs on vector
abs = np.linalg.norm

while abs(error) > tolerance and stepCount < maxStep:
    newGradient = gradient(f, p, delta)
    p = p - step*newGradient
    error = newGradient
    stepCount += 1

if stepCount >= maxStep:
    print("Algorithm ended because it took too long")
else:
    print("Algorithm used", stepCount, "steps")

print("For p =", p, "the function value is f(p)=", f(p))
print("with error =", abs(error))