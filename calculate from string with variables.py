# w pliku dane.txt:
# <- znak komentarza, = <- definiowanie zmiennej, == <- deiniowanie wzoru
import json
from math import *


file_path_splitted = __file__.split("/")[0:-1]
file_path = ""
for item in file_path_splitted:

    file_path += item+"/"


with open(file_path+"dane.txt", mode="r") as file:
    lines = []
    for line in file:
        if "#" not in line:
            lines.append(line.rstrip("\n").strip(" "))

    variables = ""
    equation = ""

    for line in lines:
        if "==" in line:
            equation = line.split("==")

        else:
            try:
                line_splitted = line.split("=")
                variables += '"' + \
                    line_splitted[0].strip(
                        " ") + '"' + ": " + line_splitted[1].strip(" ") + ","
            except IndexError:
                pass

    variables = "{" + variables[0:-1] + "}"

variables = json.loads(variables)

print(variables)

math_methods = ['factorial', 'acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs',
                'floor', 'fmod', 'hypot', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']


for method in math_methods:
    variables[method] = eval(method)

result = equation[0] + "= " + str(eval(equation[1], variables))

with open(file_path+"dane.txt", mode="a") as file:
    file.write("\n"+"# "+result)

print(result)
