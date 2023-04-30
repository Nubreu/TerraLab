a = []
b = []
for n in range(2,51):
    if n % 2 == 0:
        a.append(n)

for n in range(2,51,2):
    b.append(n)

print("Primeira opcao\n{}".format(a))
print("Segunda opcao\n{}".format(b))