import streamlit as st

st.set_page_config(
    page_title="F&Q",
)
st.title("F&Q :question:")
# st.write("# Welcome to Stock Assist F&Q! 👋")
body =   """
            <details>
                <summary>What is stock assist?</summary>
                Stock Assist is an AI based prediction app built for providing prediction related to stocks based on ML/AI.
            </details>
            
            <details>
                <summary>How to get started with stock assist?</summary>
                You can refer our <a href="https://github.com/techonerd/stock-assist/blob/main/CONTRIBUTING.md"> contribution </a> guide. 
                Also refer to our <a href="https://github.com/techonerd/stock-assist/blob/main/CODE_OF_CONDUCT.md"> code of conduct </a> for comunity guidlines.
            </details>
            
            <details>
                <summary>Where can I finds relevant documents??</summary>
                Not sure what your looking for, head towards our <a href="https://github.com/techonerd/stock-assist/blob/main/getting_started.md"> getting started doc's </a>
            </details>
            
            <details>
                <summary>How to get help?</summary>
                Feel free to join us on discord or mail us at <a href="mailto:info.stockassist@gmail.com">info.stockassist@gmail.com</a>
            </details>
            """


st.markdown(body, unsafe_allow_html=True)
