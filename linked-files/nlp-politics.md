# NLP and Politics - Research Ideas

* Collect large and varied sample of political writings. Attempt to get a wide variety, approximate representativity is desirable, but perfect representativity is not required for clustering.
* Identify list of political topics, striving for representativity of all possible ideologies.
* For each individual (or for each work), create a vector consisting of attitudes toward the above topics (and normalize?).
* Perform PCA on the matrix of attitude vectors (Monte Carlo?).
* Cluster of principal components.
* Interpret principal components and clusters.
* Examine predictions and test unseen writings.
* Possible extension:
* Train classifier on document (or thinker) tokens and identify most indicative words / n-grams.
* RUN SIMPLE VARIANT FIRSTː k ideologies and thinkers, n questions, PCA and visualization
* 1) select ideologies
* 2) select thinkers
* 3) select questions
* 4) create matrix
* 5) perform PCA
* 6) create visualization
* how to 'Monte Carlo' PCA?

* -> give range (a,b) or even distribution, for each stance (entry in the ideology matrix), then sample from ramges/distributions
* -> how to aggregate varying results? simple average?
* -> topological anaylsis to determine invariant relationships?

* Read up onːopinion mining
* Read up onːstance detection
* Read up onːquestion answering
* Read up onːknowledge discovery
* Read up onːsemantic relations
* Read up onːdimensionality reduction
* Read up onːTDA
* Read up onːclustering
* Read up onːvisualization

## Idea Space Modelling

* Elevator Pitch: My work is distinct from previous work in a few ways: ||| it uses high-quality inputs and political writings in addition to social media (hopefully making the model more grounded in the deep theoretical issues of politics, not just shallow perceptions) ||| it does not assume a spectrum; rather it uses unsupervised learning to identify clusters and linkages between ideologies ||| it allows for a robust measuring of ideological similarity that is as general as possible, allowing a wide range of comparisons, even potentially across time, language, and culture, because the method is built on attitudes toward nearly-universal ideas and concepts, rather than toward specific people and organizations ||| it brings together several fairly technical NLP/IR/TM methods that have not been used for this before: topic extraction, emotion analysis, opinion mining ||| it combines the above methods with other more common methods, such as clustering, lexical analysis (i.e. tf-idf) ||| it can take advantage of a large and relatively underutilized body of text resources ||| it has the scope for other advanced techniques: topology, measure theory, advanced matrix analysis & linear algebra, etc. ||| it answers intrinsically important and interesting questions, questions of interest to a broad audience (in addition to finer points interesting to a computational linguist) ||| while every algorithm necessarily has assumptions baked into it, this will make explicit assumptions in a way that human annotation would mke impossible
* Interesting method to build on (but automate): Globalization and the transformation of the national political space: Six European countries compared

* Wie realitätsgetreu sind die zwei verbreiteten politischen Spektren? a) links-rechts b) Political Kompass c) Hufeisentheorie

* -> Black boxes aufmachen

* -> wie Artikel über Rechtsextremist, aber mit zusätzlicher Frage: wie modellieren wir ihre Beziehung zu anderen?

* Wie viele Hauptkomponente gibt es in der Ideologie?
* Wie interpräterieren wir sie und was bedeuten sie?
* Welche und wie viele politische Cluster gibt es, und wie beziehen sie sich zueinander?
* D.h. welche politische Netzwerke bestehen?
* Wie robust ist diese Analyse?
* a) Wie verändern sich die Ergebnisse, wenn Störtermine eingeführt werden, bzw. wie groß dürfen die Störterme sein, ohne die Cluster und die Hauptkomponente grundsätzlich zu verändern?
* b) Wie viel Text braucht man für eine zuverlässige ideologische Einbettung (oder Klassifikation)?
* Was enthalten die Ideologie-Vektoren?
* a) emotion in Bezug auf t1,...tk
* ==> topic recognition (oder einfache regex) + dependency parsing + emotion analysis
* b) tf-idf von wichtigsten (prädiktivsten?) n-gramme
* Wie verändern sich die Cluster im Laufe der Zeit?
* Wie variieren die Cluster über Landes-, Sprach- und Kulturgrenzen?
* Welche Cluster gibt es in Bezug auf nur eine oder wenige Dimensionen?
* a) ==> Transformation in weniger-dimensionale Räume
* b) ==> Einbettung kleinerer Stichproben
* Lassen sich die Ergebnisse mit Wikipedia-Daten bestätigen?
* a) Einflüsse und Quelltext um Einflüsse herum
* b) Artikel zu den Ideologien und Denker (nichtautomatisch?)
* Wie repräsentieren wir ideologische Ähnlichkeit und relative Position?
* Wie können wir ideologische Ähnlichkeit veranschaulichen?
* a) In Bezug auf Grundmenge bekannter und einflussreicher Denker - entweder k nächste Denker (eventuell aus Grundliste) oder Ähnlichkeit mit vorbestimmter Liste Denker
* b) Hauptkomponente verwenden
* Wie können wir die Methoden flexibler gestalten, damit z.B. neue (spezifischere, vergänglichere) Themen berücksichtigt werden können?
