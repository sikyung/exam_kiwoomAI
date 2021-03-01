data = [('kim', 9), ('lee', 5), ('park', 10)]

result = sorted(data, key=lambda x:x[1])
print(result)

def get_sccore(t):
    return t[1]

result1 = sorted(data, key=get_sccore)
print(result1)