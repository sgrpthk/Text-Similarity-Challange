from flask import Flask, request  # import main Flask class and request object
  
app = Flask(__name__)  # create the Flask app
   

@app.route("/", methods=["GET", "POST"])  # allow both GET and POST requests
def form_example():
    if (
        request.method == "POST"
    ):  # this block is only entered when the form is submitted
        text1 = request.form.get("str1")
        text2 = request.form["str2"]
    # tokenization
        X_list = set(text1.split())
 
        # sw contains the list of stopwords
        sw = [
            "i",
            "me",
            "my",
            "myself",
            "we",
            "our",
            "ours",
            "ourselves",
            "you",
            "you're",
            "you've",
            "you'll",
            "you'd",
            "your",
            "yours",
            "yourself",
            "yourselves",
            "he",
            "him",
            "his",
            "himself",
            "she",
            "she's",
            "her",
            "hers",
            "herself",
            "it",
            "it's",
            "its",
            "itself",
            "they",
            "them",
            "their",
            "theirs",
            "themselves",
            "what",
            "which",
            "who",
            "whom",
            "this",
            "that",
            "that'll",
            "these",
            "those",
            "am",
            "is",
            "are",
            "was",
            "were",
            "be",
            "been",
            "being",
            "have",
            "has",
            "had",
            "having",
            "do",
            "does",
            "did",
            "doing",
            "a",
            "an",
            "the",
            "and",
            "but",
            "if",
            "or",
            "because",
            "as",
            "until",
            "while",
            "of",
            "at",
            "by",
            "for",
            "with",
            "about",
            "against",
            "between",
            "into",
            "through",
            "during",
            "before",
            "after",
            "above",
            "below",
            "to",
            "from",
            "up",
            "down",
            "in",
            "out",
            "on",
            "off",
            "over",
            "under",
            "again",
            "further",
            "then",
            "once",
            "here",
            "there",
            "when",
            "where",
            "why",
            "how",
            "all",
            "any",
            "both",
            "each",
            "few",
            "more",
            "most",
            "other",
            "some",
            "such",
            "no",
            "nor",
            "not",
            "only",
            "own",
            "same",
            "so",
            "than",
            "too",
            "very",
            "s",
            "t",
            "can",
            "will",
            "just",
            "don",
            "don't",
            "should",
            "should've",
            "now",
            "d",
            "ll",
            "m",
            "o",
            "re",
            "ve",
            "y",
            "ain",
            "aren",
            "aren't",
            "couldn",
            "couldn't",
            "didn",
            "didn't",
            "doesn",
            "doesn't",
            "hadn",
            "hadn't",
            "hasn",
            "hasn't",
            "haven",
            "haven't",
            "isn",
            "isn't",
            "ma",
            "mightn",
            "mightn't",
            "mustn",
            "mustn't",
            "needn",
            "needn't",
            "shan",
            "shan't",
            "shouldn",
            "shouldn't",
            "wasn",
            "wasn't",
            "weren",
            "weren't",
            "won",
            "won't",
            "wouldn",
            "wouldn't",
        ]

        # remove stop words from string
        X_set = {w for w in X_list if not w in sw}
        Y_set = {w for w in Y_list if not w in sw}

        # empty vector
        v1 = []
        v2 = []

        # form a set containing keywords of both strings
        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set:
                v1.append(1)  # create a vector
            else:
                v1.append(0)
            if w in Y_set:
                v2.append(1)
            else:
                v2.append(0)
        c = 0

        # cosine formula
        for i in range(len(rvector)):
            c += v1[i] * v2[i]
        cosine_w = c / float((sum(v1) * sum(v2)) ** 0.5)
        print("similarity: ", cosine_w)
        ############################
        ##Without remove stop words
        ############################
        # empty vector
        v1 = []
        v2 = []

        # form a set containing keywords of both strings
        rvector = X_list.union(Y_list)
        for w in rvector:
            if w in X_list:
                v1.append(1)  # create a vector
            else:
                v1.append(0)
            if w in Y_list:
                v2.append(1)
            else:
                v2.append(0)
        c = 0

        # cosine formula
        for i in range(len(rvector)):
            c += v1[i] * v2[i]
        cosine = c / float((sum(v1) * sum(v2)) ** 0.5)

        return """<h1>Cosine similarity with stopwords    : {}</h1>
                  <h1>Cosine similarity without Stopwords: {}</h1>""".format(
            cosine, cosine_w
        )

    return """<form method="POST">
                    <h1>Two String Matching Percentage</h1><br /><br />
                    <p>
                        <label>Text1</label>
                            <textarea name="str1" rows="10" cols="80" placeholder="Your text here"></textarea>
                    </p>
                    <p>
                        <label>Text2</label>
                            <textarea name="str2" rows="10" cols="80" placeholder="Your text here"></textarea>
                    </p>
                    <button>Caculate Similarity</button>
              </form>"""


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5002)  # run app in debug mode on port 5000

