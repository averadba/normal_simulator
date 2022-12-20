import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)


st.title("Normal Distribution Simulator")
st.write("by: A. Vera")


mean = st.sidebar.number_input("Mean", value=0.0)
standard_deviation = st.sidebar.number_input("Standard Deviation", value=1.0)
sample_size = st.sidebar.number_input("Sample Size", value=1000, min_value=1)

data = np.random.normal(mean, standard_deviation, sample_size)

st.write("Sample mean:", np.mean(data))
st.write("Sample standard deviation:", np.std(data))

plt.hist(data, bins=20)
plt.axvline(np.mean(data), color='r', linestyle='solid', linewidth=2)
plt.axvline(np.mean(data) + np.std(data), color='r', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(data) - np.std(data), color='r', linestyle='dashed', linewidth=2)
st.pyplot()
