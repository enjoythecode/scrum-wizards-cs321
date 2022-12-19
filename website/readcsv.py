import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import User, Entry, Team

# Function to read user csv file and populate database
def readUsersCSV(filepath):
    db = SQLAlchemy()

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create a new user object
            user = User(email=row[0], first_name=row[1], last_name=row[2], password=row[3], permission_id=row[4])
            # Add the new User to the database
            db.session.add(user)
        # Commit all the changes
        db.session.commit()
        print('Read User CSV files and added to the database')

# Function to read team csv file and populate database
def readTeamsCSV(filepath):
    db = SQLAlchemy()

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create a new team object
            team = Team(name=row[0], season_start_date=row[1], season_end_date=row[2])
            # Add the new Team to the database
            db.session.add(team)
        # Commit all the changes
        db.session.commit()
        print('Read Team CSV files and added to the database')

# Function to read entry csv file and populate database
def readEntriesCSV(filepath):
    db = SQLAlchemy()

    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Create a new entry object
            entry = Entry(user_id=row[0], team_id=row[1], category=row[2], date=row[3], value=row[4])
            # Add the new Entry to the database
            db.session.add(entry)
        # Commit all the changes
        db.session.commit()
        print('Read Entry CSV files and added to the database')
