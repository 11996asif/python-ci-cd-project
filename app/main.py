def handler(event=None, context=None):
    print("Hello from Python CI/CD Pipeline!")
    return "Deployment Successful"

if __name__ == "__main__":
    handler()

