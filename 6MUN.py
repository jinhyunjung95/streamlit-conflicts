import streamlit as st

def get_mun_procedure(topic):
    # 여기에 모의 UN 진행 절차를 가져오는 로직을 추가합니다.
    # 예를 들어, 각 단계에 해당하는 설명을 리스트에 담아 반환하도록 합니다.
    procedure_steps = [
        "1. 회의 시작 및 개회식",
        "2. 의사진행규칙 제정",
        "3. 의제 발표",
        "4. 의제 토론",
        "5. 토의 진행 중 특별 발언 및 질문",
        "6. 토의 종료 및 토의 결과 투표",
        "7. 성과 보고 및 평가",
        "8. 회의 종료"
    ]

    return procedure_steps

def main():
    st.title("모의 UN 진행 절차 확인")

    # 의제 입력 받기
    mun_topic = st.text_input("의제를 입력하세요:", "")

    # '모의 UN 진행 절차 보기' 버튼 클릭 여부 확인
    if st.button("모의 UN 진행 절차 보기"):
        # 모의 UN 진행 절차 가져오기
        procedure_steps = get_mun_procedure(mun_topic)

        # 모의 UN 진행 절차 표시
        st.header("모의 UN 진행 절차")
        for step in procedure_steps:
            st.write(f"- {step}")

if __name__ == "__main__":
    main()