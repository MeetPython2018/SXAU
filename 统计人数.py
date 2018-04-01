def tongji(xia,shang):
    for i in range(xia,shang):
        if (i%3 == 1) and (i%4 == 2) and (i%5 == 3):
            print("操场上的人数为：",i,"人")

tongji(100,300)