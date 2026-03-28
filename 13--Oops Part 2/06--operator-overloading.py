class NUmbber:
    def __init__(Self,num):
        Self.num=num
    def __add__(Self,other):
        return NUmbber(Self.num + other.num)
n=NUmbber(5)
m=NUmbber(10)
r=n+m
print(r.num)