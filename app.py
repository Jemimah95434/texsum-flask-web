from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        article = request.form['article']
        if article.strip():
            parser = PlaintextParser.from_string(article, Tokenizer("english"))
            summarizer = LsaSummarizer()
            summary_sentences = summarizer(parser.document, 3)
            summary = " ".join(str(s) for s in summary_sentences)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

