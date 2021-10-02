from core.common.serializers import ModelToDict
from core.common.database import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class AccountModel(BaseModel, ModelToDict):
    """
    Account Table.
    """
    __tablename__ = "Account"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False, unique=True)
    amount = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey('User.id'))
