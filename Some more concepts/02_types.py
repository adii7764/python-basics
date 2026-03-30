

n : int = 5#Type annotation for an integer variable

name : str = "Alice"#Type annotation for a string variable

def sum(a: int, b: int) -> int:#Type annotation for function parameters and return type
    return a + b
sum_result : int = sum(3, 4)