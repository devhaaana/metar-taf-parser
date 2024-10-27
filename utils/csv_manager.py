import os
import traceback
import pandas as pd
from settings import config_params as cfg


def CSV_to_DATAFRAME(file_path, file_name='data.csv'):
    try:
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.csv':
            df_data = pd.read_csv(file_path)
        elif file_extension == '.xlsx':
            df_data = pd.read_excel(file_path)
        return df_data
    except FileNotFoundError:
        err_msg = f'{cfg.ERR_MSG_START}The file {file_name} was not found.{cfg.MSG_END}'
        # print(f'The file {file_name} was not found.')
        print(err_msg)
        return None
    except:
        traceback_message = traceback.format_exc()
        print(traceback_message)


def DATAFRAME_to_CSV(df_data, file_path, file_name='data.csv'):
    try:
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == '.csv':
            df_data.to_csv(file_path, header=True, index=False)
        elif file_extension == '.xlsx':
            df_data.to_excel(file_path, header=True, index=False)
            
        msg = f'{cfg.MSG_START}The file "{file_name}" was saved successfully.{cfg.MSG_END}'
        msg_filepath = f'{cfg.MSG_START}File Path: "{file_path}"{cfg.MSG_END}'
        print(f'{msg}\n{msg_filepath}')
        
    except FileNotFoundError:
        err_msg = f'{cfg.ERR_MSG_START}The file {file_name} was not found.{cfg.MSG_END}'
        # print(f'The file {file_name} was not found.')
        print(err_msg)
        
    except:
        traceback_message = traceback.format_exc()
        print(traceback_message)


def DATAFRAME_DELETE_DATA(df_data, del_list, axis=1):
    if isinstance(del_list, list):
        for data in del_list:
            df_data = df_data.drop(data, axis=axis)
                
    df_data = df_data.reset_index(drop=True)
        
    return df_data