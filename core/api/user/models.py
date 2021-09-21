from core.common.serializers import ModelToDict
from core.common.database import BaseModel
from sqlalchemy import Column, Integer, String


class UserModel(BaseModel, ModelToDict):
    """
    User Table.
    """
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String, nullable=False, unique=True)
    password = Column(String)
    login_attempts = Column(Integer, default=0)

