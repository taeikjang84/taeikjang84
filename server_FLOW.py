## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_FLOW = False
hold_FLOW = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_FLOW_240 = pyupbit.get_ohlcv("KRW-FLOW", "minut240", 5)
        close_FLOW_240 = df_FLOW_240['close']
        m240_FLOW = close_FLOW_240.rolling(2).mean()
        m240_FLOW_2_1 = m240_FLOW[-1]
        time.sleep(1)
        df_FLOW_5 = pyupbit.get_ohlcv("KRW-FLOW", "minute5", 5)
        close_FLOW_5 = df_FLOW_5['close']
        m5_FLOW_2 = close_FLOW_5.rolling(2).mean()
        m5_FLOW_1 = close_FLOW_5.rolling(1).mean()
        m5_FLOW_2_2 = m5_FLOW_2[-2]
        m5_FLOW_2_1 = m5_FLOW_2[-1]
        m5_FLOW_1_2 = m5_FLOW_1[-2]
        m5_FLOW_1_1 = m5_FLOW_1[-1]
        op_mode_FLOW = True
        time.sleep(1)
  
    price_FLOW = pyupbit.get_current_price("KRW-FLOW")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_FLOW is True and hold_FLOW is False and price_FLOW is not None and\
        m5_FLOW_2_2 - m5_FLOW_1_2 > 0 and m5_FLOW_2_1 - m5_FLOW_1_1 < 0 and\
        m5_FLOW_2_1 < price_FLOW and m5_FLOW_1_1 < price_FLOW and m240_FLOW_2_1 < price_FLOW:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-FLOW", 10000)
        hold_FLOW = True
        print("Btime:", now, "Bprice(FLOW):", price_FLOW)
        P_FLOW = price_FLOW
        # time.sleep(1)
  
    
    if hold_FLOW is True:
        Buy_FLOW = P_FLOW
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_FLOW is True and hold_FLOW is True and\
        Buy_FLOW * 1.0012 < price_FLOW:
        FLOW_balance = upbit.get_balance("KRW-FLOW")
        upbit.sell_market_order("KRW-FLOW", FLOW_balance)
        hold_FLOW = False
        print("Stime:", now, "Sprice(FLOW):", price_FLOW, "IN:", round(((price_FLOW - Buy_FLOW) - (Buy_FLOW * 0.0005) + (price_FLOW * 0.0005))/(price_FLOW) * 10000, 1))
        op_mode_FLOW = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_FLOW} op: {op_mode_FLOW}")
    time.sleep(1)
   

