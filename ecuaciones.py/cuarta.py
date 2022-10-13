#importando modulos necesarios

from cmath import e, pi, sin
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import sympy
import math


# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')

# defino las incognitas
y = sympy.Function('y')
x = sympy.Symbol('x')


# expreso la ecuacion
f =(2*x*y(x).diff(x)-y(x), 3*x**2)
print("La ecuación es:",f)

# Resolviendo la ecuación
sol = sympy.Eq(y(x).diff(x) , f)
print("La respuesta es",sympy.dsolve(y(x).diff(x)))
