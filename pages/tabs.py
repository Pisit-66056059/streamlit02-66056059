import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

st.markdown('สวัสดี! **Streamlit**')
st.title('Tabs of San Francisco tree')
st.write("""
เราจะลองทำ San Francisco DataSet กันดู""")

trees_df = pd.read_csv('trees.csv')
# df_dbh_grouped = pd.DataFrame(
#     trees_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']

owners = st.sidebar.multiselect('Tree Owner Filter',
                                trees_df['caretaker'].unique())

if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

tab1, tab2, tab3 = st.tabs(['Line Chart',
                            'Bar Chart',
                            'Area Chart'])

with tab1:
    st.write('Column 1')
    st.line_chart(df_dbh_grouped)
with tab2:
    st.write('Column 2')
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.write('Column 3')
    st.area_chart(df_dbh_grouped)

st.title('แปลผล')
# st.write("""ส่วนใหญ่ของต้นไม้ใน San Fran มีเส้นผ่านศูนย์กลาง 3' (2,710 ต้น)""")
st.write('ส่วนใหญ่ของต้นไม้ใน San Fran มีเส้นผ่านศูนย์กลาง ', trees_df.groupby(['dbh']).count()['tree_id'].idxmax(),
         'นิ้ว ',
         trees_df.groupby(['dbh']).count()['tree_id'].max(), 'ต้น')
st.caption('กราฟ แสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศูนย์กลาง')

st.divider()  # ขีดเส้นขั้น)