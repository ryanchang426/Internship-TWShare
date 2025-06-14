import pandas as pd

def stock_twse_daily() -> pd.DataFrame:
    """
    台灣上市公司基本資料查詢
    資料來源：https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL
    """
    url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL"
    df = pd.read_json(url)

    column_map = {
    "Date": "交易日期",
    "Code": "證券代號",
    "Name": "公司名稱",
    "TradeVolume": "成交股數",
    "TradeValue": "成交金額",
    "OpeningPrice": "開盤價",
    "HighestPrice": "最高價",
    "LowestPrice": "最低價",
    "ClosingPrice": "收盤價",
    "Change": "漲跌價差",
    "Transaction": "成交筆數"
}

    df.rename(columns=column_map, inplace=True)
    return df
