# Semantic-and-Collaborative-FIltering-Recommendation
In this project, I:
• Led a team of 4 to develop a book recommendation and semantic search application in Python
• Developed a semantic retrieval and a genre detection algorithm that  **doubled** system retrieval speeds
• Perform web crawling, and utilized **cloud databases** like MongoDB as datastore

For the demo, click [here](https://clipchamp.com/watch/9gKmng3Q23W). For the details click [here](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/CZ4125%20Data%20Products%20Report.pdf).

Additional details:

The semantic retrieval algorithm I developed was extremely efficient because it performs matrix multiplication on genre tags instead of the book documents, dramatically cutting down on the number of comparisons made. Yet, it was accurate because it utilizes contextualized embeddings from a specialised BERT model, Phrase-BERT, that allows lexically dissimilar (and semantically similar) phrases to be matched (e.g. "werewolf" is semantically similar to "historical fantasy" but lexically dissimilar). This algorithm also doubled as a genre detection algorithm which is an added user-friendly feature.

Contents:
  1. [Semantic search and collaborative filtering pipeline functions](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/pipeline.py)
  2. [Semantic search and CF example use](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/Application.ipynb)
  3. [Development and optimization of semantic search algorithm](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/SemanticSearch2%20-%20breaking%20down%20query.ipynb)
  4. [Development and optimization of collaborative filtering ofalgorithm](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/Recommenders1%20-%20Compare%20Recommender%20Models.ipynb)
  5. [Collaborative Filtering and popularity recommendation models](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/models.py)
  6. [Recommender Evaluation funtions](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/evaluation.py)


I also implemented various other algorithms which did not end in the final application: [Product Quantization](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/Quantization1%20-%20quantization%20of%20summaries.ipynb), [Priority Queue](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/SemanticSearch0%20-%20priority%20queue.ipynb), [keyword extraction on reviews](https://github.com/chingfhen/Semantic-and-Collaborative-FIltering-Recommendation/blob/main/Mongo3%20-%20load%20keywords%20to%20mongo%20.ipynb)

