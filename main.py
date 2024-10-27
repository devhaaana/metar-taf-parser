import warnings
warnings.filterwarnings(action='ignore')
import argparse

from data_loader import *


def setting_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--station', type=str, default='RKSI', help='Airport ICAO Code')
    parser.add_argument('--data', type=str, default='all', help='Select From Available Data')
    parser.add_argument('--startDate', type=str, default='2023-01-01', help='Start Date: YYYY-MM-DD')
    parser.add_argument('--endDate', type=str, default='2023-12-31', help='End Date: YYYY-MM-DD')
    parser.add_argument('--format', type=str, default='onlycomma', help='Data Format')
    parser.add_argument('--latlon', type=str, default='no', help='Include Latitude, Longitude')
    parser.add_argument('--elev', type=str, default='no', help='Include Elevation')
    parser.add_argument('--missing', type=str, default='empty', help='Represent Missing Data')
    parser.add_argument('--trace', type=str, default='empty', help='Represent Trace Reports')
    parser.add_argument('--direct', type=str, default='no', help='Direct')
    parser.add_argument('--save', type=bool, default=True, help='Save Excel File')
    
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    args = setting_argument()
    
    data_load = IEM_DATA_LOADER(args)
    data = data_load.GET_METAR()

    