import streamlit as st
import pandas as  pd
import random

from streamlit.runtime.state import session_state

Lista1 = ["der Name", "der Vorname", "Nachname", "die Stadt", "die E-Mail Adresse", "die Handynummer", "die Telefonnummer",
          "die Sprache", "die Zahl", "die Antwort", "der Partner", "die Partnerin", "die Person", "das Wort", "der Text", "die Autobahn", "die Flasche", "der Kindergarten",
          "der Koffer"]
Traduccion1 = ["Nombre", "Primer nombre", "Apellido", "Ciudad", "Dirección de E-Mail", "Número de celular", "Número telefónico",
               "Idioma", "Número", "Respuesta", "Compañero", "Compañera", "Persona", "Palabra", "Texto", "Autopista", "Botella", "Jardín infantil",
               "Maleta"]
Lista2 = ["das Hobby", "das Buch", "das Café", "der Computer", "die Verabredung", "der Freund", "die Leute", "der Fußball",
          "das Kino", "das Theater", "das Museum", "die Musik", "das Schwimmbad", "das Foto", "der Beruf", "der Artz", "das Krankenhaus",
          "der Friseur", "die Handwerker", "der Journalist", "der Kellner", "der Koch", "der Krankenpfleger", "die Krankenschwester", "das Restaurant", "der Kollege",
          "die Firma", "die Schule", "der Kurs", "die Universität", "das Seminar", "das Taxi", "das Auto", "der Abend", "der Nachmittag",
          "der Moment", "die Stunde", "der Tag", "die Woche", "das Wochenende", "das Jahr", "die Information", "der Familienname", "die Adresse",
          "die Postleitzahl", "der Wohnort", "das Beispiel", "der Schlüssel", "das Wörterbuch", "das Zimmer"]
Traduccion2 = ["Pasatiempo", "Libro", "Cafetería", "Computadora", "La cita, compromiso", "Amigo", "La gente", "Fútbol",
               "Cine", "Teatro", "Museo", "Música", "Piscina", "Fotografía", "Oficio", "Médico", "Hospital", "Peluquero", "Obrero", "Periodista",
               "Mesero", "Cocinero", "Enfermero", "Enfermera", "Restaurante", "Colega",
               "Empresa", "Escuela", "El curso", "Universidad", "Seminario", "Taxi", "Automóvil", "Noche", "Después del medio día",
               "Momento", "La hora", "Día", "Semana", "Fin de semana", "El año", "La información", "Apellido", "Dirección",
               "Código postal", "Lugar de residencia", "Ejemplo", "Llave", "Diccionario", "Cuarto"]

Lista = Lista1 + Lista2
Traduccion = Traduccion1 + Traduccion2

st.title("HERZLICH WILLKOMMEN LIEBE STUDENTE!")

if "indice" not in st.session_state:
    st.session_state.indice = 0
if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0
if "intentos" not in st.session_state:
    st.session_state.intentos = 0
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False
if "x" not in st.session_state:
    st.session_state.x = random.randint(0, len(Lista) - 1)

st.sidebar.title("Einstellungen")
cantidad_objetivo = st.sidebar.slider("Wie viele Wörter möchten sie heute lernen?", 5, len(Lista))

if st.sidebar.button("Neu starten"):
    st.session_state.intentos = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False
    st.session_state.x = random.randint(0, len(Lista) - 1)
    st.rerun()

tab1, tab2, tab3 = st.tabs(["Lernwortschatz 1","Lernwortschatz 2", "Prüfung"])

with tab1:
    st.header("Lernwortschatz 1")
    df = pd.DataFrame({
        "Wort": Lista1,
        "Übersetzt": Traduccion1})
    st.dataframe(df, use_container_width = True)

with tab2:
    st.header("Lernwortschatz 2")
    df = pd.DataFrame({
        "Wort": Lista2,
        "Übersetzt": Traduccion2})
    st.dataframe(df, use_container_width = True)


with tab3:
    if st.session_state.intentos >= cantidad_objetivo:
        st.session_state.finalizado = True
    if st.session_state.finalizado:
        st.header("Wundabar! du hast fertiggemacht")
        nota = (st.session_state.aciertos / cantidad_objetivo*100)
        st.write("Benotung", f"{nota}")
    else:
        palabra_actual = Lista[st.session_state.x]
        art_correcto, sin_art = palabra_actual.split(" ", 1)
        st.subheader(f"Frage {st.session_state.intentos +1} von {cantidad_objetivo}")
        st.write(f"Artikel von: {sin_art}")
        respuesta = st.text_input("Schreiben Sie die Antwort: ",key = f"input_{st.session_state.intentos}")
        respuesta = respuesta.lower().strip()
        if st.button("Klicken Sie hier bitte an, um das Wort zu überprüfen"):
            if respuesta == art_correcto.lower().strip():
                st.success("Genau!")
                st.write(f"Übersetzt: {Traduccion[st.session_state.x]}")
                st.session_state.aciertos += 1
            else:
                st.error("Das ist Falsch")
        if st.button("Nächste Frage:"):
            st.session_state.intentos += 1
