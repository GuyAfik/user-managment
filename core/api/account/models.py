from core.common.serializers import ModelToDict
from core.common.database import BaseModel
from sqlalchemy import Column, Integer, String, Float


class AccountModel(BaseModel, ModelToDict):
    """
    Account Table.
    """
    __tablename__ = "Account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey('User.id'))
