from sqlalchemy import Column, Integer, Float, Interval, ForeignKey, String

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# specific_vat(default=1.), untaxable_part(default=0.), max_taxable(default=None), flat_vat(default=0), max_vat(default=None)
class VatRule(Base):
    __tablename__ = 'vat_rules'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    product = Column(String)
    min_prevat_amount = Column(Float)
    max_prevat_amount = Column(Float)

    specific_vat = Column(Float)
    untaxable_part = Column(Float)
    max_taxable = Column(Float)
    flat_vat = Column(Float)
    max_vat = Column(Float)

    parent_id = Column(Integer, ForeignKey('vat_rules.id'))

    parent = relationship('VatRule',
                          remote_side=[id],
                          primaryjoin=('VatRule.parent_id==VatRule.id'),
                          backref=backref("right", uselist=False))


