import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import pandas as pd

# Downloads necessários para o NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# Stemmer para processamento de texto
stemmer = RSLPStemmer()

# Definindo palavras-chave para as entidades e intenções
tipos_seguro_keywords = {
    "seguro_veicular": ["segur", "veicul", "carro", "automóvel", "cobert"],
    "sinistro": ["sinistr", "acident", "colisão", "roub", "furto"],
    "cobertura": ["cobert", "proteção", "danos", "incêndio", "terceiros"],
    "pagamento": ["pagament", "fatur", "boleto", "parcel", "venciment", "pagamento"]
}

intencoes_keywords = {
    "consultar": ["consult", "verific", "saber", "detalh"],
    "solicitar": ["solic", "pedir", "requis", "fazer"],
    "agendar": ["agend", "marc", "program"],
    "status": ["status", "andament", "condição", "situação"]
}

# DataFrame para armazenar dados dos usuários
dados_usuarios = pd.DataFrame(columns=["nome", "veiculo", "tipo_seguro", "sinistro_reportado"])

# Lista para armazenar agendamentos
agendamentos = []

# Lista para armazenar sinistros registrados
sinistros = []

# Função de pré-processamento do texto
def preprocessing(pergunta):
    stop_words = set(stopwords.words("portuguese"))
    tokens = word_tokenize(pergunta.lower(), language='portuguese')  # Especifica o idioma
    tokens_stemmed = [stemmer.stem(word) for word in tokens if word not in stop_words and word.isalpha()]
    return tokens_stemmed

# Função para extrair entidade
def extract_entity(tokens):
    for token in tokens:
        for entity, keywords in tipos_seguro_keywords.items():
            if token in keywords:
                return entity
    return None

# Função para extrair intenção
def extract_intention(tokens):
    for token in tokens:
        for intention, keywords in intencoes_keywords.items():
            if token in keywords:
                return intention
    return None

# Função para cadastrar dados do usuário
def cadastrar_usuario(nome, veiculo, tipo_seguro):
    global dados_usuarios
    novo_usuario = pd.DataFrame([{
        "nome": nome,
        "veiculo": veiculo,
        "tipo_seguro": tipo_seguro,
        "sinistro_reportado": False
    }])
    dados_usuarios = pd.concat([dados_usuarios, novo_usuario], ignore_index=True)
    print(f"Usuário {nome} cadastrado com sucesso!")

# Função para realizar um agendamento
def realizar_agendamento():
    print("Chatbot: Por favor, informe os detalhes do agendamento.")
    data = input("Chatbot: Qual a data desejada para o agendamento? (Formato: DD/MM/AAAA)\nVocê: ")
    hora = input("Chatbot: Qual o horário desejado? (Formato: HH:MM)\nVocê: ")
    motivo = input("Chatbot: Qual o motivo do agendamento? (Exemplo: revisão de cobertura, vistoria, etc.)\nVocê: ")
    
    agendamento = {
        "data": data,
        "hora": hora,
        "motivo": motivo
    }
    
    agendamentos.append(agendamento)
    print(f"Chatbot: Agendamento realizado com sucesso! Detalhes:")
    print(f"  Data: {data}")
    print(f"  Hora: {hora}")
    print(f"  Motivo: {motivo}")

# Função para registrar um sinistro
def registrar_sinistro():
    print("Chatbot: Vamos registrar seu sinistro. Por favor, informe os detalhes.")
    data = input("Chatbot: Qual a data do sinistro? (Formato: DD/MM/AAAA)\nVocê: ")
    tipo = input("Chatbot: Qual foi o tipo de sinistro? (Exemplo: colisão, roubo, furto)\nVocê: ")
    descricao = input("Chatbot: Por favor, forneça uma breve descrição do ocorrido.\nVocê: ")
    
    sinistro = {
        "data": data,
        "tipo": tipo,
        "descricao": descricao
    }
    
    sinistros.append(sinistro)
    print(f"Chatbot: Sinistro registrado com sucesso! Detalhes:")
    print(f"  Data: {data}")
    print(f"  Tipo: {tipo}")
    print(f"  Descrição: {descricao}")

# Função principal para processar a pergunta do usuário
def process_question(pergunta):
    tokens = preprocessing(pergunta)
    entity = extract_entity(tokens)
    intention = extract_intention(tokens)
    return entity, intention

# Respostas predefinidas para cada combinação de entidade e intenção
respostas = {
    'seguro_veicular': {
        'consultar': 'Seu seguro veicular está ativo e cobre danos contra terceiros, roubo e colisão.',
        'solicitar': 'Você pode solicitar um novo seguro veicular preenchendo nosso formulário online.',
        'agendar': 'Você gostaria de agendar uma conversa com um de nossos consultores sobre seguro veicular?',
        'status': 'Seu seguro veicular está atualmente ativo e sem pendências.'
    },
    'sinistro': {
        'consultar': 'Não há sinistros registrados para o seu veículo.',
        'solicitar': 'Vamos registrar seu sinistro agora.',
        'agendar': 'Podemos agendar uma vistoria para avaliar os danos do sinistro.',
        'status': 'O sinistro está em processo de análise. Você será notificado em breve.'
    },
    'cobertura': {
        'consultar': 'A cobertura atual inclui danos contra terceiros, roubo e incêndio.',
        'solicitar': 'Você pode solicitar uma ampliação de cobertura através do nosso portal.',
        'agendar': 'Agendamento para revisão de cobertura está disponível para a próxima semana.',
        'status': 'Sua cobertura está ativa e sem alterações.'
    },
    'pagamento': {
        'consultar': 'O próximo pagamento é devido no dia 15 do próximo mês.',
        'solicitar': 'Você pode solicitar uma segunda via do boleto através do nosso site.',
        'agendar': 'Você gostaria de agendar um pagamento automático?',
        'status': 'O status do pagamento é pendente. Por favor, realize o pagamento para evitar a suspensão.'
    }
}

# Função do chatbot principal com loop contínuo
def chatbot():
    print("Olá! Bem-vindo à Seguradora XYZ. Como posso ajudar você hoje?")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ['sair', 'exit', 'encerrar']:
            print("Chatbot: Obrigado por usar o serviço da Seguradora XYZ. Até logo!")
            break
        
        entity, intention = process_question(pergunta)

        if entity in respostas:
            if intention in respostas[entity]:
                print(f"Chatbot: {respostas[entity][intention]}")
                if intention == "agendar" and entity == "seguro_veicular":
                    realizar_agendamento()
                elif intention == "solicitar" and entity == "sinistro":
                    registrar_sinistro()
            else:
                print(f"Chatbot: Entendi que você quer falar sobre {entity}. Como posso ajudar mais especificamente?")
        else:
            print(f"Chatbot: Desculpe, não consegui entender sua solicitação. Poderia reformular a pergunta?")

# Exemplo de cadastro de usuário
cadastrar_usuario("João", "Carro XYZ", "seguro_veicular")

# Executar o chatbot
chatbot()
