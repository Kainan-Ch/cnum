import numpy as np

from algoritmos import (
    lu,
    jacobi,
    seidel,
)
"""
Sistema de equações:

5x1 + x2  + x3  = 50
-x1 + 3x2 + x3  = 10
x1  + 2x2 + 10x3  =-30
"""

def main():

    # Atividade 2
    print("-- Atividade 2 --")
    
    #Coeficientes da matriz
    A = np.array([[5, 1, 1], [-1, 3, 1], [1, 2, 10]])
    
    #Vetor de termos independentes
    B = np.array([50.0, 10.0, -30.0])
    
    print("Matriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(A, B)
    print(X)
    
    print("\nSolução LU x:")
    X = lu(A, B)
    print(X)
    A = np.array([[1, 2, 10], [-1, 3, 1],[5, 1, 1] ], dtype=float)
    B = np.array([-30.0, 10.0,50.0 ], dtype=float)
    
    print("\nMatriz A:")
    print(A)
    print("\nVetor B:")
    print(B)
    
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-3)
    print(X)
    
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-3)
    print(X)

if __name__ == "__main__":
    main()