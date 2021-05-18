## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_LTC = False
hold_LTC = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_LTC_240 = pyupbit.get_ohlcv("KRW-LTC", "minut240", 5)
        close_LTC_240 = df_LTC_240['close']
        m240_LTC = close_LTC_240.rolling(2).mean()
        m240_LTC_2_1 = m240_LTC[-1]
        time.sleep(1)
        df_LTC_5 = pyupbit.get_ohlcv("KRW-LTC", "minute5", 5)
        close_LTC_5 = df_LTC_5['close']
        m5_LTC_2 = close_LTC_5.rolling(2).mean()
        m5_LTC_1 = close_LTC_5.rolling(1).mean()
        m5_LTC_2_4 = m5_LTC_2[-4]
        m5_LTC_2_3 = m5_LTC_2[-3]
        m5_LTC_2_2 = m5_LTC_2[-2]
        m5_LTC_2_1 = m5_LTC_2[-1]
        m5_LTC_1_4 = m5_LTC_1[-4]
        m5_LTC_1_3 = m5_LTC_1[-3]
        m5_LTC_1_2 = m5_LTC_1[-2]
        m5_LTC_1_1 = m5_LTC_1[-1]
        op_mode_LTC = True
        time.sleep(1)

  
    price_LTC = pyupbit.get_current_price("KRW-LTC")
    time.sleep(1)
   
   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_LTC is True and hold_LTC is False and price_LTC is not None and\
        m5_LTC_2_4 - m5_LTC_1_4 > 0 and m5_LTC_2_3 - m5_LTC_1_3 > 0 and m5_LTC_2_2 - m5_LTC_1_2 > 0 and m5_LTC_2_1 - m5_LTC_1_1 < 0 and\
        m5_LTC_2_1 < price_LTC and m5_LTC_1_1 < price_LTC and m240_LTC_2_1 < price_LTC:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LTC", 10000)
        hold_LTC = True
        print("Btime:", now, "Bprice(LTC):", price_LTC)
        P_LTC = price_LTC
        # time.sleep(1)
  
    
    if hold_LTC is True:
        Buy_LTC = P_LTC
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_LTC is True and hold_LTC is True and\
        Buy_LTC * 1.01 < price_LTC:
        LTC_balance = upbit.get_balance("KRW-LTC")
        upbit.sell_market_order("KRW-LTC", LTC_balance)
        hold_LTC = False
        print("Stime:", now, "Sprice(LTC):", price_LTC, "IN:", round(((price_LTC - Buy_LTC) - (Buy_LTC * 0.0005) + (price_LTC * 0.0005))/(price_LTC) * 10000, 1))
        op_mode_LTC = False
        time.sleep(250)
     
    # print(f"time: {now} hold: {hold_LTC} op: {op_mode_LTC}")
    time.sleep(1)

   

