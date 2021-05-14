## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_SRM = False
hold_SRM = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_SRM_240 = pyupbit.get_ohlcv("KRW-SRM", "minut240", 5)
        close_SRM_240 = df_SRM_240['close']
        m240_SRM = close_SRM_240.rolling(2).mean()
        m240_SRM_2_1 = m240_SRM[-1]
        time.sleep(1)
        df_SRM_5 = pyupbit.get_ohlcv("KRW-SRM", "minute5", 5)
        close_SRM_5 = df_SRM_5['close']
        m5_SRM_2 = close_SRM_5.rolling(2).mean()
        m5_SRM_1 = close_SRM_5.rolling(1).mean()
        m5_SRM_2_2 = m5_SRM_2[-2]
        m5_SRM_2_1 = m5_SRM_2[-1]
        m5_SRM_1_2 = m5_SRM_1[-2]
        m5_SRM_1_1 = m5_SRM_1[-1]
        op_mode_SRM = True

  
    price_SRM = pyupbit.get_current_price("KRW-SRM")

   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_SRM is True and hold_SRM is False and price_SRM is not None and\
        m5_SRM_2_2 - m5_SRM_1_2 > 0 and m5_SRM_2_1 - m5_SRM_1_1 < 0 and\
        m5_SRM_2_1 < price_SRM and m5_SRM_1_1 < price_SRM and m240_SRM_2_1 < price_SRM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-SRM", 10000)
        hold_SRM = True
        print("Btime:", now, "Bprice(SRM):", price_SRM)
        P_SRM = price_SRM
        # time.sleep(1)
  
    
    if hold_SRM is True:
        Buy_SRM = P_SRM
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_SRM is True and hold_SRM is True and\
        Buy_SRM * 1.0012 < price_SRM:
        SRM_balance = upbit.get_balance("KRW-SRM")
        upbit.sell_market_order("KRW-SRM", SRM_balance)
        hold_SRM = False
        print("Stime:", now, "Sprice(SRM):", price_SRM, "IN:", round(((price_SRM - Buy_SRM) - (Buy_SRM * 0.0005) + (price_SRM * 0.0005))/(price_SRM) * 10000, 1))
        op_mode_SRM = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_SRM} op: {op_mode_SRM}")


