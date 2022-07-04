# 별찍기
i = int(input())
for k in range(1, i+1):
    print("*"*k)

# 별찍기2
i = int(input())
for k in range(1, i+1):
    print(" "*(i-k)+"*"*k)

# 별찍기3
i = int(input())
for k in range(1, i+1):
    print("*"*((i+1)-k))

