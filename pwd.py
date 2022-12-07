password = 'a123456'
x = 1
while x < 4:
	pwd = input('請輸入密碼:')
	if pwd == password: #密碼的縮寫是pwd和這裡要寫password,免得你之後要改密碼要改很多地方
		print('登入成功')
		break
	elif pwd != password and x == 1:
		print('密碼錯誤,還有兩次機會')
	elif pwd != password and x == 2:
		print('密碼錯誤,還有一次機會')
	else:
		print('密碼錯誤')
	x = x + 1