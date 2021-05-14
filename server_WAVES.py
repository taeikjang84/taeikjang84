## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_WAVES = False
hold_WAVES = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_WAVES_240 = pyupbit.get_ohlcv("KRW-WAVES", "minut240", 5)
        close_WAVES_240 = df_WAVES_240['close']
        m240_WAVES = close_WAVES_240.rolling(2).mean()
        m240_WAVES_2_1 = m240_WAVES[-1]
        time.sleep(1)
        df_WAVES_5 = pyupbit.get_ohlcv("KRW-WAVES", "minute5", 5)
        close_WAVES_5 = df_WAVES_5['close']
        m5_WAVES_2 = close_WAVES_5.rolling(2).mean()
        m5_WAVES_1 = close_WAVES_5.rolling(1).mean()
        m5_WAVES_2_2 = m5_WAVES_2[-2]
        m5_WAVES_2_1 = m5_WAVES_2[-1]
        m5_WAVES_1_2 = m5_WAVES_1[-2]
        m5_WAVES_1_1 = m5_WAVES_1[-1]
        op_mode_WAVES = True

  
    price_WAVES = pyupbit.get_current_price("KRW-WAVES")


   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_WAVES is True and hold_WAVES is False and price_WAVES is not None and\
        m5_WAVES_2_2 - m5_WAVES_1_2 > 0 and m5_WAVES_2_1 - m5_WAVES_1_1 < 0 and\
        m5_WAVES_2_1 < price_WAVES and m5_WAVES_1_1 < price_WAVES and m240_WAVES_2_1 < price_WAVES:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-WAVES", 10000)
        hold_WAVES = True
        print("Btime:", now, "Bprice(WAVES):", price_WAVES)
        P_WAVES = price_WAVES
        # time.sleep(1)
  
    
    if hold_WAVES is True:
        Buy_WAVES = P_WAVES
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_WAVES is True and hold_WAVES is True and\
        Buy_WAVES * 1.0012 < price_WAVES:
        WAVES_balance = upbit.get_balance("KRW-WAVES")
        upbit.sell_market_order("KRW-WAVES", WAVES_balance)
        hold_WAVES = False
        print("Stime:", now, "Sprice(WAVES):", price_WAVES, "IN:", round(((price_WAVES - Buy_WAVES) - (Buy_WAVES * 0.0005) + (price_WAVES * 0.0005))/(price_WAVES) * 10000, 1))
        op_mode_WAVES = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_WAVES} op: {op_mode_WAVES}")

   

