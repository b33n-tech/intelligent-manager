import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Actualisation & Fusion v2", page_icon="🔁", layout="centered")

st.title("🔁 Outil 3 – Actualisation des éléments de travail")
st.write("Collez ici vos anciens éléments et vos nouveaux éléments séparément. L'outil générera le prompt complet pour le LLM.")

# Boîtes de dialogue
old_input = st.text_area("Ancien(s) élément(s) :", height=200)
new_input = st.text_area("Nouveaux élément(s) :", height=200)

if st.button("🚀 C’est parti"):
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Prompt de base pour l'actualisation avec juxtaposition
    prompt_actualisation = f"""
# PROMPT — ACTUALISATION & FUSION D'ÉLÉMENTS

Contexte :
Tu es un assistant d’actualisation de projet. On t’envoie :
1️⃣ Les anciens éléments (déjà traités et structurés)
2️⃣ Les nouveaux éléments (non traités)

Objectif :
Tu dois produire une **nouvelle version complète** avec :
- Réorganisation si nécessaire
- Identification des sous-actions et dépendances
- Fusion avec les éléments existants


Instructions :
- Ancien(s) élément(s) :
{old_input}

- Nouveau(x) élément(s) :
{new_input}

Pour chaque nouvel élément :
- Reformule le sujet (style clair, froid, opérationnel)
- Détaille les sous-actions et dépendances cachées
- Prépare un identifiant unique

Fusion :
- Compare les nouveaux éléments avec les anciens
- Fusionne si doublons ou éléments proches
- Met à jour les anciens éléments si nécessaire
- Ne supprime rien sans justification

Sortie :
- Inclue un mini-journal des changements :
  + Ajouts
  ~ Mises à jour
  = Fusions éventuelles
"""

    st.success("✅ Copie le bloc ci-dessous et colle-le dans ton LLM pour générer le JSON final.")
    st.text_area("Prompt complet :", value=prompt_actualisation, height=500)

    st.download_button(
        label="📥 Télécharger le prompt .txt",
        data=prompt_actualisation,
        file_name=f"actualisation_prompt_v2_{date_str}.txt",
        mime="text/plain",
    )
