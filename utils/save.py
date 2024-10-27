import os, sys
import csv
import traceback
from settings import config_params as cfg


def SAVE_DATA(dataArr, save=True, file_path=None, file_name='data.csv'):
    if save == True:
        os.makedirs(file_path, exist_ok=True)
        log_data = os.path.join(file_path, file_name)
        with open(log_data,'w+') as fp:
            fp.close()
        try:
            data_keys = []
            data_values = []
            
            with open(log_data, 'w', newline='') as fp:
                for keys, values in dataArr[0].items():
                    data_keys.append(keys)
                    data_values.append(values)
                    
                writer = csv.DictWriter(fp, fieldnames=data_keys)
                writer.writeheader()
                writer.writerows(dataArr)
                
            msg = f'{cfg.MSG_START}The file "{file_name}" was saved successfully.{cfg.MSG_END}'
            msg_filepath = f'{cfg.MSG_START}File Path: "{file_path}"{cfg.MSG_END}'
            print(f'{msg}\n{msg_filepath}')

        except FileNotFoundError:
            err_msg = f'{cfg.ERR_MSG_START}The file "{file_name}" was not found.{cfg.MSG_END}'
            # print(f'The file {file_name} was not found.')
            print(err_msg)
            
        except:
            traceback_message = traceback.format_exc()
            print(traceback_message)