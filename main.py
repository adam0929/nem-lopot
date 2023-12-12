import streamlit as st

st.title("""ocso nem lopot cuccok""")
adat1 = st.number_input('Telefonszám a + nélkül')

if st.sidebar.button('Gomb'):
    st.write(adat1 * 4)
