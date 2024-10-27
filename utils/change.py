import pandas as pd
from datetime import datetime, timedelta


# * 날짜 시간 포맷 변경
def DATETIME_FORMAT(dateTime, format='%Y%m%d%H%M'):
    dateTime = str(dateTime)
    dateTime_format = format
    
    result = datetime.strptime(dateTime, dateTime_format)
    
    return result
    
# * 시간 포맷 변경
def TIME_FORMAT(time, format='%H%M'):
    time = str(time)
    time_format = format
    
    result = datetime.strptime(time, time_format)
    result = result.strftime('%H:%M')
    
    return result

# * 날짜 연월일 변경
def DATETIME_REPLACE(dateTime, mode='days', calculation_time=None):
    if mode == 'years':
        dateTime = dateTime.replace(year=calculation_time)
    elif mode == 'months':
        dateTime = dateTime.replace(month=calculation_time)
    elif mode == 'days':
        dateTime = dateTime.replace(day=calculation_time)
    elif mode == 'month_day':
        dateTime = dateTime.replace(month=calculation_time, day=calculation_time)
        
    return dateTime
    

# * 시간 연산
def DATETIME_TIMEDELTA(dateTime=None, mode='days', calculation_time=None):
    # TODO: dateTime이 str일 때 datetime.date 형식으로 바꿔주기
    """_summary_

    Args:
        dateTime (datetime.date, optional): _description_. Defaults to None.
        mode (str, optional): _description_. Defaults to 'days'.
        calculation_time (int, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    # if isinstance(dateTime, datetime.date):
    #     dateTime = dateTime
    # elif isinstance(dateTime, str):
    #     dateTime = dateTime
    
    if isinstance(calculation_time, int):
        calculation_time = calculation_time
    elif isinstance(calculation_time, str):
        calculation_time = int(calculation_time)
        
    if mode == 'weeks':
        result = dateTime + timedelta(weeks=calculation_time)
    elif mode == 'days':
        result = dateTime + timedelta(days=calculation_time)
    elif mode == 'minutes':
        result = dateTime + timedelta(minutes=calculation_time)
    elif mode == 'hours':
        result = dateTime + timedelta(hours=calculation_time)
    elif mode == 'seconds':
        result = dateTime + timedelta(seconds=calculation_time)
    elif mode == 'microseconds':
        result = dateTime + timedelta(microseconds=calculation_time)
    elif mode == 'milliseconds':
        result = dateTime + timedelta(milliseconds=calculation_time)
    
    return result

# * 기압 변환
def ALTIMETER_UNIT(data, mode = 'hPa', run_round=False):
    altimeter = pd.to_numeric(data, downcast='float', errors='coerce')
    if mode == 'qnh_to_hPa':
        # result = altimeter * 33.8638 * 0.01
        result = altimeter * 33.8638
        
    if run_round:
        result = round(result, 0)
    else:
        pass
    
    return result

# * 온도: 화씨 -> 섭씨, 켈빈 변환
def TEMPERATURE_UNIT(data, mode='celsius', run_round=False):
    temperature = pd.to_numeric(data, downcast='float', errors='coerce')
    if mode == 'celsius':
        result = (temperature - 32) * (5 / 9)
    elif mode == 'kelvin':
        result = (temperature - 32) * (5 / 9) + 273.15
        
    if run_round:
        result = round(result, 0)
    else:
        pass
        
    return result

# * 속도 변환
def SPEED_UNIT(data, mode='kt_to_m/s', run_round=False):
    speed = pd.to_numeric(data, downcast='float', errors='coerce')
    if mode == 'kt_to_m/s':
        conversion = 0.514444
    elif mode == 'kt_to_km/h':
        conversion = 1.852
    elif mode == 'kt_to_mph':
        conversion = 1.151
    elif mode == 'kt_to_ft/s':
        conversion = 1.688
        
    result = speed * conversion
    
    if run_round:
        result = round(result, 0)
    else:
        pass
        
    return result

# * 길이 변환
def LENGHT_UNIT(data, mode='inch_to_mm', run_round=False):
    lenght = pd.to_numeric(data, downcast="float", errors='coerce')
    if mode == 'inch':
        pass
    elif mode == 'inch_to_mm':
        conversion = 25.4
    elif mode == 'mile_to_m':
        conversion = 1609.344
    elif mode == 'ft_to_m':
        conversion = 0.3048
        
    result = lenght * conversion
    
    if run_round:
        result = round(result, 0)
    else:
        pass
    
    return result