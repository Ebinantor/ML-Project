import streamlit as st
import pickle
from PIL import Image



def mining():

    st.title("Quality Prediction in a Mining Process ")
    image = Image.open('Mining.jpg')
    st.image(image,width=580)
    model = pickle.load(open('Mining_Quality_model.sav', 'rb'))
    scaler = pickle.load(open('minmaxscaler.sav', 'rb'))

    tab1, tab2= st.tabs(["**INFO**", "**Features**"])

    with tab1:
        st.header("About")
        st.write("The main goal is to use this data to predict how much impurity is in the ore concentrate. As this impurity is measured every hour, if we can predict how much silica (impurity) is in the ore concentrate, we can help the engineers, giving them early information to take actions (empowering!). Hence, they will be able to take corrective actions in advance (reduce impurity, if it is the case) and also help the environment (reducing the amount of ore that goes to tailings as you reduce silica in the ore concentrate).")

        st.header("Links")
        st.page_link("https://colab.research.google.com/drive/1xZwZeM5Hlj0AOsm_1ai_sulW9ZFTIH4_#scrollTo=7LYAPMYN57VB", label="Colab Notebook")
        st.page_link("https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process", label="Dataset")



    with tab2:
        st.write("Fill the below fields to predict the silica %")
        sf = st.text_input('% Silica Feed')
        sfl = st.text_input('Starch Flow')
        af = st.text_input('Amina Flow')
        opf = st.text_input('Ore Pulp Flow')
        oph = st.text_input('Ore Pulp pH')
        fl1af = st.text_input('Flotation Column 01 Air Flow')
        fl2af = st.text_input('Flotation Column 02 Air Flow')
        fl3af = st.text_input('Flotation Column 03 Air Flow')
        fl4af = st.text_input('Flotation Column 04 Air Flow')
        fl5af = st.text_input('Flotation Column 05 Air Flow')
        fl6af = st.text_input('Flotation Column 06 Air Flow')
        fl7af = st.text_input('Flotation Column 07 Air Flow')
        fl1 = st.text_input('Flotation Column 01 Level')
        fl2 = st.text_input('Flotation Column 02 Level')
        fl3 = st.text_input('Flotation Column 03 Level')
        fl4 = st.text_input('Flotation Column 04 Level')
        fl5 = st.text_input('Flotation Column 05 Level')
        fl6 = st.text_input('Flotation Column 06 Level')
        fl7 = st.text_input('Flotation Column 07 Level')
        ic = st.text_input('% Iron Concentrate')
        pred = st.button('PREDICT')
        if pred:
            prediction = model.predict(scaler.transform([[int(sf), int(sfl), int(af), int(opf), int(oph), int(fl1af),
                                                          int(fl2af), int(fl3af), int(fl4af), int(fl5af), int(fl6af),
                                                          int(fl7af), int(fl1), int(fl2), int(fl3), int(fl4), int(fl5),
                                                          int(fl6), int(fl7), int(ic)]]))

            st.write(f"The predicted silica concentrate is {prediction} %")
mining()