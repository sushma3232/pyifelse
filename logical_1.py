# 4
# 200 100 400       Charlie
# 155 1000 566      bob
# 736 234 470       alice
# 124 67 2          alice


a=int(input("enter the num"))
for i in range(a):
    maximum=0
    a=int(input("enter num"))
    b=int(input("enter num"))
    c=int(input("enter num"))
    if(max(a,b,c)==a):
        print("Alice")
    elif(max(a,b,c)==b):
        print("bob")
    else:
        print("charlie")