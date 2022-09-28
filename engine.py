from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('postgresql://postgres@localhost/python')
Base = declarative_base()
Session = sessionmaker(bind=engine)


