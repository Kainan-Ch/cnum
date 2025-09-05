import numpy as np
from algoritmos import (
    lu,
    jacobi,
    seidel,
)

# Sistema original:
# x1 + 10x2 + 3x3 = 27
# 4x1 + 0x2 + x3 = 6
# 2x1 + x2 + 4x3 = 12

def main():
    #Atividade3
    print("-- Atividade 3 --")
    A=np.array([[1,10,3],[4,0,1],[2,1,4]],)
    B=np.array([27.0, 6.0 , 12.0])

    # Permutação de linhas: troca a linha 0 com a linha 1
    perm = [1, 0, 2]  # novo ordem de linhas: [linha2, linha1, linha3]
    a = A[perm, :]
    b = B[perm]
    
    print("\nMatriz Original:")
    
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
    print("\nPermutação:")
    print("Matriz A:")
    print(a)
    print("\nVetor B:")
    print(b)
    print("\nSolução NumPy x:")
    X = np.linalg.solve(a, b)
    print(X)
    print("\nSolução LU x:")
    X = lu(a, b)
    print(X)
# falta a resolver Solução Jacobi Solução Seidel x:
    print("\nSolução da Permutação:")
    print ("\nSolução Jacobi x:")
    X = jacobi(a, b, 100, 1e-8)
    print(X)
    print ("\nSolução Seidel x:")
    X = seidel(a, b, 100, 1e-8)
    print(X)
"""
    print("\nSolução Jacobi x:")
    X = jacobi(A, B, 100, 1e-3)
    print(X)
    
    print("\nSolução Seidel x:")
    X = seidel(A, B, 100, 1e-3)
    print(X)
"""

if __name__ == "__main__":
    main()
