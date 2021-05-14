## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_DOT = False
hold_DOT = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_DOT_240 = pyupbit.get_ohlcv("KRW-DOT", "minut240", 5)
        close_DOT_240 = df_DOT_240['close']
        m240_DOT = close_DOT_240.rolling(2).mean()
        m240_DOT_2_1 = m240_DOT[-1]
        df_DOT_5 = pyupbit.get_ohlcv("KRW-DOT", "minute5", 5)
        close_DOT_5 = df_DOT_5['close']
        m5_DOT_2 = close_DOT_5.rolling(2).mean()
        m5_DOT_1 = close_DOT_5.rolling(1).mean()
        m5_DOT_2_2 = m5_DOT_2[-2]
        m5_DOT_2_1 = m5_DOT_2[-1]
        m5_DOT_1_2 = m5_DOT_1[-2]
        m5_DOT_1_1 = m5_DOT_1[-1]
        op_mode_DOT = True
        time.sleep(1)
  
    price_DOT = pyupbit.get_current_price("KRW-DOT")
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_DOT is True and hold_DOT is False and price_DOT is not None and\
        m5_DOT_2_2 - m5_DOT_1_2 > 0 and m5_DOT_2_1 - m5_DOT_1_1 < 0 and\
        m5_DOT_2_1 < price_DOT and m5_DOT_1_1 < price_DOT and m240_DOT_2_1 < price_DOT:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-DOT", 10000)
        hold_DOT = True
        print("Btime:", now, "Bprice(DOT):", price_DOT)
        P_DOT = price_DOT
        # time.sleep(1)
  
    
    if hold_DOT is True:
        Buy_DOT = P_DOT
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_DOT is True and hold_DOT is True and\
        Buy_DOT * 1.0012 < price_DOT:
        DOT_balance = upbit.get_balance("KRW-DOT")
        upbit.sell_market_order("KRW-DOT", DOT_balance)
        hold_DOT = False
        print("Stime:", now, "Sprice(DOT):", price_DOT, "IN:", round(((price_DOT - Buy_DOT) - (Buy_DOT * 0.0005) + (price_DOT * 0.0005))/(price_DOT) * 10000, 1))
        op_mode_DOT = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_DOT} op: {op_mode_DOT}")
   

