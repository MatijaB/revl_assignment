from models import VatRule, Session

country_to_region_map = {
    2:1,
    3:1,
    4:1,
    5:1,
    6:1,
    8:7,
    9:7,
    10:7,
}

area_ids = {
    'eu': 1,
    'germany': 2,
    'uk': 3,
    'france': 4,
    'poland': 5,
    'spain': 6,
    'usa': 7,
    'texas': 8,
    'alaska': 9,
    'colorado': 10
}

product_ids = {
    'bread': 1,
    'wine': 2,
    'eggs': 3,
    'beer'
    'dairy': 4,
    'alcohol': 5,
    'milk': 6
}


def create_vat_rule(area, product, data, parent_rule):
    if not data:
        data = dict()

    if not parent_rule:
        parent_rule = VatRule()

    area_id = _get_area_id(area)
    product_id = _get_product_id(product)

    new_vat_rule = VatRule(
        area_id = area_id,
        product_id = product_id,
        max_prevat_amount = data.get('max_prevat_amount', parent_rule.max_prevat_amount),
        min_prevat_amount = data.get('min_prevat_amount', parent_rule.min_prevat_amount),
        specific_vat = data.get('specific_vat', parent_rule.specific_vat),
        untaxable_part = data.get('untaxable_part', parent_rule.untaxable_part),
        max_taxable = data.get('max_taxable', parent_rule.max_taxable),
        flat_vat = data.get('flat_vat', parent_rule.flat_vat),
        max_vat = data.get('max_vat', parent_rule.max_vat),
        parent_id = parent_rule.id
    )

    session = Session()
    session.add(new_vat_rule)
    session.commit()


def calculate_vat(area, product, pre_vat):
    vat_rules = get_vat_rules(area, product)

    if len(vat_rules) == 1:
        return vat_rules[0].calculate_vat(pre_vat)

    for vat_rule in vat_rules:
        if vat_rule.min_prevat_amount and vat_rule.min_prevat_amount > pre_vat:
            continue
        if vat_rule.max_prevat_amount and vat_rule.max_prevat_amount < pre_vat:
            continue
        return vat_rule.calculate_vat(pre_vat)

    return None


def get_vat_rules(area, product):
    area_id = _get_area_id(area)
    product_id = _get_product_id(product)
    region_id = _get_region_id(area_id)

    session = Session()
    vat_rules = session.query(VatRule).filter(VatRule.area_id == area_id, VatRule.product_id == product_id).all()

    if not vat_rules:
        vat_rules = session.query(VatRule).filter(VatRule.area_id == area_id).all()

    if not vat_rules:
        vat_rules = session.query(VatRule).filter(VatRule.area_id == region_id, VatRule.product_id == product_id).all()

    if not vat_rules:
        vat_rules = session.query(VatRule).filter(VatRule.area_id == region_id).all()

    return vat_rules


def _get_region_id(country_id):
    return country_to_region_map[country_id]


def _get_area_id(area):
    area = area.lower()

    if area not in area_ids:
        return None

    return area_ids[area]


def _get_product_id(product):
    product = product.lower()

    if product not in product_ids:
        return None

    return product_ids[product]
