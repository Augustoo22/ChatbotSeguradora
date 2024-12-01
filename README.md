# **Documentação do Chatbot Seguradora XYZ**


## **Descrição Geral**
Este é um chatbot desenvolvido para interagir com clientes de uma seguradora. Ele permite realizar diversas operações, como consultar informações sobre seguros, registrar sinistros, agendar eventos, e verificar status de pagamentos ou coberturas.

O chatbot utiliza **NLTK** para processamento de texto, **Pandas** para manipulação de dados e listas para armazenamento de interações como agendamentos e sinistros registrados.

---

## **Funcionalidades**
### 1. **Processamento de Texto**
Utiliza tokenização, remoção de stopwords e stemming para interpretar a entrada do usuário e determinar:
- **Entidade**: O tipo de seguro ou operação relacionada.
- **Intenção**: A ação que o usuário deseja realizar (consultar, solicitar, agendar, verificar status).

### 2. **Consultas**
Permite consultar informações sobre:
- Seguro veicular.
- Cobertura.
- Pagamento.
- Sinistro.

### 3. **Solicitação de Sinistro**
Permite registrar um sinistro com detalhes como:
- Data do evento.
- Tipo de sinistro (ex.: colisão, roubo, furto).
- Descrição do ocorrido.

### 4. **Agendamentos**
Permite ao usuário agendar eventos relacionados ao seguro, como:
- Revisões de cobertura.
- Vistorias de sinistros.

---

## **Estrutura do Código**
### **1. Bibliotecas Utilizadas**
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import pandas as pd
```
- **nltk**: Usado para processamento de linguagem natural, incluindo tokenização e stemming.
- **pandas**: Para armazenar dados do usuário em um DataFrame.

---

### **2. Pré-processamento de Texto**
A função `preprocessing` realiza o processamento do texto do usuário:
```python
def preprocessing(pergunta):
    stop_words = set(stopwords.words("portuguese"))
    tokens = word_tokenize(pergunta.lower(), language='portuguese')
    tokens_stemmed = [stemmer.stem(word) for word in tokens if word not in stop_words and word.isalpha()]
    return tokens_stemmed
```
**Exemplo de Uso:**
Entrada do usuário: `"Quero consultar meu seguro veicular."`  
Tokens processados: `['quer', 'consult', 'segur', 'veicul']`

---

### **3. Identificação de Entidade e Intenção**
As funções `extract_entity` e `extract_intention` utilizam listas de palavras-chave para identificar o contexto da pergunta:
```python
def extract_entity(tokens):
    for token in tokens:
        for entity, keywords in tipos_seguro_keywords.items():
            if token in keywords:
                return entity
    return None

def extract_intention(tokens):
    for token in tokens:
        for intention, keywords in intencoes_keywords.items():
            if token in keywords:
                return intention
    return None
```
**Exemplo de Uso:**
- Tokens: `['consult', 'segur', 'veicul']`
- **Entidade identificada**: `seguro_veicular`
- **Intenção identificada**: `consultar`

---

### **4. Cadastro de Usuário**
A função `cadastrar_usuario` adiciona os dados do cliente a um DataFrame para registro interno:
```python
def cadastrar_usuario(nome, veiculo, tipo_seguro):
    novo_usuario = pd.DataFrame([{
        "nome": nome,
        "veiculo": veiculo,
        "tipo_seguro": tipo_seguro,
        "sinistro_reportado": False
    }])
    dados_usuarios = pd.concat([dados_usuarios, novo_usuario], ignore_index=True)
    print(f"Usuário {nome} cadastrado com sucesso!")
