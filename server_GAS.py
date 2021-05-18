## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_GAS = False
hold_GAS = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_GAS_240 = pyupbit.get_ohlcv("KRW-GAS", "minut240", 5)
        close_GAS_240 = df_GAS_240['close']
        m240_GAS = close_GAS_240.rolling(2).mean()
        m240_GAS_2_1 = m240_GAS[-1]
        time.sleep(1)
        df_GAS_5 = pyupbit.get_ohlcv("KRW-GAS", "minute5", 5)
        close_GAS_5 = df_GAS_5['close']
        m5_GAS_2 = close_GAS_5.rolling(2).mean()
        m5_GAS_1 = close_GAS_5.rolling(1).mean()
        m5_GAS_2_4 = m5_GAS_2[-4]
        m5_GAS_2_3 = m5_GAS_2[-3]
        m5_GAS_2_2 = m5_GAS_2[-2]
        m5_GAS_2_1 = m5_GAS_2[-1]
        m5_GAS_1_4 = m5_GAS_1[-4]
        m5_GAS_1_3 = m5_GAS_1[-3]
        m5_GAS_1_2 = m5_GAS_1[-2]
        m5_GAS_1_1 = m5_GAS_1[-1]
        op_mode_GAS = True
        time.sleep(1)

  
    price_GAS = pyupbit.get_current_price("KRW-GAS")
    time.sleep(1)
   
   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_GAS is True and hold_GAS is False and price_GAS is not None and\
        m5_GAS_2_4 - m5_GAS_1_4 > 0 and m5_GAS_2_3 - m5_GAS_1_3 > 0 and m5_GAS_2_2 - m5_GAS_1_2 > 0 and m5_GAS_2_1 - m5_GAS_1_1 < 0 and\
        m5_GAS_2_1 < price_GAS and m5_GAS_1_1 < price_GAS and m240_GAS_2_1 < price_GAS:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-GAS", 10000)
        hold_GAS = True
        print("Btime:", now, "Bprice(GAS):", price_GAS)
        P_GAS = price_GAS
        # time.sleep(1)
  
    
    if hold_GAS is True:
        Buy_GAS = P_GAS
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_GAS is True and hold_GAS is True and\
        Buy_GAS * 1.01 < price_GAS:
        GAS_balance = upbit.get_balance("KRW-GAS")
        upbit.sell_market_order("KRW-GAS", GAS_balance)
        hold_GAS = False
        print("Stime:", now, "Sprice(GAS):", price_GAS, "IN:", round(((price_GAS - Buy_GAS) - (Buy_GAS * 0.0005) + (price_GAS * 0.0005))/(price_GAS) * 10000, 1))
        op_mode_GAS = False
        time.sleep(250)
     
    # print(f"time: {now} hold: {hold_GAS} op: {op_mode_GAS}")
    time.sleep(1)

   

