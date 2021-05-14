## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_REP = False
hold_REP = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_REP_240 = pyupbit.get_ohlcv("KRW-REP", "minut240", 5)
        close_REP_240 = df_REP_240['close']
        m240_REP = close_REP_240.rolling(2).mean()
        m240_REP_2_1 = m240_REP[-1]
        time.sleep(1)
        df_REP_5 = pyupbit.get_ohlcv("KRW-REP", "minute5", 5)
        close_REP_5 = df_REP_5['close']
        m5_REP_2 = close_REP_5.rolling(2).mean()
        m5_REP_1 = close_REP_5.rolling(1).mean()
        m5_REP_2_2 = m5_REP_2[-2]
        m5_REP_2_1 = m5_REP_2[-1]
        m5_REP_1_2 = m5_REP_1[-2]
        m5_REP_1_1 = m5_REP_1[-1]
        op_mode_REP = True
        time.sleep(1)

  
    price_REP = pyupbit.get_current_price("KRW-REP")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_REP is True and hold_REP is False and price_REP is not None and\
        m5_REP_2_2 - m5_REP_1_2 > 0 and m5_REP_2_1 - m5_REP_1_1 < 0 and\
        m5_REP_2_1 < price_REP and m5_REP_1_1 < price_REP and m240_REP_2_1 < price_REP:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-REP", 10000)
        hold_REP = True
        print("Btime:", now, "Bprice(REP):", price_REP)
        P_REP = price_REP
        # time.sleep(1)
  
    
    if hold_REP is True:
        Buy_REP = P_REP
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_REP is True and hold_REP is True and\
        Buy_REP * 1.0012 < price_REP:
        REP_balance = upbit.get_balance("KRW-REP")
        upbit.sell_market_order("KRW-REP", REP_balance)
        hold_REP = False
        print("Stime:", now, "Sprice(REP):", price_REP, "IN:", round(((price_REP - Buy_REP) - (Buy_REP * 0.0005) + (price_REP * 0.0005))/(price_REP) * 10000, 1))
        op_mode_REP = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_REP} op: {op_mode_REP}")
    time.sleep(1)

   

