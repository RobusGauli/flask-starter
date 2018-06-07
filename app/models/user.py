from sqlalchemy import Column, Integer, String

from . import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    address = Column(String(300))

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self):

        return {key: val for key, val in vars(self).items() if isinstance(val, str)}


__all__ = ['User']
