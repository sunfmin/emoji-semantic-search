from sentence_transformers import SentenceTransformer
sentences = ['The emoji 🥇 is about 1st place medal.', 'The emoji 🥈 is about 2nd place medal.']

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
