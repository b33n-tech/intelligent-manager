import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Actualisation & Fusion", page_icon="🔁", layout="centered")

st.title("🔁 Outil 3 – Actualisation des éléments de travail")
st.write("Collez ici vos nouveaux éléments ou mises à jour. L'outil générera le prompt complet pour le LLM.")

# Boîte de dialogue pour coller le texte
new_input = st.text_area("Nouveaux éléments / mise à jour :", height=400)

if st.button("🚀 C’est parti"):
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Prompt de base pour l'actualisation (Prompt 3)
    prompt_actualisation = f"""
# PROMPT — ACTUALISATION & FUSION D'ÉLÉMENTS

Contexte :
Tu es un assistant d’actualisation de projet. On t’envoie une série de nouveaux éléments à intégrer dans un projet existant.

Objectif :
Pour chaque nouvel élément, tu dois :
- Reformuler le sujet (style clair, froid, opérationnel)
- Identifier les sous-actions et dépendances cachées
- Préparer une structure prête à fusionner dans le système existant

Instructions :
1️⃣ Décante et structure chaque élément de travail.
2️⃣ Prépare le rendu sous la forme JSON simplifiée, avec un identifiant unique par élément :
{{
    "id": "new-{date_str}-01",
    "titre": "...",
    "reformulation": "...",
    "sous_actions": ["...", "..."],
    "dependances": ["..."]
}}
3️⃣ Garde le format identique aux fichiers précédents.
4️⃣ Fournis un mini-journal des changements à la fin :
- Ajouts
- Mises à jour
- Fusions éventuelles

Nouveaux éléments à traiter :
{new_input}
"""

    st.success("✅ Copie le bloc ci-dessous et colle-le dans ton LLM pour générer le JSON final.")
    st.text_area("Prompt complet :", value=prompt_actualisation, height=500)

    st.download_button(
        label="📥 Télécharger le prompt .txt",
        data=prompt_actualisation,
        file_name=f"actualisation_prompt_{date_str}.txt",
        mime="text/plain",
    )
