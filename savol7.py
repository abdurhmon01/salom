def list1(a):
    salom = []
    for i in a:
        salom.append([i, a[i]])
    return salom
print(list1({ "a": 1, "b": 2 }))