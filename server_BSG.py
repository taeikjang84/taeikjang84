## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_BTG = False
hold_BTG = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_BTG_240 = pyupbit.get_ohlcv("KRW-BTG", "minut240", 5)
        close_BTG_240 = df_BTG_240['close']
        m240_BTG = close_BTG_240.rolling(2).mean()
        m240_BTG_2_1 = m240_BTG[-1]
        time.sleep(1)
        df_BTG_5 = pyupbit.get_ohlcv("KRW-BTG", "minute5", 5)
        close_BTG_5 = df_BTG_5['close']
        m5_BTG_2 = close_BTG_5.rolling(2).mean()
        m5_BTG_1 = close_BTG_5.rolling(1).mean()
        m5_BTG_2_2 = m5_BTG_2[-2]
        m5_BTG_2_1 = m5_BTG_2[-1]
        m5_BTG_1_2 = m5_BTG_1[-2]
        m5_BTG_1_1 = m5_BTG_1[-1]
        op_mode_BTG = True
        time.sleep(1)

  
    price_BTG = pyupbit.get_current_price("KRW-BTG")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BTG is True and hold_BTG is False and price_BTG is not None and\
        m5_BTG_2_2 - m5_BTG_1_2 > 0 and m5_BTG_2_1 - m5_BTG_1_1 < 0 and\
        m5_BTG_2_1 < price_BTG and m5_BTG_1_1 < price_BTG and m240_BTG_2_1 < price_BTG:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BTG", 10000)
        hold_BTG = True
        print("Btime:", now, "Bprice(BTG):", price_BTG)
        P_BTG = price_BTG
        # time.sleep(1)
  
    
    if hold_BTG is True:
        Buy_BTG = P_BTG
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BTG is True and hold_BTG is True and\
        Buy_BTG * 1.0012 < price_BTG:
        BTG_balance = upbit.get_balance("KRW-BTG")
        upbit.sell_market_order("KRW-BTG", BTG_balance)
        hold_BTG = False
        print("Stime:", now, "Sprice(BTG):", price_BTG, "IN:", round(((price_BTG - Buy_BTG) - (Buy_BTG * 0.0005) + (price_BTG * 0.0005))/(price_BTG) * 10000, 1))
        op_mode_BTG = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_BTG} op: {op_mode_BTG}")
    time.sleep(1)
   
   

