## TPC1

O objetivo do tpc era analisar uma base de dados de plantas em formato JSON e converter os dados para uma ontologia, no formato Turtle Syntax. A visualização dos dados foi feita usada o programa Protégé, e a conversão dos dados através de um script python.

Para a maioria dos dados foram utilizadas data properties, com os ranges respetivos. Para as propriedades Estado, Caldeira, Tutor e Implantação foram utilizadas object properties, uma vez que os valores destas propriedades são bem conhecidos. Estes valores conhecidos foram inseridos à mão no script de python. Para as propriedades Código de rua, Rua, Local e Freguesia foi usada uma data property, que tira vantagem do facto de ser frequentemente usada a mesma rua (com as mesmas propriedades) em várias plantas.

Isso deixa-nos com as seguintes Classes: a referida Rua, Planta (a representação de uma planta com as data properties referidas anteriormente e uma object property de uma Rua), Estado (com as instancias Adulto, Jovem, Velho, Outro e NULL), Implantação (com as instâncias Arruamento, Espaço_Verde, Outro e NULL) e Maybe (com as instâncias Sim, Não e NULL. Esta Classe serve tanto para a object property temCaldeira como para temTutor).

Assim, o script python limita-se a escrever um cabeçalho constante, que corresponde às definições destas classes, data properties e object properties. Depois, o ficheiro JSON é lido entrada por entrada. Para cada planta, é escrita uma nova instância da classe Planta, e também uma instância de Rua caso a rua da planta não exista ainda.