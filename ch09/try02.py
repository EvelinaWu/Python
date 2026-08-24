def div(n1, n2):
    try:
        res = n1 / n2
        print(f'{n1}/{n2}={res}')
    except Exception as e:
       print('錯誤類型:', end ='')
       print(e)


div(8,0) #有異常程式就不會跑完
div(8,5)
