# Generate Curriculum

Generate Curriculum é um projeto que visa ajudar as pessoas a criar currículos automáticos e baixá-los em formato Word ou PDF. Este projeto é composto por uma aplicação web frontend e uma API backend.

## Funcionalidades

- Criação automática de currículos
- Download dos currículos em formato Word ou PDF
- Interface amigável e fácil de usar

## Estrutura do Projeto

- `api/`: Contém a API backend desenvolvida em Flask para gerar os currículos.
- `app.js`: Arquivo JavaScript principal para a aplicação frontend.
- `index.html`: Página HTML principal da aplicação frontend.
- `style.css`: Arquivo CSS para estilização da aplicação frontend.
- `requirements.txt`: Lista de dependências Python necessárias para rodar a API.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/)
- [Git](https://git-scm.com/)

## Instalação

1. Clone o repositório:

   ```bash
   git clone git@github.com:lanroo/generate-curriculum.git
   cd generate-curriculum

## Configure o ambiente virtual para a API backend:
  `cd api
  python -m venv myenv
  source myenv/bin/activate  # No Windows, use ``myenv\Scripts\activate``
  pip install -r requirements.txt`

## Inicie a API backend:
  `flask run`

## Abra outro terminal e inicie a aplicação frontend:
  `cd ..`
# Se necessário, instale um servidor web simples para servir o HTML, como o `http-server`:
  `npm install -g http-server`
  `http-server`

## Uso

1. Acesse a aplicação web em seu navegador através do endereço fornecido pelo `http-server`.
2. Preencha os dados necessários no formulário da aplicação.
3. Clique em "Gerar Currículo" para criar e baixar seu currículo em formato Word ou PDF.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.


