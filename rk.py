h = float(input("enter (h): "))
y0 = float(input("enter (y0): "))
x0 = float(input("enter (x0): "))
xn = float(input("enter (xn): "))
n = int((xn - x0) / h) + 1
func = input("enter function f(x,y): ")
x = [0]*n
y = [0]*n
x[0] = x0
y[0] = y0

def f(x, y):
    return eval(func, {"__builtins__": None}, {"x": x, "y": y, "math": __import__('math')})

for i in range(1, n):
    x[i] = x[0] + i*h
    k1 = h*f(x[i-1], y[i-1])
    k2 = h*f(x[i-1] + 0.5*h, y[i-1] + 0.5*k1)
    k3 = h*f(x[i-1] + 0.5*h, y[i-1] + 0.5*k2)
    k4 = h*f(x[i-1] + h, y[i-1] + k3)
    y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
    print(f" for {i}={k1:.4f}\n {k2:.4f} \n{k3:.4f}\n{k4:.4f}\n")

print("\nResults:")
for i in range(n):
    print(f"x[{i}] = {x[i]:.4f}, y[{i}] = {y[i]:.4f}")
