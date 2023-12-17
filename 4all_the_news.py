import streamlit as st
import time

# 영상 파일 경로 리스트
video_files = ["news1.mp4", "news2.mp4", "news4.mp4"]
current_video_index = 0

# Streamlit 앱 시작
st.title("국제 분쟁 뉴스 모음")

# 현재 영상 파일
current_video_file = video_files[current_video_index]

# 영상 보여주기
video_placeholder = st.empty()
video_placeholder.video(current_video_file)

# 다음 영상으로 넘어가는 버튼
if st.button("다음 영상"):
    current_video_index = (current_video_index + 1) % len(video_files)
    current_video_file = video_files[current_video_index]

    # 버튼 클릭 후 동적으로 업데이트
    video_placeholder.video(current_video_file)
    st.success("다음 영상으로 이동합니다. 🚀")