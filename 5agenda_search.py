import streamlit as st
from pytrends.request import TrendReq

# Streamlit 앱 시작
st.title("세 검색어의 Google Trends 검색량 비교")

# 검색어 입력 받기
keyword1 = st.text_input("검색어 1을 입력하세요:", "")
keyword2 = st.text_input("검색어 2를 입력하세요:", "")
keyword3 = st.text_input("검색어 3을 입력하세요:", "")

# Google Trends에 연결
pytrends = TrendReq(hl='en-US', tz=360)

# 검색어에 대한 트렌드 정보 가져오기
pytrends.build_payload([keyword1, keyword2, keyword3], cat=0, timeframe='today 5-y', geo='', gprop='')

# 트렌드 데이터 가져오기
trend_data = pytrends.interest_over_time()

# 트렌드 데이터 시각화
if not trend_data.empty:
    st.subheader("세 검색어에 대한 검색량 시각화 (겹쳐서 표시)")
     # 두 검색어에 대한 검색량 시각화 (겹쳐서 표시)
    st.line_chart(trend_data[[keyword1, keyword2, keyword3]], use_container_width=True)

    st.success("Google Trends에서 가져온 데이터를 시각화했습니다.")
else:
    st.warning("검색어에 대한 데이터를 찾을 수 없습니다.")
