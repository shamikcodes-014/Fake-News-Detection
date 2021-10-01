<h1>Fake News Detection in Python.</h1>

In this project, we have used vectorizers and multiple machine learning algorithms to classify fake news articles using sci-kit libraries from python.

 
 <h2> Since GitHub allows uploaded file size to be not more than 25MB, we were unable to upload out datasets. Do download the datasets (Fake.csv, True.csv, fake_and_real_news.csv) from the given drive link before running the codes, and place it in the same repository as the codes.</h2>
		
		       https://drive.google.com/drive/folders/1Jf5p5buBHd0J4uHc9Ptbf_65DjMV6Fup?usp=sharing

<h3>1. Getting Started:-</h3>
	These instructions will get you a copy of the project up and running on your local machine for testing purposes.


<h3>2. Prerequisites:-</h3>

   What things you need to run the program:
   
   a. Python 3.8
   
   b. Sklearn (scikit-learn)
   
   c. Numpy
   
   d. Pandas
   
   e. GitBash (If you want to download the repository to run the code)
   
  <h3>3. Dataset Used:</h3>
    The datset used for this project is University of Victoria Fake News Detection Datasets which contains two .csv file (Fake.csv and True.csv) provided to us by our alumni Sreeja Bhattacharya
    <br>
	 </br>
   University of Victoria Fake News Detection Datasets : ISOT Fake News Dataset
    <p></p>
   The ISOT Fake News dataset is a compilation of several thousands fake news and truthful articles, obtained from different legitimate news sites and sites flagged as unreliable by Politifact.com.
    
   the original datasets contains 5 variables/columns for both the Fake and True datasets as follows:
    
   a. Column 1: ID
    
   b. Column 2: title
    
   c. Column 3: text
    
   d. Column 4: subject
    
   e. Column 5: date
    
   Further more, 1 extra column (Label) has been added to both the Fake and True datasets. Label contains '0' in the fake.csv to indicate fake news and contains '1' in the true.csv to indicate the true news. Then, we have merged the two csv files into one csv file (fake_and_real_news.csv) to ease our training process.
    
   To make things simple we have chosen only 2 variables from this final dataset for this classification
   Below are the columns used to in this project

   Column 1: text (News text).
      
   Column 2: Label (Label class contains: 0, 1) 
  
   As you can see we have used two labels for this project.
    
   0 -- Fake
  
   1 -- True
 
    
 <h3>4. File Descriptions:</h3>
  
   a. Fake.csv - University of Victoria ISOT Fake News Dataset containing fake news.
      
   b. True.csv - University of Victoria ISOT Fake News Dataset containing true news.
      
   c. fake_and_real_news - Combined dataset of both the True.csv and Fake.csv
      
   d. Prediction.ipynb - It is the main file of the project. It takes the two datasets Fake.csv and True.csv. Adds lables and concatenate the two file as a single dataset. We take only two variables from the final dataset (text and labels). Then, we split the dataset into 70% train data and 30% test data, pass the text, which is the independent variable through the Tfidf vectorizer that checks for frequent words in the documents and the scores are normalized between 0 and 1. We ran different Classifier models (Passive-Aggressive, K-Nearest Neighbors, Logistic Regression, Random Forest, Decision Tree) on the training dataset and checked the prediction accuracy for each on the test data. We found out that Decision Tree gives us the best accuracy, so we have used the Decisoion Tree Classifier model in our Fake News Detection project.
      
   e. Fake_News_Dect.py - In this file, we performed the flask methodologies to implement the webapp. Here we have received the input news from the html file, and have loaded the pickle file which contains the loaded the Decision Tree Classifier. And used the Tfidf Vectorizer the same as in the .ipynb file to vectorize the input data. The pickle file predicts the label of the input news and returns 0 or 1 back to the html file. This is the file that needs to be executed in order to see the project.
      
   f. fake_true.pkl - It is the pickle file where we have loaded the best performing classifier (Decision Tree) for easy implementation. With the use of the pickle file we will be able to run the model without the need the run the .ipynb file everytime.
      
<h3>5. Folder Descriptions:</h3>
      
   a. static - This folder contains the style.css file that adds css styling to the frontend.
      
   b. templates - This folder contains the index.html file that is the framework of the frontend. The index.html file takes the news input from the user and passes it to the Fake_News_Dect.py flask model, it receives the returned value from the flask model and shows the user it is a fake news or real news.  
      
      
<h3>6. Steps of Execution:</h3>


  <h5>1. The first step, if would be to clone this repo in a folder in your local machine. To do that you need to go to the directory you choose to save the repository codes (make sure the same directory contains the downloaded datasets from the drive as well) and run following command in git bash.</h5>
  		
  			$ git clone https://github.com/shamikcodes-014/Fake-News-Detection.git
			
   <h4>OR</h4>
   <h5>1. Download all the files and folders from the drive link and place them in the same directory.</h5>
   
   			https://drive.google.com/drive/folders/1Jf5p5buBHd0J4uHc9Ptbf_65DjMV6Fup?usp=sharing
   
   
   <h5>2. Now, open your command prompt, change the directory to the folder where you have stored the repository/codes.</h5>
				  
				 cd C:/your project folder path goes here/
   <h5>4. Then run the command (Make sure you have set up the PATH variable while installing Python).</h5>

                 python Fake_News_Dect.py

<h5>5. After hitting the enter, program will open in your localhost server and ask for an input which will be a news text that you want to verify ( The news text has to be from the fake_and_real_news.csv file since the project is static) . Once you paste or type news headline, then press enter.</h5>

<h5>6. Once you hit the enter, program will take user input (news text) and will be used by model to classify in one of categories of "True" and "False".
<br></br>
<h2>Demonstration Video:</h2>

https://user-images.githubusercontent.com/71573124/135656949-d39c317f-38f0-4e58-b34a-a248139ace7f.mp4

			
    
  
   
