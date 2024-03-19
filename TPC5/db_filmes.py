import itertools
import requests
import json
import sys

# Define the DBpedia SPARQL endpoint
sparql_endpoint = "http://dbpedia.org/sparql"

# Define the headers
headers = {
    "Accept": "application/sparql-results+json"
}


def run_query(query, attrs):

    # Define the parameters
    params = {
        "query": query,
        "format": "json"
    }

    # Send the SPARQL query using requests
    response = requests.get(sparql_endpoint, params=params, headers=headers)

    # Check if the request was successful
    if response.status_code // 100 == 2:
        results = response.json()
        # Save the results
        output = []
        for result in results["results"]["bindings"]:
            output.append({attr: result[attr]["value"] for attr in attrs})
        
        return output
    else:
        print("\n--------------------------------------------\n")
        print(query)
        raise Exception(f"Error: {response.status_code}")

def run_full_query(query, attrs):
    n = 0
    ans = []
    while len(x := run_query(f"{query} limit 10000 offset {n}", attrs)) != 0:
        sys.stdout.write(f"\rCollected {n + len(x)} entries...")
        sys.stdout.flush()
        n += len(x)
        ans.append(x)

    print()
    return list(itertools.chain.from_iterable(ans))


def get_people(attr):
    query = f"""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo:    <http://dbpedia.org/ontology/>

SELECT ?movie ?name
WHERE {{
    ?movie a dbo:Film ;
      ({attr}/rdfs:label) ?name
    FILTER (LANG(?name) = 'en')
}}
"""
    people = {}
    for p in run_full_query(query, ["movie", "name"]):
        if p["movie"] not in people:
            people[p["movie"]] = []
        people[p["movie"]].append(p["name"])
    return people


query = """
PREFIX dbo:    <http://dbpedia.org/ontology/>
PREFIX dbp:    <http://dbpedia.org/property/>

select ?uri ?name ?runtime where {
  ?uri a dbo:Film ;
    dbp:name ?name ;
    dbp:runtime ?runtime
  FILTER (LANG(?name) = 'en')
}
"""
films = run_full_query(query, ["uri", "name", "runtime"])
print(f"{len(films)} movies collected!")

writers = get_people("dbo:writer")
directors = get_people("dbp:director")
producers = get_people("dbo:producer")
composers = get_people("dbp:music")
actors = get_people("dbo:starring")

print("Consolidating queries...")

for i, f in enumerate(films):
    f["runtime"] = f["runtime"]
    f["writers"] = writers.get(f["uri"],[])
    f["directors"] = directors.get(f["uri"],[])
    f["producers"] = producers.get(f["uri"],[])
    f["composers"] = composers.get(f["uri"],[])
    f["actors"] = actors.get(f["uri"],[])

print("Writing to file...")
f = open("filmes.json", "w")
json.dump(films, f, indent=4)
f.close()
print("Done!")