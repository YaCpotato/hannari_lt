import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from sklearn.datasets import load_boston

boston = load_boston()

df = pd.DataFrame(boston.data, columns=boston.feature_names)

pr = ProfileReport(df, explorative=True)

st.title("Pandas Profiling in Streamlit")
st.write(df)
st_profile_report(pr)