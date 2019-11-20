## Exploring some linked data set using SPARQL

| **Dataset**       | **SPARQL endpoint**                                          | **Model/ontology**                                           |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| DBpedia           | http://dbpedia.org/sparql                                    | [Collaborative ontology](http://mappings.dbpedia.org/server/ontology/classes/) |
| Talk of Europe    | http://linkedpolitics.ops.few.vu.nl/yasgui/index.html        | [InfoLink1](http://linkedpolitics.ops.few.vu.nl/web/html/home.html) (look at query examples at the bottom) [InfoLink2](http://www.talkofeurope.eu/) [Ontology](http://linkedpolitics.ops.few.vu.nl/web/html/datamodel.html) |
| Persée            | http://data.persee.fr/explorer/                              | http://data.persee.fr/explorer/schemas-de-donnees/           |
| Le Temps Archives | http://iccluster035.iccluster.epfl.ch:8899/sparql GRAPH: http://localhost:8080/letemps-data | see PDF in same folder                                       |



**Write some queries:**



**DBpedia:**

- Find all the occupations of Jacques Chirac. (hint: property is *dbo:office*)
- How many ‘Politician’ have been to ‘Harvard University’?



**Le Temps Archives**

Find all the occupations of Jacques Chirac.



**Talk of Europe**

- How many French speeches mentions “Jacques Chirac”.
- Who were the speakers?



**Persée:**

What are the titles of the documents written by Pierre Rosanvallon?