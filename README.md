# ⚔️ Maethor Bot

[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/library-discord.py-red)](https://discordpy.readthedocs.io/)

**Maethor** (do élfico, *Guerreiro*) é um bot multifuncional para o Discord desenvolvido em Python. Ele foi criado para trazer ordem, entretenimento e utilidades para o seu servidor, garantindo uma experiência estável e robusta para os membros.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Biblioteca Principal:** `discord.py`
* **Gerenciador de Dependências:** `pip`

---

## ⚙️ Como Executar o Projeto Localmente

### Pré-requisitos
Antes de começar, você vai precisar do [Python](https://www.python.org/) instalado na sua máquina (recomendado: 3.11 ou 3.12).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Jotshh/Maethor-Bot.git](https://github.com/Jotshh/Maethor-Bot.git)
   cd Maethor-Bot
   
---

## 🚀 Funcionalidades do Maethor Bot 🤖 

* **🛡️ Moderação & Utilidades:** Comandos essenciais para manter o servidor organizado.
* **🎮 Integração Gamer:** Recursos pensados para comunidades de jogos (como League of Legends).
* **🎮 Sistema de Amizade:** Recursos para estar sempre com classe e respeitando a moderação.
* **⚡ Slash Commands:** Totalmente atualizado com as interações modernas do Discord (`/comando`).

---

## 📌 Comandos Disponíveis

O prefixo padrão do bot é o ponto final: `.`

### 💬 Interação & Diversão
* **`@Maethor Bot`** *(Menção)*
  Sempre que alguém mencionar o bot no chat, ele responderá com alguma frase clássica e aleatória.

* **`.ola`**
  Responde com uma saudação amigável mencionando você.

* **`.lol`**
  Marca a galera com o cargo de League of Legends chamando todos para jogar com o League Sinal.

* **`.roll [NdN]`**
  Rola dados de forma fácil, como no RPG. 
  Exemplo: `.roll 2d6` (rola 2 dados de 6 lados).

* **`.boneco [grupo]`** (ou **`.pick`**, **`.champ`**)
  Sorteia um campeão de League of Legends para você jogar.
  Se você não escrever nenhum grupo, ele sorteia de todos os campeões. 
  *Grupos disponíveis:* `todos`, `mid`, `jungle`, `adc`, `sup`, `top`, `mains`.
  Exemplos de uso: `.boneco`, `.boneco mid`, `.boneco sup`.

### 🔨 Sistema de Amizade (Pontos)
*O bot adiciona **anos de amizade** automaticamente quando tu estiver ativo em uma chamada de voz.*

* **`.amizade [@membro]`** (ou **`.pontos`**, **`.anos`**)
  Verifica o seu total de "anos de amizade" ou de outra pessoa que você marcar.

> ⚠️ **Cuidado com a língua:** O Maethor não tolera palavrões no chat e fará tu entrar em uma roleta de punição, em que tu irá perder seus anos de amizade com ele!

### 🛡️ Moderação & Utilitários
* **`.clear <numero>`** (ou **`.limpar`**)
  Apaga a quantidade desejada de mensagens no canal de forma limpa e rápida.
  *(Requisito: Ter o cargo de moderação do servidor)*

* **`.cargos`** (ou **`.roles`**)
  Cria e envia um menu interativo com botões para os usuários escolherem sozinhos os seus cargos de jogos, como LoL e Valorant.
  *(Requisito: Ser Administrador)*
