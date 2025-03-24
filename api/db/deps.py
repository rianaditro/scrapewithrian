from sqlmodel import Session
from fastapi import Depends
from api.db.session import get_session

# Dependency for FastAPI route
def get_db(session: Session = Depends(get_session)):
    return session
