import pandas as pd
from random import randint
import streamlit as st

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from sklearn.datasets import load_boston

boston = load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)

def st_pandas_profiling():
    pr = ProfileReport(df, explorative=True)
    st.title("Pandas Profiling in Streamlit")
    st.write(df)
    st_profile_report(pr)

def main():
    PAGES = {
        "Pandas Profiling": st_pandas_profiling
    }

    st.title("タイトル")
    st.sidebar.header("ライブラリ")
    page = st.sidebar.selectbox("Select Tools", options=list(PAGES.keys()))
    PAGES[page]()


if __name__ == "__main__":
    main()