try:
    import pyodbc
    from dotenv import load_dotenv
    print("Both pyodbc and dotenv were imported successfully.")
except ImportError as e:
    print(f"import failed: {e}")