## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_TON = False
hold_TON = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_TON_240 = pyupbit.get_ohlcv("KRW-TON", "minut240", 5)
        close_TON_240 = df_TON_240['close']
        m240_TON = close_TON_240.rolling(2).mean()
        m240_TON_2_1 = m240_TON[-1]
        time.sleep(1)
        df_TON_5 = pyupbit.get_ohlcv("KRW-TON", "minute5", 5)
        close_TON_5 = df_TON_5['close']
        m5_TON_2 = close_TON_5.rolling(2).mean()
        m5_TON_1 = close_TON_5.rolling(1).mean()
        m5_TON_2_2 = m5_TON_2[-2]
        m5_TON_2_1 = m5_TON_2[-1]
        m5_TON_1_2 = m5_TON_1[-2]
        m5_TON_1_1 = m5_TON_1[-1]
        op_mode_TON = True
        time.sleep(1)

  
    price_TON = pyupbit.get_current_price("KRW-TON")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_TON is True and hold_TON is False and price_TON is not None and\
        m5_TON_2_2 - m5_TON_1_2 > 0 and m5_TON_2_1 - m5_TON_1_1 < 0 and\
        m5_TON_2_1 < price_TON and m5_TON_1_1 < price_TON and m240_TON_2_1 < price_TON:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-TON", 10000)
        hold_TON = True
        print("Btime:", now, "Bprice(TON):", price_TON)
        P_TON = price_TON
        # time.sleep(1)
  
    
    if hold_TON is True:
        Buy_TON = P_TON
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_TON is True and hold_TON is True and\
        Buy_TON * 1.0012 < price_TON:
        TON_balance = upbit.get_balance("KRW-TON")
        upbit.sell_market_order("KRW-TON", TON_balance)
        hold_TON = False
        print("Stime:", now, "Sprice(TON):", price_TON, "IN:", round(((price_TON - Buy_TON) - (Buy_TON * 0.0005) + (price_TON * 0.0005))/(price_TON) * 10000, 1))
        op_mode_TON = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_TON} op: {op_mode_TON}")
    time.sleep(1)

   

