#importando modulos necesarios

from cmath import e, pi, sin
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import sympy
import math
math.pi
math.e
math.sin
N=5
nep = math.log( N )
# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')

# defino las incognitas
y = sympy.Function('y')
x = sympy.symbols('x')

# Condición inicial
cond =({y(pi/2): e})


# expreso la ecuacion
f =sympy.Eq(sin(x)*y(x).diff(),y(x)*nep(y(x)))


# Resolviendo la ecuación
sol = sympy.Eq(y(x).diff(x) , f)
print(sol)

#Aquí encontramos la solución general de nuestra Ecuación diferencial, ahora reemplazamos los valores de la condición inicial en nuestra ecuación.
eqG = sympy.Eq(sol.lhs.subs(x, 0).subs(cond), sol.rhs.subs(x, 0))
print(eqG)

#Aquí encontramos la solución general de nuestra Ecuación diferencial, ahora reemplazamos los valores de la condición inicial en nuestra ecuación.
print(sympy.solve(eqG))