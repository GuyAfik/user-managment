import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database


engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI', "sqlite:///UserDB.db"), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class CustomBase(object):
    """
    Enables the models to have the DB methods.
    """
    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

    @classmethod
    def __tablename__(cls):
        return cls.__name__.lower()

    def save(self):
        """
        Save the model into the DB.

        Returns:
            CustomBase: any CustomBase subclass.
        """
        db_session.add(self)
        CustomBase._commit()
        return self

    def update(self, **kwargs):
        """
        Update the model into the DB.

        Returns:
            CustomBase: any CustomBase subclass.
        """
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self.save()

    def delete(self):
        """
        Delete the model from the DB.
        """
        db_session.delete(self)
        CustomBase._commit()

    @staticmethod
    def _commit():
        """
        Commit the DB, rollback in case of a failure.

        Raises:
            DatabaseError: any error that the DB raises.
        """
        try:
            db_session.commit()
        except DatabaseError as e:
            # print(str(e))
            # print(type(e))
            db_session.rollback()
            raise e


BaseModel = declarative_base(cls=CustomBase, constructor=None)
BaseModel.query = db_session.query_property()


def init_db():
    """
    Create database if doesn't exist and
    create all tables.
    """
    if not database_exists(engine.url):
        create_database(engine.url)
    BaseModel.metadata.create_all(bind=engine)


def drop_db():
    """
    Drop all of the record from tables and the tables
    themselves.
    Drop the database as well.
    """
    BaseModel.metadata.drop_all(bind=engine)
    drop_database(engine.url)
