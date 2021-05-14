## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_BCH = False
hold_BCH = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_BCH_240 = pyupbit.get_ohlcv("KRW-BCH", "minut240", 5)
        close_BCH_240 = df_BCH_240['close']
        m240_BCH = close_BCH_240.rolling(2).mean()
        m240_BCH_2_1 = m240_BCH[-1]
        time.sleep(1)
        df_BCH_5 = pyupbit.get_ohlcv("KRW-BCH", "minute5", 5)
        close_BCH_5 = df_BCH_5['close']
        m5_BCH_2 = close_BCH_5.rolling(2).mean()
        m5_BCH_1 = close_BCH_5.rolling(1).mean()
        m5_BCH_2_2 = m5_BCH_2[-2]
        m5_BCH_2_1 = m5_BCH_2[-1]
        m5_BCH_1_2 = m5_BCH_1[-2]
        m5_BCH_1_1 = m5_BCH_1[-1]
        op_mode_BCH = True
        time.sleep(1)

  
    price_BCH = pyupbit.get_current_price("KRW-BCH")


   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_BCH is True and hold_BCH is False and price_BCH is not None and\
        m5_BCH_2_2 - m5_BCH_1_2 > 0 and m5_BCH_2_1 - m5_BCH_1_1 < 0 and\
        m5_BCH_2_1 < price_BCH and m5_BCH_1_1 < price_BCH and m240_BCH_2_1 < price_BCH:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-BCH", 10000)
        hold_BCH = True
        print("Btime:", now, "Bprice(BCH):", price_BCH)
        P_BCH = price_BCH
        # time.sleep(1)
  
    
    if hold_BCH is True:
        Buy_BCH = P_BCH
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_BCH is True and hold_BCH is True and\
        Buy_BCH * 1.0012 < price_BCH:
        BCH_balance = upbit.get_balance("KRW-BCH")
        upbit.sell_market_order("KRW-BCH", BCH_balance)
        hold_BCH = False
        print("Stime:", now, "Sprice(BCH):", price_BCH, "IN:", round(((price_BCH - Buy_BCH) - (Buy_BCH * 0.0005) + (price_BCH * 0.0005))/(price_BCH) * 10000, 1))
        op_mode_BCH = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_BCH} op: {op_mode_BCH}")
    time.sleep(1)

   

