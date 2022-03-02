from main import db
from flask import Blueprint
import random

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    """Creates tables in the database based on the models."""
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    """Drops all tables in the database"""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")

@db_commands.cli.command("seed")
def seed_db():
    from schemas.street_schema import single_street_schema
    from faker import Faker
    faker = Faker()

    for i in range(20):
        street = single_street_schema.load(
            {
                "street_name": faker.street_name(), 
                'street_flooded': random.choice([True, False])
            }
        )
        db.session.add(street)
    
    db.session.commit()
    print("Tables seeded!")