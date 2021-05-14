## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_STRK = False
hold_STRK = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_STRK_240 = pyupbit.get_ohlcv("KRW-STRK", "minut240", 5)
        close_STRK_240 = df_STRK_240['close']
        m240_STRK = close_STRK_240.rolling(2).mean()
        m240_STRK_2_1 = m240_STRK[-1]
        time.sleep(1)
        df_STRK_5 = pyupbit.get_ohlcv("KRW-STRK", "minute5", 5)
        close_STRK_5 = df_STRK_5['close']
        m5_STRK_2 = close_STRK_5.rolling(2).mean()
        m5_STRK_1 = close_STRK_5.rolling(1).mean()
        m5_STRK_2_2 = m5_STRK_2[-2]
        m5_STRK_2_1 = m5_STRK_2[-1]
        m5_STRK_1_2 = m5_STRK_1[-2]
        m5_STRK_1_1 = m5_STRK_1[-1]
        op_mode_STRK = True
        time.sleep(1)
  
    price_STRK = pyupbit.get_current_price("KRW-STRK")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_STRK is True and hold_STRK is False and price_STRK is not None and\
        m5_STRK_2_2 - m5_STRK_1_2 > 0 and m5_STRK_2_1 - m5_STRK_1_1 < 0 and\
        m5_STRK_2_1 < price_STRK and m5_STRK_1_1 < price_STRK and m240_STRK_2_1 < price_STRK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-STRK", 10000)
        hold_STRK = True
        print("Btime:", now, "Bprice(STRK):", price_STRK)
        P_STRK = price_STRK
        # time.sleep(1)
  
    
    if hold_STRK is True:
        Buy_STRK = P_STRK
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_STRK is True and hold_STRK is True and\
        Buy_STRK * 1.0012 < price_STRK:
        STRK_balance = upbit.get_balance("KRW-STRK")
        upbit.sell_market_order("KRW-STRK", STRK_balance)
        hold_STRK = False
        print("Stime:", now, "Sprice(STRK):", price_STRK, "IN:", round(((price_STRK - Buy_STRK) - (Buy_STRK * 0.0005) + (price_STRK * 0.0005))/(price_STRK) * 10000, 1))
        op_mode_STRK = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_STRK} op: {op_mode_STRK}")
    time.sleep(1)

