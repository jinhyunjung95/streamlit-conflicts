import streamlit as st
from PIL import Image
import base64

def main():
    st.subheader("관심 있는 국제 분쟁을 한 가지 선택하여 뉴스를 제작해 봅시다.")

    # 파일 업로드 섹션
    st.text_area("완성한 뉴스를 컴퓨터에 저장한 후 아래 버튼을 눌러 업로드하세요.")

    # 영상 파일 업로드
    video_file = st.file_uploader("영상 파일 업로드", type=["mp4", "avi", "mov"])

    if video_file is not None:
        st.video(video_file)

        # 업로드된 비디오를 세션에 저장
        st.session_state.uploaded_video = video_file

        # 다음 페이지로 이동하는 버튼
        if st.button("다음 페이지로 이동"):
            st.experimental_rerun()

def show_video():
    st.title("우리 모둠의 뉴스")

    # 세션에서 업로드된 비디오를 가져옴
    uploaded_video = st.session_state.get("uploaded_video", None)

    if uploaded_video is not None:
        st.video(uploaded_video)

if __name__ == "__main__":
    # 메인 페이지를 표시
    if "uploaded_video" not in st.session_state:
        main()
    # 다음 페이지를 표시
    else:
        show_video()
