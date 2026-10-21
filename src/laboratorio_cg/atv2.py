import numpy as np
import streamlit as st
def ampliar(bandeira, k=30):
    return bandeira.repeat(k, axis=0).repeat(k, axis=1)

st.title("Oia a bandeira aí!")
bandeira = np.zeros((16, 22, 3), dtype=np.uint8)
bandeira[:] = (186, 12, 47)
bandeira[6:10, :] = (255, 255, 255)
bandeira[:, 6:10] = (255, 255, 255)
bandeira[7:9, :] = (0, 32, 91)
bandeira[:, 7:9] = (0, 32, 91)
st.image(ampliar(bandeira))