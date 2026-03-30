try:
    a=int(input("Hey Enter a number: "))

    print(a)
except Exception as e:
    print(f"Error: {e}")
except ValueError as ve:
    print(f"Value Error: {ve}")
print("This will always execute")