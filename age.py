driving = input("請問你有沒有開過車? ")
if driving != '有' and driving != '沒有':
	print('只能輸入「有」或「沒有」')
	raise SystemExit

age = int(input("請問你的年齡? "))

if driving == "有":
	if age >= 18:
		print("你通過測驗了!")
	else:
		print("你很強!!")
elif driving == "沒有":
	if age >= 18:
		print("可以去考駕照了")
	else:
		print("再過幾年就可以去考了")
else:
	print("只能輸入「有」或「沒有」")		