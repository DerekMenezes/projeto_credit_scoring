import streamlit as st
import pandas as pd
import joblib
from pycaret.classification import load_model, predict_model
from io import BytesIO
from datetime import datetime

modelo = load_model('LGBM Model CREDIT SCORING 00000')

@st.cache_data
def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

st.set_page_config(page_title = 'Credit Scoring', \
        page_icon = '💶',
        layout="wide",
        initial_sidebar_state='expanded'
    )

st.title("📊 Predição de Risco de Crédito")
st.write("Carregue um arquivo CSV ou insira os dados manualmente para previsões.")



uploaded_file = st.file_uploader("Carregar arquivo CSV ou Feather", type=["csv", "ftr"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_feather(uploaded_file)

    
    predictions = predict_model(modelo, data=df)

    
    st.write("### 🔍 Previsões:")
    st.dataframe(predictions)

    
    df_xlsx = to_excel(predictions)
    st.download_button(
        label="📥 Baixar Previsões",
        data=df_xlsx,
        file_name="previsoes.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# 📊 Entrada manual de dados
with st.form("manual_input"):
    st.header("Entrada Manual")

    # Campos para as variáveis
    renda = st.number_input("Renda Mensal (R$)", min_value=0.0)
    tempo_emprego = st.number_input("Tempo no Emprego (anos)", min_value=0.0)
    qtd_filhos = st.number_input("Quantidade de Filhos", min_value=0)
    idade = st.number_input("Idade", min_value=18, max_value=100)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
    posse_veiculo = st.selectbox("Possui Veículo?", ["Sim", "Não"])
    qt_pessoas_residencia = st.number_input("Quantidade de Pessoas na Residência", min_value=1)
    posse_imovel = st.selectbox("Possui Imóvel?", ["Sim", "Não"])
    tipo_renda = st.selectbox("Tipo de Renda", ['Empresário', 'Assalariado', 'Servidor público', 'Pensionista',
       'Bolsista'])
    educacao = st.selectbox("Educação", ['Médio', 'Superior incompleto', 'Superior completo', 'Fundamental',
       'Pós graduação'])
    estado_civil = st.selectbox("Estado Civil", ['Solteiro', 'Casado', 'União', 'Separado', 'Viúvo'])
    tipo_residencia = st.selectbox("Tipo de Residência", ['Casa', 'Com os pais', 'Aluguel', 'Comunitário', 'Governamental',
       'Estúdio'])

    
    submitted = st.form_submit_button("Prever")

if submitted:
    input_data = pd.DataFrame([{
        'renda': renda,
        'tempo_emprego': tempo_emprego,
        'qtd_filhos': qtd_filhos,
        'idade': idade,
        'sexo': 'M' if sexo == "Masculino" else 'F',
        'posse_de_veiculo': 1 if posse_veiculo == "Sim" else 0,
        'posse_de_imovel': 1 if posse_imovel == "Sim" else 0,
        'qt_pessoas_residencia': qt_pessoas_residencia,
        'tipo_renda': tipo_renda,
        'educacao': educacao,
        'estado_civil': estado_civil,
        'tipo_residencia': tipo_residencia,
    }])

    # Fazer previsão
    try:
        colunas_esperadas = modelo.feature_names_in_ 
        input_data = input_data.reindex(columns=colunas_esperadas, fill_value=0)    
        input_data['data_ref'] = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))
        input_data['index'] = 0
        prediction = predict_model(modelo, data=input_data)
        score = prediction['prediction_score'][0]
        st.success(f"Probabilidade de Inadimplência: {score:.2%}")
    except Exception as e:
        st.error(f"Erro na previsão: {str(e)}")