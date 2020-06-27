import allure


class TestSetup:
    # 最重要的用例
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤名称")
    def test_001(self):
        """添加测试步骤"""
        allure.attach("我是步骤描述的内容", "附件名字")

    # 比较重要用例
    @allure.severity(allure.severity_level.CRITICAL)
    def test_002(self):
        assert False

    # 正常用例
    @allure.severity(allure.severity_level.NORMAL)
    def test_003(self):
        assert True

    # 比一般低一些用例
    @allure.severity(allure.severity_level.MINOR)
    def test_004(self):
        assert True

    # 可以忽略的用例
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_005(self):
        assert True











