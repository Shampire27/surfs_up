# import our app.py file into example.py

import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

# run the script with: python app.py
# the __name__ variable will be set to __main__
