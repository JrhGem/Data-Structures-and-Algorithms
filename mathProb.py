import matplotlib.pyplot as plt
import numpy as np

# Define the mathematical functions to be plotted
def f1(x):
    return x**2 + 7*x + 2

def f2(x):
    return 3*x + 2

def f3(x):
    return x**2

def f4(x):
    return x**3

def f5(x):
    return x**5

def f6(x):
    return x**3 + 2*x**2 + x + 10

def f7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def f8(x):
    return np.sin(x)

def f9(x):
    return np.cos(x)

def f10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

while True:
    # Load the input values from a file
    with open('mathProb.txt') as f:
        x = [int(line.strip()) for line in f]

    # Choose the function to be plotted
    print()
    print("1. x^2 + 7x + 2")
    print("2. 3x + 2")
    print("3. x^2")
    print("4. x^3")
    print("5. x^5")
    print("6. x^3 + 2(x^2) + x + 10")
    print("7. x^4 - 3(x^3) + 2(x^2) - x + 11")
    print("8. sin(x)")
    print("9. cos(x)")
    print("10. x^5 + 4(x^4) + x^3 - 2(x^2) + 100")
    print("11. Exit")
    
    func_num = int(input("Enter the function number (1-10) to be plotted or 11 to exit: "))

    if func_num == 11:
        break

    if 1 <= func_num <= 10:
        # Plot the chosen function
        if func_num == 1:
            y = [f1(i) for i in x]
        elif func_num == 2:
            y = [f2(i) for i in x]
        elif func_num == 3:
            y = [f3(i) for i in x]
        elif func_num == 4:
            y = [f4(i) for i in x]
        elif func_num == 5:
            y = [f5(i) for i in x]
        elif func_num == 6:
            y = [f6(i) for i in x]
        elif func_num == 7:
            y = [f7(i) for i in x]
        elif func_num == 8:
            y = [f8(i) for i in x]
        elif func_num == 9:
            y = [f9(i) for i in x]
        elif func_num == 10:
            y = [f10(i) for i in x]

        # Plot the function
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Function {func_num}')
        plt.grid()
        plt.show()

    else:
        print("Invalid function number")
        continue