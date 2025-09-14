import numpy as np
from algoritmos import jacobi, seidel

# Atividade 3
# Faça uma permutação de linhas no sistema abaixo e resolva pelos métodos de Jacobi e Gauss-Seidel:
# x1 + 10x2 + 3x3 = 27
# 4x1 + 0x2 + x3 = 6
# 2x1 + x2 + 4x3 = 12

def main():
    print("-- Atividade 3 --")

    # Matriz de coeficientes do sistema original
    A = np.array([[1, 10, 3], [4, 0, 1], [2, 1, 4]])

    # Vetor de termos independentes
    B = np.array([27.0, 6.0, 12.0])

    # O sistema original não é diagonalmente dominante.
    # É necessário permutá-lo para que os métodos de Jacobi e Gauss-Seidel convirjam.
    
    # Permutação de linhas para tornar a matriz diagonalmente dominante
    # Trocando a linha 0 com a 1, e a 1 com a 2, a matriz se torna:
    # 4x1 + 0x2 + x3 = 6
    # 2x1 + x2 + 4x3 = 12
    # x1 + 10x2 + 3x3 = 27

    perm = [1, 2, 0]
    a = A[perm, :]
    b = B[perm]

    print("\nMatriz Original A:")
    print(A)
    print("\nVetor Original B:")
    print(B)

    print("\nMatriz Permutada a (Diagonalmente Dominante):")
    print(a)
    print("\nVetor Permutado b:")
    print(b)

    # Resolvendo o sistema permutado pelos métodos de Jacobi e Gauss-Seidel
    print("\nSolução pelo método de Jacobi:")
    X_jacobi = jacobi(a, b, 100, 1e-8)
    print(X_jacobi)

    print("\nSolução pelo método de Gauss-Seidel:")
    X_seidel = seidel(a, b, 100, 1e-8)
    print(X_seidel)

if __name__ == "__main__":
    main()
