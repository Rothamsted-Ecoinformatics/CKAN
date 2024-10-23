
def customapi_hello():
    return "Hello, customapi!"


def get_helpers():
    return {
        "customapi_hello": customapi_hello,
    }
