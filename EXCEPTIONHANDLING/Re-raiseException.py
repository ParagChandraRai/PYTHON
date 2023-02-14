try:
    # Code that could raise an exception
    raise ValueError("An error occurred.")
except ValueError:
    # Catch the exception and then re-raise it
    print("Caught an exception.")
    raise
