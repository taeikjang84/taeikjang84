## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_OMG = False
hold_OMG = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_OMG_240 = pyupbit.get_ohlcv("KRW-OMG", "minut240", 5)
        close_OMG_240 = df_OMG_240['close']
        m240_OMG = close_OMG_240.rolling(2).mean()
        m240_OMG_2_1 = m240_OMG[-1]
        time.sleep(1)
        df_OMG_5 = pyupbit.get_ohlcv("KRW-OMG", "minute5", 5)
        close_OMG_5 = df_OMG_5['close']
        m5_OMG_2 = close_OMG_5.rolling(2).mean()
        m5_OMG_1 = close_OMG_5.rolling(1).mean()
        m5_OMG_2_2 = m5_OMG_2[-2]
        m5_OMG_2_1 = m5_OMG_2[-1]
        m5_OMG_1_2 = m5_OMG_1[-2]
        m5_OMG_1_1 = m5_OMG_1[-1]
        op_mode_OMG = True
        time.sleep(1)
  
    price_OMG = pyupbit.get_current_price("KRW-OMG")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_OMG is True and hold_OMG is False and price_OMG is not None and\
        m5_OMG_2_2 - m5_OMG_1_2 > 0 and m5_OMG_2_1 - m5_OMG_1_1 < 0 and\
        m5_OMG_2_1 < price_OMG and m5_OMG_1_1 < price_OMG and m240_OMG_2_1 < price_OMG:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-OMG", 10000)
        hold_OMG = True
        print("Btime:", now, "Bprice(OMG):", price_OMG)
        P_OMG = price_OMG
        # time.sleep(1)
  
    
    if hold_OMG is True:
        Buy_OMG = P_OMG
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_OMG is True and hold_OMG is True and\
        Buy_OMG * 1.0012 < price_OMG:
        OMG_balance = upbit.get_balance("KRW-OMG")
        upbit.sell_market_order("KRW-OMG", OMG_balance)
        hold_OMG = False
        print("Stime:", now, "Sprice(OMG):", price_OMG, "IN:", round(((price_OMG - Buy_OMG) - (Buy_OMG * 0.0005) + (price_OMG * 0.0005))/(price_OMG) * 10000, 1))
        op_mode_OMG = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_OMG} op: {op_mode_OMG}")
    time.sleep(1)
   

