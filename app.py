import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('สวัสดี! **Streamlit**')
st.title('Layout and Decoration')
st.write("""
เราจะลองทำ San Francisco DataSet กันดู""")

col1, col2, col3 = st.columns(3)
with col1:
    st.write('Column 1')
with col2:
    st.write('Column 2')
with col3:
    st.write('Column 3')

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)
st.title('แปลผล')
st.write("""
ส่วนใหญ่ของต้นไม้ใน San Fran มีเส้นผ่านศูนย์กลาง 3' (2,721 ต้น)""")
st.caption('กราฟ แสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศูนย์กลาง')
