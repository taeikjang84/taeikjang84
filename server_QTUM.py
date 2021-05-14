## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_QTUM = False
hold_QTUM = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_QTUM_240 = pyupbit.get_ohlcv("KRW-QTUM", "minut240", 5)
        close_QTUM_240 = df_QTUM_240['close']
        m240_QTUM = close_QTUM_240.rolling(2).mean()
        m240_QTUM_2_1 = m240_QTUM[-1]
        time.sleep(1)
        df_QTUM_5 = pyupbit.get_ohlcv("KRW-QTUM", "minute5", 5)
        close_QTUM_5 = df_QTUM_5['close']
        m5_QTUM_2 = close_QTUM_5.rolling(2).mean()
        m5_QTUM_1 = close_QTUM_5.rolling(1).mean()
        m5_QTUM_2_2 = m5_QTUM_2[-2]
        m5_QTUM_2_1 = m5_QTUM_2[-1]
        m5_QTUM_1_2 = m5_QTUM_1[-2]
        m5_QTUM_1_1 = m5_QTUM_1[-1]
        op_mode_QTUM = True
  
  
    price_QTUM = pyupbit.get_current_price("KRW-QTUM")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_QTUM is True and hold_QTUM is False and price_QTUM is not None and\
        m5_QTUM_2_2 - m5_QTUM_1_2 > 0 and m5_QTUM_2_1 - m5_QTUM_1_1 < 0 and\
        m5_QTUM_2_1 < price_QTUM and m5_QTUM_1_1 < price_QTUM and m240_QTUM_2_1 < price_QTUM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-QTUM", 10000)
        hold_QTUM = True
        print("Btime:", now, "Bprice(QTUM):", price_QTUM)
        P_QTUM = price_QTUM
        # time.sleep(1)
  
    
    if hold_QTUM is True:
        Buy_QTUM = P_QTUM
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_QTUM is True and hold_QTUM is True and\
        Buy_QTUM * 1.0012 < price_QTUM:
        QTUM_balance = upbit.get_balance("KRW-QTUM")
        upbit.sell_market_order("KRW-QTUM", QTUM_balance)
        hold_QTUM = False
        print("Stime:", now, "Sprice(QTUM):", price_QTUM, "IN:", round(((price_QTUM - Buy_QTUM) - (Buy_QTUM * 0.0005) + (price_QTUM * 0.0005))/(price_QTUM) * 10000, 1))
        op_mode_QTUM = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_QTUM} op: {op_mode_QTUM}")

   

