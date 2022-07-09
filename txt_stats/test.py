
with open("data.json", 'rb') as f:
    contents = f.read()

with open("data1.json", "w") as w:
    w.write(str(contents))

print("OK")
