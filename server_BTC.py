## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_BTC = False
hold_BTC = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_BTC_240 = pyupbit.get_ohlcv("KRW-BTC", "minut240", 5)
        close_BTC_240 = df_BTC_240['close']
        m240_BTC = close_BTC_240.rolling(2).mean()
        m240_BTC_2_1 = m240_BTC[-1]
        df_BTC_5 = pyupbit.get_ohlcv("KRW-BTC", "minute5", 5)
        close_BTC_5 = df_BTC_5['close']
        m5_BTC_2 = close_BTC_5.rolling(2).mean()
        m5_BTC_1 = close_BTC_5.rolling(1).mean()
        m5_BTC_2_2 = m5_BTC_2[-2]
        m5_BTC_2_1 = m5_BTC_2[-1]
        m5_BTC_1_2 = m5_BTC_1[-2]
        m5_BTC_1_1 = m5_BTC_1[-1]
        op_mode_BTC = True
        time.sleep(1)
  
    price_BTC = pyupbit.get_current_price("KRW-BTC")
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BTC is True and hold_BTC is False and price_BTC is not None and\
        m5_BTC_2_2 - m5_BTC_1_2 > 0 and m5_BTC_2_1 - m5_BTC_1_1 < 0 and\
        m5_BTC_2_1 < price_BTC and m5_BTC_1_1 < price_BTC and m240_BTC_2_1 < price_BTC:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BTC", 10000)
        hold_BTC = True
        print("Btime:", now, "Bprice(BTC):", price_BTC)
        P_BTC = price_BTC
        # time.sleep(1)
  
    
    if hold_BTC is True:
        Buy_BTC = P_BTC
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BTC is True and hold_BTC is True and\
        Buy_BTC * 1.0012 < price_BTC:
        BTC_balance = upbit.get_balance("KRW-BTC")
        upbit.sell_market_order("KRW-BTC", BTC_balance)
        hold_BTC = False
        print("Stime:", now, "Sprice(BTC):", price_BTC, "IN:", round(((price_BTC - Buy_BTC) - (Buy_BTC * 0.0005) + (price_BTC * 0.0005))/(price_BTC) * 10000, 1))
        op_mode_BTC = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_BTC} op: {op_mode_BTC}")
   

