import streamlit as st

st.title("📝 Examen de Conocimientos")

# Preguntas
questions = [
    {
        "question": "¿Capital de Francia?",
        "options": ["", "Madrid", "París", "Roma", "Berlín"],
        "answer": "París"
    },
    {
        "question": "¿Cuánto es 5 + 3?",
        "options": ["", "6", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "¿Planeta rojo?",
        "options": ["", "Venus", "Marte", "Júpiter", "Saturno"],
        "answer": "Marte"
    },
    {
        "question": "¿Lenguaje usado en Streamlit?",
        "options": ["", "Python", "Java", "C++", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "¿Cuántos días tiene una semana?",
        "options": ["", "5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "¿Océano más grande?",
        "options": ["", "Atlántico", "Índico", "Pacífico", "Ártico"],
        "answer": "Pacífico"
    },
    {
        "question": "¿Quién pintó la Mona Lisa?",
        "options": ["", "Van Gogh", "Da Vinci", "Picasso", "Dalí"],
        "answer": "Da Vinci"
    },
    {
        "question": "¿Resultado de 10 / 2?",
        "options": ["", "3", "4", "5", "6"],
        "answer": "5"
    },
    {
        "question": "¿Gas que respiramos principalmente?",
        "options": ["", "Oxígeno", "Hidrógeno", "Nitrógeno", "CO2"],
        "answer": "Nitrógeno"
    }
]

# Tabs
tab1, tab2 = st.tabs(["📋 Cuestionario", "📊 Informe"])

answers = []

with tab1:
    st.header("Responde las preguntas:")

    for i, q in enumerate(questions):
        ans = st.radio(q["question"], q["options"], key=i)
        answers.append(ans)

    if st.button("Calcular nota"):

        score = 0
        correct = []
        incorrect = []

        for i, q in enumerate(questions):

            if answers[i] == "":
                continue

            if answers[i] == q["answer"]:
                score += 1
                correct.append(q["question"])
            else:
                score -= 1
                incorrect.append(q["question"])

        # Escalar nota a 10
        grade = (score / len(questions)) * 10
        grade = round(grade, 2)

        st.subheader(f"Nota final: {grade}")

        # Feedback
        if grade < 2:
            st.error("Muy insuficiente 😞")
        elif 3 <= grade < 5:
            st.warning("Insuficiente")
        elif 5 <= grade < 6:
            st.info("Suficiente 👍")
            st.balloons()
        elif 6 <= grade < 7:
            st.success("Bien 👌")
            st.balloons()
        elif 7 <= grade < 9:
            st.success("Notable ⭐")
            st.balloons()
        elif 9 <= grade < 10:
            st.success("Sobresaliente 🌟")
            st.snow()
        elif grade == 10:
            st.success("Excelente 🏆")
            st.snow()

        st.session_state.correct = correct
        st.session_state.incorrect = incorrect
        st.session_state.grade = grade


with tab2:
    st.header("Informe del examen")

    if "grade" in st.session_state:

        st.markdown(f"### Nota final: **{st.session_state.grade}**")

        st.markdown("### ✅ Preguntas correctas")
        for q in st.session_state.correct:
            st.markdown(f"- {q}")

        st.markdown("### ❌ Preguntas incorrectas")
        for q in st.session_state.incorrect:
            st.markdown(f"- {q}")

    else:
        st.info("Primero completa el examen en la pestaña de cuestionario.")
