"""
excel_deal - 
Author: Alwin
Date:   2024/5/22
"""
import streamlit as st
import pandas as pd


upload_file = st.file_uploader('excel 文件',type=['xlsx', 'xls'])

if upload_file is None:
    # 每次streamlit都上到下执行，当满足条件是，这里就会停止运行
    st.stop()       # stop the app

# # 这里每次选择文件都会被执行一次，由以下替换
# dfs = pd.read_excel(upload_file,None)

@st.cache_data
def load_data(file):
    print('执行加载数据：')
    return pd.read_excel(file,None)

dfs = load_data(upload_file)

# 使用明确函数构建表格
names = list(dfs.keys())
sheet_selects = st.multiselect('工作表',names,[])

# 如果没有选择任何工作表，跳出执行
if len(sheet_selects) == 0:
    st.stop()

# 创建页签
tabs = st.tabs(sheet_selects)

for tab,name in zip(tabs,sheet_selects):
    with tab:
        df = dfs[name]
        st.dataframe(df)