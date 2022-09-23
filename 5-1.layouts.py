import streamlit as st

st.title('Unit 5. Layouts & Containers')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')

# sidebar- with 사용하기 📧  📱  ☎︎

with st.sidebar:
    st.header('1. Sidebar')
add_selectbox = st.sidebar.selectbox( '어떻게 연락 드릴까요?',
('Email', 'Mobile phone', 'Office phone')) 

if add_selectbox == 'Email':
    st.sidebar.title('📧')
elif add_selectbox == 'Mobile phone': 
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎︎')



# columns  
# https://static.streamlit.io/examples/cat.jpg
# https://static.streamlit.io/examples/dog.jpg
# https://static.streamlit.io/examples/owl.jpg 
st.header('2. Columns')

col1, col2, col3 =st.columns(3)

with col1:
    st.text('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg') 
with col2:
    st.text('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg') 
with col3:
    st.text('An owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')

 


    
# # tabs  
st.header('3. Tabs')

tab1, tab2, tab3= st.tabs(['고양이', '개', '부엉이'])
with tab1:
    st.caption('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg', width=200) 
with tab2:
    st.caption('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg', width=200) 
with tab3:
    st.caption('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)




    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-1.layouts.py