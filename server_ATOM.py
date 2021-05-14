## moving average 

import pyupbit
import time # 1초에 한 번 출력 위해
import datetime # 현재time

upbit = pyupbit.Upbit("", "") # Upbit class의 객체 생성

op_mode_ATOM = False
hold_ATOM = False

while True: 
    now = datetime.datetime.now()

    # 24time 목표가 계산
    if 0 <= now.hour <= 23 and 0 <= now.minute <= 59 and 0 <= now.second <= 59: # 9시 0분 20~30초 사이
        df_ATOM_240 = pyupbit.get_ohlcv("KRW-ATOM", "minut240", 5)
        close_ATOM_240 = df_ATOM_240['close']
        m240_ATOM = close_ATOM_240.rolling(2).mean()
        m240_ATOM_2_1 = m240_ATOM[-1]
        time.sleep(1)
        df_ATOM_5 = pyupbit.get_ohlcv("KRW-ATOM", "minute5", 5)
        close_ATOM_5 = df_ATOM_5['close']
        m5_ATOM_2 = close_ATOM_5.rolling(2).mean()
        m5_ATOM_1 = close_ATOM_5.rolling(1).mean()
        m5_ATOM_2_2 = m5_ATOM_2[-2]
        m5_ATOM_2_1 = m5_ATOM_2[-1]
        m5_ATOM_1_2 = m5_ATOM_1[-2]
        m5_ATOM_1_1 = m5_ATOM_1[-1]
        op_mode_ATOM = True

  
    price_ATOM = pyupbit.get_current_price("KRW-ATOM")
   

   
    ## 매초마다 조건을 확인한 후 매수 시도 (현재가격 확인 후)
  
    if op_mode_ATOM is True and hold_ATOM is False and price_ATOM is not None and\
        m5_ATOM_2_2 - m5_ATOM_1_2 > 0 and m5_ATOM_2_1 - m5_ATOM_1_1 < 0 and\
        m5_ATOM_2_1 < price_ATOM and m5_ATOM_1_1 < price_ATOM and m240_ATOM_2_1 < price_ATOM:
        krw_balance = upbit.get_balance("KRW") # 잔고 조회하고
        upbit.buy_market_order("KRW-ATOM", 10000)
        hold_ATOM = True
        print("Btime:", now, "Bprice(ATOM):", price_ATOM)
        P_ATOM = price_ATOM
        # time.sleep(1)
  
    
    if hold_ATOM is True:
        Buy_ATOM = P_ATOM
  
    ## 매수가보다 X% 오르면 매도
 
    if op_mode_ATOM is True and hold_ATOM is True and\
        Buy_ATOM * 1.0012 < price_ATOM:
        ATOM_balance = upbit.get_balance("KRW-ATOM")
        upbit.sell_market_order("KRW-ATOM", ATOM_balance)
        hold_ATOM = False
        print("Stime:", now, "Sprice(ATOM):", price_ATOM, "IN:", round(((price_ATOM - Buy_ATOM) - (Buy_ATOM * 0.0005) + (price_ATOM * 0.0005))/(price_ATOM) * 10000, 1))
        op_mode_ATOM = False
        # time.sleep(1)
     
    print(f"time: {now} hold: {hold_ATOM} op: {op_mode_ATOM}")

   

