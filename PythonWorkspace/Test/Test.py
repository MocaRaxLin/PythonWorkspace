from sympy import *

init_printing(use_unicode=True)
M = Matrix([[550, 30, 20, 20, 150, 636],
            [2048, 60, 35, 35, 200, 936],
            [3072, 90, 50, 50, 250, 1136],
            [4096, 120, 65, 65,300, 1336],
            [8120, 180, 100, 100, 450, 1736]])
print(M.rref())

