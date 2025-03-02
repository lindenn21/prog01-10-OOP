
ODD = 0
for i in range(0, 10):
    NUM = float(input(f"Input number {i + 1}:"))
    if NUM % 2 != 0:
        ODD += 1

print(ODD)
