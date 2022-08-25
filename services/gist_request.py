import datetime

import sqlalchemy.exc
from sqlalchemy import and_

from db.database import Database
from models.models import GistRequest

database = Database()
engine = database.get_db_connection()


def get_gist_request_date_by_username(username: str):
    session = database.get_db_session(engine)
    try:
        gist_request = session.query(GistRequest).filter(and_(GistRequest.username == username)).one()
        at = gist_request.at
        session.flush()
        session.commit()
        session.close()
        return at
    except sqlalchemy.exc.NoResultFound:
        return None


def update_gist_request_date(username: str):
    session = database.get_db_session(engine)
    gist_queryset = session.query(GistRequest).filter(and_(GistRequest.username == username))
    gist_queryset.update({
        GistRequest.at: datetime.datetime.now()
    }, synchronize_session=False)
    session.flush()
    session.commit()


def create_gist_request(username: str):
    new_request = GistRequest()
    new_request.username = username
    session = database.get_db_session(engine)
    session.add(new_request)
    session.flush()
    session.commit()
    session.close()
