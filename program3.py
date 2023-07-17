def generate_odd_series(a):
    if  a<1:
        return"Input value must be in greater than or equal to 1>"
    series=[]
    for i in range(1,a+1):
        if i %2 !=0:
            series.append(str(i))
    return",".join(series)
a = int(input("ENTER THE VALUE OF A :"))
series = generate_odd_series(a)
print("Output", series)