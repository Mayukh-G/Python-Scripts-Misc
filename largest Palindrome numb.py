# find the largest palindrome num

n1 = 999
n2 = 999

not_done = True
not_found = True
palin = []

while not_done:
    prod = n1 * n2
    prod = str(prod)
    length = len(prod)
    if prod[length - 1] == '0':
        prod = None
    elif length % 2 == 0:
        int_half_len = int(length/2)
        for i in range(int_half_len):
            if not prod[int_half_len - 1 - i] == prod[int_half_len + i]:
                prod = None
                break
        if prod is not None:
            not_found = False
    else:
        int_half_len = int((length / 2) - 0.5)
        for i in range(int((length-1)/2)):
            if not prod[int_half_len - 1 - i] == prod[int_half_len + 1 + i]:
                prod = None
                break
        if prod is not None:
            not_found = False

    if not n1 - 1 == 99:
        n1 -= 1
    elif n2 - 1 == 99:
        not_done = False
    else:
        n2 -= 1
        n1 = 999
    if not not_found:
        palin.append(prod)
        not_found = True

max = 0
for n in palin:
    n = int(n)
    if n > max:
        max = n

print(f"Max : {max}")
print(f"list : {palin}")

