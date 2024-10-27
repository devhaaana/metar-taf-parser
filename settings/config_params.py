import os
from datetime import date, datetime


# ERROR MSG
ERR_MSG_START = '\033[31m'
MSG_START = '\033[94m'
MSG_END = '\033[0m'

# URL
BASE_URL_IEM = 'https://mesonet.agron.iastate.edu'

# DIR Path
BASE_DIR = '../METAR/'
# BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/')

TODAY = date.today().strftime('%Y%m%d')
TIME = datetime.now().strftime('%H') + '00'
NOTICE_TIME = TODAY + TIME
