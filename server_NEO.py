## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_NEO = False
hold_NEO = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_NEO_240 = pyupbit.get_ohlcv("KRW-NEO", "minut240", 5)
        close_NEO_240 = df_NEO_240['close']
        m240_NEO = close_NEO_240.rolling(2).mean()
        m240_NEO_2_1 = m240_NEO[-1]
        df_NEO_5 = pyupbit.get_ohlcv("KRW-NEO", "minute5", 5)
        close_NEO_5 = df_NEO_5['close']
        m5_NEO_2 = close_NEO_5.rolling(2).mean()
        m5_NEO_1 = close_NEO_5.rolling(1).mean()
        m5_NEO_2_2 = m5_NEO_2[-2]
        m5_NEO_2_1 = m5_NEO_2[-1]
        m5_NEO_1_2 = m5_NEO_1[-2]
        m5_NEO_1_1 = m5_NEO_1[-1]
        op_mode_NEO = True
        time.sleep(1)
  
    price_NEO = pyupbit.get_current_price("KRW-NEO")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_NEO is True and hold_NEO is False and price_NEO is not None and\
        m5_NEO_2_2 - m5_NEO_1_2 > 0 and m5_NEO_2_1 - m5_NEO_1_1 < 0 and\
        m5_NEO_2_1 < price_NEO and m5_NEO_1_1 < price_NEO and m240_NEO_2_1 < price_NEO:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-NEO", 10000)
        hold_NEO = True
        print("Btime:", now, "Bprice(NEO):", price_NEO)
        P_NEO = price_NEO
        # time.sleep(1)
  
    
    if hold_NEO is True:
        Buy_NEO = P_NEO
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_NEO is True and hold_NEO is True and\
        Buy_NEO * 1.0012 < price_NEO:
        NEO_balance = upbit.get_balance("KRW-NEO")
        upbit.sell_market_order("KRW-NEO", NEO_balance)
        hold_NEO = False
        print("Stime:", now, "Sprice(NEO):", price_NEO, "IN:", round(((price_NEO - Buy_NEO) - (Buy_NEO * 0.0005) + (price_NEO * 0.0005))/(price_NEO) * 10000, 1))
        op_mode_NEO = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_NEO} op: {op_mode_NEO}")
   

