## TPC2

O objetivo do tpc era analisar uma base de dados de uma escola de música em formato JSON e converter os dados para uma ontologia, no formato Turtle Syntax. A conversão dos dados através de um script python, e a visualização da ontologia resultante através do programa graphdb.

As classes relevantes para a ontologia são Aluno, Curso e Instrumento. Para a maioria dos dados foram utilizadas data properties, com os ranges respetivos. As únicas object properties utilizadas foram "ensinaInstrumento", entre Curso e Instrumento, e inscritoEmCurso, entre Aluno e Curso.

Foi escrito um script python que escreve em formato TTL um cabeçalho constante, que corresponde às definições destas classes, data properties e object properties, e de seguida popula a ontologia com os indivíduos lidos do input JSON e as relações entre eles. O TTL resultante foi testado no Protégé para garantir a correção da sua sintaxe.

Por último, a ontologia foi visualizada usando graphdb.