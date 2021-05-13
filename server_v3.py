## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

# get 240 minutes 2 ave before 1
def get_m240_2_1(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute60", 3)
    close = df['close']
    m240_2_1 = close.rolling(2).mean()
    return m240_2_1[-1]
m240_2_1_BTC = get_m240_2_1("KRW-BTC")
m240_2_1_ETH = get_m240_2_1("KRW-ETH")
m240_2_1_BCH = get_m240_2_1("KRW-BCH")
m240_2_1_BSV = get_m240_2_1("KRW-BSV")
m240_2_1_LTC = get_m240_2_1("KRW-LTC")
m240_2_1_BTG = get_m240_2_1("KRW-BTG")
m240_2_1_NEO = get_m240_2_1("KRW-NEO")
m240_2_1_ETC = get_m240_2_1("KRW-ETC")
m240_2_1_BCHA = get_m240_2_1("KRW-BCHA")
m240_2_1_REP = get_m240_2_1("KRW-REP")
m240_2_1_LINK = get_m240_2_1("KRW-LINK")
m240_2_1_DOT = get_m240_2_1("KRW-DOT")
m240_2_1_QTUM = get_m240_2_1("KRW-QTUM")
m240_2_1_ATOM = get_m240_2_1("KRW-ATOM")
m240_2_1_WAVES = get_m240_2_1("KRW-WAVES")
m240_2_1_EOS = get_m240_2_1("KRW-EOS")
m240_2_1_STRK = get_m240_2_1("KRW-STRK")
m240_2_1_GAS = get_m240_2_1("KRW-GAS")
m240_2_1_OMG = get_m240_2_1("KRW-OMG")
m240_2_1_THETA = get_m240_2_1("KRW-THETA")
m240_2_1_TON = get_m240_2_1("KRW-TON")
m240_2_1_LSK = get_m240_2_1("KRW-LSK")
m240_2_1_SRM = get_m240_2_1("KRW-SRM")
m240_2_1_FLOW = get_m240_2_1("KRW-FLOW")

# get 1 minute 2 ave befor 2
def get_m1_2_2(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_2_2 = close.rolling(2).mean()
    return m1_2_2[-2]
m1_2_2_BTC = get_m1_2_2("KRW-BTC")
m1_2_2_ETH = get_m1_2_2("KRW-ETH")
m1_2_2_BCH = get_m1_2_2("KRW-BCH")
m1_2_2_BSV = get_m1_2_2("KRW-BSV")
m1_2_2_LTC = get_m1_2_2("KRW-LTC")
m1_2_2_BTG = get_m1_2_2("KRW-BTG")
m1_2_2_NEO = get_m1_2_2("KRW-NEO")
m1_2_2_ETC = get_m1_2_2("KRW-ETC")
m1_2_2_BCHA = get_m1_2_2("KRW-BCHA")
m1_2_2_REP = get_m1_2_2("KRW-REP")
m1_2_2_LINK = get_m1_2_2("KRW-LINK")
m1_2_2_DOT = get_m1_2_2("KRW-DOT")
m1_2_2_QTUM = get_m1_2_2("KRW-QTUM")
m1_2_2_ATOM = get_m1_2_2("KRW-ATOM")
m1_2_2_WAVES = get_m1_2_2("KRW-WAVES")
m1_2_2_EOS = get_m1_2_2("KRW-EOS")
m1_2_2_STRK = get_m1_2_2("KRW-STRK")
m1_2_2_GAS = get_m1_2_2("KRW-GAS")
m1_2_2_OMG = get_m1_2_2("KRW-OMG")
m1_2_2_THETA = get_m1_2_2("KRW-THETA")
m1_2_2_TON = get_m1_2_2("KRW-TON")
m1_2_2_LSK = get_m1_2_2("KRW-LSK")
m1_2_2_SRM = get_m1_2_2("KRW-SRM")
m1_2_2_FLOW = get_m1_2_2("KRW-FLOW")

# get 1 minutes 2 ave befor 1
def get_m1_2_1(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_2_1 = close.rolling(2).mean()
    return m1_2_1[-1]
m1_2_1_BTC = get_m1_2_1("KRW-BTC")
m1_2_1_ETH = get_m1_2_1("KRW-ETH")
m1_2_1_BCH = get_m1_2_1("KRW-BCH")
m1_2_1_BSV = get_m1_2_1("KRW-BSV")
m1_2_1_LTC = get_m1_2_1("KRW-LTC")
m1_2_1_BTG = get_m1_2_1("KRW-BTG")
m1_2_1_NEO = get_m1_2_1("KRW-NEO")
m1_2_1_ETC = get_m1_2_1("KRW-ETC")
m1_2_1_BCHA = get_m1_2_1("KRW-BCHA")
m1_2_1_REP = get_m1_2_1("KRW-REP")
m1_2_1_LINK = get_m1_2_1("KRW-LINK")
m1_2_1_DOT = get_m1_2_1("KRW-DOT")
m1_2_1_QTUM = get_m1_2_1("KRW-QTUM")
m1_2_1_ATOM = get_m1_2_1("KRW-ATOM")
m1_2_1_WAVES = get_m1_2_1("KRW-WAVES")
m1_2_1_EOS = get_m1_2_1("KRW-EOS")
m1_2_1_STRK = get_m1_2_1("KRW-STRK")
m1_2_1_GAS = get_m1_2_1("KRW-GAS")
m1_2_1_OMG = get_m1_2_1("KRW-OMG")
m1_2_1_THETA = get_m1_2_1("KRW-THETA")
m1_2_1_TON = get_m1_2_1("KRW-TON")
m1_2_1_LSK = get_m1_2_1("KRW-LSK")
m1_2_1_SRM = get_m1_2_1("KRW-SRM")
m1_2_1_FLOW = get_m1_2_1("KRW-FLOW")

# get 1 minutes 1 ave befor 2
def get_m1_1_2(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_1_2 = close.rolling(1).mean()
    return m1_1_2[-2]
m1_1_2_BTC = get_m1_1_2("KRW-BTC")
m1_1_2_ETH = get_m1_1_2("KRW-ETH")
m1_1_2_BCH = get_m1_1_2("KRW-BCH")
m1_1_2_BSV = get_m1_1_2("KRW-BSV")
m1_1_2_LTC = get_m1_1_2("KRW-LTC")
m1_1_2_BTG = get_m1_1_2("KRW-BTG")
m1_1_2_NEO = get_m1_1_2("KRW-NEO")
m1_1_2_ETC = get_m1_1_2("KRW-ETC")
m1_1_2_BCHA = get_m1_1_2("KRW-BCHA")
m1_1_2_REP = get_m1_1_2("KRW-REP")
m1_1_2_LINK = get_m1_1_2("KRW-LINK")
m1_1_2_DOT = get_m1_1_2("KRW-DOT")
m1_1_2_QTUM = get_m1_1_2("KRW-QTUM")
m1_1_2_ATOM = get_m1_1_2("KRW-ATOM")
m1_1_2_WAVES = get_m1_1_2("KRW-WAVES")
m1_1_2_EOS = get_m1_1_2("KRW-EOS")
m1_1_2_STRK = get_m1_1_2("KRW-STRK")
m1_1_2_GAS = get_m1_1_2("KRW-GAS")
m1_1_2_OMG = get_m1_1_2("KRW-OMG")
m1_1_2_THETA = get_m1_1_2("KRW-THETA")
m1_1_2_TON = get_m1_1_2("KRW-TON")
m1_1_2_LSK = get_m1_1_2("KRW-LSK")
m1_1_2_SRM = get_m1_1_2("KRW-SRM")
m1_1_2_FLOW = get_m1_1_2("KRW-FLOW")

# get 1 minutes 1ave befor 1
def get_m1_1_1(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_1_1 = close.rolling(1).mean()
    return m1_1_1[-1]
m1_1_1_BTC = get_m1_1_1("KRW-BTC")
m1_1_1_ETH = get_m1_1_1("KRW-ETH")
m1_1_1_BCH = get_m1_1_1("KRW-BCH")
m1_1_1_BSV = get_m1_1_1("KRW-BSV")
m1_1_1_LTC = get_m1_1_1("KRW-LTC")
m1_1_1_BTG = get_m1_1_1("KRW-BTG")
m1_1_1_NEO = get_m1_1_1("KRW-NEO")
m1_1_1_ETC = get_m1_1_1("KRW-ETC")
m1_1_1_BCHA = get_m1_1_1("KRW-BCHA")
m1_1_1_REP = get_m1_1_1("KRW-REP")
m1_1_1_LINK = get_m1_1_1("KRW-LINK")
m1_1_1_DOT = get_m1_1_1("KRW-DOT")
m1_1_1_QTUM = get_m1_1_1("KRW-QTUM")
m1_1_1_ATOM = get_m1_1_1("KRW-ATOM")
m1_1_1_WAVES = get_m1_1_1("KRW-WAVES")
m1_1_1_EOS = get_m1_1_1("KRW-EOS")
m1_1_1_STRK = get_m1_1_1("KRW-STRK")
m1_1_1_GAS = get_m1_1_1("KRW-GAS")
m1_1_1_OMG = get_m1_1_1("KRW-OMG")
m1_1_1_THETA = get_m1_1_1("KRW-THETA")
m1_1_1_TON = get_m1_1_1("KRW-TON")
m1_1_1_LSK = get_m1_1_1("KRW-LSK")
m1_1_1_SRM = get_m1_1_1("KRW-SRM")
m1_1_1_FLOW = get_m1_1_1("KRW-FLOW")

# f = open("upbit.txt")
# lines = f.readline()
# access = lines[0].strip()
# secret = lines[1].strip()
# f.close()
# upbit = pyupbit.Upbit(access, secret)
upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성


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

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        m1_2_2_BTC = get_m1_2_2("KRW-BTC")
        m1_2_2_ETH = get_m1_2_2("KRW-ETH")
        m1_2_2_BCH = get_m1_2_2("KRW-BCH")
        m1_2_2_BSV = get_m1_2_2("KRW-BSV")
        m1_2_2_LTC = get_m1_2_2("KRW-LTC")
        m1_2_2_BTG = get_m1_2_2("KRW-BTG")
        m1_2_2_NEO = get_m1_2_2("KRW-NEO")
        m1_2_2_ETC = get_m1_2_2("KRW-ETC")
        m1_2_2_BCHA = get_m1_2_2("KRW-BCHA")
        m1_2_2_REP = get_m1_2_2("KRW-REP")
        m1_2_2_LINK = get_m1_2_2("KRW-LINK")
        m1_2_2_DOT = get_m1_2_2("KRW-DOT")
        m1_2_2_QTUM = get_m1_2_2("KRW-QTUM")
        m1_2_2_ATOM = get_m1_2_2("KRW-ATOM")
        m1_2_2_WAVES = get_m1_2_2("KRW-WAVES")
        m1_2_2_EOS = get_m1_2_2("KRW-EOS")
        m1_2_2_STRK = get_m1_2_2("KRW-STRK")
        m1_2_2_GAS = get_m1_2_2("KRW-GAS")
        m1_2_2_OMG = get_m1_2_2("KRW-OMG")
        m1_2_2_THETA = get_m1_2_2("KRW-THETA")
        m1_2_2_TON = get_m1_2_2("KRW-TON")
        m1_2_2_LSK = get_m1_2_2("KRW-LSK")
        m1_2_2_SRM = get_m1_2_2("KRW-SRM")
        m1_2_2_FLOW = get_m1_2_2("KRW-FLOW")
        m1_2_1_BTC = get_m1_2_1("KRW-BTC")
        m1_2_1_ETH = get_m1_2_1("KRW-ETH")
        m1_2_1_BCH = get_m1_2_1("KRW-BCH")
        m1_2_1_BSV = get_m1_2_1("KRW-BSV")
        m1_2_1_LTC = get_m1_2_1("KRW-LTC")
        m1_2_1_BTG = get_m1_2_1("KRW-BTG")
        m1_2_1_NEO = get_m1_2_1("KRW-NEO")
        m1_2_1_ETC = get_m1_2_1("KRW-ETC")
        m1_2_1_BCHA = get_m1_2_1("KRW-BCHA")
        m1_2_1_REP = get_m1_2_1("KRW-REP")
        m1_2_1_LINK = get_m1_2_1("KRW-LINK")
        m1_2_1_DOT = get_m1_2_1("KRW-DOT")
        m1_2_1_QTUM = get_m1_2_1("KRW-QTUM")
        m1_2_1_ATOM = get_m1_2_1("KRW-ATOM")
        m1_2_1_WAVES = get_m1_2_1("KRW-WAVES")
        m1_2_1_EOS = get_m1_2_1("KRW-EOS")
        m1_2_1_STRK = get_m1_2_1("KRW-STRK")
        m1_2_1_GAS = get_m1_2_1("KRW-GAS")
        m1_2_1_OMG = get_m1_2_1("KRW-OMG")
        m1_2_1_THETA = get_m1_2_1("KRW-THETA")
        m1_2_1_TON = get_m1_2_1("KRW-TON")
        m1_2_1_LSK = get_m1_2_1("KRW-LSK")
        m1_2_1_SRM = get_m1_2_1("KRW-SRM")
        m1_2_1_FLOW = get_m1_2_1("KRW-FLOW")
        m1_1_2_BTC = get_m1_1_2("KRW-BTC")
        m1_1_2_ETH = get_m1_1_2("KRW-ETH")
        m1_1_2_BCH = get_m1_1_2("KRW-BCH")
        m1_1_2_BSV = get_m1_1_2("KRW-BSV")
        m1_1_2_LTC = get_m1_1_2("KRW-LTC")
        m1_1_2_BTG = get_m1_1_2("KRW-BTG")
        m1_1_2_NEO = get_m1_1_2("KRW-NEO")
        m1_1_2_ETC = get_m1_1_2("KRW-ETC")
        m1_1_2_BCHA = get_m1_1_2("KRW-BCHA")
        m1_1_2_REP = get_m1_1_2("KRW-REP")
        m1_1_2_LINK = get_m1_1_2("KRW-LINK")
        m1_1_2_DOT = get_m1_1_2("KRW-DOT")
        m1_1_2_QTUM = get_m1_1_2("KRW-QTUM")
        m1_1_2_ATOM = get_m1_1_2("KRW-ATOM")
        m1_1_2_WAVES = get_m1_1_2("KRW-WAVES")
        m1_1_2_EOS = get_m1_1_2("KRW-EOS")
        m1_1_2_STRK = get_m1_1_2("KRW-STRK")
        m1_1_2_GAS = get_m1_1_2("KRW-GAS")
        m1_1_2_OMG = get_m1_1_2("KRW-OMG")
        m1_1_2_THETA = get_m1_1_2("KRW-THETA")
        m1_1_2_TON = get_m1_1_2("KRW-TON")
        m1_1_2_LSK = get_m1_1_2("KRW-LSK")
        m1_1_2_SRM = get_m1_1_2("KRW-SRM")
        m1_1_2_FLOW = get_m1_1_2("KRW-FLOW")
        m1_1_1_BTC = get_m1_1_1("KRW-BTC")
        m1_1_1_ETH = get_m1_1_1("KRW-ETH")
        m1_1_1_BCH = get_m1_1_1("KRW-BCH")
        m1_1_1_BSV = get_m1_1_1("KRW-BSV")
        m1_1_1_LTC = get_m1_1_1("KRW-LTC")
        m1_1_1_BTG = get_m1_1_1("KRW-BTG")
        m1_1_1_NEO = get_m1_1_1("KRW-NEO")
        m1_1_1_ETC = get_m1_1_1("KRW-ETC")
        m1_1_1_BCHA = get_m1_1_1("KRW-BCHA")
        m1_1_1_REP = get_m1_1_1("KRW-REP")
        m1_1_1_LINK = get_m1_1_1("KRW-LINK")
        m1_1_1_DOT = get_m1_1_1("KRW-DOT")
        m1_1_1_QTUM = get_m1_1_1("KRW-QTUM")
        m1_1_1_ATOM = get_m1_1_1("KRW-ATOM")
        m1_1_1_WAVES = get_m1_1_1("KRW-WAVES")
        m1_1_1_EOS = get_m1_1_1("KRW-EOS")
        m1_1_1_STRK = get_m1_1_1("KRW-STRK")
        m1_1_1_GAS = get_m1_1_1("KRW-GAS")
        m1_1_1_OMG = get_m1_1_1("KRW-OMG")
        m1_1_1_THETA = get_m1_1_1("KRW-THETA")
        m1_1_1_TON = get_m1_1_1("KRW-TON")
        m1_1_1_LSK = get_m1_1_1("KRW-LSK")
        m1_1_1_SRM = get_m1_1_1("KRW-SRM")
        m1_1_1_FLOW = get_m1_1_1("KRW-FLOW")
        m240_2_1_BTC = get_m240_2_1("KRW-BTC")
        m240_2_1_ETH = get_m240_2_1("KRW-ETH")
        m240_2_1_BCH = get_m240_2_1("KRW-BCH")
        m240_2_1_BSV = get_m240_2_1("KRW-BSV")
        m240_2_1_LTC = get_m240_2_1("KRW-LTC")
        m240_2_1_BTG = get_m240_2_1("KRW-BTG")
        m240_2_1_NEO = get_m240_2_1("KRW-NEO")
        m240_2_1_ETC = get_m240_2_1("KRW-ETC")
        m240_2_1_BCHA = get_m240_2_1("KRW-BCHA")
        m240_2_1_REP = get_m240_2_1("KRW-REP")
        m240_2_1_LINK = get_m240_2_1("KRW-LINK")
        m240_2_1_DOT = get_m240_2_1("KRW-DOT")
        m240_2_1_QTUM = get_m240_2_1("KRW-QTUM")
        m240_2_1_ATOM = get_m240_2_1("KRW-ATOM")
        m240_2_1_WAVES = get_m240_2_1("KRW-WAVES")
        m240_2_1_EOS = get_m240_2_1("KRW-EOS")
        m240_2_1_STRK = get_m240_2_1("KRW-STRK")
        m240_2_1_GAS = get_m240_2_1("KRW-GAS")
        m240_2_1_OMG = get_m240_2_1("KRW-OMG")
        m240_2_1_THETA = get_m240_2_1("KRW-THETA")
        m240_2_1_TON = get_m240_2_1("KRW-TON")
        m240_2_1_LSK = get_m240_2_1("KRW-LSK")
        m240_2_1_SRM = get_m240_2_1("KRW-SRM")
        m240_2_1_FLOW = get_m240_2_1("KRW-FLOW")
        
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
    price_NEO = pyupbit.get_current_price("KRW-NEO")
    price_ETC = pyupbit.get_current_price("KRW-ETC")
    price_BCHA = pyupbit.get_current_price("KRW-BCHA")
    price_REP = pyupbit.get_current_price("KRW-REP")
    price_LINK = pyupbit.get_current_price("KRW-LINK")
    price_DOT = pyupbit.get_current_price("KRW-DOT")
    price_QTUM = pyupbit.get_current_price("KRW-QTUM")
    price_ATOM = pyupbit.get_current_price("KRW-ATOM")
    price_WAVES = pyupbit.get_current_price("KRW-WAVES")
    price_EOS = pyupbit.get_current_price("KRW-EOS")
    price_STRK = pyupbit.get_current_price("KRW-STRK") 
    price_GAS = pyupbit.get_current_price("KRW-GAS") 
    price_OMG = pyupbit.get_current_price("KRW-OMG")
    price_THETA = pyupbit.get_current_price("KRW-THETA")
    price_TON = pyupbit.get_current_price("KRW-TON")
    price_LSK = pyupbit.get_current_price("KRW-LSK")
    price_SRM = pyupbit.get_current_price("KRW-SRM") 
    price_FLOW = pyupbit.get_current_price("KRW-FLOW") 


    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    # if op_mode_BTC is True and hold_BTC is False and price_BTC is not None and\
    #     m1_1_2_BTC - m1_2_2_BTC < 0 and m1_1_1_BTC - m1_2_1_BTC > 0 and\
    #     m1_1_1_BTC < price_BTC and m1_2_1_BTC <= price_BTC and m240_2_1_BTC < price_BTC:
    #     krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
    #     upbit.buy_market_order("KRW-BTC", 10000)
    #     hold_BTC = True
    #     print("Btime:", now, "Bprice(BTC):", price_BTC)
    #     P_BTC = price_BTC
    #     # time.sleep(1)
    if op_mode_ETH is True and hold_ETH is False and price_ETH is not None and\
        m1_1_2_ETH - m1_2_2_ETH < 0 and m1_1_1_ETH - m1_2_1_ETH > 0 and\
        m1_1_1_ETH < price_ETH and m1_2_1_ETH <= price_ETH and m240_2_1_ETH < price_ETH:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ETH", 10000)
        hold_ETH = True
        print("Btime:", now, "Bprice(ETH):", price_ETH)
        P_ETH = price_ETH
        # time.sleep(1)
    if op_mode_BCH is True and hold_BCH is False and price_BCH is not None and\
        m1_1_2_BCH - m1_2_2_BCH < 0 and m1_1_1_BCH - m1_2_1_BCH > 0 and\
        m1_1_1_BCH < price_BCH and m1_2_1_BCH <= price_BCH and m240_2_1_BCH < price_BCH:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BCH", 10000)
        hold_BCH = True
        print("Btime:", now, "Bprice(BCH):", price_BCH)
        P_BCH = price_BCH
        # time.sleep(1)
    if op_mode_BSV is True and hold_BSV is False and price_BSV is not None and\
        m1_1_2_BSV - m1_2_2_BSV < 0 and m1_1_1_BSV - m1_2_1_BSV > 0 and\
        m1_1_1_BSV < price_BSV and m1_2_1_BSV <= price_BSV and m240_2_1_BSV < price_BSV:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BSV", 10000)
        hold_BSV = True
        print("Btime:", now, "Bprice(BSV):", price_BSV)
        P_BSV = price_BSV
        # time.sleep(1)
    if op_mode_LTC is True and hold_LTC is False and price_LTC is not None and\
        m1_1_2_LTC - m1_2_2_LTC < 0 and m1_1_1_LTC - m1_2_1_LTC > 0 and\
        m1_1_1_LTC < price_LTC and m1_2_1_LTC <= price_LTC and m240_2_1_LTC < price_LTC:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LTC", 10000)
        hold_LTC = True
        print("Btime:", now, "Bprice(LTC):", price_LTC)
        P_LTC = price_LTC
        # time.sleep(1)
    if op_mode_BTG is True and hold_BTG is False and price_BTG is not None and\
        m1_1_2_BTG - m1_2_2_BTG < 0 and m1_1_1_BTG - m1_2_1_BTG > 0 and\
        m1_1_1_BTG < price_BTG and m1_2_1_BTG <= price_BTG and m240_2_1_BTG < price_BTG:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BTG", 10000)
        hold_BTG = True
        print("Btime:", now, "Bprice(BTG):", price_BTG)
        P_BTG = price_BTG
        # time.sleep(1)
    if op_mode_NEO is True and hold_NEO is False and price_NEO is not None and\
        m1_1_2_NEO - m1_2_2_NEO < 0 and m1_1_1_NEO - m1_2_1_NEO > 0 and\
        m1_1_1_NEO < price_NEO and m1_2_1_NEO <= price_NEO and m240_2_1_NEO < price_NEO:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-NEO", 10000)
        hold_NEO = True
        print("Btime:", now, "Bprice(NEO):", price_NEO)
        P_NEO = price_NEO
        # time.sleep(1)
    if op_mode_ETC is True and hold_ETC is False and price_ETC is not None and\
        m1_1_2_ETC - m1_2_2_ETC < 0 and m1_1_1_ETC - m1_2_1_ETC > 0 and\
        m1_1_1_ETC < price_ETC and m1_2_1_ETC <= price_ETC and m240_2_1_ETC < price_ETC:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ETC", 10000)
        hold_ETC = True
        print("Btime:", now, "Bprice(ETC):", price_ETC)
        P_ETC = price_ETC
        # time.sleep(1)
    if op_mode_BCHA is True and hold_BCHA is False and price_BCHA is not None and\
        m1_1_2_BCHA - m1_2_2_BCHA < 0 and m1_1_1_BCHA - m1_2_1_BCHA > 0 and\
        m1_1_1_BCHA < price_BCHA and m1_2_1_BCHA <= price_BCHA and m240_2_1_BCHA < price_BCHA:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BCHA", 10000)
        hold_BCHA = True
        print("Btime:", now, "Bprice(BCHA):", price_BCHA)
        P_BCHA = price_BCHA
        # time.sleep(1)
    if op_mode_REP is True and hold_REP is False and price_REP is not None and\
        m1_1_2_REP - m1_2_2_REP < 0 and m1_1_1_REP - m1_2_1_REP > 0 and\
        m1_1_1_REP < price_REP and m1_2_1_REP <= price_REP and m240_2_1_REP < price_REP:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-REP", 10000)
        hold_REP = True
        print("Btime:", now, "Bprice(REP):", price_REP)
        P_REP = price_REP
        # time.sleep(1)
    if op_mode_LINK is True and hold_LINK is False and price_LINK is not None and\
        m1_1_2_LINK - m1_2_2_LINK < 0 and m1_1_1_LINK - m1_2_1_LINK > 0 and m1_1_1_LINK < price_LINK and m1_2_1_LINK <= price_LINK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LINK", 10000)
        hold_LINK = True
        print("Btime:", now, "Bprice(LINK):", price_LINK)
        P_LINK = price_LINK
        # time.sleep(1)
    if op_mode_DOT is True and hold_DOT is False and price_DOT is not None and\
        m1_1_2_DOT - m1_2_2_DOT < 0 and m1_1_1_DOT - m1_2_1_DOT > 0 and m1_1_1_DOT < price_DOT and m1_2_1_DOT <= price_DOT:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-DOT", 10000)
        hold_DOT = True
        print("Btime:", now, "Bprice(DOT):", price_DOT)
        P_DOT = price_DOT
        # time.sleep(1)
    if op_mode_QTUM is True and hold_QTUM is False and price_QTUM is not None and\
        m1_1_2_QTUM - m1_2_2_QTUM < 0 and m1_1_1_QTUM - m1_2_1_QTUM > 0 and m1_1_1_QTUM < price_QTUM and m1_2_1_QTUM <= price_QTUM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-QTUM", 10000)
        hold_QTUM = True
        print("Btime:", now, "Bprice(QTUM):", price_QTUM)
        P_QTUM = price_QTUM
        # time.sleep(1)
    if op_mode_ATOM is True and hold_ATOM is False and price_ATOM is not None and\
        m1_1_2_ATOM - m1_2_2_ATOM < 0 and m1_1_1_ATOM - m1_2_1_ATOM > 0 and\
        m1_1_1_ATOM < price_ATOM and m1_2_1_ATOM <= price_ATOM and m240_2_1_ATOM < price_ATOM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ATOM", 10000)
        hold_ATOM = True
        print("Btime:", now, "Bprice(ATOM):", price_ATOM)
        P_ATOM = price_ATOM
        # time.sleep(1)
    if op_mode_WAVES is True and hold_WAVES is False and price_WAVES is not None and\
        m1_1_2_WAVES - m1_2_2_WAVES < 0 and m1_1_1_WAVES - m1_2_1_WAVES > 0 and\
        m1_1_1_WAVES < price_WAVES and m1_2_1_WAVES <= price_WAVES and m240_2_1_WAVES < price_WAVES:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-WAVES", 10000)
        hold_WAVES = True
        print("Btime:", now, "Bprice(WAVES):", price_WAVES)
        P_WAVES = price_WAVES
        # time.sleep(1)
    if op_mode_EOS is True and hold_EOS is False and price_EOS is not None and\
        m1_1_2_EOS - m1_2_2_EOS < 0 and m1_1_1_EOS - m1_2_1_EOS > 0 and\
        m1_1_1_EOS < price_EOS and m1_2_1_EOS <= price_EOS and m240_2_1_EOS < price_EOS:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-EOS", 10000)
        hold_EOS = True
        print("Btime:", now, "Bprice(EOS):", price_EOS)
        P_EOS = price_EOS
        # time.sleep(1)
    if op_mode_STRK is True and hold_STRK is False and price_STRK is not None and\
        m1_1_2_STRK - m1_2_2_STRK < 0 and m1_1_1_STRK - m1_2_1_STRK > 0 and\
        m1_1_1_STRK < price_STRK and m1_2_1_STRK <= price_STRK and m240_2_1_STRK < price_STRK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-STRK", 10000)
        hold_STRK = True
        print("Btime:", now, "Bprice(STRK):", price_STRK)
        P_STRK = price_STRK
        # time.sleep(1)
    if op_mode_GAS is True and hold_GAS is False and price_GAS is not None and\
        m1_1_2_GAS - m1_2_2_GAS < 0 and m1_1_1_GAS - m1_2_1_GAS > 0 and\
        m1_1_1_GAS < price_GAS and m1_2_1_GAS <= price_GAS and m240_2_1_GAS < price_GAS:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-GAS", 10000)
        hold_GAS = True
        print("Btime:", now, "Bprice(GAS):", price_GAS)
        P_GAS = price_GAS
        # time.sleep(1)
    if op_mode_OMG is True and hold_OMG is False and price_OMG is not None and\
        m1_1_2_OMG - m1_2_2_OMG < 0 and m1_1_1_OMG - m1_2_1_OMG > 0 and\
        m1_1_1_OMG < price_OMG and m1_2_1_OMG <= price_OMG and m240_2_1_OMG < price_OMG:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-OMG", 10000)
        hold_OMG = True
        print("Btime:", now, "Bprice(OMG):", price_OMG)
        P_OMG = price_OMG
        # time.sleep(1)
    if op_mode_THETA is True and hold_THETA is False and price_THETA is not None and\
        m1_1_2_THETA - m1_2_2_THETA < 0 and m1_1_1_THETA - m1_2_1_THETA > 0 and\
        m1_1_1_THETA < price_THETA and m1_2_1_THETA <= price_THETA and m240_2_1_THETA < price_THETA:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-THETA", 10000)
        hold_THETA = True
        print("Btime:", now, "Bprice(THETA):", price_THETA)
        P_THETA = price_THETA
        # time.sleep(1)
    if op_mode_TON is True and hold_TON is False and price_TON is not None and\
        m1_1_2_TON - m1_2_2_TON < 0 and m1_1_1_TON - m1_2_1_TON > 0 and\
        m1_1_1_TON < price_TON and m1_2_1_TON <= price_TON and m240_2_1_TON < price_TON:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-TON", 10000)
        hold_TON = True
        print("Btime:", now, "Bprice(TON):", price_TON)
        P_TON = price_TON
        # time.sleep(1)
    if op_mode_LSK is True and hold_LSK is False and price_LSK is not None and\
        m1_1_2_LSK - m1_2_2_LSK < 0 and m1_1_1_LSK - m1_2_1_LSK > 0 and\
        m1_1_1_LSK < price_LSK and m1_2_1_LSK <= price_LSK and m240_2_1_LSK < price_LSK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LSK", 10000)
        hold_LSK = True
        print("Btime:", now, "Bprice(LSK):", price_LSK)
        P_LSK = price_LSK
        # time.sleep(1)
    if op_mode_SRM is True and hold_SRM is False and price_SRM is not None and\
        m1_1_2_SRM - m1_2_2_SRM < 0 and m1_1_1_SRM - m1_2_1_SRM > 0 and\
        m1_1_1_SRM < price_SRM and m1_2_1_SRM <= price_SRM and m240_2_1_SRM < price_SRM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-SRM", 10000)
        hold_SRM = True
        print("Btime:", now, "Bprice(SRM):", price_SRM)
        P_SRM = price_SRM
        # time.sleep(1)
    if op_mode_FLOW is True and hold_FLOW is False and price_FLOW is not None and\
        m1_1_2_FLOW - m1_2_2_FLOW < 0 and m1_1_1_FLOW - m1_2_1_FLOW > 0 and\
        m1_1_1_FLOW < price_FLOW and m1_2_1_FLOW <= price_FLOW and m240_2_1_FLOW < price_FLOW:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-FLOW", 10000)
        hold_FLOW = True
        print("Btime:", now, "Bprice(FLOW):", price_FLOW)
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
        Buy_BTC * 1.0012 < price_BTC:
        BTC_balance = upbit.get_balance("KRW-BTC")
        upbit.sell_market_order("KRW-BTC", BTC_balance)
        hold_BTC = False
        print("Stime:", now, "Sprice(BTC):", price_BTC, "IN:", round(((price_BTC - Buy_BTC) - (Buy_BTC * 0.0005) + (price_BTC * 0.0005))/(price_BTC) * 10000, 1))
        op_mode_BTC = False
        # time.sleep(1)
    if op_mode_ETH is True and hold_ETH is True and\
        Buy_ETH * 1.0012 < price_ETH:
        ETH_balance = upbit.get_balance("KRW-ETH")
        upbit.sell_market_order("KRW-ETH", ETH_balance)
        hold_ETH = False
        print("Stime:", now, "Sprice(ETH):", price_ETH, "IN:", round(((price_ETH - Buy_ETH) - (Buy_ETH * 0.0005) + (price_ETH * 0.0005))/(price_ETH) * 10000, 1))
        op_mode_ETH = False
        # time.sleep(1)
    if op_mode_BCH is True and hold_BCH is True and\
        Buy_BCH * 1.0012 < price_BCH:
        BCH_balance = upbit.get_balance("KRW-BCH")
        upbit.sell_market_order("KRW-BCH", BCH_balance)
        hold_BCH = False
        print("Stime:", now, "Sprice(BCH):", price_BCH, "IN:", round(((price_BCH - Buy_BCH) - (Buy_BCH * 0.0005) + (price_BCH * 0.0005))/(price_BCH) * 10000, 1))
        op_mode_BCH = False
        # time.sleep(1)
    if op_mode_BSV is True and hold_BSV is True and\
        Buy_BSV * 1.0012 < price_BSV:
        BSV_balance = upbit.get_balance("KRW-BSV")
        upbit.sell_market_order("KRW-BSV", BSV_balance)
        hold_BSV = False
        print("Stime:", now, "Sprice(BSV):", price_BSV, "IN:", round(((price_BSV - Buy_BSV) - (Buy_BSV * 0.0005) + (price_BSV * 0.0005))/(price_BSV) * 10000, 1))
        op_mode_BSV = False
        # time.sleep(1)
    if op_mode_LTC is True and hold_LTC is True and\
        Buy_LTC * 1.0012 < price_LTC:
        LTC_balance = upbit.get_balance("KRW-LTC")
        upbit.sell_market_order("KRW-LTC", LTC_balance)
        hold_LTC = False
        print("Stime:", now, "Sprice(LTC):", price_LTC, "IN:", round(((price_LTC - Buy_LTC) - (Buy_LTC * 0.0005) + (price_LTC * 0.0005))/(price_LTC) * 10000, 1))
        op_mode_LTC = False
        # time.sleep(1)
    if op_mode_BTG is True and hold_BTG is True and\
        Buy_BTG * 1.0012 < price_BTG:
        BTG_balance = upbit.get_balance("KRW-BTG")
        upbit.sell_market_order("KRW-BTG", BTG_balance)
        hold_BTG = False
        print("Stime:", now, "Sprice(BTG):", price_BTG, "IN:", round(((price_BTG - Buy_BTG) - (Buy_BTG * 0.0005) + (price_BTG * 0.0005))/(price_BTG) * 10000, 1))
        op_mode_BTG = False
        # time.sleep(1)
    if op_mode_NEO is True and hold_NEO is True and\
        Buy_NEO * 1.0012 < price_NEO:
        NEO_balance = upbit.get_balance("KRW-NEO")
        upbit.sell_market_order("KRW-NEO", NEO_balance)
        hold_NEO = False
        print("Stime:", now, "Sprice(NEO):", price_NEO, "IN:", round(((price_NEO - Buy_NEO) - (Buy_NEO * 0.0005) + (price_NEO * 0.0005))/(price_NEO) * 10000, 1))
        op_mode_NEO = False
        # time.sleep(1)
    if op_mode_ETC is True and hold_ETC is True and\
        Buy_ETC * 1.0012 < price_ETC:
        ETC_balance = upbit.get_balance("KRW-ETC")
        upbit.sell_market_order("KRW-ETC", ETC_balance)
        hold_ETC = False
        print("Stime:", now, "Sprice(ETC):", price_ETC, "IN:", round(((price_ETC - Buy_ETC) - (Buy_ETC * 0.0005) + (price_ETC * 0.0005))/(price_ETC) * 10000, 1))
        op_mode_ETC = False
        # time.sleep(1)
    if op_mode_BCHA is True and hold_BCHA is True and\
        Buy_BCHA * 1.0012 < price_BCHA:
        BCHA_balance = upbit.get_balance("KRW-BCHA")
        upbit.sell_market_order("KRW-BCHA", BCHA_balance)
        hold_BCHA = False
        print("Stime:", now, "Sprice(BCHA):", price_BCHA, "IN:", round(((price_BCHA - Buy_BCHA) - (Buy_BCHA * 0.0005) + (price_BCHA * 0.0005))/(price_BCHA) * 10000, 1))
        op_mode_BCHA = False
        # time.sleep(1)
    if op_mode_REP is True and hold_REP is True and\
        Buy_REP * 1.0012 < price_REP:
        REP_balance = upbit.get_balance("KRW-REP")
        upbit.sell_market_order("KRW-REP", REP_balance)
        hold_REP = False
        print("Stime:", now, "Sprice(REP):", price_REP, "IN:", round(((price_REP - Buy_REP) - (Buy_REP * 0.0005) + (price_REP * 0.0005))/(price_REP) * 10000, 1))
        op_mode_REP = False
        # time.sleep(1)
    if op_mode_LINK is True and hold_LINK is True and\
        Buy_LINK * 1.0012 < price_LINK:
        LINK_balance = upbit.get_balance("KRW-LINK")
        upbit.sell_market_order("KRW-LINK", LINK_balance)
        hold_LINK = False
        print("Stime:", now, "Sprice(LINK):", price_LINK, "IN:", round(((price_LINK - Buy_LINK) - (Buy_LINK * 0.0005) + (price_LINK * 0.0005))/(price_LINK) * 10000, 1))
        op_mode_LINK = False
        # time.sleep(1)
    if op_mode_DOT is True and hold_DOT is True and\
        Buy_DOT * 1.0012 < price_DOT:
        DOT_balance = upbit.get_balance("KRW-DOT")
        upbit.sell_market_order("KRW-DOT", DOT_balance)
        hold_DOT = False
        print("Stime:", now, "Sprice(DOT):", price_DOT, "IN:", round(((price_DOT - Buy_DOT) - (Buy_DOT * 0.0005) + (price_DOT * 0.0005))/(price_DOT) * 10000, 1))
        op_mode_DOT = False
        # time.sleep(1)
    if op_mode_QTUM is True and hold_QTUM is True and\
        Buy_QTUM * 1.0012 < price_QTUM:
        QTUM_balance = upbit.get_balance("KRW-QTUM")
        upbit.sell_market_order("KRW-QTUM", QTUM_balance)
        hold_QTUM = False
        print("Stime:", now, "Sprice(QTUM):", price_QTUM, "IN:", round(((price_QTUM - Buy_QTUM) - (Buy_QTUM * 0.0005) + (price_QTUM * 0.0005))/(price_QTUM) * 10000, 1))
        op_mode_QTUM = False
        # time.sleep(1)
    if op_mode_ATOM is True and hold_ATOM is True and\
        Buy_ATOM * 1.0012 < price_ATOM:
        ATOM_balance = upbit.get_balance("KRW-ATOM")
        upbit.sell_market_order("KRW-ATOM", ATOM_balance)
        hold_ATOM = False
        print("Stime:", now, "Sprice(ATOM):", price_ATOM, "IN:", round(((price_ATOM - Buy_ATOM) - (Buy_ATOM * 0.0005) + (price_ATOM * 0.0005))/(price_ATOM) * 10000, 1))
        op_mode_ATOM = False
        # time.sleep(1)
    if op_mode_WAVES is True and hold_WAVES is True and\
        Buy_WAVES * 1.0012 < price_WAVES:
        WAVES_balance = upbit.get_balance("KRW-WAVES")
        upbit.sell_market_order("KRW-WAVES", WAVES_balance)
        hold_WAVES = False
        print("Stime:", now, "Sprice(WAVES):", price_WAVES, "IN:", round(((price_WAVES - Buy_WAVES) - (Buy_WAVES * 0.0005) + (price_WAVES * 0.0005))/(price_WAVES) * 10000, 1))
        op_mode_WAVES = False
        # time.sleep(1)
    if op_mode_EOS is True and hold_EOS is True and\
        Buy_EOS * 1.0012 < price_EOS:
        EOS_balance = upbit.get_balance("KRW-EOS")
        upbit.sell_market_order("KRW-EOS", EOS_balance)
        hold_EOS = False
        print("Stime:", now, "Sprice(EOS):", price_EOS, "IN:", round(((price_EOS - Buy_EOS) - (Buy_EOS * 0.0005) + (price_EOS * 0.0005))/(price_EOS) * 10000, 1))
        op_mode_EOS = False
        # time.sleep(1)
    if op_mode_STRK is True and hold_STRK is True and\
        Buy_STRK * 1.0012 < price_STRK:
        STRK_balance = upbit.get_balance("KRW-STRK")
        upbit.sell_market_order("KRW-STRK", STRK_balance)
        hold_STRK = False
        print("Stime:", now, "Sprice(STRK):", price_STRK, "IN:", round(((price_STRK - Buy_STRK) - (Buy_STRK * 0.0005) + (price_STRK * 0.0005))/(price_STRK) * 10000, 1))
        op_mode_STRK = False
        # time.sleep(1)
    if op_mode_GAS is True and hold_GAS is True and\
        Buy_GAS * 1.0012 < price_GAS:
        GAS_balance = upbit.get_balance("KRW-GAS")
        upbit.sell_market_order("KRW-GAS", GAS_balance)
        hold_GAS = False
        print("Stime:", now, "Sprice(GAS):", price_GAS, "IN:", round(((price_GAS - Buy_GAS) - (Buy_GAS * 0.0005) + (price_GAS * 0.0005))/(price_GAS) * 10000, 1))
        op_mode_GAS = False
        # time.sleep(1)
    if op_mode_OMG is True and hold_OMG is True and\
        Buy_OMG * 1.0012 < price_OMG:
        OMG_balance = upbit.get_balance("KRW-OMG")
        upbit.sell_market_order("KRW-OMG", OMG_balance)
        hold_OMG = False
        print("Stime:", now, "Sprice(OMG):", price_OMG, "IN:", round(((price_OMG - Buy_OMG) - (Buy_OMG * 0.0005) + (price_OMG * 0.0005))/(price_OMG) * 10000, 1))
        op_mode_OMG = False
        # time.sleep(1)
    if op_mode_THETA is True and hold_THETA is True and\
        Buy_THETA * 1.0012 < price_THETA:
        THETA_balance = upbit.get_balance("KRW-THETA")
        upbit.sell_market_order("KRW-THETA", THETA_balance)
        hold_THETA = False
        print("Stime:", now, "Sprice(THETA):", price_THETA, "IN:", round(((price_THETA - Buy_THETA) - (Buy_THETA * 0.0005) + (price_THETA * 0.0005))/(price_THETA) * 10000, 1))
        op_mode_THETA = False
        # time.sleep(1)
    if op_mode_TON is True and hold_TON is True and\
        Buy_TON * 1.0012 < price_TON:
        TON_balance = upbit.get_balance("KRW-TON")
        upbit.sell_market_order("KRW-TON", TON_balance)
        hold_TON = False
        print("Stime:", now, "Sprice(TON):", price_TON, "IN:", round(((price_TON - Buy_TON) - (Buy_TON * 0.0005) + (price_TON * 0.0005))/(price_TON) * 10000, 1))
        op_mode_TON = False
        # time.sleep(1)
    if op_mode_LSK is True and hold_LSK is True and\
        Buy_LSK * 1.0012 < price_LSK:
        LSK_balance = upbit.get_balance("KRW-LSK")
        upbit.sell_market_order("KRW-LSK", LSK_balance)
        hold_LSK = False
        print("Stime:", now, "Sprice(LSK):", price_LSK, "IN:", round(((price_LSK - Buy_LSK) - (Buy_LSK * 0.0005) + (price_LSK * 0.0005))/(price_LSK) * 10000, 1))
        op_mode_LSK = False
        # time.sleep(1)
    if op_mode_SRM is True and hold_SRM is True and\
        Buy_SRM * 1.0012 < price_SRM:
        SRM_balance = upbit.get_balance("KRW-SRM")
        upbit.sell_market_order("KRW-SRM", SRM_balance)
        hold_SRM = False
        print("Stime:", now, "Sprice(SRM):", price_SRM, "IN:", round(((price_SRM - Buy_SRM) - (Buy_SRM * 0.0005) + (price_SRM * 0.0005))/(price_SRM) * 10000, 1))
        op_mode_SRM = False
        # time.sleep(1)
    if op_mode_FLOW is True and hold_FLOW is True and\
        Buy_FLOW * 1.0012 < price_FLOW:
        FLOW_balance = upbit.get_balance("KRW-FLOW")
        upbit.sell_market_order("KRW-FLOW", FLOW_balance)
        hold_FLOW = False
        print("Stime:", now, "Sprice(FLOW):", price_FLOW, "IN:", round(((price_FLOW - Buy_FLOW) - (Buy_FLOW * 0.0005) + (price_FLOW * 0.0005))/(price_FLOW) * 10000, 1))
        op_mode_FLOW = False
        # time.sleep(1)
        
    print(f"time: {now} BTC: {hold_BTC} ETH: {hold_ETH} BCH: {hold_BCH} BSV: {hold_BSV} LTC: {hold_LTC} BTG: {hold_BTG} NEO: {hold_NEO} ETC: {hold_ETC} BCHA: {hold_BCHA} REP: {hold_REP} LINK: {hold_LINK}")
    print(f"DOT: {hold_DOT} QTUM: {hold_QTUM} ATOM: {hold_ATOM} WAVES: {hold_WAVES} EOS: {hold_EOS} STRK: {hold_STRK} GAS: {hold_GAS} OMG: {hold_OMG} THETA: {hold_THETA} TON: {hold_TON} LSK: {hold_LSK} SRM: {hold_SRM} FLOW: {hold_FLOW}")
    # time.sleep(1)


    
