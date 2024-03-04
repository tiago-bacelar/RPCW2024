## TPC3

Tal como nos tpcs anteriores, os dados foram extraídos do ficheiro json, convertidos para formato TTL através de um script python e inseridos num repositório graphdb.

A primeira query SPARQL pedida consistia em obter as cidades de determinado distrito. Braga foi usado como exemplo. A resolução consiste em procurar os objetos que se relacionam com "Braga" através do predicado :CidadeDistrito, e apresentar o seu nome através do predicado :CidadeNome.

A segunda query pedia a distribuição de cidades por distrito. Para isto foi utilizadas as mesmas restrições que na query anterior, mas foi adicionado um GROUP BY e um COUNT, para agrupar os resultados e contar por distrito.

A terceira query era a mais interessante, pedia que se listasse todas as cidades que é possivel alcançar começando em cidades do distrito do Porto. Para o conseguir precisamos de utilizar os operadores de caminho de SPARQL. Os que nos são de maior uso são /, que permite compôr dois predicados, ^, que permite inverter um predicado, e \*, que aplica um predicado 0 ou mais vezes. A query começa por obter as 4 cidades do distrito do Porto e, seguidamente, é usado o predicado (^:LigacaoOrigem / :LigacaoDestino)\* para descobrir todas as cidades alcançáveis a partir das iniciais. Por fim, são selecionados os nomes destas cidades. Deve ser utilizada a cláusula DISTINCT para eliminar cidades alcançáveis a partir de várias cidades iniciais. O resultado é uma tabela contendo os nomes de 100 cidades.

A última query era relativamente mais simples, pedia a lista de cidades acima de X habitantes. Como exemplo foi utilizado o valor de 500000 habitantes. Para resolver esta query é necessária a cláusula FILTER, para eliminar cidades que não cumpram o limite de população. O resto da query é trivial, e parecida com as anteriores.