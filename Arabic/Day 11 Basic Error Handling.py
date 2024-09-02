# التعامل مع الأخطاء باستخدام try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("لا يمكنك القسمة على الصفر!")

# التعامل مع عدة استثناءات
try:
    num = int("abc")
except ValueError:
    print("مدخل غير صالح! يرجى إدخال رقم.")
