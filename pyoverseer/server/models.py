from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    """A client providing one or more services."""

    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(32), index=True)
    name = Column(String)

    def __repr__(self):
        return '<Client "%s">' % self.name

class Service(Base):
    """A distinct service providing a group of metrics."""

    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    name = Column(String)

    client = relationship('Client', backref=backref('services', order_by=name))

    def __repr__(self):
        return '<Service "%s">' % self.name

class Metric(Base):
    """A statistic from a service being monitored."""

    __tablename__ = 'metric'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('service.id'))
    name = Column(String)

    service = relationship('Service', backref=backref('metrics', order_by=name))

    def __repr__(self):
        return '<Metric "%s">' % self.name

class Sample(Base):
    """An individual sample from a metric."""

    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    metric_id = Column(Integer, ForeignKey('metric.id'))
    date = Column(DateTime)
    data = Column(Numeric)

    metric = relationship('Metric', backref=backref('samples', order_by=date))

    def __repr__(self):
        return '<Sample "%s">' % self.data
