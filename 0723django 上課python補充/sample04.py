height_cm = float(input("請輸入身高（公分）："))
weight_kg = float(input("請輸入體重（公斤）："))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print(f"您的 BMI 是：{bmi:.2f}")