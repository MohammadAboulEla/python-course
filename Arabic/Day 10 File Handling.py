# الكتابة إلى ملف
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# القراءة من ملف
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
