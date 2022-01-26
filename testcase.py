import matplotlib.pyplot as plt

while True :
    x_min = int(input("ค่า x_min : "))
    x_max = int(input("ค่า x_max : "))

    if (x_min < 1 or x_max < 1) :
        print("get only positive number")
    elif (x_min > 30000 or x_max > 30000) :
        print("value is over 30000")
    elif (x_max <= x_min) :
        print("x_max have to more than x_min")
    else :
        x_avg = (x_max + x_min) // 2
        break  
    # กำหนดค่า x

while True :
    y_min = int(input("ค่า y_min : "))
    y_max = int(input("ค่า y_max : "))

    if (y_min < 1 or y_max < 1) :
        print("get only positive number")
    elif (y_min > 30000 or y_max > 30000) :
        print("value is over 30000")
    elif (y_max <= y_min) :
        print("y_max have to more than y_min")
    else :
        y_avg = (y_max + y_min) // 2 
        break
    # กำหนดค่า y

while True :
    test = int(input("เลือกรูปแบบ testcase [1]BVA [2]Robustness [3]Worstcase [4]Worstcase for Robustness : "))
    if test == 1 :
        print("----------Boundary Value Analysis----------")
        x = [x_min, x_min+1, x_max-1, x_max]
        y = [y_min, y_min+1, y_max-1, y_max]
        n=0
        for i in x:
            n += 1
            print("["+str(n)+"]"+str(i)+","+str(y_avg))
            plt.scatter(i, y_avg, color = '#88c999')
        for j in y:
            n += 1
            print("["+str(n)+"]"+str(x_avg)+","+str(j))
            plt.scatter(x_avg, j, color = 'hotpink')
        print("["+str(n+1)+"]"+str(x_avg)+","+str(y_avg))
        plt.scatter(x_avg, y_avg, color = '#88c999')
        break
    elif test == 2 :
        print("----------Robustness----------")
        x = [x_min-1, x_min, x_min+1, x_max-1, x_max, x_max+1]
        y = [y_min-1, y_min, y_min+1, y_max-1, y_max, y_max+1]
        n=0
        for i in x:
            n+=1
            print("["+str(n)+"]"+str(i)+","+str(y_avg))
            plt.scatter(i, y_avg, color = '#88c999')
        for j in y:
            n += 1
            print("["+str(n)+"]"+str(x_avg)+","+str(j))
            plt.scatter(x_avg, j, color = 'hotpink')
        print("["+str(n+1)+"]"+str(x_avg)+","+str(y_avg))
        plt.scatter(x_avg, y_avg, color = '#88c999')
        break
    elif test == 3 :
        print("----------Worse Case----------")
        x = [x_min, x_min+1, x_max-1, x_max]
        y = [y_min, y_min+1, y_max-1, y_max]
        n = 0
        for i in x:
            for j in y:
                n += 1
                print("["+str(n)+"]"+str(i)+","+str(j))
                plt.scatter(i, j, color = '#88c999')
        n += 1
        print("["+str(n)+"]"+str(x_avg)+","+str(y_avg))
        plt.scatter(x_avg, y_avg, color = '#88c999')
        for i in x:
            n += 1
            print("["+str(n)+"]"+str(y_avg)+","+str(i))
            plt.scatter(i, y_avg, color = 'hotpink')
        for j in y:
            n += 1
            print("["+str(n)+"]"+str(x_avg)+","+str(j))
            plt.scatter(x_avg, j, color = '#88c999')
            break
    elif test == 4 :
        print("----------Worse Case for robustness----------")
        x = [x_min-1, x_min, x_min+1, x_max-1, x_max, x_max+1]
        y = [y_min-1, y_min, y_min+1, y_max-1, y_max, y_max+1]
        n = 0
        for i in x:
            for j in y:
                n += 1
                print("["+str(n)+"]"+str(i)+","+str(j))
                plt.scatter(i, j, color = '#88c999')
        n += 1
        print("["+str(n)+"]"+str(x_avg)+","+str(y_avg))
        plt.scatter(x_avg, y_avg, color = '#88c999')
        for i in x:
            n += 1
            print("["+str(n)+"]"+str(y_avg)+","+str(i))
            plt.scatter(i, y_avg, color = 'hotpink')
        for j in y:
            n += 1
            print("["+str(n)+"]"+str(x_avg)+","+str(j))
            plt.scatter(x_avg, j, color = '#88c999')
            break
    else :
        print("choose wrong option, please try again")
    # เลือก testcase

plt.show()