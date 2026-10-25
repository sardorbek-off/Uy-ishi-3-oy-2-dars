sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
juftlar = []
for son in sonlar:
    if son % 2 == 0:
        juftlar.append(son)
print(juftlar)
