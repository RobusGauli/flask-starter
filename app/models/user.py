from sqlalchemy import Column, Integer, String

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))


__all__ = ['User']
