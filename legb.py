a = 10
API_KEY = "5sddc4d4c4dfvdvsd54sd"

def nGunc(x):
    a = 5
    for i in range(x):
        n = i + 1
        print(n)
nGunc(4)
print(a)


name = "Anna" #global value
def p_name():
    name = "Firdavs"  # p_name local valuse, p_name2 enclusive value
    print("First name " + name)
    def p_name2():
        name = "Alex" # p_name2 local value
        print("Second name " + name)
    p_name2()
p_name()
