 ### 🐍 Desafio python

Este projeto foi feito a partir dos requisitos de um desafio django(tomei algumas liberdades criativas com os nomes), este sistema entrega uma api de gestão de usuários, produtos e pedidos, tudo feito com django restframework e documentado via swagger.

link do diagrama uml do projeto:https://lucid.app/lucidchart/225fdc2f-169b-4e37-bce6-753d2dc50640/edit?viewport_loc=-2079%2C-414%2C1623%2C793%2C0_0&invitationId=inv_7417fca3-c7de-430f-8301-e774e686afd3



### 📋 Pré-requisitos

Para a execução deste projeto é necessária a instalação do python 3.12.3.



## 🛠️ Passos para executar o projeto


* 1. Iniciar uma máquina virtual python utilizando o comando: python -m venv env
* 2. Ativar a máquina virtual com o comando para windows: .\env\Scripts\activate ou para linux source env/bin/activate
* 3. Instalar as dependências declaradas no requirements.txt via o comando: pip install -r requirements.txt
* 4. Executar as migrações com o comando: python manage.py migrate
* 5. Criar um super usuario para acessar o django admin com o comando: python manage.py createsuperuser    
* 6. Executar o servidor de desenvolvimento com o comando: python manage.py runserver
* 7. acessar as documentações que mostram como autenticar um usuario e todas as outras requisições no modelo swagger ou redoc nas urls http://127.0.0.1:8000/swagger/ e http://127.0.0.1:8000/redoc/ respectivamente.
## ✒️ Autor

* **Rommel Bonfim** -  [Rommel Bonfim](https://github.com/rommelbonfim)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](https://github.com/rommelbonfim/Mercado/blob/main/LICENSE) para detalhes.
