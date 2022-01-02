num = int(input("請輸入欲產生數目:"))

def fab(max):
    n, a, b = 0, 0, 1
    list_num = []
    while n < max:
        list_num.append(b)
        a, b = b, b + a
        n += 1
    return list_num

for i in fab(num):
    print(i)