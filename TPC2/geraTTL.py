import json

f = open("musica.json")
bd = json.load(f)
f.close()

def prettify(a):
    return a.replace(" ", "_") if a else "NULL"

print("""@prefix : <http://rpcw.di.uminho.pt/2024/musica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/musica/> .

<http://rpcw.di.uminho.pt/2024/musica> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/musica/ensinaInstrumento
:ensinaInstrumento rdf:type owl:ObjectProperty ,
                            owl:FunctionalProperty ;
                   rdfs:domain :Curso ;
                   rdfs:range :Instrumento .


###  http://rpcw.di.uminho.pt/2024/musica/inscritoEmCurso
:inscritoEmCurso rdf:type owl:ObjectProperty ,
                          owl:FunctionalProperty ;
                 rdfs:domain :Aluno ;
                 rdfs:range :Curso .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/musica#AlunoInstrumento
:AlunoInstrumento rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Aluno ;
                  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/AlunoAnoCurso
:AlunoAnoCurso rdf:type owl:DatatypeProperty ;
               rdfs:domain :Aluno ;
               rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/musica/AlunoDataNascimento
:AlunoDataNascimento rdf:type owl:DatatypeProperty ;
                     rdfs:domain :Aluno ;
                     rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/AlunoId
:AlunoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Aluno ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/AlunoNome
:AlunoNome rdf:type owl:DatatypeProperty ;
           rdfs:domain :Aluno ;
           rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/CursoDesignacao
:CursoDesignacao rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Curso ;
                 rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/CursoDuracao
:CursoDuracao rdf:type owl:DatatypeProperty ;
              rdfs:domain :Curso ;
              rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/musica/CursoId
:CursoId rdf:type owl:DatatypeProperty ;
         rdfs:domain :Curso ;
         rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/InstrumentoId
:InstrumentoId rdf:type owl:DatatypeProperty ;
               rdfs:domain :Instrumento ;
               rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/musica/InstrumentoNome
:InstrumentoNome rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Instrumento ;
                 rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/musica/Aluno
:Aluno rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/musica/Curso
:Curso rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/musica/Instrumento
:Instrumento rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################
""")

for aluno in bd["alunos"]:
    print(f"""
###  http://rpcw.di.uminho.pt/2024/musica#{aluno["id"]}
:{aluno["id"]} rdf:type owl:NamedIndividual ,
                :Aluno ;
       :inscritoEmCurso :{aluno["curso"]} ;
       :AlunoInstrumento "{aluno["instrumento"]}" ;
       :AlunoAnoCurso "{aluno["anoCurso"]}"^^xsd:int ;
       :AlunoDataNascimento "{aluno["dataNasc"]}" ;
       :AlunoId "{aluno["id"]}" ;
       :AlunoNome "{aluno["nome"]}" .
""")


for curso in bd["cursos"]:
    print(f"""
###  http://rpcw.di.uminho.pt/2024/musica#{curso["id"]}
:{curso["id"]} rdf:type owl:NamedIndividual ,
              :Curso ;
     :ensinaInstrumento :{curso["instrumento"]["id"]} ;
     :CursoDesignacao "{curso["designacao"]}" ;
     :CursoDuracao "{curso["duracao"]}"^^xsd:int ;
     :CursoId "{curso["id"]}" .
""")


for instrumento in bd["instrumentos"]:
    print(f"""
###  http://rpcw.di.uminho.pt/2024/musica#{instrumento["id"]}
:{instrumento["id"]} rdf:type owl:NamedIndividual ,
             :Instrumento ;
    :InstrumentoId "{instrumento["id"]}" ;
    :InstrumentoNome "{instrumento["#text"]}" .
""")

print("""
#################################################################
#    General axioms
#################################################################

[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :Aluno
                :Curso
                :Instrumento
              )
] .


###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi

""")