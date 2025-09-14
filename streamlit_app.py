import streamlit as st

pages = [
    st.Page(page="app_pages/main.py", title="Home"),
    st.Page(page="app_pages/random_word.py", title="Random Word"),
    st.Page(page="app_pages/about.py", title="About")
    ]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()

