import yaml

from base.base_api import BaseApi


class WinecellarDateBaseTest:
    def __init__(self):
        self.ba = BaseApi()

    def sku_list_test(self):
        return self.ba.base_api(**yaml.safe_load(open('../data/winecellar_test.yml'))['sku_list_test'])

