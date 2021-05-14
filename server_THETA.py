## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_THETA = False
hold_THETA = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_THETA_240 = pyupbit.get_ohlcv("KRW-THETA", "minut240", 5)
        close_THETA_240 = df_THETA_240['close']
        m240_THETA = close_THETA_240.rolling(2).mean()
        m240_THETA_2_1 = m240_THETA[-1]
        time.sleep(1)
        df_THETA_5 = pyupbit.get_ohlcv("KRW-THETA", "minute5", 5)
        close_THETA_5 = df_THETA_5['close']
        m5_THETA_2 = close_THETA_5.rolling(2).mean()
        m5_THETA_1 = close_THETA_5.rolling(1).mean()
        m5_THETA_2_2 = m5_THETA_2[-2]
        m5_THETA_2_1 = m5_THETA_2[-1]
        m5_THETA_1_2 = m5_THETA_1[-2]
        m5_THETA_1_1 = m5_THETA_1[-1]
        op_mode_THETA = True
        time.sleep(1)
  
    price_THETA = pyupbit.get_current_price("KRW-THETA")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_THETA is True and hold_THETA is False and price_THETA is not None and\
        m5_THETA_2_2 - m5_THETA_1_2 > 0 and m5_THETA_2_1 - m5_THETA_1_1 < 0 and\
        m5_THETA_2_1 < price_THETA and m5_THETA_1_1 < price_THETA and m240_THETA_2_1 < price_THETA:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-THETA", 10000)
        hold_THETA = True
        print("Btime:", now, "Bprice(THETA):", price_THETA)
        P_THETA = price_THETA
        # time.sleep(1)
  
    
    if hold_THETA is True:
        Buy_THETA = P_THETA
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_THETA is True and hold_THETA is True and\
        Buy_THETA * 1.0012 < price_THETA:
        THETA_balance = upbit.get_balance("KRW-THETA")
        upbit.sell_market_order("KRW-THETA", THETA_balance)
        hold_THETA = False
        print("Stime:", now, "Sprice(THETA):", price_THETA, "IN:", round(((price_THETA - Buy_THETA) - (Buy_THETA * 0.0005) + (price_THETA * 0.0005))/(price_THETA) * 10000, 1))
        op_mode_THETA = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_THETA} op: {op_mode_THETA}")
    time.sleep(1)
   

