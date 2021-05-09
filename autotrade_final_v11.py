## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재시간

# get 240 minutes befor 4
def get_m240_2(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute10", 5)
    close = df['close']
    m240_4 = close.rolling(2).mean()
    return m240_4[-1]
m240_2_BTC = get_m240_2("KRW-BTC")
m240_2_ETH = get_m240_2("KRW-ETH")
m240_2_BCH = get_m240_2("KRW-BCH")
m240_2_BSV = get_m240_2("KRW-BSV")
m240_2_LTC = get_m240_2("KRW-LTC")
m240_2_BTG = get_m240_2("KRW-BTG")
m240_2_NEO = get_m240_2("KRW-NEO")
m240_2_ETC = get_m240_2("KRW-ETC")
m240_2_BCHA = get_m240_2("KRW-BCHA")
m240_2_REP = get_m240_2("KRW-REP")
m240_2_LINK = get_m240_2("KRW-LINK")
m240_2_DOT = get_m240_2("KRW-DOT")
m240_2_QTUM = get_m240_2("KRW-QTUM")
m240_2_ATOM = get_m240_2("KRW-ATOM")
m240_2_WAVES = get_m240_2("KRW-WAVES")
m240_2_EOS = get_m240_2("KRW-EOS")
m240_2_STRK = get_m240_2("KRW-STRK")
m240_2_GAS = get_m240_2("KRW-GAS")
m240_2_OMG = get_m240_2("KRW-OMG")
m240_2_THETA = get_m240_2("KRW-THETA")
m240_2_TON = get_m240_2("KRW-TON")
m240_2_LSK = get_m240_2("KRW-LSK")
m240_2_SRM = get_m240_2("KRW-SRM")
m240_2_FLOW = get_m240_2("KRW-FLOW")

# get 240 minutes befor 4
# def get_m240_1(ticker):
#     df = pyupbit.get_ohlcv(ticker, "minute5")
#     close = df['close']
#     m240_4 = close.rolling(3).mean()
#     return m240_4[-1]
# m240_1_BTC = get_m240_1("KRW-BTC")
# m240_1_ETH = get_m240_1("KRW-ETH")
# m240_1_BCH = get_m240_1("KRW-BCH")
# m240_1_BSV = get_m240_1("KRW-BSV")
# m240_1_LTC = get_m240_1("KRW-LTC")
# m240_1_BTG = get_m240_1("KRW-BTG")
# time.sleep(1)
# m240_1_NEO = get_m240_1("KRW-NEO")
# m240_1_ETC = get_m240_1("KRW-ETC")
# m240_1_BCHA = get_m240_1("KRW-BCHA")
# m240_1_REP = get_m240_1("KRW-REP")
# m240_1_LINK = get_m240_1("KRW-LINK")
# m240_1_DOT = get_m240_1("KRW-DOT")
# m240_1_QTUM = get_m240_1("KRW-QTUM")
# m240_1_ATOM = get_m240_1("KRW-ATOM")
# m240_1_WAVES = get_m240_1("KRW-WAVES")
# m240_1_EOS = get_m240_1("KRW-EOS")
# m240_1_STRK = get_m240_1("KRW-STRK")
# m240_1_GAS = get_m240_1("KRW-GAS")
# m240_1_OMG = get_m240_1("KRW-OMG")
# m240_1_THETA = get_m240_1("KRW-THETA")
# m240_1_TON = get_m240_1("KRW-TON")
# m240_1_LSK = get_m240_1("KRW-LSK")
# m240_1_SRM = get_m240_1("KRW-SRM")
# m240_1_FLOW = get_m240_1("KRW-FLOW")


# f = open("upbit.txt")
# lines = f.readline()
# access = lines[0].strip()
# secret = lines[1].strip()
# f.close()
# upbit = pyupbit.Upbit(access, secret)
# upbit = pyupbit.Upbit("N2ITzkiEwC2qFucpR6MYmxxm2vrBoAqtN3ScIcSU", "urMWfjBtfEQvAgDcN0ve0Qxkf180Dwhs2ysadpMx") # Upbit class의 객체 생성


op_mode_BTC = False
op_mode_ETH = False
op_mode_BCH = False
op_mode_BSV = False
op_mode_LTC = False
op_mode_BTG = False
op_mode_NEO = False
op_mode_ETC = False
op_mode_BCHA = False
op_mode_REP = False
op_mode_LINK = False
op_mode_DOT = False
op_mode_QTUM = False
op_mode_ATOM = False
op_mode_WAVES = False
op_EOS_WAVES = False
op_mode_STRK = False
op_mode_GAS = False
op_mode_OMG = False
op_mode_THETA = False
op_mode_TON = False
op_mode_LSK = False
op_mode_SRM = False
op_mode_FLOW = False

hold_BTC = False
hold_ETH = False
hold_BCH = False
hold_BSV = False
hold_LTC = False
hold_BTG = False
hold_NEO = False
hold_ETC = False
hold_BCHA = False
hold_REP = False
hold_LINK = False
hold_DOT = False
hold_QTUM = False
hold_ATOM = False
hold_WAVES = False
hold_EOS = False
hold_STRK = False
hold_GAS = False
hold_OMG = False
hold_THETA = False
hold_TON = False
hold_LSK = False
hold_SRM = False
hold_FLOW = False


while True: 
    now = datetime.datetime.now()

    # 24시간 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        m240_2_BTC = get_m240_2("KRW-BTC")
        m240_2_ETH = get_m240_2("KRW-ETH")
        m240_2_BCH = get_m240_2("KRW-BCH")
        m240_2_BSV = get_m240_2("KRW-BSV")
        m240_2_LTC = get_m240_2("KRW-LTC")
        m240_2_BTG = get_m240_2("KRW-BTG")
        time.sleep(1)
        m240_2_NEO = get_m240_2("KRW-NEO")
        m240_2_ETC = get_m240_2("KRW-ETC")
        m240_2_BCHA = get_m240_2("KRW-BCHA")
        m240_2_REP = get_m240_2("KRW-REP")
        m240_2_LINK = get_m240_2("KRW-LINK")
        m240_2_DOT = get_m240_2("KRW-DOT")
        time.sleep(1)
        m240_2_QTUM = get_m240_2("KRW-QTUM")
        m240_2_ATOM = get_m240_2("KRW-ATOM")
        m240_2_WAVES = get_m240_2("KRW-WAVES")
        m240_2_EOS = get_m240_2("KRW-EOS")
        m240_2_STRK = get_m240_2("KRW-STRK")
        m240_2_GAS = get_m240_2("KRW-GAS")
        time.sleep(1)
        # m240_1_BTC = get_m240_1("KRW-BTC")
        # m240_1_ETH = get_m240_1("KRW-ETH")
        # m240_1_BCH = get_m240_1("KRW-BCH")
        # m240_1_BSV = get_m240_1("KRW-BSV")
        # m240_1_LTC = get_m240_1("KRW-LTC")
        # m240_1_BTG = get_m240_1("KRW-BTG")
        # time.sleep(1)
        # m240_1_NEO = get_m240_1("KRW-NEO")
        # m240_1_ETC = get_m240_1("KRW-ETC")
        # m240_1_BCHA = get_m240_1("KRW-BCHA")
        # m240_1_REP = get_m240_1("KRW-REP")
        # m240_1_LINK = get_m240_1("KRW-LINK")
        # m240_1_DOT = get_m240_1("KRW-DOT")
        # time.sleep(1)
        # m240_1_QTUM = get_m240_1("KRW-QTUM")
        # m240_1_ATOM = get_m240_1("KRW-ATOM")
        # m240_1_WAVES = get_m240_1("KRW-WAVES")
        # m240_1_EOS = get_m240_1("KRW-EOS")
        # m240_1_STRK = get_m240_1("KRW-STRK")
        # m240_1_GAS = get_m240_1("KRW-GAS")
        # time.sleep(1)
        m240_2_OMG = get_m240_2("KRW-OMG")
        m240_2_THETA = get_m240_2("KRW-THETA")
        m240_2_TON = get_m240_2("KRW-TON")
        m240_2_LSK = get_m240_2("KRW-LSK")
        m240_2_SRM = get_m240_2("KRW-SRM")
        m240_2_FLOW = get_m240_2("KRW-FLOW")
        time.sleep(1)
        # m240_1_OMG = get_m240_1("KRW-OMG")
        # m240_1_THETA = get_m240_1("KRW-THETA")
        # m240_1_TON = get_m240_1("KRW-TON")
        # m240_1_LSK = get_m240_1("KRW-LSK")
        # m240_1_SRM = get_m240_1("KRW-SRM")
        # m240_1_FLOW = get_m240_1("KRW-FLOW")
        # time.sleep(1)

        op_mode_BTC = True
        op_mode_ETH = True
        op_mode_BCH = True
        op_mode_BSV = True
        op_mode_LTC = True
        op_mode_BTG = True
        op_mode_NEO = True
        op_mode_ETC = True
        op_mode_BCHA = True
        op_mode_REP = True
        op_mode_LINK = True
        op_mode_QTUM = True
        op_mode_ATOM = True
        op_mode_DOT = True
        op_mode_WAVES = True
        op_mode_EOS = True
        op_mode_STRK = True
        op_mode_GAS = True
        op_mode_OMG = True
        op_mode_THETA = True
        op_mode_TON = True
        op_mode_LSK = True
        op_mode_SRM = True
        op_mode_FLOW = True
        

    price_BTC = pyupbit.get_current_price("KRW-BTC")
    price_ETH = pyupbit.get_current_price("KRW-ETH")
    price_BCH = pyupbit.get_current_price("KRW-BCH")
    price_BSV = pyupbit.get_current_price("KRW-BSV")
    price_LTC = pyupbit.get_current_price("KRW-LTC")
    price_BTG = pyupbit.get_current_price("KRW-BTG")
    time.sleep(1)
    price_NEO = pyupbit.get_current_price("KRW-NEO")
    price_ETC = pyupbit.get_current_price("KRW-ETC")
    price_BCHA = pyupbit.get_current_price("KRW-BCHA")
    price_REP = pyupbit.get_current_price("KRW-REP")
    price_LINK = pyupbit.get_current_price("KRW-LINK")
    price_DOT = pyupbit.get_current_price("KRW-DOT")
    time.sleep(1)
    price_QTUM = pyupbit.get_current_price("KRW-QTUM")
    price_ATOM = pyupbit.get_current_price("KRW-ATOM")
    price_WAVES = pyupbit.get_current_price("KRW-WAVES")
    price_EOS = pyupbit.get_current_price("KRW-EOS")
    price_STRK = pyupbit.get_current_price("KRW-STRK") 
    price_GAS = pyupbit.get_current_price("KRW-GAS") 
    time.sleep(1)
    price_OMG = pyupbit.get_current_price("KRW-OMG")
    price_THETA = pyupbit.get_current_price("KRW-THETA")
    price_TON = pyupbit.get_current_price("KRW-TON")
    price_LSK = pyupbit.get_current_price("KRW-LSK")
    price_SRM = pyupbit.get_current_price("KRW-SRM") 
    price_FLOW = pyupbit.get_current_price("KRW-FLOW") 
    time.sleep(1)


    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BTC is True and hold_BTC is False and price_BTC is not None and\
        price_BTC - m240_2_BTC > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-BTC", 10000)
        hold_BTC = True
        print("매수시간:", now, "매수가격(BTC):", price_BTC)
        P_BTC = price_BTC
        # time.sleep(1)
    if op_mode_ETH is True and hold_ETH is False and price_ETH is not None and\
        price_ETH - m240_2_ETH> 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-ETH", 10000)
        hold_ETH = True
        print("매수시간:", now, "매수가격(ETH):", price_ETH)
        P_ETH = price_ETH
        # time.sleep(1)
    if op_mode_BCH is True and hold_BCH is False and price_BCH is not None and\
        price_BCH - m240_2_BCH > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-BCH", 10000)
        hold_BCH = True
        print("매수시간:", now, "매수가격(BCH):", price_BCH)
        P_BCH = price_BCH
        # time.sleep(1)
    if op_mode_BSV is True and hold_BSV is False and price_BSV is not None and\
        price_BSV - m240_2_BSV > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-BSV", 10000)
        hold_BSV = True
        print("매수시간:", now, "매수가격(BSV):", price_BSV)
        P_BSV = price_BSV
        # time.sleep(1)
    if op_mode_LTC is True and hold_LTC is False and price_LTC is not None and\
        price_LTC - m240_2_LTC > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-LTC", 10000)
        hold_LTC = True
        print("매수시간:", now, "매수가격(LTC):", price_LTC)
        P_LTC = price_LTC
        # time.sleep(1)
    if op_mode_BTG is True and hold_BTG is False and price_BTG is not None and\
        price_BTG - m240_2_BTG > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-BTG", 10000)
        hold_BTG = True
        print("매수시간:", now, "매수가격(BTG):", price_BTG)
        P_BTG = price_BTG
        # time.sleep(1)
    if op_mode_NEO is True and hold_NEO is False and price_NEO is not None and\
        price_NEO - m240_2_NEO > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-NEO", 10000)
        hold_NEO = True
        print("매수시간:", now, "매수가격(NEO):", price_NEO)
        P_NEO = price_NEO
        # time.sleep(1)
    if op_mode_ETC is True and hold_ETC is False and price_ETC is not None and\
        price_ETC - m240_2_ETC > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-ETC", 10000)
        hold_ETC = True
        print("매수시간:", now, "매수가격(ETC):", price_ETC)
        P_ETC = price_ETC
        # time.sleep(1)
    if op_mode_BCHA is True and hold_BCHA is False and price_BCHA is not None and\
        price_BCHA - m240_2_BCHA > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-BCHA", 10000)
        hold_BCHA = True
        print("매수시간:", now, "매수가격(BCHA):", price_BCHA)
        P_BCHA = price_BCHA
        # time.sleep(1)
    if op_mode_REP is True and hold_REP is False and price_REP is not None and\
        price_REP - m240_2_REP > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-REP", 10000)
        hold_REP = True
        print("매수시간:", now, "매수가격(REP):", price_REP)
        P_REP = price_REP
        # time.sleep(1)
    if op_mode_LINK is True and hold_LINK is False and price_LINK is not None and\
        price_LINK - m240_2_LINK > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-LINK", 10000)
        hold_LINK = True
        print("매수시간:", now, "매수가격(LINK):", price_LINK)
        P_LINK = price_LINK
        # time.sleep(1)
    if op_mode_DOT is True and hold_DOT is False and price_DOT is not None and\
        price_DOT - m240_2_DOT > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-DOT", 10000)
        hold_DOT = True
        print("매수시간:", now, "매수가격(DOT):", price_DOT)
        P_DOT = price_DOT
        # time.sleep(1)
    if op_mode_QTUM is True and hold_QTUM is False and price_QTUM is not None and\
        price_QTUM - m240_2_QTUM > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-QTUM", 10000)
        hold_QTUM = True
        print("매수시간:", now, "매수가격(QTUM):", price_QTUM)
        P_QTUM = price_QTUM
        # time.sleep(1)
    if op_mode_ATOM is True and hold_ATOM is False and price_ATOM is not None and\
        price_ATOM - m240_2_ATOM > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-ATOM", 10000)
        hold_ATOM = True
        print("매수시간:", now, "매수가격(ATOM):", price_ATOM)
        P_ATOM = price_ATOM
        # time.sleep(1)
    if op_mode_WAVES is True and hold_WAVES is False and price_WAVES is not None and\
        price_WAVES - m240_2_WAVES > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-WAVES", 10000)
        hold_WAVES = True
        print("매수시간:", now, "매수가격(WAVES):", price_WAVES)
        P_WAVES = price_WAVES
        # time.sleep(1)
    if op_mode_EOS is True and hold_EOS is False and price_EOS is not None and\
        price_EOS - m240_2_EOS > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-EOS", 10000)
        hold_EOS = True
        print("매수시간:", now, "매수가격(EOS):", price_EOS)
        P_EOS = price_EOS
        # time.sleep(1)
    if op_mode_STRK is True and hold_STRK is False and price_STRK is not None and\
        price_STRK - m240_2_STRK > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-STRK", 10000)
        hold_STRK = True
        print("매수시간:", now, "매수가격(STRK):", price_STRK)
        P_STRK = price_STRK
        # time.sleep(1)
    if op_mode_GAS is True and hold_GAS is False and price_GAS is not None and\
        price_GAS - m240_2_GAS > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-GAS", 10000)
        hold_GAS = True
        print("매수시간:", now, "매수가격(GAS):", price_GAS)
        P_GAS = price_GAS
        # time.sleep(1)
    if op_mode_OMG is True and hold_OMG is False and price_OMG is not None and\
        price_OMG - m240_2_OMG > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-OMG", 10000)
        hold_OMG = True
        print("매수시간:", now, "매수가격(OMG):", price_OMG)
        P_OMG = price_OMG
        # time.sleep(1)
    if op_mode_THETA is True and hold_THETA is False and price_THETA is not None and\
        price_THETA - m240_2_THETA > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-THETA", 10000)
        hold_THETA = True
        print("매수시간:", now, "매수가격(THETA):", price_THETA)
        P_THETA = price_THETA
        # time.sleep(1)
    if op_mode_TON is True and hold_TON is False and price_TON is not None and\
        price_TON - m240_2_TON > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-TON", 10000)
        hold_TON = True
        print("매수시간:", now, "매수가격(TON):", price_TON)
        P_TON = price_TON
        # time.sleep(1)
    if op_mode_LSK is True and hold_LSK is False and price_LSK is not None and\
        price_LSK - m240_2_LSK > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-LSK", 10000)
        hold_LSK = True
        print("매수시간:", now, "매수가격(LSK):", price_LSK)
        P_LSK = price_LSK
        # time.sleep(1)
    if op_mode_SRM is True and hold_SRM is False and price_SRM is not None and\
        price_SRM - m240_2_SRM > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-SRM", 10000)
        hold_SRM = True
        print("매수시간:", now, "매수가격(SRM):", price_SRM)
        P_SRM = price_SRM
        # time.sleep(1)
    if op_mode_FLOW is True and hold_FLOW is False and price_FLOW is not None and\
        price_FLOW - m240_2_FLOW > 0:
        # krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        # upbit.buy_market_order("KRW-FLOW", 10000)
        hold_FLOW = True
        print("매수시간:", now, "매수가격(FLOW):", price_FLOW)
        P_FLOW = price_FLOW
        # time.sleep(1)

    if hold_BTC is True:
        Buy_BTC = P_BTC
    if hold_ETH is True:
        Buy_ETH = P_ETH
    if hold_BCH is True:
        Buy_BCH = P_BCH
    if hold_BSV is True:
        Buy_BSV = P_BSV
    if hold_LTC is True:
        Buy_LTC = P_LTC
    if hold_BTG is True:
        Buy_BTG = P_BTG
    if hold_NEO is True:
        Buy_NEO = P_NEO
    if hold_ETC is True:
        Buy_ETC = P_ETC
    if hold_BCHA is True:
        Buy_BCHA = P_BCHA
    if hold_REP is True:
        Buy_REP = P_REP
    if hold_LINK is True:
        Buy_LINK = P_LINK
    if hold_DOT is True:
        Buy_DOT = P_DOT
    if hold_QTUM is True:
        Buy_QTUM = P_QTUM
    if hold_ATOM is True:
        Buy_ATOM = P_ATOM
    if hold_WAVES is True:
        Buy_WAVES = P_WAVES
    if hold_EOS is True:
        Buy_EOS = P_EOS
    if hold_STRK is True:
        Buy_STRK = P_STRK
    if hold_GAS is True:
        Buy_GAS = P_GAS
    if hold_OMG is True:
        Buy_OMG = P_OMG
    if hold_THETA is True:
        Buy_THETA = P_THETA
    if hold_TON is True:
        Buy_TON = P_TON
    if hold_LSK is True:
        Buy_LSK = P_LSK
    if hold_SRM is True:
        Buy_SRM = P_SRM
    if hold_FLOW is True:
        Buy_FLOW = P_FLOW


    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BTC is True and hold_BTC is True and\
        Buy_BTC * 1.0011 < price_BTC:
        # BTC_balance = upbit.get_balance("KRW-BTC")
        # upbit.sell_market_order("KRW-BTC", BTC_balance)
        hold_BTC = False
        print("매도시간:", now, "매도가격(BTC):", price_BTC, "이익:", round(((price_BTC - Buy_BTC) - (Buy_BTC * 0.0005) + (price_BTC * 0.0005))/(price_BTC) * 10000, 1))
        op_mode_BTC = False
        # time.sleep(1)
    if op_mode_ETH is True and hold_ETH is True and\
        Buy_ETH * 1.0011 < price_ETH:
        # ETH_balance = upbit.get_balance("KRW-ETH")
        # upbit.sell_market_order("KRW-ETH", ETH_balance)
        hold_ETH = False
        print("매도시간:", now, "매도가격(ETH):", price_ETH, "이익:", round(((price_ETH - Buy_ETH) - (Buy_ETH * 0.0005) + (price_ETH * 0.0005))/(price_ETH) * 10000, 1))
        op_mode_ETH = False
        # time.sleep(1)
    if op_mode_BCH is True and hold_BCH is True and\
        Buy_BCH * 1.0011 < price_BCH:
        # BCH_balance = upbit.get_balance("KRW-BCH")
        # upbit.sell_market_order("KRW-BCH", BCH_balance)
        hold_BCH = False
        print("매도시간:", now, "매도가격(BCH):", price_BCH, "이익:", round(((price_BCH - Buy_BCH) - (Buy_BCH * 0.0005) + (price_BCH * 0.0005))/(price_BCH) * 10000, 1))
        op_mode_BCH = False
        # time.sleep(1)
    if op_mode_BSV is True and hold_BSV is True and\
        Buy_BSV * 1.0011 < price_BSV:
        # BSV_balance = upbit.get_balance("KRW-BSV")
        # upbit.sell_market_order("KRW-BSV", BSV_balance)
        hold_BSV = False
        print("매도시간:", now, "매도가격(BSV):", price_BSV, "이익:", round(((price_BSV - Buy_BSV) - (Buy_BSV * 0.0005) + (price_BSV * 0.0005))/(price_BSV) * 10000, 1))
        op_mode_BSV = False
        # time.sleep(1)
    if op_mode_LTC is True and hold_LTC is True and\
        Buy_LTC * 1.0011 < price_LTC:
        # LTC_balance = upbit.get_balance("KRW-LTC")
        # upbit.sell_market_order("KRW-LTC", LTC_balance)
        hold_LTC = False
        print("매도시간:", now, "매도가격(LTC):", price_LTC, "이익:", round(((price_LTC - Buy_LTC) - (Buy_LTC * 0.0005) + (price_LTC * 0.0005))/(price_LTC) * 10000, 1))
        op_mode_LTC = False
        # time.sleep(1)
    if op_mode_BTG is True and hold_BTG is True and\
        Buy_BTG * 1.0011 < price_BTG:
        # BTG_balance = upbit.get_balance("KRW-BTG")
        # upbit.sell_market_order("KRW-BTG", BTG_balance)
        hold_BTG = False
        print("매도시간:", now, "매도가격(BTG):", price_BTG, "이익:", round(((price_BTG - Buy_BTG) - (Buy_BTG * 0.0005) + (price_BTG * 0.0005))/(price_BTG) * 10000, 1))
        op_mode_BTG = False
        # time.sleep(1)
    if op_mode_NEO is True and hold_NEO is True and\
        Buy_NEO * 1.0011 < price_NEO:
        # NEO_balance = upbit.get_balance("KRW-NEO")
        # upbit.sell_market_order("KRW-NEO", NEO_balance)
        hold_NEO = False
        print("매도시간:", now, "매도가격(NEO):", price_NEO, "이익:", round(((price_NEO - Buy_NEO) - (Buy_NEO * 0.0005) + (price_NEO * 0.0005))/(price_NEO) * 10000, 1))
        op_mode_NEO = False
        # time.sleep(1)
    if op_mode_ETC is True and hold_ETC is True and\
        Buy_ETC * 1.0011 < price_ETC:
        # ETC_balance = upbit.get_balance("KRW-ETC")
        # upbit.sell_market_order("KRW-ETC", ETC_balance)
        hold_ETC = False
        print("매도시간:", now, "매도가격(ETC):", price_ETC, "이익:", round(((price_ETC - Buy_ETC) - (Buy_ETC * 0.0005) + (price_ETC * 0.0005))/(price_ETC) * 10000, 1))
        op_mode_ETC = False
        # time.sleep(1)
    if op_mode_BCHA is True and hold_BCHA is True and\
        Buy_BCHA * 1.0011 < price_BCHA:
        # BCHA_balance = upbit.get_balance("KRW-BCHA")
        # upbit.sell_market_order("KRW-BCHA", BCHA_balance)
        hold_BCHA = False
        print("매도시간:", now, "매도가격(BCHA):", price_BCHA, "이익:", round(((price_BCHA - Buy_BCHA) - (Buy_BCHA * 0.0005) + (price_BCHA * 0.0005))/(price_BCHA) * 10000, 1))
        op_mode_BCHA = False
        # time.sleep(1)
    if op_mode_REP is True and hold_REP is True and\
        Buy_REP * 1.0011 < price_REP:
        # REP_balance = upbit.get_balance("KRW-REP")
        # upbit.sell_market_order("KRW-REP", REP_balance)
        hold_REP = False
        print("매도시간:", now, "매도가격(REP):", price_REP, "이익:", round(((price_REP - Buy_REP) - (Buy_REP * 0.0005) + (price_REP * 0.0005))/(price_REP) * 10000, 1))
        op_mode_REP = False
        # time.sleep(1)
    if op_mode_LINK is True and hold_LINK is True and\
        Buy_LINK * 1.0011 < price_LINK:
        # LINK_balance = upbit.get_balance("KRW-LINK")
        # upbit.sell_market_order("KRW-LINK", LINK_balance)
        hold_LINK = False
        print("매도시간:", now, "매도가격(LINK):", price_LINK, "이익:", round(((price_LINK - Buy_LINK) - (Buy_LINK * 0.0005) + (price_LINK * 0.0005))/(price_LINK) * 10000, 1))
        op_mode_LINK = False
        # time.sleep(1)
    if op_mode_DOT is True and hold_DOT is True and\
        Buy_DOT * 1.0011 < price_DOT:
        # DOT_balance = upbit.get_balance("KRW-DOT")
        # upbit.sell_market_order("KRW-DOT", DOT_balance)
        hold_DOT = False
        print("매도시간:", now, "매도가격(DOT):", price_DOT, "이익:", round(((price_DOT - Buy_DOT) - (Buy_DOT * 0.0005) + (price_DOT * 0.0005))/(price_DOT) * 10000, 1))
        op_mode_DOT = False
        # time.sleep(1)
    if op_mode_QTUM is True and hold_QTUM is True and\
        Buy_QTUM * 1.0011 < price_QTUM:
        # QTUM_balance = upbit.get_balance("KRW-QTUM")
        # upbit.sell_market_order("KRW-QTUM", QTUM_balance)
        hold_QTUM = False
        print("매도시간:", now, "매도가격(QTUM):", price_QTUM, "이익:", round(((price_QTUM - Buy_QTUM) - (Buy_QTUM * 0.0005) + (price_QTUM * 0.0005))/(price_QTUM) * 10000, 1))
        op_mode_QTUM = False
        # time.sleep(1)
    if op_mode_ATOM is True and hold_ATOM is True and\
        Buy_ATOM * 1.0011 < price_ATOM:
        # ATOM_balance = upbit.get_balance("KRW-ATOM")
        # upbit.sell_market_order("KRW-ATOM", ATOM_balance)
        hold_ATOM = False
        print("매도시간:", now, "매도가격(ATOM):", price_ATOM, "이익:", round(((price_ATOM - Buy_ATOM) - (Buy_ATOM * 0.0005) + (price_ATOM * 0.0005))/(price_ATOM) * 10000, 1))
        op_mode_ATOM = False
        # time.sleep(1)
    if op_mode_WAVES is True and hold_WAVES is True and\
        Buy_WAVES * 1.0011 < price_WAVES:
        # WAVES_balance = upbit.get_balance("KRW-WAVES")
        # upbit.sell_market_order("KRW-WAVES", WAVES_balance)
        hold_WAVES = False
        print("매도시간:", now, "매도가격(WAVES):", price_WAVES, "이익:", round(((price_WAVES - Buy_WAVES) - (Buy_WAVES * 0.0005) + (price_WAVES * 0.0005))/(price_WAVES) * 10000, 1))
        op_mode_WAVES = False
        # time.sleep(1)
    if op_mode_EOS is True and hold_EOS is True and\
        Buy_EOS * 1.0011 < price_EOS:
        # EOS_balance = upbit.get_balance("KRW-EOS")
        # upbit.sell_market_order("KRW-EOS", EOS_balance)
        hold_EOS = False
        print("매도시간:", now, "매도가격(EOS):", price_EOS, "이익:", round(((price_EOS - Buy_EOS) - (Buy_EOS * 0.0005) + (price_EOS * 0.0005))/(price_EOS) * 10000, 1))
        op_mode_EOS = False
        # time.sleep(1)
    if op_mode_STRK is True and hold_STRK is True and\
        Buy_STRK * 1.0011 < price_STRK:
        # STRK_balance = upbit.get_balance("KRW-STRK")
        # upbit.sell_market_order("KRW-STRK", STRK_balance)
        hold_STRK = False
        print("매도시간:", now, "매도가격(STRK):", price_STRK, "이익:", round(((price_STRK - Buy_STRK) - (Buy_STRK * 0.0005) + (price_STRK * 0.0005))/(price_STRK) * 10000, 1))
        op_mode_STRK = False
        # time.sleep(1)
    if op_mode_GAS is True and hold_GAS is True and\
        Buy_GAS * 1.0011 < price_GAS:
        # GAS_balance = upbit.get_balance("KRW-GAS")
        # upbit.sell_market_order("KRW-GAS", GAS_balance)
        hold_GAS = False
        print("매도시간:", now, "매도가격(GAS):", price_GAS, "이익:", round(((price_GAS - Buy_GAS) - (Buy_GAS * 0.0005) + (price_GAS * 0.0005))/(price_GAS) * 10000, 1))
        op_mode_GAS = False
        # time.sleep(1)
    if op_mode_OMG is True and hold_OMG is True and\
        Buy_OMG * 1.0011 < price_OMG:
        # OMG_balance = upbit.get_balance("KRW-OMG")
        # upbit.sell_market_order("KRW-OMG", OMG_balance)
        hold_OMG = False
        print("매도시간:", now, "매도가격(OMG):", price_OMG, "이익:", round(((price_OMG - Buy_OMG) - (Buy_OMG * 0.0005) + (price_OMG * 0.0005))/(price_OMG) * 10000, 1))
        op_mode_OMG = False
        # time.sleep(1)
    if op_mode_THETA is True and hold_THETA is True and\
        Buy_THETA * 1.0011 < price_THETA:
        # THETA_balance = upbit.get_balance("KRW-THETA")
        # upbit.sell_market_order("KRW-THETA", THETA_balance)
        hold_THETA = False
        print("매도시간:", now, "매도가격(THETA):", price_THETA, "이익:", round(((price_THETA - Buy_THETA) - (Buy_THETA * 0.0005) + (price_THETA * 0.0005))/(price_THETA) * 10000, 1))
        op_mode_THETA = False
        # time.sleep(1)
    if op_mode_TON is True and hold_TON is True and\
        Buy_TON * 1.0011 < price_TON:
        # TON_balance = upbit.get_balance("KRW-TON")
        # upbit.sell_market_order("KRW-TON", TON_balance)
        hold_TON = False
        print("매도시간:", now, "매도가격(TON):", price_TON, "이익:", round(((price_TON - Buy_TON) - (Buy_TON * 0.0005) + (price_TON * 0.0005))/(price_TON) * 10000, 1))
        op_mode_TON = False
        # time.sleep(1)
    if op_mode_LSK is True and hold_LSK is True and\
        Buy_LSK * 1.0011 < price_LSK:
        # LSK_balance = upbit.get_balance("KRW-LSK")
        # upbit.sell_market_order("KRW-LSK", LSK_balance)
        hold_LSK = False
        print("매도시간:", now, "매도가격(LSK):", price_LSK, "이익:", round(((price_LSK - Buy_LSK) - (Buy_LSK * 0.0005) + (price_LSK * 0.0005))/(price_LSK) * 10000, 1))
        op_mode_LSK = False
        # time.sleep(1)
    if op_mode_SRM is True and hold_SRM is True and\
        Buy_SRM * 1.0011 < price_SRM:
        # SRM_balance = upbit.get_balance("KRW-SRM")
        # upbit.sell_market_order("KRW-SRM", SRM_balance)
        hold_SRM = False
        print("매도시간:", now, "매도가격(SRM):", price_SRM, "이익:", round(((price_SRM - Buy_SRM) - (Buy_SRM * 0.0005) + (price_SRM * 0.0005))/(price_SRM) * 10000, 1))
        op_mode_SRM = False
        # time.sleep(1)
    if op_mode_FLOW is True and hold_FLOW is True and\
        Buy_FLOW * 1.0011 < price_FLOW:
        # FLOW_balance = upbit.get_balance("KRW-FLOW")
        # upbit.sell_market_order("KRW-FLOW", FLOW_balance)
        hold_FLOW = False
        print("매도시간:", now, "매도가격(FLOW):", price_FLOW, "이익:", round(((price_FLOW - Buy_FLOW) - (Buy_FLOW * 0.0005) + (price_FLOW * 0.0005))/(price_FLOW) * 10000, 1))
        op_mode_FLOW = False
        # time.sleep(1)
        
    print(f"TIME: {now} BTC: {hold_BTC} ETH: {hold_ETH} BCH: {hold_BCH} BSV: {hold_BSV} LTC: {hold_LTC} BTG: {hold_BTG} NEO: {hold_NEO} ETC: {hold_ETC} BCHA: {hold_BCHA} REP: {hold_REP} LINK: {hold_LINK}")
    print(f"DOT: {hold_DOT} QTUM: {hold_QTUM} ATOM: {hold_ATOM} WAVES: {hold_WAVES} EOS: {hold_EOS} STRK: {hold_STRK} GAS: {hold_GAS} OMG: {hold_OMG} THETA: {hold_THETA} TON: {hold_TON} LSK: {hold_TON} SRM: {hold_SRM} FLOW: {hold_FLOW}")
    # time.sleep(1)


    
