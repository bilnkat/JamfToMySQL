from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
import os

sql = os.environ.get('SQL_URI')
engine = create_engine(sql, echo=True)

Base = declarative_base()

class Computer(Base):
    __tablename__ = 'AllComputers'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=False, nullable = False)
    managed = Column(Boolean, unique=False, nullable = False)
    username = Column(String(20), unique=False, nullable = False)
    model = Column(String(100), unique=False, nullable = False)
    department = Column(String(20), unique=False, nullable = True)
    building = Column(String(20), unique=False, nullable = True)
    mac_address = Column(String(20), unique=False, nullable = False)
    udid = Column(String(20), unique=False, nullable = False)
    serial_number = Column(String(20), unique=False, nullable = False)
    report_date_utc = Column(String(20), unique=False, nullable = False)
    report_date_epoch = Column(String(20), unique=False, nullable = False)

    def __repr__(self):
        return '{} {}'.format(self.id, self.username)