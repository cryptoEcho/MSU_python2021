for a in range(20):
    if a == 10:
        break
    a += 1
    print(a)
    if a < 7:
        continue
    print(a)