import csv
from flask import Flask
from faker import Faker
from flask_sqlalchemy import SQLAlchemy
from .models import User, Entry, Team
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint

# Writing 100 random users to a csv file
def writeUsersCSV():
    fake = Faker()

    # Write the users to a csv file
    with open("users.csv", 'w') as file:
        writer = csv.writer(file)
        for i in range(100):
            user = User(email = fake.email(), password = generate_password_hash("password", method='sha256'), first_name = fake.first_name(), last_name = fake.last_name(), permission_id = randint(1, 3))
            writer.writerow([fake.email(), user.first_name, user.last_name, user.password, user.permission_id])
        print('Wrote User CSV files')
