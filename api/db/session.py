from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///scrapewithrian.db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print("================================================")
        print(f"Error in session: {e}")
        print("================================================")