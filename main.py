h1, m1 = int(input()), int(input())
h2, m2 = int(input()), int(input())

startm = h1 * 60 + m1
endm = h2 * 60 + m2

for i in range(startm, endm + 1):
    h = i // 60
    m = i % 60
    print(f"{h02d}:{m02d}")