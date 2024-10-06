from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")



text='''As I wandered through the dimly lit corridors of Hogwarts, I stumbled upon a hidden passageway that led me to a mysterious portrait of Salazar Slytherin. The painting depicted the cunning founder of Slytherin House, his piercing eyes seeming to follow me as I moved. I felt an eerie chill run down my spine as I gazed into his enigmatic smile.

Suddenly, the portrait began to speak to me in a low, raspy voice, "Ah, a curious student, I see. Very well, I shall grant you a glimpse into the secrets of the ancient magic that lies within these castle walls." With a flick of his wand, the portrait conjured up a swirling vortex of misty blue light, beckoning me to step forward.'''

sentences = text.split('.')

# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)

