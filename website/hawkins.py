import click
from flask import Blueprint

hawkins = Blueprint("hawkins", __name__)

@hawkins.cli.command("fetch")
@click.argument("api_key")
def fetch_data(api_key):
    print(f"key: {api_key}")
