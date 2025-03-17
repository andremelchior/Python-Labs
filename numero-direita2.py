#ex 02

n = int(input("Número? "))
result_div = n // 100
result_mul = result_div * 100
result_final = n - result_mul
print(f"O número a direita é: {result_final}")
