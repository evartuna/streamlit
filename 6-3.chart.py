import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

st.title('심화문제')

st.subheader('1. Altair Scatter chart- 재무 분석')

# https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv 읽어오기 
# 한글 encoding='CP949'
fi = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_financial.csv', encoding='CP949')

# 체크박스 버튼을 선택하여 데이터 확인
agree = st.checkbox('재무분석 데이터 조회')
if (agree):
    st.write(fi)


    
#  radio button을 사용하여 판매량/매출원가/수익을 선택
#  circle chart 그리기: 총매출, 선택된 항목, color = '상품', size =

sel = st.radio( '총매출 대비 분석을 원하는 항목을 선택하세요.',  ('판매량', '매출원가', '수익'))

if sel == '판매량':
    chart = alt.Chart(fi).mark_circle().encode(x = '총매출', y=sel, color = '상품', size=alt.Size(sel, scale=alt.Scale(range=[100, 300])))  
    st.altair_chart(chart, use_container_width=True)
elif sel == '매출원가':
    chart = alt.Chart(fi).mark_circle().encode(x = '총매출', y=sel, color = '상품', size=alt.Size(sel, scale=alt.Scale(range=[100, 300])))  
    st.altair_chart(chart, use_container_width=True) 
else:
    chart = alt.Chart(fi).mark_circle().encode(x = '총매출', y=sel, color = '상품', size=alt.Size(sel, scale=alt.Scale(range=[100, 300])))  
    st.altair_chart(chart, use_container_width=True)




st.subheader('2. Plotly Pie chart- 타이타닉 생존 분석')

# # https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv 데이터 읽어오기 
titanic = pd.read_csv('https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv')

# # 체크박스 버튼을 선택하여 데이터 확인

agree = st.checkbox('타이타닉 데이터 조회')
if (agree):
    st.write(titanic)
    


option = st.selectbox('생존자 분석을 위한 항목을 선택하세요.', ('탑승지역별 분석', '객실등급별 분석')) 
if option=='탑승지역별 분석':
    col1, col2=st.columns(2)
    with col1:
        fig = px.pie(titanic, values = "Survived", names = "Embarked", hole=.3 )
        fig.update_traces(textposition='inside', textinfo = 'percent+label')
        fig.update_layout(height=400, width=400)
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
    with col2:
        fig = px.bar(titanic, x="Embarked", y="Survived", color="Sex")
        fig.update_layout(height=400, width=400)
        st.plotly_chart(fig)
else:
    
    col1, col2=st.columns(2)
    with col1:
        fig = px.pie(titanic, values = "Survived", names = "Pclass", title="객실등급별 생존자 분석",  hole=.3 )
        fig.update_traces(textposition='inside', textinfo = 'percent+label')
        fig.update_layout(height=400, width=400)
        fig.update(layout_showlegend=False)
        st.plotly_chart(fig)
    with col2:
        fig = px.bar(titanic, x="Pclass", y='Survived',color="Sex")
        fig.update_layout(height=400, width=400)
        st.plotly_chart(fig)

# # columns 함수를 이용하여 좌-pie chart, 우-bar chart 그리기
# # 차트 크기 조정- fig.update_layout(height=400, width=400)

# with col1:
#     # pie chart 그리기: values='Survived'
#     fig = 
#     fig.update_traces(
#     fig.update_layout(
#     fig.update(layout_showlegend=False)
    
# with col2:
#     # bar chart 그리기: y="Survived", color="Sex"
#     fig = 
#     fig.update_layout(height=400, width=400)
    
    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\6-3.chart.py