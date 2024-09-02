# القوائم في بايثون
fruits = ["apple", "banana", "cherry"]

# الوصول إلى عناصر القائمة
print(fruits[0])  # العنصر الأول
print(fruits[-1])  # العنصر الأخير

# تعديل القوائم
fruits[1] = "blueberry"
print(fruits)

# إضافة وإزالة العناصر
fruits.append("orange")
fruits.remove("apple")
print(fruits)
