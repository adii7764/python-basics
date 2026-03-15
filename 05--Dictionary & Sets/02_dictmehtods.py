marks={
    "Harry":100,
    "ZYX":56,
    "Rohan":45
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99})
print(marks)
print(marks.get("Harry"))#We get none if key not exist
print(marks["Harry"])#we get error if key not exist
