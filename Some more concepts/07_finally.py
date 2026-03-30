def main():
    try:
        a=int(input("Enter a number: "))

        print(a)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("No exceptions occurred, the number is valid.")
    finally:
        print("Execution completed.")
main()
