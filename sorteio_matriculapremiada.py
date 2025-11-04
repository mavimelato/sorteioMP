import streamlit as st
import pandas as pd
import random

st.title("🎲 Sorteio - Matrícula Premiada")

# Upload da base (ou leitura direta de arquivo)
uploaded_file = st.file_uploader("base_sorteio.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Prévia da base:")
    st.dataframe(df.head())

    # Define semente fixa
    seed = st.number_input("Escolha a semente (opcional)", value=42)
    random.seed(seed)

    # Cria lista de tickets (repete conforme numeros_da_sorte)
    tickets = []
    for _, row in df.iterrows():
        tickets.extend([(row["branch_id"], row["branch_name"])] * int(row["numeros_da_sorte"]))

    st.write(f"Total de tickets: {len(tickets)}")

    # Define número de vencedores
    k = st.number_input("Número de vencedores", min_value=1, value=5, step=1)

    if st.button("🎉 Realizar sorteio"):
        vencedores = random.sample(tickets, k)
        vencedores_df = pd.DataFrame(vencedores, columns=["branch_id", "branch_name"]).drop_duplicates()

        st.success("🏆 Escolas sorteadas:")
        st.dataframe(vencedores_df)

        # Download dos resultados
        csv = vencedores_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Baixar resultado", csv, "vencedores.csv", "text/csv")
