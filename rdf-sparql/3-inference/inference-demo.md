### Very brief demonstration of inference

#### Frame

- We have a sample of Garzoni data, expressed according to a small ontology. 

- Some facts are there, but we would like to infer new facts, i.e. construct new triples.

- We will do so using 2 methods: ontology-based and rule-based reasoning

  

#### What we have

- ontology file: garzoni.owl

- small data file: sample-contract.nt

- inference engine: Inference Jena API (Apache)

  

#### Exercise: Looking at the data

Given the ontology and the content of sample-contract.nt

- Question 1: What can be inferred via RDFS?

    *hint*: look at the resource instance of dh101-owl:Contract

- Question 1: What can be inferred via OWL?

    *hint*: look at ‘master1’ and ‘other1’ resources

Warning: URIs names do not necessarily reflect their class.



#### Quick insight into Jena's rule syntax  

- rule between brackets `[ ]`
- 2 parts: 
  - left-hand side: premises
  - right-hand side: conclusions
- parts separated by arrow `->` (indicates chaining direction)
- triple pattern : `(node, node, node)`



Example: 

```
[rule1: (?person onto:teaches ?class) -> (?person a onto:Teacher) ]
```



More details: https://jena.apache.org/documentation/inference/index.html#rules

#### Exercise on rules

As a start, a rule to infer a professional relationship between 2 entities of a contract:

```
[
	rule1 professionRelation:
	(?a fdh-owl:role fdh-data:ApprenticeRole),
	(?m fdh-owl:role fdh-data:MasterRole)
	...
	-> (?m fdh-owl:masterOf ?a)
]
```

Try to write a set of rules to infer the following:

- professional relationships between persons:

 dh-owl:masterOf, dh-owl:guarantorOf

(based on the knowledge that a master has ‘hired’ an apprentice through a contract)

- social relationships: foaf:knows

(based on the knowledge that people who work together know each other)



**Using the inference engine for automatic reasoning using RDFS and OWL**

- open a terminal
- go to the directory where inference.jar is
- execute java -jar inference.jar
- load garzoni.owl as ontology file (give full path)
- load sample-contract.nt as data file (give full path)
- execute RDFS reasoning and compare results with original data
- execute OWL reasoning and compare results with original data

