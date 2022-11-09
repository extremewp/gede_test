import yaml

from util.Winecellar_data_base import WinecellarDateBaseTest
from util.user_app_login import UserAppLogin


class TestWinecellar:
    def setup(self):
        self.wcdbt = WinecellarDateBaseTest()

    def test_winecellar(self):
        res = self.wcdbt.sku_list_test()
        assert res['header']['message'] == '成功'

