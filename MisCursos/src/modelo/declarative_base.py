from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///AlumnoCurso.db')
Session = sessionmaker(bind=Engine)

Base = declarative_base()