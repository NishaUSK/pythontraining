#using  methods(join,split,replace)

pen = "Students have different types of pens to write"
print(" ".join(pen))
print("-------------------------------------")
print(" ".join(reversed(pen)))
print("-------------------------------------")
print(pen.split("e"))
print("-------------------------------------")
print(pen.replace("write","practice"))
