## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_LINK = False
hold_LINK = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_LINK_240 = pyupbit.get_ohlcv("KRW-LINK", "minut240", 5)
        close_LINK_240 = df_LINK_240['close']
        m240_LINK = close_LINK_240.rolling(2).mean()
        m240_LINK_2_1 = m240_LINK[-1]
        time.sleep(1)
        df_LINK_5 = pyupbit.get_ohlcv("KRW-LINK", "minute5", 5)
        close_LINK_5 = df_LINK_5['close']
        m5_LINK_2 = close_LINK_5.rolling(2).mean()
        m5_LINK_1 = close_LINK_5.rolling(1).mean()
        m5_LINK_2_2 = m5_LINK_2[-2]
        m5_LINK_2_1 = m5_LINK_2[-1]
        m5_LINK_1_2 = m5_LINK_1[-2]
        m5_LINK_1_1 = m5_LINK_1[-1]
        op_mode_LINK = True
        time.sleep(1)
  
    price_LINK = pyupbit.get_current_price("KRW-LINK")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_LINK is True and hold_LINK is False and price_LINK is not None and\
        m5_LINK_2_2 - m5_LINK_1_2 > 0 and m5_LINK_2_1 - m5_LINK_1_1 < 0 and\
        m5_LINK_2_1 < price_LINK and m5_LINK_1_1 < price_LINK and m240_LINK_2_1 < price_LINK:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-LINK", 10000)
        hold_LINK = True
        print("Btime:", now, "Bprice(LINK):", price_LINK)
        P_LINK = price_LINK
        # time.sleep(1)
  
    
    if hold_LINK is True:
        Buy_LINK = P_LINK
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_LINK is True and hold_LINK is True and\
        Buy_LINK * 1.0012 < price_LINK:
        LINK_balance = upbit.get_balance("KRW-LINK")
        upbit.sell_market_order("KRW-LINK", LINK_balance)
        hold_LINK = False
        print("Stime:", now, "Sprice(LINK):", price_LINK, "IN:", round(((price_LINK - Buy_LINK) - (Buy_LINK * 0.0005) + (price_LINK * 0.0005))/(price_LINK) * 10000, 1))
        op_mode_LINK = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_LINK} op: {op_mode_LINK}")
    time.sleep(1)
   

