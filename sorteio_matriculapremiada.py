import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Sorteio Matricula Premiada", layout="centered")

st.title("🎉 Sorteio Matricula Premiada")

# Upload do CSV
st.markdown("Faça upload do CSV com os dados das escolas (branch_id, branch_name, numeros_da_sorte)")
file = st.file_uploader("Escolha o arquivo CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.success(f"CSV carregado com sucesso! {len(df)} escolas encontradas.")
    st.dataframe(df.head())

    # Opções de sorteio
    total_vencedores = st.number_input("Quantos vencedores sortear?", min_value=1, max_value=len(df), value=1, step=1)

    if st.button("Sortear!"):
        # Criar lista de tickets (cada escola repete conforme numeros_da_sorte)
        tickets = []
        for _, row in df.iterrows():
            tickets.extend([{"branch_id": row["branch_id"], "branch_name": row["branch_name"]}] * int(row["numeros_da_sorte"]))

        # Definir semente para reproducibilidade
        random.seed()

        # Sorteio sem repetição
        vencedores = random.sample(tickets, k=total_vencedores)

        st.markdown("### 🏆 Resultado do Sorteio")
        for i, v in enumerate(vencedores, start=1):
            st.write(f"{i}. {v['branch_name']} (ID: {v['branch_id']})")

        st.balloons()
