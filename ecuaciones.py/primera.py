 #importando modulos necesarios

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import sympy
# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')


# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')


# Condición inicial
cond =({y(3): -1})

# expreso la ecuacion
f = (x**2*(y(x)) - (y(x)))/ ((y(x))+1)


# Resolviendo la ecuación
sol = sympy.Eq(y(x).diff(x) , f)
print(sol)

#Aquí encontramos la solución general de nuestra Ecuación diferencial, ahora reemplazamos los valores de la condición inicial en nuestra ecuación.
eqG = sympy.Eq(sol.lhs.subs(x, 0).subs(cond), sol.rhs.subs(x, 0))
print(eqG)

#Aquí encontramos la solución general de nuestra Ecuación diferencial, ahora reemplazamos los valores de la condición inicial en nuestra ecuación.
print(sympy.solve(eqG))