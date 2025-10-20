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
    # PROMPT — ANALYSE, SÉQUENÇAGE ET PRIORISATION

Contexte :
Tu reçois une série de fiches de travail préparées (une par sujet). Ton rôle est maintenant de **les traiter comme un système d’opérations**, pour dégager une séquence d’exécution optimisée, fluide et sans redondance.

Objectif :
À partir des fiches fournies, produis une version traitée et structurée selon la trame suivante :

---
1️⃣ Synthèse opérationnelle :
- Objectif global implicite de l’ensemble des tâches.
- État d’avancement perçu (si certains éléments paraissent déjà prêts / clairs).
- Zones de flou ou de surcharge identifiées.

2️⃣ Séquençage logique :
Hiérarchise et ordonne toutes les actions (de toutes les fiches confondues) dans un ordre optimal d’exécution.  
But : qu’un opérateur humain puisse exécuter la séquence sans hésitation ni question.  
Format :
N° action / Description courte / Origine (N° sujet initial) / Type (action, dépendance, ou validation)

3️⃣ Optimisation & simplification :
- Fusionne ou regroupe les actions redondantes.  
- Supprime les doublons.  
- Si une action dépend d’une autre, fais-le apparaître clairement (ex : 4 → dépend de 2).  
- Réécris chaque action dans un style “mission log” : clair, froid, direct.  
- Si certaines tâches sont inutiles ou hors périmètre, isole-les en “parking”.

4️⃣ Jalons clés :
Dresse la liste des points de bascule ou livrables majeurs qui structurent la séquence.  
Format : N° jalon / Description / Actions concernées.

5️⃣ Recommandation d’exécution :
En 3 lignes maximum, indique la manière optimale de dérouler le plan (approche, rythme, focus).

---

Contraintes :
- Tu ne refais pas le travail de décantation : tu travailles à partir des fiches déjà produites.
- L’output doit tenir sur une structure claire et lisible, sans préambule ni commentaire.
- Si tu modifies la structure ou reformules des éléments, mentionne-le à la fin sous la forme :
“🔁 Modifications : [liste courte des ajustements effectués]”

---

Rends ton output dans un format lisible immédiatement et copiable tel quel dans un fichier `.txt`.

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
