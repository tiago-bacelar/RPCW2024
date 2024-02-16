import json

f = open("plantas.json")
bd = json.load(f)
f.close()

def prettify(a):
    return a.replace(" ", "_") if a else "NULL"

print("""@prefix : <http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4/> .

<http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#emRua
:emRua rdf:type owl:ObjectProperty ;
       rdfs:domain :Planta ;
       rdfs:range :Rua .

      
###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#estado
:estado rdf:type owl:ObjectProperty ;
        rdfs:domain :Planta ;
        rdfs:range :Estado .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#temCaldeira
:temCaldeira rdf:type owl:ObjectProperty ;
             rdfs:domain :Planta ;
             rdfs:range :Maybe .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#temTutor
:temTutor rdf:type owl:ObjectProperty ;
          rdfs:domain :Planta ;
          rdfs:range :Maybe .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#tipo
:tipo rdf:type owl:ObjectProperty ;
      rdfs:domain :Planta ;
      rdfs:range :Implantação .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Código_de_rua
:Código_de_rua rdf:type owl:DatatypeProperty ;
               rdfs:domain :Rua ;
               rdfs:range xsd:long .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Data_de_Plantação
:Data_de_Plantação rdf:type owl:DatatypeProperty ;
                   rdfs:domain :Planta ;
                   rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Data_de_actualização
:Data_de_actualização rdf:type owl:DatatypeProperty ;
                      rdfs:domain :Planta ;
                      rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Espécie
:Espécie rdf:type owl:DatatypeProperty ;
         rdfs:domain :Planta ;
         rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Freguesia
:Freguesia rdf:type owl:DatatypeProperty ;
           rdfs:domain :Rua ;
           rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Gestor
:Gestor rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Id
:Id rdf:type owl:DatatypeProperty ;
    rdfs:domain :Planta ;
    rdfs:range xsd:long .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Local
:Local rdf:type owl:DatatypeProperty ;
       rdfs:domain :Rua ;
       rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Nome_Científico
:Nome_Científico rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Planta ;
                 rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Número_de_Registo
:Número_de_Registo rdf:type owl:DatatypeProperty ;
                   rdfs:domain :Planta ;
                   rdfs:range xsd:long .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Número_de_intervenções
:Número_de_intervenções rdf:type owl:DatatypeProperty ;
                        rdfs:domain :Planta ;
                        rdfs:range xsd:int .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Origem
:Origem rdf:type owl:DatatypeProperty ;
        rdfs:domain :Planta ;
        rdfs:range xsd:string .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Rua
:Rua rdf:type owl:DatatypeProperty ;
     rdfs:domain :Rua ;
     rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Estado
:Estado rdf:type owl:Class .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Implantação
:Implantação rdf:type owl:Class .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Maybe
:Maybe rdf:type owl:Class .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Planta
:Planta rdf:type owl:Class .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Rua
:Rua rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Adulto
:Adulto rdf:type owl:NamedIndividual ,
                 :Estado .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Arruamento
:Arruamento rdf:type owl:NamedIndividual ,
                     :Implantação .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Espaço_Verde
:Espaço_Verde rdf:type owl:NamedIndividual ,
                       :Implantação .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Jovem
:Jovem rdf:type owl:NamedIndividual ,
                :Estado .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#NULL
:NULL rdf:type owl:NamedIndividual ,
               :Estado ,
               :Implantação ,
               :Maybe .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Não
:Não rdf:type owl:NamedIndividual ,
              :Maybe .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Outro
:Outro rdf:type owl:NamedIndividual ,
                :Estado ,
                :Implantação .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Sim
:Sim rdf:type owl:NamedIndividual ,
              :Maybe .


###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#Velho
:Velho rdf:type owl:NamedIndividual ,
                :Estado .
""")

ruas = set()

for planta in bd:
    id = planta["Id"]
    codigo = planta['Código de rua'] if planta['Código de rua'] else 0
    if codigo not in ruas:
        ruas.add(codigo)
        print(f"""
###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#{codigo}
<http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#{codigo}> rdf:type owl:NamedIndividual ,
                          :Rua ;
                 :Código_de_rua "{codigo}"^^xsd:long ;
                 :Freguesia "{planta["Freguesia"]}" ;
                 :Local "{planta["Local"]}" ;
                 :Rua "{planta["Rua"].replace('"','')}" .
""")
    caldeira = prettify(planta['Caldeira'])
    tutor = prettify(planta['Tutor'])
    implantacao = prettify(planta['Implantação'])
    estado = prettify(planta['Estado'])

    print(f"""
###  http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#{id}
<http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#{id}> rdf:type owl:NamedIndividual ,
                                                                                             :Planta ;
                                                                                    :emRua <http://www.semanticweb.org/bacelar/ontologies/2024/1/untitled-ontology-4#{codigo}> ; ;
                                                                                    :estado :{estado} ;
                                                                                    :temCaldeira :{caldeira} ;
                                                                                    :temTutor :{tutor} ;
                                                                                    :tipo :{implantacao} ;
                                                                                    :Data_de_Plantação "{planta['Data de Plantação']}" ;
                                                                                    :Data_de_actualização "{planta['Data de actualização']}" ;
                                                                                    :Espécie "{planta['Espécie']}" ;
                                                                                    :Gestor "{planta['Gestor']}" ;
                                                                                    :Id "{id}"^^xsd:long ;
                                                                                    :Nome_Científico "{planta['Nome Científico']}" ;
                                                                                    :Número_de_Registo "3"^^xsd:long ;
                                                                                    :Número_de_intervenções "6"^^xsd:int ;
                                                                                    :Origem "{planta['Origem']}" .
""")

print("###  Generated by the OWL API (version 4.5.26.2023-07-17T20:34:13Z) https://github.com/owlcs/owlapi")