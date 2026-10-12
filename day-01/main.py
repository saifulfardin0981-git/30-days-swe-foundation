import sys
import platform 

def main():
    user_name = "Future Software Engineer"
    py_version = platform.python_version()
    os_name = platform.system()

    print("=" * 40)
    print(f"Day 1 Execution Logged for: {user_name}")
    print(f"Os: {os_name}")
    print(f"Python Version: {py_version}")
    print("Status: 30-Day Foundation Underway")
    print("=" * 40)

if __name__ == "__main__":
    main()