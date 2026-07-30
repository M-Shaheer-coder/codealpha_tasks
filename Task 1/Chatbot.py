from tkinter import *
from tkinter import messagebox
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------- FAQ DATABASE ----------------------

questions = [
    "What is AI?",
    "What is Python?",
    "Who developed Python?",
    "What is Machine Learning?",
    "What is NLP?",
    "What is ChatGPT?",
    "What is Programming?",
    "What is Computer Science?"
]

answers = [
    "AI stands for Artificial Intelligence.",
    "Python is a high-level programming language.",
    "Python was developed by Guido van Rossum.",
    "Machine Learning is a branch of Artificial Intelligence.",
    "NLP stands for Natural Language Processing.",
    "ChatGPT is an AI chatbot developed by OpenAI.",
    "Programming is the process of writing computer programs.",
    "Computer Science is the study of computers and algorithms."
]

# ---------------------- PREPROCESS FUNCTION ----------------------

stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = text.lower()

    words = word_tokenize(text)

    cleaned = []

    for word in words:

        if word not in string.punctuation:

            if word not in stop_words:

                cleaned.append(word)

    return " ".join(cleaned)

# ---------------------- CHATBOT FUNCTION ----------------------

def chatbot():

    user_question = question_box.get()

    if user_question == "":

        messagebox.showwarning("Warning", "Please enter a question.")

        return

    processed_questions = []

    for q in questions:

        processed_questions.append(preprocess(q))

    processed_user = preprocess(user_question)

    processed_questions.append(processed_user)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(processed_questions)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    best_match = similarity.argmax()

    confidence = similarity[0][best_match]

    answer_box.delete("1.0", END)

    if confidence > 0.20:

        answer_box.insert(END, answers[best_match])

    else:

        answer_box.insert(END, "Sorry, I couldn't understand your question.")

# ---------------------- GUI ----------------------

window = Tk()

window.title("FAQ Chatbot")

window.geometry("700x550")

window.configure(bg="white")

heading = Label(
    window,
    text="FAQ Chatbot",
    font=("Arial",20,"bold"),
    bg="white",
    fg="blue"
)

heading.pack(pady=15)

Label(
    window,
    text="Ask your Question",
    font=("Arial",12,"bold"),
    bg="white"
).pack()

question_box = Entry(
    window,
    font=("Arial",12),
    width=60
)

question_box.pack(pady=10)

Button(
    window,
    text="Ask",
    font=("Arial",12,"bold"),
    bg="green",
    fg="white",
    command=chatbot
).pack(pady=10)

Label(
    window,
    text="Bot Response",
    font=("Arial",12,"bold"),
    bg="white"
).pack()

answer_box = Text(
    window,
    height=10,
    width=60,
    font=("Arial",11)
)

answer_box.pack(pady=10)

window.mainloop()
