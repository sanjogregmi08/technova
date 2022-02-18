from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve

from customer.views import allproducts, casing, coolingfan, dashboard, gpu, homepage, inventory, keyboard,login, motherboard, mouse, powersupply, processor, ram, registration, whats_new
# Create your tests here.
class TestURLS(SimpleTestCase):

    def test_case_customer_home(self):
        url =  reverse('home')
        self.assertEquals(resolve(url).func,homepage)
    def test_case_customer_login(self):
        url =  reverse('login')
        self.assertEquals(resolve(url).func,login)
    def test_case_customer_register(self):
        url =  reverse('registration')
        self.assertEquals(resolve(url).func,registration)
    def test_case_customer_dashboard(self):
        url =  reverse('dashboard')
        self.assertEquals(resolve(url).func,dashboard)
    def test_case_customer_inventory(self):
        url =  reverse('inventory')
        self.assertEquals(resolve(url).func,inventory)
    def test_case_customer_whats_new(self):
        url =  reverse('whats_new')
        self.assertEquals(resolve(url).func,whats_new)    
    def test_case_customerallproducts(self):
        url =  reverse('allproducts')
        self.assertEquals(resolve(url).func,allproducts)
    def test_case_customermouse(self):
        url =  reverse('mouse')
        self.assertEquals(resolve(url).func,mouse)         
    def test_case_customermotherboard(self):
        url =  reverse('motherboard')
        self.assertEquals(resolve(url).func,motherboard)
    def test_case_customercoolingfan(self):
        url =  reverse('coolingfan')
        self.assertEquals(resolve(url).func,coolingfan)
    def test_case_customerkeyboard(self):
        url =  reverse('keyboard')
        self.assertEquals(resolve(url).func,keyboard)
    def test_case_customerprocessor(self):
        url =  reverse('processor')
        self.assertEquals(resolve(url).func,processor)
    def test_case_customercasing(self):
        url =  reverse('casing')
        self.assertEquals(resolve(url).func,casing)
    def test_case_customergpu(self):
        url =  reverse('gpu')
        self.assertEquals(resolve(url).func,gpu)
    def test_case_customerpowersupply(self):
        url =  reverse('powersupply')
        self.assertEquals(resolve(url).func,powersupply)
    def test_case_customerram(self):
        url =  reverse('ram')
        self.assertEquals(resolve(url).func,ram)    