```
**Exemplo de Uso:**
```python
cadastrar_usuario("João", "Carro XYZ", "seguro_veicular")
```
Resultado:  
Usuário João cadastrado com sucesso!

---

### **5. Registro de Sinistros**
A função `registrar_sinistro` coleta dados do sinistro e os armazena em uma lista:
```python
def registrar_sinistro():
    print("Chatbot: Vamos registrar seu sinistro. Por favor, informe os detalhes.")
    data = input("Chatbot: Qual a data do sinistro? (Formato: DD/MM/AAAA)\nVocê: ")
    tipo = input("Chatbot: Qual foi o tipo de sinistro? (Exemplo: colisão, roubo, furto)\nVocê: ")
    descricao = input("Chatbot: Por favor, forneça uma breve descrição do ocorrido.\nVocê: ")
    
    sinistro = {"data": data, "tipo": tipo, "descricao": descricao}
    sinistros.append(sinistro)
    print(f"Chatbot: Sinistro registrado com sucesso! Detalhes:")
    print(f"  Data: {data}")
    print(f"  Tipo: {tipo}")
    print(f"  Descrição: {descricao}")
```
**Exemplo de Uso:**
Usuário: `"Quero registrar um sinistro."`  
Chatbot:
```
Chatbot: Vamos registrar seu sinistro. Por favor, informe os detalhes.
Chatbot: Qual a data do sinistro? (Formato: DD/MM/AAAA)
Você: 01/12/2024
Chatbot: Qual foi o tipo de sinistro? (Exemplo: colisão, roubo, furto)
Você: colisão
Chatbot: Por favor, forneça uma breve descrição do ocorrido.
Você: Bati o carro em outro veículo na esquina.
Chatbot: Sinistro registrado com sucesso! Detalhes:
  Data: 01/12/2024
  Tipo: colisão
  Descrição: Bati o carro em outro veículo na esquina.
```

---

### **6. Agendamentos**
A função `realizar_agendamento` permite que o usuário informe data, hora e motivo do agendamento:
```python
def realizar_agendamento():
    print("Chatbot: Por favor, informe os detalhes do agendamento.")
    data = input("Chatbot: Qual a data desejada para o agendamento? (Formato: DD/MM/AAAA)\nVocê: ")
    hora = input("Chatbot: Qual o horário desejado? (Formato: HH:MM)\nVocê: ")
    motivo = input("Chatbot: Qual o motivo do agendamento? (Exemplo: revisão de cobertura, vistoria, etc.)\nVocê: ")
    
    agendamento = {"data": data, "hora": hora, "motivo": motivo}
    agendamentos.append(agendamento)
    print(f"Chatbot: Agendamento realizado com sucesso! Detalhes:")
    print(f"  Data: {data}")
    print(f"  Hora: {hora}")
    print(f"  Motivo: {motivo}")
```
**Exemplo de Uso:**
Usuário: `"Preciso agendar uma vistoria."`  
Chatbot:
```
Chatbot: Por favor, informe os detalhes do agendamento.
Chatbot: Qual a data desejada para o agendamento? (Formato: DD/MM/AAAA)
Você: 05/12/2024
Chatbot: Qual o horário desejado? (Formato: HH:MM)
Você: 15:00
Chatbot: Qual o motivo do agendamento? (Exemplo: revisão de cobertura, vistoria, etc.)
Você: vistoria de sinistro
Chatbot: Agendamento realizado com sucesso! Detalhes:
  Data: 05/12/2024
  Hora: 15:00
  Motivo: vistoria de sinistro
```

---

### **7. Chatbot Principal**
O chatbot opera em um loop contínuo, processando a entrada do usuário e respondendo de acordo:
```python
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
```

---

## **Testando o Chatbot**
### Comandos Úteis:
1. **Para Agendar**:
   - "Quero agendar uma vistoria."
   - "Preciso marcar uma reunião sobre cobertura."
   
2. **Para Registrar Sinistro**:
   - "Quero registrar um sinistro."
   - "Preciso relatar um acidente com meu carro."

3. **Para Consultar**:
   - "Quero consultar meu seguro."
   - "Qual é o status do meu pagamento?"

4. **Para Sair**:
   - "Sair"
   - "Encerrar"

---