from st_aggrid import AgGrid
import streamlit as st
import altair as alt
import pandas as pd
import sheets as sh
from bokeh.models import Div


# Get password from user
password = st.sidebar.text_input("Password:", value="")

# select our text input field and make it into a password input
js = "el = document.querySelectorAll('.sidebar-content input')[0]; el.type = 'password';"

# passing js code to the onerror handler of an img tag with no src
# triggers an error and allows automatically running our code
html = f'<img src onerror="{js}">'

# in contrast to st.write, this seems to allow passing javascript
div = Div(text=html)
st.bokeh_chart(div)

if password != st.secrets["PASSWORD"]:
    st.error("the password you entered is incorrect")

else:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SPREADSHEET_ID = '1MYdAevCV4bvw73-h925A1Hlt5Gadgcm6pEFcxYGtvXg'
    DATA_TO_PULL = 'Export!A1:F25'

    data = sh.pull_sheet_data(SCOPES, SPREADSHEET_ID, DATA_TO_PULL)
    df = pd.DataFrame(data[1:], columns=data[0])

    st.markdown("# caseWhen Consulting :man-surfing:")
    st.markdown("")
    st.markdown("### Up and to the Right :chart_with_upwards_trend:")

    # df3 = pd.DataFrame({
    #   'Month': df['Month'].values,
    #   'Cumulative Profit': [int(x.replace(',', '')) for x in df['Cumulative Profit'].values]
    # })
    #
    # bar_chart = alt.Chart(df3).mark_bar().encode(
    #     alt.X('Month', title=''),
    #     alt.Y('Cumulative Profit', title='Cumulative Profit')
    # )
    #
    # st.altair_chart(bar_chart)

    # Example with Streamlit wrapper
    df2 = pd.DataFrame({
      'Month': df['Month'].values,
      'Cumulative Profit': [int(x.replace(',', '')) for x in df['Cumulative Profit'].values]
    })
    df2 = df2.set_index('Month')

    st.bar_chart(data=df2)
    # AgGrid(df2)

    st.markdown("### Financials :moneybag:")
    AgGrid(df)
