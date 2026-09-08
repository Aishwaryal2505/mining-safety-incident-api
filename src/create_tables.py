from src.database import engine, Base
from src.models import Incident

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully in PostgreSQL")


if __name__ == "__main__":
    create_tables()