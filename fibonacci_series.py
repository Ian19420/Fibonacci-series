num = int(input("請輸入欲產生數目:"))

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, b + a
        n += 1
fab(num)