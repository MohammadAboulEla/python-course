# القواميس في بايثون
person = {
    "name": "Alice",
    "age": 15,
    "city": "New York"
}

# الوصول إلى قيم القاموس
print(person["name"])
print(person["age"])

# إضافة وإزالة عناصر من القاموس
person["email"] = "alice@example.com"
del person["city"]
print(person)
