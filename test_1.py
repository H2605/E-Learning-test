import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

st.header("test html import")

HtmlFile = open("IT-Projektmanagement b2e38fa49c854cbcb09a6d508cca20f7.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code)