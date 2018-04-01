for hang in range(1,10):
    '''if (hang==3):
        continue'''
    for lie in range(1,hang+1):
        if (hang==3 and lie==3) or (hang==4 and lie==3):
            print("  ",end="")
        else:
            print(" ",end="")
        print("%d*%d=%d" %(hang,lie,hang*lie),end=" ")
    print("")
