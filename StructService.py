from StructPacket import Service
from config import services, service_call, services_sms
import random

class Distribution_Service():
    def __init__(self):
        self.number_attack = Service()
        self.services = services
        self.services_calls = service_call
        self.services_sms = services_sms
        self.next = iter(self.services)
        self.call = iter(self.services_calls)
        self.sms = iter(self.services_sms)

    def phone(self, phone):
        self.number_attack.number(phone)

    def sms_random_service(self):
        try:
            self.request_service(random.choice(self.services_sms))
        except Exception:
            pass

    def sms_next_service(self):
        try:
            self.request_service(next(self.sms))
        except StopIteration:
            self.next = iter(self.services_sms)
        else:
            pass

    def call_next_service(self):
        try:
            self.request_service(next(self.call))
        except StopIteration:
            self.next = iter(self.services_call)
        else:
            pass

    def random_service(self):
        try:
            self.request_service(random.choice(self.services))
        except Exception:
            pass

    def next_service(self):
        try:
            self.request_service(next(self.next))
        except StopIteration:
            self.next = iter(self.services)
        else:
            pass

    def request_service(self, service):
        try:
            if service == 'autheasypayua':
                self.number_attack.autheasypayua()


            elif service == 'ionua':
                self.number_attack.ionua()


            elif service == 'sloncreditua':
                self.number_attack.sloncreditua()


            elif service == 'backzecreditcomua':
                self.number_attack.backzecreditcomua()


            elif service == 'ontaxicomua':
                self.number_attack.ontaxicomua()


            elif service == 'ukloncomua_two':
                self.number_attack.ukloncomua_two()


            elif service == 'partner_uklo_two':
                self.number_attack.partner_uklo_two()


            elif service == 'alloua':
                self.number_attack.alloua()


            elif service == 'n17459yclientscom':
                self.number_attack.n17459yclientscom()


            elif service == 'passporttwitchtv_two':
                self.number_attack.passporttwitchtv_two()


            elif service == 'apiiconjob_co_two':
                self.number_attack.apiiconjob_co_two()


            elif service == 'ggbetru':
                self.number_attack.ggbetru()


            elif service == 'durexrubackendprod':
                self.number_attack.durexrubackendprod()


            elif service == 'wwwdnsshopru_two':
                self.number_attack.wwwdnsshopru_two()


            elif service == 'almatyinstashopkz':
                self.number_attack.almatyinstashopkz()


            elif service == 'gdz_ruwork':
                self.number_attack.gdz_ruwork()


            elif service == 'smotrimru':
                self.number_attack.smotrimru()


            elif service == 'wwwriglaru':
                self.number_attack.wwwriglaru()


            elif service == 'wwwriglaru':
                self.number_attack.wwwriglaru()


            elif service == 'apteka_one':
                self.number_attack.apteka_one()


            elif service == 'loymaxivoinru':
                self.number_attack.loymaxivoinru()


            elif service == 'amurfarmaru':
                self.number_attack.amurfarmaru()


            elif service == 'kulinaristamarket':
                self.number_attack.kulinaristamarket()


            elif service == 'aptekamagnitu':
                self.number_attack.aptekamagnitu()


            elif service == 'autodozvon':
                self.number_attack.autodozvon()


            elif service == 'htvplatform24tv':
                self.number_attack.htvplatform24tv()


            elif service == 'apilike_videocom':
                self.number_attack.apilike_videocom()


            elif service == 'x80aaiccccwa6aik':
                self.number_attack.x80aaiccccwa6aik()


            elif service == 'mydrom_ru':
                self.number_attack.mydrom_ru()


            elif service == 'x80aaiccccwa6aik':
                self.number_attack.x80aaiccccwa6aik()


            elif service == 'harabaru':
                self.number_attack.harabaru()


            elif service == 'zaimbistrodengi':
                self.number_attack.zaimbistrodengi()


            elif service == 'passrutuberu':
                self.number_attack.passrutuberu()


            elif service == 'mobileapiqiwicom':
                self.number_attack.mobileapiqiwicom()


            elif service == 'medicina360ru':
                self.number_attack.medicina360ru()


            elif service == 'apieldoradoua_two':
                self.number_attack.apieldoradoua_two()


            elif service == 'x80aaiccccwa6aik':
                self.number_attack.x80aaiccccwa6aik()


            elif service == 'wwwutairru':
                self.number_attack.wwwutairru()


            elif service == 'aistaxi':
                self.number_attack.aistaxi()


            elif service == 'wowworks2':
                self.number_attack.wowworks2()


            elif service == 'farmacia24':
                self.number_attack.farmacia24()


            elif service == 'carte':
                self.number_attack.carte()


            elif service == 'delivio':
                self.number_attack.delivio()


            elif service == 'www360':
                self.number_attack.www360()


            elif service == 'turbosms':
                self.number_attack.turbosms()


            elif service == 'smsint2':
                self.number_attack.smsint2()


            elif service == 'dtrparts':
                self.number_attack.dtrparts()


            elif service == 'eshko':
                self.number_attack.eshko()


            elif service == 'alfalife':
                self.number_attack.alfalife()


            elif service == 'alpari':
                self.number_attack.alpari()


            elif service == 'api_prime':
                self.number_attack.api_prime()


            elif service == 'apteka':
                self.number_attack.apteka()


            elif service == 'artonline':
                self.number_attack.artonline()


            elif service == 'avtobzvon':
                self.number_attack.avtobzvon()


            elif service == 'bamperby':
                self.number_attack.bamperby()


            elif service == 'bartokyo':
                self.number_attack.bartokyo()


            elif service == 'beeline_kz':
                self.number_attack.beeline_kz()


            elif service == 'beltelecom':
                self.number_attack.beltelecom()


            elif service == 'benzuber':
                self.number_attack.benzuber()


            elif service == 'bluefin':
                self.number_attack.bluefin()


            elif service == 'boosty':
                self.number_attack.boosty()


            elif service == 'buzzolls':
                self.number_attack.buzzolls()


            elif service == 'cabinet_wi_fi':
                self.number_attack.cabinet_wi_fi()


            elif service == 'callmyphone':
                self.number_attack.callmyphone()


            elif service == 'carsmile':
                self.number_attack.carsmile()


            elif service == 'chibbis':
                self.number_attack.chibbis()


            elif service == 'cian':
                self.number_attack.cian()


            elif service == 'cinema5':
                self.number_attack.cinema5()


            elif service == 'citilink':
                self.number_attack.citilink()


            elif service == 'citrus':
                self.number_attack.citrus()


            elif service == 'city24':
                self.number_attack.city24()


            elif service == 'cleversite':
                self.number_attack.cleversite()


            elif service == 'cloudmailru':
                self.number_attack.cloudmailru()


            elif service == 'comfy_ua':
                self.number_attack.comfy_ua()


            elif service == 'creditter':
                self.number_attack.creditter()


            elif service == 'delitime':
                self.number_attack.delitime()


            elif service == 'derevenskoe':
                self.number_attack.derevenskoe()


            elif service == 'dgtl':
                self.number_attack.dgtl()


            elif service == 'dianet':
                self.number_attack.dianet()


            elif service == 'dns_shop':
                self.number_attack.dns_shop()


            elif service == 'e_vse':
                self.number_attack.e_vse()


            elif service == 'easypay':
                self.number_attack.easypay()


            elif service == 'edame':
                self.number_attack.edame()


            elif service == 'edostav':
                self.number_attack.edostav()


            elif service == 'eldorado':
                self.number_attack.eldorado()


            elif service == 'esk_ural':
                self.number_attack.esk_ural()


            elif service == 'etm':
                self.number_attack.etm()


            elif service == 'farpost':
                self.number_attack.farpost()


            elif service == 'finam':
                self.number_attack.finam()


            elif service == 'findclone':
                self.number_attack.findclone()


            elif service == 'fixprice':
                self.number_attack.fixprice()


            elif service == 'flipkart':
                self.number_attack.flipkart()


            elif service == 'foodband':
                self.number_attack.foodband()


            elif service == 'foxtrot':
                self.number_attack.foxtrot()


            elif service == 'friendsclub':
                self.number_attack.friendsclub()


            elif service == 'gazprom':
                self.number_attack.gazprom()


            elif service == 'getmancar':
                self.number_attack.getmancar()


            elif service == 'ginzadelivery':
                self.number_attack.ginzadelivery()


            elif service == 'gnevskii':
                self.number_attack.gnevskii()


            elif service == 'grabtaxi':
                self.number_attack.grabtaxi()


            elif service == 'grinica':
                self.number_attack.grinica()


            elif service == 'groshi':
                self.number_attack.groshi()


            elif service == 'gurutaxi':
                self.number_attack.gurutaxi()


            elif service == 'hatimaki':
                self.number_attack.hatimaki()


            elif service == 'helsi':
                self.number_attack.helsi()


            elif service == 'hmara':
                self.number_attack.hmara()


            elif service == 'icq':
                self.number_attack.icq()


            elif service == 'icqcom':
                self.number_attack.icqcom()


            elif service == 'id_ykt':
                self.number_attack.id_ykt()


            elif service == 'ievaphone':
                self.number_attack.ievaphone()


            elif service == 'imgur':
                self.number_attack.imgur()


            elif service == 'indriver':
                self.number_attack.indriver()


            elif service == 'ingos':
                self.number_attack.ingos()


            elif service == 'invitro':
                self.number_attack.invitro()


            elif service == 'iqlab':
                self.number_attack.iqlab()


            elif service == 'ivi':
                self.number_attack.ivi()


            elif service == 'iwant':
                self.number_attack.iwant()


            elif service == 'izi':
                self.number_attack.izi()


            elif service == 'kant':
                self.number_attack.kant()


            elif service == 'karusel':
                self.number_attack.karusel()


            elif service == 'kaspi':
                self.number_attack.kaspi()


            elif service == 'kasta':
                self.number_attack.kasta()


            elif service == 'kfc':
                self.number_attack.kfc()


            elif service == 'kilovkusa':
                self.number_attack.kilovkusa()


            elif service == 'kinolab':
                self.number_attack.kinolab()


            elif service == 'koronapay':
                self.number_attack.koronapay()


            elif service == 'krista':
                self.number_attack.krista()


            elif service == 'kvivstart':
                self.number_attack.kvivstart()


            elif service == 'lenta':
                self.number_attack.lenta()


            elif service == 'levin':
                self.number_attack.levin()


            elif service == 'limetaxi':
                self.number_attack.limetaxi()


            elif service == 'loany':
                self.number_attack.loany()


            elif service == 'logistic':
                self.number_attack.logistic()


            elif service == 'macdonal':
                self.number_attack.macdonal()


            elif service == 'makarolls':
                self.number_attack.makarolls()


            elif service == 'makimaki':
                self.number_attack.makimaki()


            elif service == 'menuau':
                self.number_attack.menuau()


            elif service == 'menzacafe':
                self.number_attack.menzacafe()


            elif service == 'mistercash':
                self.number_attack.mistercash()


            elif service == 'mngogomenu':
                self.number_attack.mngogomenu()


            elif service == 'mobileplanet':
                self.number_attack.mobileplanet()


            elif service == 'modulbank':
                self.number_attack.modulbank()


            elif service == 'molbulak':
                self.number_attack.molbulak()


            elif service == 'moneymanu':
                self.number_attack.moneymanu()


            elif service == 'monobank':
                self.number_attack.monobank()


            elif service == 'moscow':
                self.number_attack.moscow()


            elif service == 'mospizza':
                self.number_attack.mospizza()


            elif service == 'moyo':
                self.number_attack.moyo()


            elif service == 'mtstv':
                self.number_attack.mtstv()


            elif service == 'multiplex':
                self.number_attack.multiplex()


            elif service == 'mygames':
                self.number_attack.mygames()


            elif service == 'nb99':
                self.number_attack.nb99()


            elif service == 'niyama':
                self.number_attack.niyama()


            elif service == 'nl':
                self.number_attack.nl()


            elif service == 'nncard':
                self.number_attack.nncard()


            elif service == 'pravdop':
                self.number_attack.pravdop()


            elif service == 'planeta_tc':
                self.number_attack.planeta_tc()


            elif service == 'widgetsbinotelcom':
                self.number_attack.widgetsbinotelcom()


            elif service == 'freefoodcomua':
                self.number_attack.freefoodcomua()


            elif service == 'call2friends':
                self.number_attack.call2friends()


            elif service == 'wwwhyundai_vostokru':
                self.number_attack.wwwhyundai_vostokru()


            elif service == 'perevozimvse':
                self.number_attack.perevozimvse()


            elif service == 'an_telecom':
                self.number_attack.an_telecom()


            elif service == 'notecash':
                self.number_attack.notecash()


            elif service == 'nova':
                self.number_attack.nova()


            elif service == 'oauth_av':
                self.number_attack.oauth_av()


            elif service == 'ok':
                self.number_attack.ok()


            elif service == 'okean':
                self.number_attack.okean()


            elif service == 'oldi':
                self.number_attack.oldi()


            elif service == 'ollis':
                self.number_attack.ollis()


            elif service == 'online_sbis':
                self.number_attack.online_sbis()


            elif service == 'onlineua':
                self.number_attack.onlineua()


            elif service == 'oyorooms':
                self.number_attack.oyorooms()


            elif service == 'ozon':
                self.number_attack.ozon()


            elif service == 'panda99':
                self.number_attack.panda99()


            elif service == 'panpizza':
                self.number_attack.panpizza()


            elif service == 'pikru':
                self.number_attack.pikru()


            elif service == 'pirogin':
                self.number_attack.pirogin()


            elif service == 'pizza46':
                self.number_attack.pizza46()


            elif service == 'pizza_33':
                self.number_attack.pizza_33()


            elif service == 'pizzakaz':
                self.number_attack.pizzakaz()


            elif service == 'pizzasinizza':
                self.number_attack.pizzasinizza()


            elif service == 'planetak':
                self.number_attack.planetak()


            elif service == 'plink_tech':
                self.number_attack.plink_tech()


            elif service == 'pliskov':
                self.number_attack.pliskov()


            elif service == 'pomodoro':
                self.number_attack.pomodoro()


            elif service == 'privatebank':
                self.number_attack.privatebank()


            elif service == 'prosushi':
                self.number_attack.prosushi()


            elif service == 'protovar':
                self.number_attack.protovar()


            elif service == 'qbbox':
                self.number_attack.qbbox()


            elif service == 'qiwi':
                self.number_attack.qiwi()


            elif service == 'qlean':
                self.number_attack.qlean()


            elif service == 'raiffeisen':
                self.number_attack.raiffeisen()


            elif service == 'rbt':
                self.number_attack.rbt()


            elif service == 'remontnik':
                self.number_attack.remontnik()


            elif service == 'rendesvouz':
                self.number_attack.rendesvouz()


            elif service == 'richfamely':
                self.number_attack.richfamely()


            elif service == 'rieltor':
                self.number_attack.rieltor()


            elif service == 'rutaxi':
                self.number_attack.rutaxi()


            elif service == 'rutaxi_ru':
                self.number_attack.rutaxi_ru()


            elif service == 'rutube':
                self.number_attack.rutube()


            elif service == 'samaraetagi':
                self.number_attack.samaraetagi()


            elif service == 'sayoris':
                self.number_attack.sayoris()


            elif service == 'sedi':
                self.number_attack.sedi()


            elif service == 'shafa':
                self.number_attack.shafa()


            elif service == 'shopandshow':
                self.number_attack.shopandshow()


            elif service == 'signalis':
                self.number_attack.signalis()


            elif service == 'sipnet':
                self.number_attack.sipnet()


            elif service == 'smartomato':
                self.number_attack.smartomato()


            elif service == 'smartspace':
                self.number_attack.smartspace()


            elif service == 'sms4':
                self.number_attack.sms4()


            elif service == 'smsint':
                self.number_attack.smsint()


            elif service == 'sovest':
                self.number_attack.sovest()


            elif service == 'sportmasterua':
                self.number_attack.sportmasterua()


            elif service == 'sravni':
                self.number_attack.sravni()


            elif service == 'startpizza':
                self.number_attack.startpizza()


            elif service == 'studio':
                self.number_attack.studio()


            elif service == 'suandi':
                self.number_attack.suandi()


            elif service == 'sumaster':
                self.number_attack.sumaster()


            elif service == 'sunlignt':
                self.number_attack.sunlignt()


            elif service == 'sushifuji':
                self.number_attack.sushifuji()


            elif service == 'sushigour':
                self.number_attack.sushigour()


            elif service == 'sushiprof':
                self.number_attack.sushiprof()


            elif service == 'sushiroll':
                self.number_attack.sushiroll()


            elif service == 'bigd_host':
                self.number_attack.bigd_host()


            elif service == 'cian':
                self.number_attack.cian()


            elif service == 'sushiwokru':
                self.number_attack.sushiwokru()


            elif service == 'bettery_ru':
                self.number_attack.bettery_ru()


            elif service == 'pass_media':
                self.number_attack.pass_media()


            elif service == 'sushivesla':
                self.number_attack.sushivesla()


            elif service == 'syzran':
                self.number_attack.syzran()


            elif service == 'tabasko':
                self.number_attack.tabasko()


            elif service == 'tabris':
                self.number_attack.tabris()


            elif service == 'tanuki':
                self.number_attack.tanuki()


            elif service == 'tarantionofamely':
                self.number_attack.tarantionofamely()


            elif service == 'taxi310':
                self.number_attack.taxi310()


            elif service == 'taziritm':
                self.number_attack.taziritm()


            elif service == 'tehnosvit':
                self.number_attack.tehnosvit()


            elif service == 'tele2':
                self.number_attack.tele2()


            elif service == 'telegram':
                self.number_attack.telegram()


            elif service == 'thehive':
                self.number_attack.thehive()


            elif service == 'tiktok':
                self.number_attack.tiktok()


            elif service == 'tinder':
                self.number_attack.tinder()


            elif service == 'tinkoff':
                self.number_attack.tinkoff()


            elif service == 'topladeba':
                self.number_attack.topladeba()


            elif service == 'topshop':
                self.number_attack.topshop()


            elif service == 'tvoaapteka':
                self.number_attack.tvoaapteka()


            elif service == 'zaymer':
                self.number_attack.zaymer()


            elif service == 'twitch':
                self.number_attack.twitch()


            elif service == 'ubepmsmorg':
                self.number_attack.ubepmsmorg()


            elif service == 'ubki':
                self.number_attack.ubki()


            elif service == 'uklon':
                self.number_attack.uklon()


            elif service == 'ulabka':
                self.number_attack.ulabka()


            elif service == 'uralsib':
                self.number_attack.uralsib()


            elif service == 'uteka':
                self.number_attack.uteka()


            elif service == 'utrair':
                self.number_attack.utrair()


            elif service == 'vezitaxi':
                self.number_attack.vezitaxi()


            elif service == 'viza':
                self.number_attack.viza()


            elif service == 'vks':
                self.number_attack.vks()


            elif service == 'vladimirvilkinetru':
                self.number_attack.vladimirvilkinetru()


            elif service == 'vodafone':
                self.number_attack.vodafone()


            elif service == 'api_sushisellru':
                self.number_attack.api_sushisellru()


            elif service == 'sergiopizza':
                self.number_attack.sergiopizza()


            elif service == 'unicom24':
                self.number_attack.unicom24()


            elif service == 'zoloto585_2':
                self.number_attack.zoloto585_2()


            elif service == 'mymodulbank':
                self.number_attack.mymodulbank()


            elif service == 'tvmtsru':
                self.number_attack.tvmtsru()


            elif service == 'wwwtanukiru':
                self.number_attack.wwwtanukiru()


            elif service == 'cashucom':
                self.number_attack.cashucom()


            elif service == 'apizenkyio':
                self.number_attack.apizenkyio()


            elif service == 'sbguestsushiboxorg':
                self.number_attack.sbguestsushiboxorg()


            elif service == 'apipapajohnsru':
                self.number_attack.apipapajohnsru()


            elif service == 'pizzaboxru':
                self.number_attack.pizzaboxru()


            elif service == 'burgerking':
                self.number_attack.burgerking()


            elif service == 'kakvkusno_ru':
                self.number_attack.kakvkusno_ru()


            elif service == 'igooodsru':
                self.number_attack.igooodsru()


            elif service == 'starboxvrn':
                self.number_attack.starboxvrn()


            elif service == 'rollserv':
                self.number_attack.rollserv()


            elif service == 'igooods_two':
                self.number_attack.igooods_two()


            elif service == 'zoopt_two':
                self.number_attack.zoopt_two()


            elif service == 'yobidoyobi':
                self.number_attack.yobidoyobi()


            elif service == 'sberfood':
                self.number_attack.sberfood()


            elif service == 'lbelkacaru_two':
                self.number_attack.lbelkacaru_two()


            elif service == 'broniboyru':
                self.number_attack.broniboyru()


            elif service == 'yakitoriyaru':
                self.number_attack.yakitoriyaru()


            elif service == 'antisushiru':
                self.number_attack.antisushiru()


            elif service == 'newtelnet':
                self.number_attack.newtelnet()


            elif service == 'ulyanovsk':
                self.number_attack.ulyanovsk()


            elif service == 'retailkbkbappru':
                self.number_attack.retailkbkbappru()


            elif service == 'loyalty_apidixyru':
                self.number_attack.loyalty_apidixyru()


            elif service == 'utkonos':
                self.number_attack.utkonos()


            elif service == 'appsmapisportmasterru':
                self.number_attack.appsmapisportmasterru()


            elif service == 'apidetmirru':
                self.number_attack.apidetmirru()


            elif service == 'apizakazakaru':
                self.number_attack.apizakazakaru()


            elif service == 'autoriacom':
                self.number_attack.autoriacom()


            elif service == 'wwwyakabooua':
                self.number_attack.wwwyakabooua()


            elif service == 'biuaapiv':
                self.number_attack.biuaapiv()


            elif service == 'kharkovestate':
                self.number_attack.kharkovestate()


            elif service == 'ieltorua':
                self.number_attack.ieltorua()


            elif service == 'hh_ru':
                self.number_attack.hh_ru()


            elif service == 'phonetua':
                self.number_attack.phonetua()


            elif service == 'uslugiru':
                self.number_attack.uslugiru()


            elif service == 'docservisinua':
                self.number_attack.docservisinua()


            elif service == 'mylugacomcom':
                self.number_attack.mylugacomcom()


            elif service == 'mybankby':
                self.number_attack.mybankby()


            elif service == 'qlean_two':
                self.number_attack.qlean_two()


            elif service == 'taxi7788':
                self.number_attack.taxi7788()


            elif service == 'ibpsbankru':
                self.number_attack.ibpsbankru()


            elif service == 'wwwvprokru':
                self.number_attack.wwwvprokru()


            elif service == 'authorization_front_api':
                self.number_attack.authorization_front_api()


            elif service == 'apimarkethomecredit':
                self.number_attack.apimarkethomecredit()


            elif service == 'onlinehomecreditru':
                self.number_attack.onlinehomecreditru()


            elif service == 'mvideo_two_or_one':
                self.number_attack.mvideo_two_or_one()


            elif service == 'apistartru':
                self.number_attack.apistartru()


            elif service == 'admineurogroshicomua':
                self.number_attack.admineurogroshicomua()


            elif service == 'moneycasecomua':
                self.number_attack.moneycasecomua()


            elif service == 'admintopcreditua':
                self.number_attack.admintopcreditua()


            elif service == 'admin1groshivsimcom':
                self.number_attack.admin1groshivsimcom()


            elif service == 'perifyskorozvonru':
                self.number_attack.perifyskorozvonru()


            elif service == 'nalog':
                self.number_attack.nalog()


            elif service == 'baptekaru':
                self.number_attack.baptekaru()


            elif service == 'webbank':
                self.number_attack.webbank()


            elif service == 'disk_apimegafonru':
                self.number_attack.disk_apimegafonru()


            elif service == 'x80aaiccccwa6aik':
                self.number_attack.x80aaiccccwa6aik()


            elif service == 'wifimetro':
                self.number_attack.wifimetro()


            elif service == 'work':
                self.number_attack.work()


            elif service == 'wowworks':
                self.number_attack.wowworks()


            elif service == 'yandexeda':
                self.number_attack.yandexeda()


            elif service == 'yapochink':
                self.number_attack.yapochink()


            elif service == 'youla':
                self.number_attack.youla()


            elif service == 'zaminka':
                self.number_attack.zaminka()


            elif service == 'zoopt':
                self.number_attack.zoopt()
        except Exception as e:
            pass
