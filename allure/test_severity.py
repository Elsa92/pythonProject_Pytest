import pytest
import allure

def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass

@allure.severity(allure.severity_level.MINOR)
def test_with_minor_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity():
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_overriding_critical_severity(self):
        pass

@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical_severity():
    pass

@allure.severity(allure.severity_level.BLOCKER)
def test_with_blocker_severity():
    pass

if __name__ == '__main__':
    pytest.main()


