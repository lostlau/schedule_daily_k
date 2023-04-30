from sqlalchemy import create_engine
from datetime import datetime

from utils import get_index_components,get_history_k


def job():
    # 初始化数据库连接，使用pymysql模块
    user = "lostlau"
    pwd = "Liuwn_0717"
    ip_port = "110.40.223.131:3306"
    db_name = "db_quant"
    engine = create_engine(f"mysql+pymysql://{user}:{pwd}@{ip_port}/{db_name}")

    today = datetime.today().strftime("%Y-%m-%d")
    print(f"{today}")
    stock_list = get_index_components(index_code='399102')
    df_output = get_history_k(stock_list,stt_date=today,end_date=today)
    df_output.to_sql('stock_daily_k', engine, if_exists='append',index=False,chunksize=1000)
    print("写入成功！")

