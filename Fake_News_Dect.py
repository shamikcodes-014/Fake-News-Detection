from typing import TypedDict
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split

app= Flask(__name__)
tfvect=TfidfVectorizer(stop_words='english', max_df=0.7)
loaded_model=pickle.load(open('fake_true.pkl', 'rb'))
dataframe=pd.read_csv('fake_and_real_news.csv')
x=dataframe['text']
y=dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)

def fake_news_dect(news):
    tfid_x_train=tfvect.fit_transform(x_train)
    tfid_x_text=tfvect.transform(x_test)
    input_text=[news]
    vectorized_input_text=tfvect.transform(input_text)
    prediction= loaded_model.predict(vectorized_input_text)
    print(prediction)
    return(prediction)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        message=request.form['message']
        predict=fake_news_dect(message)
        print(predict)
        return render_template('index.html', prediction=predict)
    return None

if __name__=='__main__':
    app.run(debug=True)


