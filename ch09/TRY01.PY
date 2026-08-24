def div(n1, n2):
    try:
        res = n1 / n2
        print(f'{n1}/{n2}={res}')

div(8,0) #有異常程式就不會跑完
div(8,5)


    except ZeroDivisionError as e:
        print('除數不能為0')
        return None