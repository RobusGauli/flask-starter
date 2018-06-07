from sqlalchemy import Column, Integer, String

from . import Base


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    depart_name = Column(String(40))


__all__ = ['Department']
