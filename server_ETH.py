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
m240_2_1_ETH = get_m240_2_1("KRW-ETH")

# get 1 minute 2 ave befor 2
def get_m1_2_2(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_2_2 = close.rolling(2).mean()
    return m1_2_2[-2]
m1_2_2_ETH = get_m1_2_2("KRW-ETH")

# get 1 minutes 2 ave befor 1
def get_m1_2_1(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_2_1 = close.rolling(2).mean()
    return m1_2_1[-1]
m1_2_1_ETH = get_m1_2_1("KRW-ETH")

# get 1 minutes 1 ave befor 2
def get_m1_1_2(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_1_2 = close.rolling(1).mean()
    return m1_1_2[-2]
m1_1_2_ETH = get_m1_1_2("KRW-ETH")

# get 1 minutes 1ave befor 1
def get_m1_1_1(ticker):
    df = pyupbit.get_ohlcv(ticker, "minute1", 3)
    close = df['close']
    m1_1_1 = close.rolling(1).mean()
    return m1_1_1[-1]
m1_1_1_ETH = get_m1_1_1("KRW-ETH")

# f = open("upbit.txt")
# lines = f.readline()
# access = lines[0].strip()
# secret = lines[1].strip()
# f.close()
# upbit = pyupbit.Upbit(access, secret)
upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성


op_mode_ETH = False
hold_ETH = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        m240_2_1_ETH = get_m240_2_1("KRW-ETH")
        m1_2_2_ETH = get_m1_2_2("KRW-ETH")
        m1_2_1_ETH = get_m1_2_1("KRW-ETH")
        m1_1_2_ETH = get_m1_1_2("KRW-ETH")
        m1_1_1_ETH = get_m1_1_1("KRW-ETH")
        op_mode_ETH = True
        time.sleep(1)
    price_ETH = pyupbit.get_current_price("KRW-ETH")
 


    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_ETH is True and hold_ETH is False and price_ETH is not None and\
        m1_1_2_ETH - m1_2_2_ETH < 0 and m1_1_1_ETH - m1_2_1_ETH > 0 and\
        m1_1_1_ETH < price_ETH and m1_2_1_ETH <= price_ETH and m240_2_1_ETH < price_ETH:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ETH", 10000)
        hold_ETH = True
        print("Btime:", now, "Bprice(ETH):", price_ETH)
        P_ETH = price_ETH
        # time.sleep(1)
    
    if hold_ETH is True:
        Buy_ETH = P_ETH
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_ETH is True and hold_ETH is True and\
        Buy_ETH * 1.0012 < price_ETH:
        ETH_balance = upbit.get_balance("KRW-ETH")
        upbit.sell_market_order("KRW-ETH", ETH_balance)
        hold_ETH = False
        print("Stime:", now, "Sprice(ETH):", price_ETH, "IN:", round(((price_ETH - Buy_ETH) - (Buy_ETH * 0.0005) + (price_ETH * 0.0005))/(price_ETH) * 10000, 1))
        op_mode_ETH = False
        # time.sleep(1)
 
    print(f"time: {now} hold: {hold_ETH} op: {op_mode_ETH}")


    
