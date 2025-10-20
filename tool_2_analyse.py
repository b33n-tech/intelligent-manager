import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Analyse & Traitement", page_icon="🧠", layout="centered")

st.title("🧠 Outil 2 – Analyse et Séquençage")
st.write("Colle ici le résultat du LLM issu de l’Outil 1, tel quel.")

llm_output = st.text_area("Output LLM brut :", height=400)

if st.button("🚀 C’est parti"):
    date_str = datetime.now().strftime("%Y-%m-%d")

    # TODO: remplace par ton prompt d’analyse depuis le repo GitHub
    prompt_analyse = """
    [PROMPT ANALYSE ICI]
    """

    final_prompt = f"{prompt_analyse}\n\n{llm_output}"

    st.success("✅ Copie le bloc ci-dessous et colle-le dans ton LLM pour la phase 2.")
    st.text_area("Prompt complet :", value=final_prompt, height=400)

    st.download_button(
        label="📥 Télécharger .txt",
        data=final_prompt,
        file_name=f"analyse_traitement_{date_str}.txt",
        mime="text/plain",
    )
