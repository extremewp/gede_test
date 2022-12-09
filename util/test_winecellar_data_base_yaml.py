import yaml

from base.header import Header


class TestWinecellarDateBaseYaml:
    def setup(self):

        self.token = yaml.safe_load(open('../data/token.yml'))['token']
        print(type(self.token))
    def test_asd(self):
        print(Header().header("asdasdas"))

    def test_winecellar(self):
        data = {

            "sku_list_test": {
                "method": "post",
                "url": "/commodity/wineStock/myWineSkuList",
                "data": {
                     "body": {"page_index": 1, "page_size": 10, "product_name": ""}
                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           }
            },

        }

        with open('../data/winecellar_test.yml', 'w') as f:
            yaml.safe_dump(stream=f, data=data)
