## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_LSK = False
hold_LSK = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_LSK_240 = pyupbit.get_ohlcv("KRW-LSK", "minut240", 5)
        close_LSK_240 = df_LSK_240['close']
        m240_LSK = close_LSK_240.rolling(2).mean()
        m240_LSK_2_1 = m240_LSK[-1]
        df_LSK_5 = pyupbit.get_ohlcv("KRW-LSK", "minute5", 5)
        close_LSK_5 = df_LSK_5['close']
        m5_LSK_2 = close_LSK_5.rolling(2).mean()
        m5_LSK_1 = close_LSK_5.rolling(1).mean()
        m5_LSK_2_2 = m5_LSK_2[-2]
        m5_LSK_2_1 = m5_LSK_2[-1]
        m5_LSK_1_2 = m5_LSK_1[-2]
        m5_LSK_1_1 = m5_LSK_1[-1]
        op_mode_LSK = True
        time.sleep(1)
  
    price_LSK = pyupbit.get_current_price("KRW-LSK")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_LSK is True and hold_LSK is False and price_LSK is not None and\
        m5_LSK_2_2 - m5_LSK_1_2 > 0 and m5_LSK_2_1 - m5_LSK_1_1 < 0 and\
        m5_LSK_2_1 < price_LSK and m5_LSK_1_1 < price_LSK and m240_LSK_2_1 < price_LSK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LSK", 10000)
        hold_LSK = True
        print("Btime:", now, "Bprice(LSK):", price_LSK)
        P_LSK = price_LSK
        # time.sleep(1)
  
    
    if hold_LSK is True:
        Buy_LSK = P_LSK
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_LSK is True and hold_LSK is True and\
        Buy_LSK * 1.0012 < price_LSK:
        LSK_balance = upbit.get_balance("KRW-LSK")
        upbit.sell_market_order("KRW-LSK", LSK_balance)
        hold_LSK = False
        print("Stime:", now, "Sprice(LSK):", price_LSK, "IN:", round(((price_LSK - Buy_LSK) - (Buy_LSK * 0.0005) + (price_LSK * 0.0005))/(price_LSK) * 10000, 1))
        op_mode_LSK = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_LSK} op: {op_mode_LSK}")
   

