import click
from flask import Blueprint
import requests
import pandas as pd
import json

hawkins = Blueprint("hawkins", __name__)

@hawkins.cli.command("fetch")
@click.argument("api_key")
def fetch_data(api_key):
    access_token = get_access_token(api_key)
    print("> acquired access token")

    tennis_team_id = get_team_id_by_name("Tennis", access_token)
    print(f"> tennis team id is {tennis_team_id}")

    tennis_tests = get_tests_of_team(tennis_team_id, access_token)["data"]

    df = pd.read_json(json.dumps(tennis_tests))

    # filter to columns of interest
    columns_that_matter = [ "athlete", "segment", "timestamp", 'Jump Momentum(kg.m/s)',   'Takeoff Velocity(m/s)', 'Peak Velocity(m/s)']
    df = df[columns_that_matter]

    # shuffle athletes
    df['athlete'] = df["athlete"].sample(frac=1).values

    def extract_name_from_athlete_json(athlete_val):
        raw_name = athlete_val["name"]
        words = raw_name.split(" ")
        name = " ".join([word.capitalize() for word in words])
        return name

    # extract names from the athletes
    df['athlete'] = df['athlete'].apply(extract_name_from_athlete_json)

    print(df)

    df.to_csv("data/tennis_hawkins_anonymized.csv", index = False)

def get_access_token(api_key):
    response = requests.get("https://cloud.hawkindynamics.com/api/token",
            headers={'Authorization': f'Bearer {api_key}'})

    assert response.status_code == 200

    data = response.json()
    access_token = data["access_token"]

    return access_token

def get_tests_of_team(team_id, access_token):
    response = requests.get(f"https://cloud.hawkindynamics.com/api/athletemonitoring?teamId={team_id}",
        headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200

    print(response.text)
    data = response.json()

    return data

def get_team_id_by_name(name, access_token):
    teams = get_teams(access_token)
    for team in teams:
        if team["name"] == name:
            return team["id"]

    assert False

def get_teams(access_token):
    response = requests.get("https://cloud.hawkindynamics.com/api/athletemonitoring/teams",
        headers={'Authorization': f'Bearer {access_token}'})

    assert response.status_code == 200

    data = response.json()["data"]
    return data
