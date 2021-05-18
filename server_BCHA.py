## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_BCHA = False
hold_BCHA = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_BCHA_240 = pyupbit.get_ohlcv("KRW-BCHA", "minut240", 5)
        close_BCHA_240 = df_BCHA_240['close']
        m240_BCHA = close_BCHA_240.rolling(2).mean()
        m240_BCHA_2_1 = m240_BCHA[-1]
        time.sleep(1)
        df_BCHA_5 = pyupbit.get_ohlcv("KRW-BCHA", "minute5", 5)
        close_BCHA_5 = df_BCHA_5['close']
        m5_BCHA_2 = close_BCHA_5.rolling(2).mean()
        m5_BCHA_1 = close_BCHA_5.rolling(1).mean()
        m5_BCHA_2_4 = m5_BCHA_2[-4]
        m5_BCHA_2_3 = m5_BCHA_2[-3]
        m5_BCHA_2_2 = m5_BCHA_2[-2]
        m5_BCHA_2_1 = m5_BCHA_2[-1]
        m5_BCHA_1_4 = m5_BCHA_1[-4]
        m5_BCHA_1_3 = m5_BCHA_1[-3]
        m5_BCHA_1_2 = m5_BCHA_1[-2]
        m5_BCHA_1_1 = m5_BCHA_1[-1]
        op_mode_BCHA = True
        time.sleep(1)

  
    price_BCHA = pyupbit.get_current_price("KRW-BCHA")
    time.sleep(1)
   
   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BCHA is True and hold_BCHA is False and price_BCHA is not None and\
        m5_BCHA_2_4 - m5_BCHA_1_4 > 0 and m5_BCHA_2_3 - m5_BCHA_1_3 > 0 and m5_BCHA_2_2 - m5_BCHA_1_2 > 0 and m5_BCHA_2_1 - m5_BCHA_1_1 < 0 and\
        m5_BCHA_2_1 < price_BCHA and m5_BCHA_1_1 < price_BCHA and m240_BCHA_2_1 < price_BCHA:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BCHA", 10000)
        hold_BCHA = True
        print("Btime:", now, "Bprice(BCHA):", price_BCHA)
        P_BCHA = price_BCHA
        # time.sleep(1)
  
    
    if hold_BCHA is True:
        Buy_BCHA = P_BCHA
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BCHA is True and hold_BCHA is True and\
        Buy_BCHA * 1.01 < price_BCHA:
        BCHA_balance = upbit.get_balance("KRW-BCHA")
        upbit.sell_market_order("KRW-BCHA", BCHA_balance)
        hold_BCHA = False
        print("Stime:", now, "Sprice(BCHA):", price_BCHA, "IN:", round(((price_BCHA - Buy_BCHA) - (Buy_BCHA * 0.0005) + (price_BCHA * 0.0005))/(price_BCHA) * 10000, 1))
        op_mode_BCHA = False
        time.sleep(250)
     
    # print(f"time: {now} hold: {hold_BCHA} op: {op_mode_BCHA}")
    time.sleep(1)

   

