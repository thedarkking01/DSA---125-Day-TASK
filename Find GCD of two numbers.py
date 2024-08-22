# 1 - approach point comlexity = o(n)
def gcd(a,b):
    while a>0 and b>0:
        if a>b:
            a = a%b
        else:
            b = b%a
    if a==0:
        return b
    return a

# 2- approach point  complexity= o(n)
def find_gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i
    return 1

def main():
    n1 = 20
    n2 = 15

    # Find the GCD of n1 and n2
    gcd = gcd(n1, n2)

    print(f"GCD of {n1} and {n2} is: {gcd}")


if __name__ == "__main__":
    main()