from sqlalchemy import Column, Integer, Float, Interval, ForeignKey, String, create_engine

from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VatRule(Base):
    __tablename__ = 'vat_rules'

    id = Column(Integer, primary_key=True)
    area_id = Column(Integer, nullable=False)
    product_id = Column(Integer)
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

    def calculate_vat(self, pre_vat):
        specific_vat = self.specific_vat or 1.0
        untaxable_part = self.untaxable_part or 0.0
        flat_vat = self.flat_vat or 0.0

        deductions = pre_vat - untaxable_part

        if self.max_taxable:
            deductions = min(deductions, self.max_taxable)

        vat_added = specific_vat * deductions + flat_vat

        if self.max_vat:
            vat_added = min(vat_added, self.max_vat)

        return pre_vat + vat_added, vat_added


engine = create_engine('postgresql://postgres:1234@172.17.0.2:5432/postgres') #ad pg stuff here

Session = sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)