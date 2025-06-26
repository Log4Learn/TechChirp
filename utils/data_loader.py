import pandas as pd

def load_tips(file_path):
    return pd.read_excel(file_path).dropna(subset=["テーマ", "内容"])
