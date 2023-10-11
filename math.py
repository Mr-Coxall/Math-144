length = 1
width = 1
height = 1

for length in range(1, 144):
    for width in range(1, 144):
        for height in range(1, 144):
            if length * width * height == 144:
                print(length, width, height)    # 1 1 144