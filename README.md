Fake News Detection in Python.

In this project, we have used vectorizers and multiple machine learning algorithms to classify fake news articles using sci-kit libraries from python.


1. Getting Started:-
These instructions will get you a copy of the project up and running on your local machine for testing purposes.



2. Prerequisites:-

   What things you need to run the program:
   
   a. Python 3.8 or higher
   
   b. Sklearn (scikit-learn)
   
   c. Numpy
   
   d. Pandas
   
   e. GitBash (if you want to download the repository)
   
3. Dataset Used:
    The datset used for this project is University of Victoria Fake News Detection Datasets which contains two .csv file (Fake.csv and True.csv) provided to us by our alumni Sreeja Bhattacharya
    
    University of Victoria Fake News Detection Datasets:ISOT Fake News Dataset
    
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
  
  4. File Descriptions:
  
   
