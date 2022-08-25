from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, TIMESTAMP, text

Base = declarative_base()


class GistRequest(Base):
    __tablename__ = "gist_request"
    id = Column(INTEGER, primary_key=True)
    username = Column(String(1024), nullable=False)
    at = Column(TIMESTAMP, nullable=False,
                        server_default=text("CURRENT_TIMESTAMP"))
