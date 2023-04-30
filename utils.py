import re
import pandas as pd
import numpy as np
import baostock as bs
import akshare as ak

"""
命名：驼峰转下划线
"""
def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


"""
获取当日指数成分股票列表
    -- by akshare
"""
def get_index_components(index_code='399102'):
    stock_list = ak.index_stock_cons(index_code)["品种代码"].apply(ak.stock_a_code_to_symbol).apply(lambda s:s[:2]+'.'+s[2:]).values
    return np.unique(stock_list)


"""
获取股票列表的历史K线
    -- by baostock
"""
def get_history_k(stock_list, stt_date, end_date, freq='d', adjust='2'):
    bs.login()
    output_list = []
    for stk in stock_list:
        rs = bs.query_history_k_data_plus(stk, "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,psTTM,pcfNcfTTM,pbMRQ,isST",
                start_date=stt_date, end_date=end_date,
                frequency=freq, adjustflag=adjust)
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        output_list.append(pd.DataFrame(data_list, columns=rs.fields))
    df_output = pd.concat(output_list)
    # 格式转换
    df_output['date'] = df_output['date'].astype('datetime64[ns]')
    for col in np.setdiff1d(df_output.columns, ['code', 'date']):
        df_output[col] = pd.to_numeric(df_output[col])
    # 字段名转换
    df_output.columns = df_output.columns.map(camel_to_snake)
    bs.logout()
    return df_output
