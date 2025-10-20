import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Préparateur de tâches", page_icon="⚙️", layout="centered")

st.title("⚙️ Outil 1 – Input & Préparation des éléments de travail")
st.write("Ajoute ici toutes tes idées, tâches, missions… Une box = un sujet clair.")

if "subjects" not in st.session_state:
    st.session_state.subjects = [""]

# --- Ajouter / Supprimer des box
if st.button("+ Ajouter un sujet"):
    st.session_state.subjects.append("")

for i, val in enumerate(st.session_state.subjects):
    st.session_state.subjects[i] = st.text_area(f"Sujet {i+1}", value=val, height=80, key=f"subject_{i}")
    col1, col2 = st.columns([9,1])
    with col2:
        if st.button("🗑️", key=f"delete_{i}"):
            st.session_state.subjects.pop(i)
            st.experimental_rerun()

st.markdown("---")

# --- Génération du prompt
if st.button("🚀 C’est parti"):
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Charger le prompt depuis ton GitHub ou un fichier local
    # TODO: remplace par le lien ou le texte de ton prompt
    prompt_preparation = """
    [PROMPT PRÉPARATION ICI]
    """  

    # Crée le contenu formaté
    formatted_subjects = "\n".join([f"Sujet {i+1} : {s}" for i, s in enumerate(st.session_state.subjects) if s.strip() != ""])
    
    output = f"{prompt_preparation}\n\n{formatted_subjects}"

    st.success("✅ Copie le bloc ci-dessous et colle-le dans ton LLM.")
    st.text_area("Prompt complet :", value=output, height=400)

    st.download_button(
        label="📥 Télécharger .txt",
        data=output,
        file_name=f"input_preparation_{date_str}.txt",
        mime="text/plain",
    )
