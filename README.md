<div align="center">

# APEX BANK

**Sistema de gerenciamento bancário com interface gráfica moderna.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![JSON](https://img.shields.io/badge/Database-JSON-lightgrey?style=for-the-badge)

---

</div>

## Sobre o Projeto

O **Apex Bank** é uma aplicação desktop desenvolvida em Python e Tkinter para simulação de operações bancárias. O sistema conta com tema escuro (Dark Mode) e realiza a leitura e escrita de dados de forma assíncrona em arquivos JSON locais.

---

## Funcionalidades

- **Autenticação:** Login e validação de credenciais de usuários.
- **Cadastro de Contas:** Registro de novos clientes com carteira inicial zerada.
- **Consulta de Saldo:** Exibição dinâmica e atualizada em tempo real.
- **Saque e Depósito:** Validação de saldo, tratamento de centavos (suporte a vírgula e ponto) e arredondamento automático para evitar valores negativos zerados.
- **Persistência de Dados:** Salvamento automático das operações no arquivo local de usuários.

---

## Como Executar o Projeto

Siga as instruções abaixo para rodar a aplicação em sua máquina local.

### Pré-requisitos

- **Python 3.x** instalado.
- **Git** instalado.

### Passo a Passo

1. **Clonar o Repositório**
   Abra o seu terminal ou prompt de comando e execute:
 ```bash
    git clone [https://github.com/SEU-USUARIO/Apex-Bank.git](https://github.com/SEU-USUARIO/Apex-Bank.git)
```
2. **Acessar a Pasta do Projeto**
   Entre no diretório clonado:
```bash
   cd Apex-Bank
```

3. **Verificar Dependências**
   O projeto utiliza o **Tkinter**, que já vem incluso na instalação padrão do Python. Caso receba erro de módulo não encontrado (comum em algumas distribuições Linux), instale com:
```bash
   sudo apt-get install python3-tk
```
   Se houver um arquivo `requirements.txt` com outras dependências, instale-as com:
```bash
   pip install -r requirements.txt
```

4. **Executar a Aplicação**
   Com tudo pronto, inicie o sistema:
```bash
   python main.py
```

5. **Primeiro Acesso**
   Na primeira execução, o arquivo JSON de usuários será criado automaticamente. Use a tela de cadastro para criar sua conta antes de fazer login.
