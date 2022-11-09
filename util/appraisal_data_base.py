import yaml

from base.base_api import BaseApi


class AppraisalDataBase:
    # 查询鉴定属性
    def __init__(self):
        self.base_api = BaseApi()

    def appraisaldatabase(self):
        res = self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['appraisaldatabase'])
        return res

    def listappraisalitem(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listappraisalitem'])

    def addEvaluation_pass(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['addEvaluation_pass'])

    def listUserEvaluationBill_dpg(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listUserEvaluationBill_dpg'])

    def listUserEvaluationBill_ypg(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listUserEvaluationBill_ypg'])

    def listUserEvaluationBill_djb(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listUserEvaluationBill_djb'])

    def listUserEvaluationBill_yjj(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listUserEvaluationBill_yjj'])

    def listUserEvaluationBill_ygb(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['listUserEvaluationBill_ygb'])

    def getUserEvaluationBill_pass(self):
        return self.base_api.base_api(**yaml.safe_load(open('../data/appraisal.yml'))['getUserEvaluationBill_pass'])
