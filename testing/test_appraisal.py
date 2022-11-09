import time
from datetime import datetime, date

from util.appraisal_data_base import AppraisalDataBase


class TestAppraisal:
    def setup(self):
        self.adb = AppraisalDataBase()

    # 酒市鉴定查询勾选标签
    def test_appraisal(self):
        res = self.adb.appraisaldatabase()
        assert res['header']['message'] == '成功'

    # 酒市鉴定查看箱规属性
    def test_listappraisalitem(self):
        res = self.adb.listappraisalitem()
        assert res['header']['message'] == '成功'

    # 新增酒市评估单
    def test_addEvaluation_pass(self):
        res = self.adb.addEvaluation_pass()
        print(res)
        assert res['header']['message'] == '成功'

    # 查看酒市鉴定单——待评估
    def test_listUserEvaluationBill_dpg(self):
        res = self.adb.listUserEvaluationBill_dpg()
        assert res['header']['message'] == '成功'

    # 查看酒市鉴定单——已鉴酒
    def test_listUserEvaluationBill_yjj(self):
        res = self.adb.listUserEvaluationBill_yjj()
        assert res['header']['message'] == '成功'

    # 查看酒市鉴定单——待鉴别
    def test_listUserEvaluationBill_djb(self):
        res = self.adb.listUserEvaluationBill_djb()
        assert res['header']['message'] == '成功'

    # 查看酒市鉴定单——已鉴别
    def test_listUserEvaluationBill_ygb(self):
        res = self.adb.listUserEvaluationBill_ygb()
        assert res['header']['message'] == '成功'

    # 查看酒市鉴定单——已评估
    def test_listUserEvaluationBill_ypg(self):
        res = self.adb.listUserEvaluationBill_ypg()
        assert res['header']['message'] == '成功'

    # 查询鉴定单详情
    def test_getUserEvaluationBill_pass(self):
        res = self.adb.getUserEvaluationBill_pass()
        assert res['header']['message'] == '成功'
