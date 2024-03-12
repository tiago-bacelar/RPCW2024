from flask import Flask,render_template,url_for
from datetime import datetime
import requests

app = Flask(__name__)
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

def get_date():
    date = datetime.now()
    return date.isoformat()

def query_graphdb(query):
    result = None
    error = ""
    try:
        response = requests.get(graphdb_endpoint, params={"query":query},headers={"Accept":"application/sparql-results+json"})
        if response.status_code == 200:
            result = response.json()['results']['bindings']
        else:
            error = f"Error response ({response.status_code}) from graphdb"
    except Exception as e:
        error = f"Error requesting data: {e}"
    return (result, error)

def render_query(template, query, treatResult):
    result, error = query_graphdb(query)
    if result:
        if treatResult:
            result = treatResult(result)
        return render_template(template, data={"date": get_date(), "query": result})
    else:
        return render_template('erro.html', data={"date": get_date(), "message": error})


@app.route('/')
def index():
    return render_template('index.html', data={"date": get_date()})

def treat_elem(elem):
    elem["id"] = elem["elem"]["value"].split("#")[1]
    if "group" in elem:
        elem["group_id"] = elem["group"]["value"].split("#")[1]
        elem["group_name"] = elem.get("group_name", f'Group {elem.get("group_num",{"value":"?"})["value"]}')
    return elem

@app.route('/elementos')
def elementos():
    query = """
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?elem ?num ?sim ?nome ?group ?group_name ?group_num where {
    ?elem a :Element ;
          :name ?nome ;
          :symbol ?sim ;
          :atomicNumber ?num ;
          :group ?group .
    ?group :name ?group_name ;
           :number ?group_num .

} order by (?num)
"""
    return render_query('elementos.html', query, lambda l: map(treat_elem, l))

def treat_group(g):
    g["id"] = g["group"]["value"].split("#")[1]
    g["nome"] = g.get("nome", {'type': 'literal', 'value': f'Group {g.get("num", {"value": "?"})["value"]}'})
    g["num"] = g.get("num", {'type': 'literal', 'value': '?'})
    return g

@app.route('/grupos')
def grupos():
    query = """
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?group ?nome ?num where {
    ?group a :Group ;
    optional { ?group :name ?nome  . }
    optional { ?group :number ?num . }
} order by (?num)
"""
    return render_query('grupos.html', query, lambda l: map(treat_group, l))

@app.route('/elemento/<string:e>')
def elemento(e):
    query = f"""
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (:{e} as ?elem) ?num ?mass ?sim ?nome ?color ?period ?group ?group_name ?group_num where {{
    :{e} a :Element ;
          :name ?nome ;
          :symbol ?sim ;
          :atomicNumber ?num ;
          :atomicWeight ?mass ;
          :color ?color ;
          (:period/:number) ?period ;
          :group ?group .
    ?group :name ?group_name ;
           :number ?group_num .
}}
"""
    return render_query('elemento.html', query, lambda l: treat_elem(l[0]))

@app.route('/grupo/<string:g>')
def grupo(g):
    query1 = f"""
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (:{g} as ?group) ?nome ?num where {{
    :{g} a :Group
    optional {{ :{g} :name ?nome }}
    optional {{ :{g} :number ?num }}
}}
"""
    query2 = f"""
PREFIX : <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?elem ?nome ?num ?sim where {{
    ?elem :group :{g} ;
          :name ?nome ;
          :symbol ?sim ;
          :atomicNumber ?num .
}} order by (?num)
"""
    result, error = query_graphdb(query1)
    if not result:
        return render_template('erro.html', data={"date": get_date(), "message": error})
    
    group_name = treat_group(result[0])["nome"]["value"]
    return render_query('grupo.html', query2, lambda l: { "nome": group_name, "elementos": map(lambda e: treat_elem(e),l) })


if __name__ == "__main__":
    app.run(debug=True)