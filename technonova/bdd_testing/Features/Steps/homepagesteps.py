from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from technonova.bdd_testing.utilities.readproperty import ReadConfig
from technonova.bdd_testing.utilities.customlogger import LogGen


baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()


@given(u'Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("**** Driver Initialised****")
    context.driver.get(baseURL)
    mylogger.info("***** browser launched*****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "Technonova"
    if actual_title == expected_title:
        assert True
        mylogger.info("***title matched**")
    else:
        mylogger.info("***title  not matched")
        assert False


@then(u'close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info("***** browser closed ***** ")
