#1
name = input("Введите имя:")
name = name.strip()
if name.isalnum():
    name = name.lower()
    print("Имя корректно:", name)
else:
    print("Ошибка")

#2
password = input("Введите пароль:")
digits = 0
uppers = 0
for i in password:
    if i.isdigit():
        digits += 1
    if i.isupper():
        uppers += 1
if len(password) >= 8 and digits >= 1 and uppers >= 1:
    print("Пароль надёжен")
else:
    print("Пароль слаб")

#3
log = "ACCESS DENIED"
print(log.capitalize() + " – вход запрещён")

#4
data = "ERROR connection ERROR failed access"
data1 = data.replace("ERROR","ALERT")
count_alerts = data1.count("ALERT")
print(data1, "Количество предупреждений:", count_alerts)

#5
email = input("Введите email: ")
if email.find("@") != -1:
    parts = email.split("@")
    if len(parts) == 2 and parts[1].endswith((".com", ".ru", ".org")):
        print("Домен:", parts[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")

#6
text = input("Введите текст: ")
edited = text.strip().lower().replace(" ", "_")
print(edited)


#7
message = input("Введите сообщение: ")
if message.find("SECRET") != -1:
    message = message.replace("SECRET", "**")
    print(message)
    print("Сообщение содержит конфиденциальную информацию!")
else:
    print("Сообщение безопасно.")

#8
word = input("Введите слово: ")
codes = ""
for i in word:
    codes = codes + str(ord(i)) + " "
print("Коды символов:", codes)
decoded = ""
for code in codes.split():
    decoded = decoded + chr(int(code))
print("Восстановленное слово:", decoded)

#9
text = "login attempt failed access denied unauthorized access"
if text.count("failed") > 0 or text.count(" denied") > 0:
    print("Попытка несанкционированного доступа!")
else:
    print("Доступ безопасен.")

#10
report = input("Введите отсчет: ")
sentences = report.split(".")
kolvo_sentences = 0
for i in sentences:
    kolvo_sentences = kolvo_sentences + 1
delite_spaces = report.split()
count_symbols = len(delite_spaces)
starts_with_report = report.lower().startswith("report")
error_count = report.count("error")
print("Количество предложений:", kolvo_sentences)
print("Количество символов без пробелов:", count_symbols)
print("Начинается с 'Report':", starts_with_report)
if error_count >= 2:
    print("Ошибки найдены")
else:
    print("Ошибок нет")