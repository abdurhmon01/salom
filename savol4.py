def reverse(a):
    if len(a)==0:
        return a
    else:
        return reverse(a[1:]) + a[0] 
print(reverse("Salom"))