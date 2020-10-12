import pandas as pd
from random import randint
import streamlit as st

from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts


def main():
    PAGES = {
        "Pandas Profiling": render_basic_line,
        "Basic area chart": render_basic_area,
        "Stacked area chart": render_stacked_area,
        "Mixed line and bar": render_mixed_line_bar,
        "Custom pie chart": render_custom_pie,
        "Effect scatter chart": render_effect_scatter,
        "Calendar heatmap": render_calendar_heatmap,
        "Basic treemap": render_treemap,
        "Datazoom": render_datazoom,
        "Dataset": render_dataset,
        "Map": render_map,
        "Click event": render_event,
    }

    st.title("Hello ECharts !")
    st.sidebar.header("Configuration")
    page = st.sidebar.selectbox("Choose an example", options=list(PAGES.keys()))
    PAGES[page]()


if __name__ == "__main__":
    main()