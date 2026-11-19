<div align="center">

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 📇 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <h1>˚₊‧꒰ა 📓 Gerenciador de Lista de Contatos em Python 📓 ໒꒱‧₊˚</h1>

  <p>
    <i>✧･ﾟ: *✧･ﾟ:* Agenda de contatos em Python via linha de comando construída com listas e dicionários em memória para cadastrar, consultar, filtrar e remover registros de contatos *:･ﾟ✧*:･ﾟ✧</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Estruturas%20de%20Dados-Listas%20%26%20Dicts-E6E6FA?style=for-the-badge&logoColor=555555" alt="Listas e Dicts" />
    <img src="https://img.shields.io/badge/Opera%C3%A7%C3%B5es-CRUD%20em%20Mem%C3%B3ria-FFD1DC?style=for-the-badge&logoColor=white" alt="CRUD" />
  </p>

</div>

<br/>

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 📞 ꒱ Funcionalidades da Agenda

O menu interativo em CLI oferece gerenciamento completo de contatos em memória:

- **₊˚✒️ Cadastrar Contato (`Create`):** Salva um novo registro de contato mapeado por `ID`, `Nome`, `Atividade/Cargo` e `Telefone`.
- **₊˚🔖 Consultar Contatos (`Read`):**
  - *Ver Todos:* Percorre a agenda para exibir todos os contatos cadastrados.
  - *Buscar por ID:* Localiza um registro específico pelo seu identificador único.
  - *Buscar por Atividade:* Filtra os registros dinamicamente por ocupação ou setor.
- **₊˚✒️ Remover Contato (`Delete`):** Localiza e remove o dicionário do contato na lista a partir do `ID`.
- **₊˚🔖 Sair:** Encerra a sessão interativa com segurança.

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 💌 ꒱ Como Foi Construído

- **₊˚📓 Estruturas de Dados Compostas (`list[dict]`):** Modelagem de cada contato como um `dict` chave-valor adicionado a uma `list` central em memória.
- **₊˚📇 Arquitetura CRUD Modular (`def`):** Separação do cadastro, consultas por múltiplos critérios e remoção em funções parametrizadas conduzidas por loops de menu `while` aninhados.
- **₊˚📓 Percorrimento e Filtragem de Coleções:** Uso de laços `for` com correspondência condicional de chaves para inspecionar, filtrar e alterar registros com segurança.

<br/>

<div align="center">
  <p>°•. 📓 .•° ────── ꒰ 💗 ꒱ ────── °•. 📓 .•°</p>
  <p><i>feito com 💗 por <b>Maria Eduarda Gonçalves</b></i></p>
</div>
