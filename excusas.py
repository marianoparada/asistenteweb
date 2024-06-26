import streamlit as st
from g4f.client import Client

def chatear(modelo, mensaje):
    client = Client()
    with st.spinner('Generando la excusa...'):
        response = client.chat.completions.create(
            model=modelo,
            messages=[{'role': 'user', 'content': mensaje}]
        )
        respuesta = response.choices[0].message.content
    return respuesta

def main():
    st.title("Generador de Excusas")

    st.write("Generador de excusas creativas para llegar tarde al trabajo:")

    modelo = st.selectbox("Selecciona el modelo de lenguaje", ["gpt-3.5-turbo","gpt-4-turbo","gpt-4o"])
    mensaje = "Necesito que inventes una excusa. que hables en primera persona y te dirijas a Lucas. Tienes que poner una excusa de porque vas a llegar tarde al trabajo. Puedes inventar lo que sea, pero debes involucrar algun medio de transporte. Debes comenzar con: Hola Lucas, hoy llego un ratito mas tarde porque XXX. Debes reemplazar las XXX con la excusa. Puedes incluir algo morboso. Puedes incluir calles de Buenos Aires. Puede haber muertes de por medio. Debe ser en español, específicamente como si fueras argentino. Debes decir a que hora llegaras aproximadamente, siempre despues de las 11:30."
    
    if st.button("Generar Excusa"):
        respuesta = chatear(modelo, mensaje)
        st.markdown("### Excusa Generada")
        st.success(respuesta)

if __name__ == "__main__":
    main()
