import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.font_manager as fm

font_list = fm.findSystemFonts()
for font in font_list:
    print(font)

def generate_word_cloud(answers, title):
    text = ' '.join(answers)

    # Specify a Korean font (replace 'YOUR_KOREAN_FONT.ttf' with the path to a Korean font file on your system)
    korean_font_path = 'H2GTRE.TTF'  # Replace with your font file path
    korean_font_prop = font_manager.FontProperties(fname=korean_font_path)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=korean_font_path,  # Use the Korean font
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontproperties=korean_font_prop)

    # Use st.pyplot to display the plot in Streamlit app
    st.pyplot(plt)

def main():
    st.title("지구촌 갈등에 대한 나의 생각")

    # Lists to store submitted answers
    types_of_conflicts_answers = []
    causes_of_conflict_answers = []

    # Text area and button for the first question
    opinion1 = st.text_area("지구촌에는 어떠한 갈등이 발생하고 있을까요?")
    if st.button("답변 제출하기"):
        types_of_conflicts_answers.append(opinion1)
        st.success(f"갈등의 종류 답변: {opinion1}")

    # Text area and button for the second question
    opinion2 = st.text_area("이러한 갈등의 원인에는 어떤 것들이 있을까요?")
    if st.button("답변 제출하기"):
        causes_of_conflict_answers.append(opinion2)
        st.success(f"갈등의 원인 답변: {opinion2}")

    # Display submitted answers
    st.header("제출 답변")
    st.subheader("갈등의 종류:")
    st.write(types_of_conflicts_answers)

    st.subheader("갈등의 원인:")
    st.write(causes_of_conflict_answers)

    # Generate and display word cloud for 갈등의 종류
    if types_of_conflicts_answers:
        st.header("Word Cloud for 갈등의 종류")
        generate_word_cloud(types_of_conflicts_answers, "갈등의 종류")

    # Generate and display word cloud for causes of global conflict
    if causes_of_conflict_answers:
        st.header("Word Cloud for 갈등의 원인")
        generate_word_cloud(causes_of_conflict_answers, "갈등의 원인")

if __name__ == "__main__":
    main()