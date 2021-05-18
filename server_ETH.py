## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_ETH = False
hold_ETH = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_ETH_240 = pyupbit.get_ohlcv("KRW-ETH", "minut240", 5)
        close_ETH_240 = df_ETH_240['close']
        m240_ETH = close_ETH_240.rolling(2).mean()
        m240_ETH_2_1 = m240_ETH[-1]
        time.sleep(1)
        df_ETH_5 = pyupbit.get_ohlcv("KRW-ETH", "minute5", 5)
        close_ETH_5 = df_ETH_5['close']
        m5_ETH_2 = close_ETH_5.rolling(2).mean()
        m5_ETH_1 = close_ETH_5.rolling(1).mean()
        m5_ETH_2_4 = m5_ETH_2[-4]
        m5_ETH_2_3 = m5_ETH_2[-3]
        m5_ETH_2_2 = m5_ETH_2[-2]
        m5_ETH_2_1 = m5_ETH_2[-1]
        m5_ETH_1_4 = m5_ETH_1[-4]
        m5_ETH_1_3 = m5_ETH_1[-3]
        m5_ETH_1_2 = m5_ETH_1[-2]
        m5_ETH_1_1 = m5_ETH_1[-1]
        op_mode_ETH = True
        time.sleep(1)

  
    price_ETH = pyupbit.get_current_price("KRW-ETH")
    time.sleep(1)
   
   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_ETH is True and hold_ETH is False and price_ETH is not None and\
        m5_ETH_2_4 - m5_ETH_1_4 > 0 and m5_ETH_2_3 - m5_ETH_1_3 > 0 and m5_ETH_2_2 - m5_ETH_1_2 > 0 and m5_ETH_2_1 - m5_ETH_1_1 < 0 and\
        m5_ETH_2_1 < price_ETH and m5_ETH_1_1 < price_ETH and m240_ETH_2_1 < price_ETH:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ETH", 10000)
        hold_ETH = True
        print("Btime:", now, "Bprice(ETH):", price_ETH)
        P_ETH = price_ETH
        # time.sleep(1)
  
    
    if hold_ETH is True:
        Buy_ETH = P_ETH
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_ETH is True and hold_ETH is True and\
        Buy_ETH * 1.01 < price_ETH:
        ETH_balance = upbit.get_balance("KRW-ETH")
        upbit.sell_market_order("KRW-ETH", ETH_balance)
        hold_ETH = False
        print("Stime:", now, "Sprice(ETH):", price_ETH, "IN:", round(((price_ETH - Buy_ETH) - (Buy_ETH * 0.0005) + (price_ETH * 0.0005))/(price_ETH) * 10000, 1))
        op_mode_ETH = False
        time.sleep(250)
     
    # print(f"time: {now} hold: {hold_ETH} op: {op_mode_ETH}")
    time.sleep(1)

   

