<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>꒰ა Gerenciador de Lista de Contatos em Python ໒꒱</h1>

  <p>
    <i>Agenda de contatos em Python via linha de comando com listas e dicionários em memória para cadastrar, consultar e remover registros.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Estruturas%20de%20Dados-Listas%20%26%20Dicts-E6E6FA?style=for-the-badge&logoColor=555555" alt="Listas e Dicts" />
    <img src="https://img.shields.io/badge/Opera%C3%A7%C3%B5es-CRUD%20em%20Mem%C3%B3ria-FFD1DC?style=for-the-badge&logoColor=white" alt="CRUD" />
  </p>

</div>

<br/>

### ✦ Resumo

Permite gerenciar uma agenda de contatos diretamente no terminal em memória, com cadastro de novos registros, consulta geral ou por critérios, remoção por `ID` e validação das opções do menu.

### ✦ Tecnologias

- **Python 3.x:** Linguagem principal para manipulação de listas e dicionários, funções modulares, laços de repetição (`while` e `for`) e interação via console (sem bibliotecas externas).

### ✦ Regras

Cada contato é armazenado em memória com os campos `ID`, `Nome`, `Atividade/Cargo` e `Telefone`, e o menu principal oferece quatro ações:

- **1. Cadastrar Contato:** Recebe o `ID` e solicita `Nome`, `Atividade/Cargo` e `Telefone`, adicionando o registro à lista de contatos.
- **2. Consultar Contato(s):** Abre o submenu para ver todos os contatos, buscar por `ID` ou filtrar por `atividade/setor` (sem diferenciar maiúsculas e minúsculas), ou voltar ao menu principal.
- **3. Remover Contato:** Procura o contato pelo `ID` informado e remove o registro correspondente da lista.
- **4. Sair:** Encerra a execução do programa.
<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Executar

1. **Pré-requisitos:** Tenha o **Python 3.x** instalado na máquina.
2. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Madoard/Madoard-python-contact-list-manager.git](https://github.com/Madoard/Madoard-python-contact-list-manager.git)
   cd Madoard-python-contact-list-manager
   ```
3. **Execute o script (`contatos.py`):**
   ```bash
   python contatos.py
   ```

### ✦ Exemplo de Uso

```text
Bem-vindo à Lista de Contatos de Maria Eduarda Gonçalves!
Escolha a opção desejada:
1. Cadastrar Contato
2. Consultar Contato(s)
3. Remover Contato
4. Sair
Opção: 2

Escolha a opção desejada:
1. Consultar todos os contatos
2. Consultar por ID
3. Consultar por atividade/setor
4. Retornar ao menu principal
Opção: 2
Por favor, informe o ID do contato: 8922
ID: 8922
Nome: Duda
Atividade: Estudante
Telefone: 2196446681

Escolha a opção desejada:
1. Consultar todos os contatos
2. Consultar por ID
3. Consultar por atividade/setor
4. Retornar ao menu principal
Opção: 4

Bem-vindo à Lista de Contatos de Maria Eduarda Gonçalves!
Escolha a opção desejada:
1. Cadastrar Contato
2. Consultar Contato(s)
3. Remover Contato
4. Sair
Opção: 4
Encerrando o programa. Até mais!
```

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

O código completo está em [`contatos.py`](./contatos.py). Abaixo está a estrutura principal e como cada parte funciona:

```python
lista_contatos = [
    {"id": "4002", "nome": "Moises", "atividade": "Estudante", "telefone": "21988465143"},
    {"id": "8922", "nome": "Duda", "atividade": "Estudante", "telefone": "2196446681"}
]


def cadastrar_contato(id_contato):
    novo_contato = {
        "id": id_contato,
        "nome": input("Por favor, informe o nome do contato: ").strip(),
        "atividade": input("Por favor, informe a atividade/cargo do contato: ").strip(),
        "telefone": input("Por favor, informe o telefone do contato: ").strip()
    }
    lista_contatos.append(novo_contato.copy())
    print("Contato cadastrado com sucesso!\n")


def remover_contato():
    id_alvo = input("Por favor, informe o ID do contato a ser removido: ").strip()
    for i, contato in enumerate(lista_contatos):
        if contato["id"] == id_alvo:
            del lista_contatos[i]
            print("Contato removido com sucesso.\n")
            return
    print("Nenhum contato encontrado com este ID.\n")
```

- **Estrutura em memória (`lista_contatos`):** Armazena cada contato como um dicionário com `id`, `nome`, `atividade` e `telefone` dentro de uma lista, facilitando buscas e alterações durante a execução.
- **Funções de cadastro, consulta e remoção (`cadastrar_contato`, `consultar_contatos`, `remover_contato`):** Organizam o fluxo com loops `while True`, normalização de entradas com `.strip()` e `.lower()`, `enumerate()` com `del` para remover por índice e `f-strings` para exibir os dados.
- **Menu principal:** Mantém o programa rodando até o usuário escolher a opção de saída (`4`), tratando escolhas inválidas sem interromper a sessão.

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
