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
    # PROMPT — PRÉPARATION DES ÉLÉMENTS DE TRAVAIL

Contexte :
Tu es un assistant d’analyse et de préparation de travail. On t’envoie une liste d’éléments bruts : tâches, missions, idées, to-do… Ton rôle est de **clarifier, reformuler, et décortiquer** chaque sujet pour en faire une base exploitable de travail.

Objectif :
Pour chaque sujet, tu dois produire une fiche de travail concise et opérationnelle, sous la trame suivante :

---
N° sujet : [numéro]
Description initiale : [copie brute de l’input]
Reformulation : [formule claire, efficace, sans jargon. Style concis, ton “industriel / militaire”.]
Sous-actions : [liste d’actions concrètes et séquentielles à effectuer pour mener ce sujet à bien]
Dépendances cachées : [éléments implicites, prérequis, ressources, validations, informations manquantes ou liens logiques à d’autres sujets]
---

Contraintes :
- Ne pas fusionner les sujets entre eux.
- Être synthétique mais exhaustif sur les sous-actions.
- Si une tâche semble trop vague, note “⚠️ À clarifier” et précise ce qu’il faut demander ou définir.
- Le ton doit être **sec, net, sans émotion**, façon log de mission.
- Pas de fioritures, pas de bullet points décoratifs.

Exemple de rendu :
---
N° sujet : 1  
Description initiale : Refaire la page d’accueil du site.  
Reformulation : Reconcevoir l’architecture et le contenu de la page d’accueil pour refléter la nouvelle offre.  
Sous-actions : 
- Auditer la version actuelle et lister les points de friction.  
- Définir la nouvelle arborescence et les blocs de contenu.  
- Rédiger les textes.  
- Faire valider par X.  
- Intégrer dans Webflow.  
Dépendances cachées : Accès au CMS, validation de la charte graphique, inputs marketing à jour.
---

Maintenant, traite chaque sujet de la liste ci-dessous.
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
