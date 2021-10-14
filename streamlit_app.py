from st_aggrid import AgGrid
import streamlit as st
import altair as alt
import pandas as pd
import sheets as sh
import numpy as np


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1MYdAevCV4bvw73-h925A1Hlt5Gadgcm6pEFcxYGtvXg'
DATA_TO_PULL = 'Export!A1:F25'

data = sh.pull_sheet_data(SCOPES, SPREADSHEET_ID, DATA_TO_PULL)
df = pd.DataFrame(data[1:], columns=data[0])

st.markdown("# caseWhen Consulting :man-surfing:")
st.markdown("")
st.markdown("### Up and to the Right :chart_with_upwards_trend:")

df3 = pd.DataFrame({
  'Month': df['Month'].values,
  'Cumulative Profit': [int(x.replace(',', '')) for x in df['Cumulative Profit'].values]
})

bar_chart = alt.Chart(df3).mark_bar().encode(
    alt.X('Month', title=''),
    alt.Y('Cumulative Profit', title='Cumulative Profit')
)

st.altair_chart(bar_chart)

# # Example with Streamlit wrapper
# df2 = pd.DataFrame({
#   'Month': df['Month'].values,
#   'Cumulative Profit': [int(x.replace(',', '')) for x in df['Cumulative Profit'].values]
# })
# df2 = df2.set_index('Month')
#
# st.bar_chart(data=df2)
# AgGrid(df2)

st.markdown("### Financials :moneybag:")
AgGrid(df)




# source = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
#                     columns=['alcohol', 'beer', 'coke'], index=pd.RangeIndex(100, name='x'))
# source = source.reset_index().melt('x', var_name='category', value_name='y')
#
# line_chart = alt.Chart(df2).mark_line(interpolate='basis').encode(
#     alt.X('x', title='Month'),
#     alt.Y('y', title='Cumulative Profit'),
#     color='category:N'
# ).properties(
#     title='Cumulative Profit by Month'
# )
#
# st.altair_chart(line_chart)

# source = pd.DataFrame({
#     'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
#     'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
# })
#
# alt.Chart(source).mark_bar().encode(
#     x='a',
#     y='b'
# )
