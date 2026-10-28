import streamlit as st
paginas = [
st.Page("src/laboratorio_cg/atv1.py", title="Atv 1"),
st.Page("src/laboratorio_cg/atv2.py", title="Atv 2"),
st.Page("src/laboratorio_cg/atv3.py", title="Atv 3"),
]
st.navigation(paginas).run()