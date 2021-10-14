from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import sheets as sh


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1MYdAevCV4bvw73-h925A1Hlt5Gadgcm6pEFcxYGtvXg'
DATA_TO_PULL = 'Export!A1:F25'

data = sh.pull_sheet_data(SCOPES, SPREADSHEET_ID, DATA_TO_PULL)
df = pd.DataFrame(data[1:], columns=data[0])

df2 = pd.DataFrame({
  'Month': df['Month'].values,
  'Cumulative Profit': [int(x.replace(',', '')) for x in df['Cumulative Profit'].values]
})
df2 = df2.set_index('Month')

st.markdown("# caseWhen Consulting :man-surfing:")
st.markdown("")
st.markdown("### Up and to the Right :chart_with_upwards_trend:")
st.bar_chart(data=df2)
# AgGrid(df2)

st.markdown("### Financials :moneybag:")
AgGrid(df)
