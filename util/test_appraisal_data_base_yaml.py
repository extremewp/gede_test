import yaml


class TestAppraisalDataBase:

    def test_appraisal_data_base(self):
        data = {
            'appraisaldatabase': {"method": "post",
                                  "url": "/commodity/label/listEvaluationLabel",
                                  "header": {'Content-Type': 'application/json;charset=UTF-8'
                                             },

                                  'data': {
                                      "body": {"system_source": "2"}},
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                  },
            'listappraisalitem': {
                "method": "post",
                "url": "/commodity/appraisal/listAppraisalItem",
                "data": {
                    "body": {"system_source": 2}
                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           },
                                  "Assertions":{
                                      "message": '成功'
                                  }
            },
            'addEvaluation_pass': {
                "method": "post",
                "url": "/commodity/identification/addEvaluation",
                "data": {
                    "body": {"product_name": "老旧茅台", "product_quantity": 6, "remarks": "哇哈哈", "system_source": 2,
                             "evaluation_product_tag_vos": [{"tag_id": 2, "option_id": 4, "tag_value": "完好"}],
                             "appraisal_item_relation_vos": [{"item_id": -1, "item_content": 3},
                                                             {"item_id": 2, "item_content": "2022年"},
                                                             {"item_id": 3, "item_content": "34°"},
                                                             {"item_id": 4, "item_content": "400ml"},
                                                             {"item_id": 11, "item_content": "瓶"}],
                             "product_evaluation_image_vos": [
                                 {"url_domain": "https://googutwine.oss-cn-beijing.aliyuncs.com/",
                                  "url_path": "web-dev-file/2022-10-16/7424c6117e5c4717bf2a3111492b6dfe-02b32253-95cf-4af4-9a6a-ecdc60803754678085223324006117236.jpg",
                                  "type": 1}, {"url_domain": "https://googutwine.oss-cn-beijing.aliyuncs.com/",
                                               "url_path": "web-dev-file/2022-10-16/7424c6117e5c4717bf2a3111492b6dfe-02b32253-95cf-4af4-9a6a-ecdc60803754678085223324006117236.jpg",
                                               "type": 2},
                                 {"url_domain": "https://googutwine.oss-cn-beijing.aliyuncs.com/",
                                  "url_path": "web-dev-file/2022-10-16/7424c6117e5c4717bf2a3111492b6dfe-02b32253-95cf-4af4-9a6a-ecdc60803754678085223324006117236.jpg",
                                  "type": 3}, {"url_domain": "https://googutwine.oss-cn-beijing.aliyuncs.com/",
                                               "url_path": "web-dev-file/2022-10-16/7424c6117e5c4717bf2a3111492b6dfe-02b32253-95cf-4af4-9a6a-ecdc60803754678085223324006117236.jpg",
                                               "type": 4},
                                 {"url_domain": "https://googutwine.oss-cn-beijing.aliyuncs.com/",
                                  "url_path": "web-dev-file/2022-10-16/7424c6117e5c4717bf2a3111492b6dfe-02b32253-95cf-4af4-9a6a-ecdc60803754678085223324006117236.jpg",
                                  "type": 5}]
                             }
                },
                "header": {'Content-Type': 'application/json;charset=UTF-8'
                           },
                                  "Assertions":{
                                      "message": '成功'
                                  }
            },
            "listUserEvaluationBill_dpg": {"method": "post",
                                           "url": "/commodity/identification/listUserEvaluationBill",
                                           "data": { "body":{"identification_status": 1, "page_size": 10, "page_index": 1}},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                                      },
                                  "Assertions":{
                                      "message": '成功'
                                  }

                                           },
            "listUserEvaluationBill_ypg": {"method": "post",
                                           "url": "/commodity/identification/listUserEvaluationBill",
                                           "data":  { "body":{"identification_status": 2, "page_size": 10, "page_index": 1}},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                                      },
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                           },

            "listUserEvaluationBill_djb": {"method": "post",
                                           "url": "/commodity/identification/listUserEvaluationBill",
                                           "data":  { "body":{"identification_status": 6, "page_size": 10, "page_index": 1}},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                           },
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                           },

            'listUserEvaluationBill_yjj': {"method": "post",
                                           "url": "/commodity/identification/listUserEvaluationBill",
                                           "data":  { "body":{"identification_status": 7, "page_size": 10, "page_index": 1}},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                                      },
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                           },

            'listUserEvaluationBill_ygb': {"method": "post",
                                           "url": "/commodity/identification/listUserEvaluationBill",
                                           "data":  { "body":{"identification_status": 10, "page_size": 10, "page_index": 1}},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                                      },
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                           },

            'getUserEvaluationBill_pass':{"method": "post",
                                           "url": "/commodity/identification/getUserEvaluationBill",
                                           "data":  { "body":{"bill_number": 'JD2022101600512', }},
                                           "header": {'Content-Type': 'application/json;charset=UTF-8'
                                                      },
                                  "Assertions":{
                                      "message": '成功'
                                  }
                                           },

        }
        with open("../data/appraisal.yml", 'w') as f:
            yaml.safe_dump(data, f)
