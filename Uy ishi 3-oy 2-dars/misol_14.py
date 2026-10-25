sonlar = list(map(int, input("Sonlarni kiriting: ").split()))
musbatlar = []
for son in sonlar:
    if son > 0:
        musbatlar.append(son)
print(musbatlar)
