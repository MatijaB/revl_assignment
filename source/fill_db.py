from models import Session, VatRule

session = Session()

# eu general
session.add(VatRule(
    area_id = 1,
    specific_vat = 0.125,
))
# eu bread
session.add(VatRule(
    area_id = 1,
    product_id = 1,
    flat_vat = 0.05,
))
# germany general
session.add(VatRule(
    area_id = 2,
    specific_vat = 0.15,
))
# germany bread
session.add(VatRule(
    area_id = 2,
    product_id = 1,
    flat_vat = 0.05,
    untaxable_part = 1,
))
# germany wine
session.add(VatRule(
    area_id = 2,
    product_id = 2,
    specific_vat = 0.2
))
# uk low
session.add(VatRule(
    area_id = 3,
    specific_vat = 0.125,
    min_prevat_amount = 0,
    max_prevat_amount = 20
))
# uk mid
session.add(VatRule(
    area_id = 3,
    specific_vat = 0.15,
    min_prevat_amount = 20,
    max_prevat_amount = 100
))
# uk high
session.add(VatRule(
    area_id = 3,
    specific_vat = 0.2,
    min_prevat_amount = 100
))
# uk wine
session.add(VatRule(
    area_id = 3,
    product_id = 2,
    specific_vat = 0.1
))
# france wine
session.add(VatRule(
    area_id = 4,
    product_id = 2,
    specific_vat = 0.125,
    max_vat = 5
))
# france eggs
session.add(VatRule(
    area_id = 4,
    product_id = 3,
    specific_vat = 0.125,
    untaxable_part = 0.5,
))
# france beer
session.add(VatRule(
    area_id = 4,
    product_id = 4,
    specific_vat = 0.175,
))
session.commit()