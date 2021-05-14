## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_EOS = False
hold_EOS = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_EOS_240 = pyupbit.get_ohlcv("KRW-EOS", "minut240", 5)
        close_EOS_240 = df_EOS_240['close']
        m240_EOS = close_EOS_240.rolling(2).mean()
        m240_EOS_2_1 = m240_EOS[-1]
        df_EOS_5 = pyupbit.get_ohlcv("KRW-EOS", "minute5", 5)
        close_EOS_5 = df_EOS_5['close']
        m5_EOS_2 = close_EOS_5.rolling(2).mean()
        m5_EOS_1 = close_EOS_5.rolling(1).mean()
        m5_EOS_2_2 = m5_EOS_2[-2]
        m5_EOS_2_1 = m5_EOS_2[-1]
        m5_EOS_1_2 = m5_EOS_1[-2]
        m5_EOS_1_1 = m5_EOS_1[-1]
        op_mode_EOS = True
        time.sleep(1)
  
    price_EOS = pyupbit.get_current_price("KRW-EOS")
    time.sleep(1)
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_EOS is True and hold_EOS is False and price_EOS is not None and\
        m5_EOS_2_2 - m5_EOS_1_2 > 0 and m5_EOS_2_1 - m5_EOS_1_1 < 0 and\
        m5_EOS_2_1 < price_EOS and m5_EOS_1_1 < price_EOS and m240_EOS_2_1 < price_EOS:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-EOS", 10000)
        hold_EOS = True
        print("Btime:", now, "Bprice(EOS):", price_EOS)
        P_EOS = price_EOS
        # time.sleep(1)
  
    
    if hold_EOS is True:
        Buy_EOS = P_EOS
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_EOS is True and hold_EOS is True and\
        Buy_EOS * 1.0012 < price_EOS:
        EOS_balance = upbit.get_balance("KRW-EOS")
        upbit.sell_market_order("KRW-EOS", EOS_balance)
        hold_EOS = False
        print("Stime:", now, "Sprice(EOS):", price_EOS, "IN:", round(((price_EOS - Buy_EOS) - (Buy_EOS * 0.0005) + (price_EOS * 0.0005))/(price_EOS) * 10000, 1))
        op_mode_EOS = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_EOS} op: {op_mode_EOS}")
   

