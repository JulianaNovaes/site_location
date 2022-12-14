import streamlit as st
from map import (
    load_file,
    scale_map,
    multiply_array,
    combine_maps,
    save_file,
    update_plot,
    on_confirm_button_clicked,
    on_download_button_clicked,
)

st.set_page_config(page_title="Site Location Project")


st.title("Site Location Project")


st.markdown(
    "This project aims to create a combined view of the UK map that is able to highlight the best areas to build a factory that makes rock aggregates based on three factors: population, railway networks and geology. "
)

col1, col2 = st.columns(2)

with col1:

    pop = st.slider("Population", min_value=1, max_value=3, step=1)

    rail = st.slider("Railway", min_value=0, max_value=3, step=1)

    geo = st.slider("Geology", min_value=0, max_value=3, step=1)

    confirm_button = st.button("Confirmy my choices")
    download_button = st.download_button("Download File", "file:///tmp/map.txt")

with col2:
    if confirm_button:
        on_confirm_button_clicked(pop, rail, geo)

    if download_button:
        on_download_button_clicked()
