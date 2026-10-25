# TaskTracker - Sistema de Gerenciamento de Tarefas

**Estudante:** Paulo Eduardo Fernandes Dias  
**RA:** 22303387  
**Curso:** Ciência da Computação  
**Disciplina:** Bootcamp II - Fase 3 (Entrega Final: Conteinerização, Orquestração e Deploy)  

---

##  Sobre o Projeto
O **TaskTracker** é uma aplicação CLI (Interface de Linha de Comando) desenvolvida em Python 3 para auxílio no gerenciamento e acompanhamento de tarefas diárias. Nesta **Fase 3 (Entrega Final)**, a aplicação foi empacotada e orquestrada com **Docker** e **Docker Compose**, garantindo que rode de forma autossuficiente e idêntica em qualquer ambiente de produção.

---

##  Estrutura do Repositório (Árvore de Diretórios)
```plaintext
tasktracker-projeto/
├── .gitignore                # Regras para ignorar arquivos temporários e ambientes virtuais
├── Dockerfile                # Receita de construção da imagem Docker da aplicação
├── docker-compose.yml        # Orquestrador para execução interativa da CLI
├── README.md                 # Documentação principal com instruções de execução e guia Docker
├── docs/                     # Planejamento lógico da Fase 1
│   └── planejamento_logico.pdf
└── src/                      # Código-fonte Python da aplicação (Fase 2)
    └── main.py
```

---

##  Tecnologias Utilizadas
- **Linguagem:** Python 3.11-slim
- **Controle de Versão:** Git & GitHub
- **Containerização & Orquestração:** Docker & Docker Compose

---

##  Guia de Execução com Docker (Comandos Oficiais)

### 1. Construir a Imagem Docker (Build)
Para construir a imagem leve e autossuficiente da aplicação a partir do `Dockerfile`:
```bash
docker build -t tasktracker-app .
```

### 2. Rodar o Container de Forma Interativa (Docker Run)
Como o TaskTracker é uma aplicação CLI interativa que utiliza `input()`, é necessário utilizar as flags `-it` para alocar um pseudo-TTY e manter o `stdin` aberto:
```bash
docker run -it --name tasktracker-container tasktracker-app
```

### 3. Rodar via Orquestração (Docker Compose - Recomendado)
A forma mais prática e padronizada de executar a CLI interativa é através do Docker Compose, que já possui as diretivas `stdin_open: true` e `tty: true` pré-configuradas:
```bash
docker compose run tasktracker
```

---

## 💻 Execução Nativa (Sem Docker)
Caso deseje rodar o script Python diretamente na sua máquina local:
```bash
python src/main.py
```
