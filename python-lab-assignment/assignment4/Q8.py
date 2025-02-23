def eval_exp(exp):
    return eval(exp)
exp = input("Enter an arithmetic exp (e.g., 2 + 3 * 4): ")
result = eval_exp(exp)
print("Result:", result)
