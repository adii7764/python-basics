def http_status(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Unknown status"
print(http_status(400))  # Output: Bad Request
print(http_status(404))  # Output: Not Found
print(http_status(418))  # Output: I'm a teapot
print(http_status(500))  # Output: Unknown status
