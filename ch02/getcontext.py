import decimal #匯入decimal模組
d1=decimal.Decimal.from_float(123.4567)
d2=decimal.Decimal.from_float(34.5678)#將浮點數的型別變成decimal的型別
#取出目前decimal資料型別運算得設定值 有些設定的條件
print(decimal.getcontext())
print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)
print(d1+d2)
decimal.getcontext().prec=8     #有效位數包含整數(prec為有效位數之意思)
print(d1+d2)
