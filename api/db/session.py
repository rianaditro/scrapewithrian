from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///scrapewithrian.db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except:
        print("Error while getting session. Please check the database file location.")