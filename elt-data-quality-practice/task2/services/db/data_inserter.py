from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from typing import List

def insert_data(engine: Engine, instances: List):
    """
    Inserts a list of ORM instances into the database.

    Args:
        engine (Engine): The SQLAlchemy engine to bind the session to.
        instances (List): List of ORM instances to insert.
    """
    with Session(bind=engine) as session:
        session.add_all(instances)
        session.commit()
    print(f"{len(instances)} instances inserted successfully!")