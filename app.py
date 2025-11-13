"""
Simple greeting application for Jenkins CI/CD demonstration.
"""

def greet(name):
    """
    Returns a personalized greeting message.

    Args:
        name (str): The name to greet

    Returns:
        str: A greeting message
    """
    return f"Hello, {name} from Hussein Yaacoub!"

def farewell(name):
    """
    Returns a farewell message.

    Args:
        name (str): The name to say goodbye to

    Returns:
        str: A farewell message
    """
    return f"Goodbye, {name}!"

def main():
    """Main function to demonstrate the application."""
    print(greet("World"))
    print(farewell("World"))

if __name__ == "__main__":
    main()