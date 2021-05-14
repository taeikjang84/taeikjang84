## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_ETC = False
hold_ETC = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_ETC_240 = pyupbit.get_ohlcv("KRW-ETC", "minut240", 5)
        close_ETC_240 = df_ETC_240['close']
        m240_ETC = close_ETC_240.rolling(2).mean()
        m240_ETC_2_1 = m240_ETC[-1]
        df_ETC_5 = pyupbit.get_ohlcv("KRW-ETC", "minute5", 5)
        close_ETC_5 = df_ETC_5['close']
        time.sleep(1)
        m5_ETC_2 = close_ETC_5.rolling(2).mean()
        m5_ETC_1 = close_ETC_5.rolling(1).mean()
        m5_ETC_2_2 = m5_ETC_2[-2]
        m5_ETC_2_1 = m5_ETC_2[-1]
        m5_ETC_1_2 = m5_ETC_1[-2]
        m5_ETC_1_1 = m5_ETC_1[-1]
        op_mode_ETC = True

  
    price_ETC = pyupbit.get_current_price("KRW-ETC")
 
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_ETC is True and hold_ETC is False and price_ETC is not None and\
        m5_ETC_2_2 - m5_ETC_1_2 > 0 and m5_ETC_2_1 - m5_ETC_1_1 < 0 and\
        m5_ETC_2_1 < price_ETC and m5_ETC_1_1 < price_ETC and m240_ETC_2_1 < price_ETC:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ETC", 10000)
        hold_ETC = True
        print("Btime:", now, "Bprice(ETC):", price_ETC)
        P_ETC = price_ETC
        # time.sleep(1)
  
    
    if hold_ETC is True:
        Buy_ETC = P_ETC
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_ETC is True and hold_ETC is True and\
        Buy_ETC * 1.0012 < price_ETC:
        ETC_balance = upbit.get_balance("KRW-ETC")
        upbit.sell_market_order("KRW-ETC", ETC_balance)
        hold_ETC = False
        print("Stime:", now, "Sprice(ETC):", price_ETC, "IN:", round(((price_ETC - Buy_ETC) - (Buy_ETC * 0.0005) + (price_ETC * 0.0005))/(price_ETC) * 10000, 1))
        op_mode_ETC = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_ETC} op: {op_mode_ETC}")

   

