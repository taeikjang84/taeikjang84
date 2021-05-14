## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_BSV = False
hold_BSV = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_BSV_240 = pyupbit.get_ohlcv("KRW-BSV", "minut240", 5)
        close_BSV_240 = df_BSV_240['close']
        m240_BSV = close_BSV_240.rolling(2).mean()
        m240_BSV_2_1 = m240_BSV[-1]
        time.sleep(1)
        df_BSV_5 = pyupbit.get_ohlcv("KRW-BSV", "minute5", 5)
        close_BSV_5 = df_BSV_5['close']
        m5_BSV_2 = close_BSV_5.rolling(2).mean()
        m5_BSV_1 = close_BSV_5.rolling(1).mean()
        m5_BSV_2_2 = m5_BSV_2[-2]
        m5_BSV_2_1 = m5_BSV_2[-1]
        m5_BSV_1_2 = m5_BSV_1[-2]
        m5_BSV_1_1 = m5_BSV_1[-1]
        op_mode_BSV = True
        time.sleep(1)

  
    price_BSV = pyupbit.get_current_price("KRW-BSV")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BSV is True and hold_BSV is False and price_BSV is not None and\
        m5_BSV_2_2 - m5_BSV_1_2 > 0 and m5_BSV_2_1 - m5_BSV_1_1 < 0 and\
        m5_BSV_2_1 < price_BSV and m5_BSV_1_1 < price_BSV and m240_BSV_2_1 < price_BSV:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BSV", 10000)
        hold_BSV = True
        print("Btime:", now, "Bprice(BSV):", price_BSV)
        P_BSV = price_BSV
        # time.sleep(1)
  
    
    if hold_BSV is True:
        Buy_BSV = P_BSV
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BSV is True and hold_BSV is True and\
        Buy_BSV * 1.0012 < price_BSV:
        BSV_balance = upbit.get_balance("KRW-BSV")
        upbit.sell_market_order("KRW-BSV", BSV_balance)
        hold_BSV = False
        print("Stime:", now, "Sprice(BSV):", price_BSV, "IN:", round(((price_BSV - Buy_BSV) - (Buy_BSV * 0.0005) + (price_BSV * 0.0005))/(price_BSV) * 10000, 1))
        op_mode_BSV = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_BSV} op: {op_mode_BSV}")
    time.sleep(1)
   

