from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

ENGINE =  create_engine('postgresql://postgres:postgres@localhost/fast_2', echo=True)
Base = declarative_base()
Session = sessionmaker()
