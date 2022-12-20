# Importing the csv module to write to a csv file
import csv
# Importing the Flask module
from flask import Flask
# Importing the Faker module to generate fake data
from faker import Faker
# Importing the SQLAlchemy module
from flask_sqlalchemy import SQLAlchemy
# Importing the User, Entry, and Team models
from .models import User, Entry, Team
# Importing the generate_password_hash and check_password_hash functions from the werkzeug.security module to hash passwords
from werkzeug.security import generate_password_hash, check_password_hash
# Importing the random module to generate random numbers
from random import randint

# Writing 100 random users to a csv file
def writeUsersCSV():
    # Create a Faker object
    fake = Faker()

    # Write the users to a csv file
    with open("users.csv", 'w') as file:
        writer = csv.writer(file)
        # Writing 100 random users to the csv file
        for i in range(100):
            # Create a new user object
            user = User(email = fake.email(), password = generate_password_hash("password", method='sha256'), first_name = fake.first_name(), last_name = fake.last_name(), permission_id = randint(1, 3))
            # Write the user to the csv file
            writer.writerow([fake.email(), user.first_name, user.last_name, user.password, user.permission_id])
        print('Wrote User CSV files')
