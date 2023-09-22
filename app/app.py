from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

# モデルとトークナイザーのロード
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    text = request.json['text']
    
    # トークン化とモデルの実行
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    results = logits.argmax(dim=1)
    
    if results[0] == 1:
        sentiment = "positive"
    else:
        sentiment = "negative"
    
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
