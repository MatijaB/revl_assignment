# vat_added = min(specific_vat * min((pre_vat - untaxable_part), max_taxable) + flat_vat, max_vat)
# specific_vat depends on country, region, product and pre_vat value
# flat_vat depends on country, region, product and pre_vat value
# after_vat will also hav

# specific_vat(default=1.), untaxable_part(default=0.), max_taxable(default=None), flat_vat(default=0), max_vat(default=None)

# 1. get all the variables from the three input arguments
# 2. calculate from formula above and return vat value
# 3. write setters for new regions/countries
# 4. set and test out
# 5(?). write test_cases

# vat_rule (country, product, min_pre_vat, max_pre_vat)


def calculate_vat(self, product, pre_vat, country):
    pass

