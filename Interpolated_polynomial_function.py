from sympy import symbols, interpolate

def interpolate_points_lagrange(points, max_precision):

    x_values, y_values = zip(*points)    
    x = symbols('x')

    if len(points) < 2:
        return points[0][1]
    
    interpolated_function = interpolate(list(zip(x_values, y_values)), x) #Lagrange
    
    rounded_function = interpolated_function.evalf(n=max_precision)  
    rounded_function_str = str(rounded_function).replace('**', '^')
    
    return rounded_function_str

points = []
while True:
    point_input = input("New point '(x, y)' : ")
    if not point_input:
        break
    try:
        x, y = map(float, point_input.strip('()').split(','))
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
        if any(point[0] == x for point in points):
            print("two points cannot have the same x value")
            continue
        points.append((x, y))
    except ValueError:
        print("Wrong Format")

while True:
    max_precision_input = input("precision : ")
    try:
        max_precision = int(max_precision_input)
        break
    except ValueError:
        print("Should be integer")

fitted_function = interpolate_points_lagrange(points, max_precision)

print("\nPoints :", end=" ")
for point in points:
    if point!=points[-1]: print(f"({point[0]:g}, {point[1]:g})", end=",")
    else: print(f"({point[0]:g}, {point[1]:g})", end="")
    
print("\nInterpolated polynomial function :", fitted_function)
input("\nAppuyez sur n'importe quelle touche pour quitter...")
