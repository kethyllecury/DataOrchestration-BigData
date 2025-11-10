# DataOrchestration-BigData
# 🏫 Projeto ETL de Universidades com Prefect

Este projeto implementa um fluxo de **Extração, Transformação e Carga (ETL)** para coletar dados de universidades de um país específico, extraídos de uma **API pública**, e persistir esses dados em um **banco de dados MongoDB Atlas**.  
A orquestração e o agendamento do fluxo são gerenciados pela plataforma **Prefect**.

---

## ✨ Funcionalidades do ETL

O fluxo é dividido em três etapas principais, cada uma implementada como uma **Task Prefect** para garantir **observabilidade e resiliência**:

### 🧩 Extract (`extract_task`)
- Faz uma requisição HTTP para a API pública: [http://universities.hipolabs.com/search](http://universities.hipolabs.com/search)  
- Filtra os dados pelo **country** especificado (padrão: `Brazil`)  
- Possui tratamento de erro robusto e **3 tentativas automáticas de reexecução** em caso de falha de conexão  

### 🔄 Transform (`transform_task`)
- Padroniza os dados, selecionando apenas os campos essenciais:  
  - `name`  
  - `country`  
  - `domains`  
  - `web_pages`  

### 💾 Load (`load_task`)
- Conecta-se a um cluster **MongoDB Atlas** usando a variável de ambiente `MONGODB_URI`  
- Limpa a coleção `universidades` no banco de dados `universidades_db` antes de cada inserção  
- Insere os registros transformados  

---

## 📦 Tecnologias e Pré-requisitos

- **Linguagem:** Python 3.x  
- **Orquestração:** Prefect  
- **Banco de Dados:** MongoDB Atlas  
- **Bibliotecas Python:** `requests`, `pymongo`, `python-dotenv`

---

## 📋 `requirements.txt` sugerido
-prefect
-requests
-pymongo
-python-dotenv

---

## 🛠️ Configuração e Instalação

### 1. Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto.  
Este arquivo é crucial, pois contém a credencial de conexão ao seu banco de dados.

Exemplo de conteúdo do arquivo `.env`:

```bash
# OBS: MONGODB_URI deve ser a URI de Conexão (Connection String) do seu cluster Atlas.
MONGODB_URI="mongodb+srv://<user>:<password>@<cluster_name>/<database_name>?retryWrites=true&w=majority"

