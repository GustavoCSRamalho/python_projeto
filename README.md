# Projeto
> Foram resolvidos os exercicios presentes no PDF.

# Documentação:
> Segue o link do swagger com a documentação das rotas.
* https://app.swaggerhub.com/apis-docs/milenarx/pyhton_projeto/1.0.0

# Exercicio 1:
## 1.1
> Existe alguns problemas no código.
* Código duplicado.
* Utilização de variaveis diretamente ao invez de um objeto.
* Leitura da pagina web dentro de um método que deveria retornar o cep
em json ou xml.
* Formatação do resultado junto com a leitura dos dados na pagina web.
* Varios if's com retorno em diferentes situações, sendo que poderia
ser substituido por um método que realizase a logica e retornase
apenas o resultado solicitado.
* Tratamento de erro diretamente no EXCEPT, oque pode causar codigo
duplicado quando o mesmo erro aconteçer em outro lugar.

## 1.2
* Não é facil escrever um teste para o código mostrado no exercicio 1, 
    pois este método está fazendo mais de um serviço. Para que fosse possível
    realizar os testes, o código deveria ser quebrado em outros arquivos,cada
    um possuindo um determinado objetivo e realizando apenas a tarefa descrita
    em seu nome.

    Exemplo:
        Um método que pega dados de um banco de dados não deve possuir regra de 
        negocio no mesmo código
## 1.3
> O código refatorado se encontra na pasta 
* resposta_codigo_refatorado
# 2
## Resposta
* Uma das abordagens seria criar um map com o valor N dado como entrada ao metodo
    e o seu resultado pelo fibonacci, depois adicionar uma logica depois do if para verificar
    se o valor ja existe, se existir então ele retorna o resultado ja existente em fibonacci,
    caso contrario ele entra no ultimo return.
# 3
## 3.1
* O problema destá implementação é que ocorre varias chamadas para obter 
    o valor da variavel execution na sessão do DB sem ao menos ter sido modificada,
    fazendo com que uma chamada possa sobreescrever o valor da outra por conta
    da falta de sincronização no acesso dessa variavel.
    Isso ocorre porque não há um controlar que defina de quem é a vez de obter
    a referência da variavel para modificar ou para informar que a variavel 
    está sendo acessada por outro método, e assim que este método terminar
    a referência será passada para outro.
## 3.2
* Podemos syncronizar esse método para que o a leitura e modficação
    das variaveis sejam acessadas de forma sincrona, ou seja, que uma tenha acesso a referencia
    de cada vez sem que uma sobreescreva o resultado da outra.
# Exercicio 4:
## 4.1
* Eu começaria pelo levantamento de requisitos funcionais e não funcionais 
    da aplicação,depois iria para o banco de dados, fazendo a modelagem pelo Draw.io,
    em seguida eu documentaria como seria as entradas das rotas da api com 
    o swagger,prepararia um ambiente docker e começaria a desenvolver a 
    aplicação com python, utilizando o flask para fazer as rotas, json para
    enviar os valores para a tela ou xml, tudo depende dos requisitos,
    peewee para gerar um banco de dados local, fazer consultas e tambem para ja adicionar valores
    para que quando a aplicação suba, ela ja tenha uma base carregada com dados para que 
    faça a api funcionar sem a necessidade de colocar os dados um por um.

## 4.2
> Para visualizar os dados no banco de dados, foi utilizado o sqlitebrowser no ubuntu, para instalar use o comando abaixo:
* sudo apt-get install sqlitebrowser
* Para usar, digite sqlitebrowser e abra o arquivo com a extensão .db
> Antes de executar o projeto instale esses frameworks se não tiver :
* flask
* peewee 
> Para executar o projeto, execute o comando dentro da pasta miniProjeto.
* python run.py
> Foi utilizado o python 2.7 para a realização do projeto.

## 4.3
* Uma maneira de documentar a api seria utilizando o swagger, nele como
    você consegue demostrar o nome da rota, os parametros necessarios para envio,
    metodo de envio, corpo, informações no header como o token para a autenticação.
> Exemplo :
* https://app.swaggerhub.com/apis-docs/milenarx/pyhton_projeto/1.0.0