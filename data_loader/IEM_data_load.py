import io
import os
import requests
import pandas as pd

from utils import *
from settings import config_params as cfg


class IEM_DATA_LOADER():
    def __init__(self, args):
        self.url = ''
        self.args = args
        
        self.METAR_SAVE_FILE = f'METAR/{args.station}_METAR_{cfg.TODAY}.csv'
        self.METAR_EXCEL_SAVE_DIR = os.path.join(cfg.DATA_DIR, self.METAR_SAVE_FILE)
        
    # ? PARAMS 설정
    def GET_PARAMS(self):
        PARAMS = {}
        startDate = self.args.startDate.split('-')
        endDate = self.args.endDate.split('-')
        
        PARAMS.setdefault('station', self.args.station)
        PARAMS.setdefault('data', self.args.data)
        PARAMS.setdefault('year1', startDate[0])
        PARAMS.setdefault('month1', startDate[1])
        PARAMS.setdefault('day1', startDate[2])
        PARAMS.setdefault('year2', endDate[0])
        PARAMS.setdefault('month2', endDate[1])
        PARAMS.setdefault('day2', endDate[2])
        PARAMS.setdefault('format', self.args.format)
        PARAMS.setdefault('latlon', self.args.latlon)
        PARAMS.setdefault('elev', self.args.elev)
        PARAMS.setdefault('missing', self.args.missing)
        PARAMS.setdefault('trace', self.args.trace)
        PARAMS.setdefault('direct', self.args.direct)
        
        return PARAMS
    
    
    def GET_METAR(self):
        self.url = cfg.BASE_URL_IEM + '/cgi-bin/request/asos.py'
        self.PARAMS = self.GET_PARAMS()

        response = requests.get(url=self.url, params=self.PARAMS).text
        df_data = pd.read_csv(io.StringIO(response), parse_dates=['valid'],).rename({'valid':'time'}, axis=1)
        
        # * 온도: 화씨 -> 섭씨 변경
        df_data['temp_o'] = TEMPERATURE_UNIT(data=df_data['tmpf'], mode='celsius', run_round=True)
        df_data['dewpoint_o'] = TEMPERATURE_UNIT(data=df_data['dwpf'], mode='celsius', run_round=True)
        
        # * 습도
        df_data['rh_o'] = pd.to_numeric(df_data['relh'], downcast='float', errors='coerce')
        df_data['rh_o'] = round(df_data['rh_o'], 0)
        
        # * 바람 방향: NaN -> -1로 변경
        substitution = -1.0
        df_data['wind_dir_o'] = pd.to_numeric(df_data['drct'], downcast='float', errors='ignore')
        # NaN_data = df_data['wind_dir_o'].isnull().sum()
        df_data.dir_o = df_data['wind_dir_o'].fillna(substitution)
        df_data.loc[:, 'wind_dir_o'] = pd.to_numeric(df_data['wind_dir_o'], downcast='float', errors='coerce')
        
        # * 바람 속도: kt -> m/s 변경
        df_data['wind_spd_o'] = pd.to_numeric(df_data['sknt'], downcast='float', errors='coerce')
        # df_data['wind_spd_o'] = SPEED_UNIT(speed=df_data['sknt'], mode='kt_to_m/s')
        
        # * 돌풍: kt -> m/s 변경
        df_data['wind_gust_o'] = pd.to_numeric(df_data['gust'], downcast='float', errors='coerce')
        # df_data['wind_gust_o'] = SPEED_UNIT(df_data['gust'], mode='kt_to_m/s')
        df_data['wind_gust_o'] = df_data['wind_gust_o'].fillna('M')
        
        # * 강수량: inch -> mm 변경
        df_data['prec_o'] = LENGHT_UNIT(data=df_data['p01i'], mode='inch_to_mm', run_round=False)
        
        # * 기압: QNH -> hPa 변경
        df_data['alti_o'] = ALTIMETER_UNIT(data=df_data['alti'], mode='qnh_to_hPa', run_round=True)
        
        # * 해수면기압: hPa
        df_data['slp_o'] = df_data['mslp']
        
        # * 가시성: mile -> m 변환
        df_data['visibility_o'] = LENGHT_UNIT(data=df_data['vsby'], mode='mile_to_m', run_round=True)
        
        # * 하늘 레벨 고도 feet -> m
        df_data['skyc1_o'] = df_data['skyc1']
        df_data['skyc2_o'] = df_data['skyc2']
        df_data['skyc3_o'] = df_data['skyc3']
        
        df_data['skyl1_o'] = LENGHT_UNIT(data=df_data['skyl1'], mode='ft_to_m', run_round=True)
        df_data['skyl1_o'] = df_data.skyl1_o.fillna('M')
        df_data['skyl2_o'] = LENGHT_UNIT(data=df_data['skyl2'], mode='ft_to_m', run_round=True)
        df_data['skyl2_o'] = df_data.skyl2_o.fillna('M')
        df_data['skyl3_o'] = LENGHT_UNIT(data=df_data['skyl3'], mode='ft_to_m', run_round=True)
        df_data['skyl3_o'] = df_data.skyl3_o.fillna('M')
        df_data['skyl4_o'] = LENGHT_UNIT(data=df_data['skyl4'], mode='ft_to_m', run_round=True)
        df_data['skyl4_o'] = df_data.skyl4_o.fillna('M')
        
        # * 현재 날씨 코드
        pd.set_option('display.max_rows', 100)
        df_data["wxcodes_o"] = df_data["wxcodes"]
        df_data['wxcodes_o'] = df_data.wxcodes_o.fillna('M')
        
        # * METAR 데이터
        df_data["metar_o"] = df_data["metar"]
        
        df_final_data = df_data[['time','temp_o','dewpoint_o', 'rh_o', 'wind_dir_o', 'wind_spd_o', 'wind_gust_o', 'alti_o', 'visibility_o', 'skyc1_o', 'skyc2_o', 'skyc3_o', 'skyl1_o', 'skyl2_o', 'skyl3_o', 'wxcodes_o', 'prec_o', 'metar_o']]
        
        if self.args.save:
            DATAFRAME_to_CSV(df_data=df_final_data, file_path=self.METAR_EXCEL_SAVE_DIR, file_name=self.METAR_SAVE_FILE)
            return None
        else:
            return df_final_data
        
        
    def GET_TAF(self):
        pass

