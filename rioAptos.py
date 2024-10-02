import streamlit as st
import pandas as pd

st.title("Quantidade de passaportes emitidos até 2023")

rioAptos = pd.read_csv("./bases/SINPA_QUANTIDADE_PASSAPORTES_2023_08.csv")

# st.data_editor(rioAptos)

bairros = st.multiselect("Escolha um bairro:", rioAptos['bairro'].unique())

st.write(f"Bairro escolhido foi: {bairros}")

if bairros: # filtragem para não renderizar itens vazios
    rioAptos_bairro = rioAptos[rioAptos["bairro"].isin(bairros)]

    # st.data_editor(rioAptos_bairro)

    menor_preco = rioAptos_bairro["preco"].min()
    maior_preco = rioAptos_bairro["preco"].max()
    st.write("Apartamento mais barato:", menor_preco)
    st.write("Apartamento mais caro:", maior_preco)

    valor = st.slider("Faixa de $:,", menor_preco, maior_preco, (menor_preco, maior_preco))

    rioAptos_bairro_preco = rioAptos_bairro[(rioAptos_bairro['preco'] >= valor[0]) & (rioAptos_bairro["preco"] <= valor[1])]
    st.write(rioAptos_bairro_preco)