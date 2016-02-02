# Building a Real-time Sentiment Pipeline for Live Tweets using Python, R, & Azure

## Requirements
* Twitter Accont + Twitter App setup (https://apps.twitter.com/)
* Anaconda 3.5 or Python 3.5 Installed
* Azure subscription or free trial account
	* [30 day free trial](https://azure.microsoft.com/en-us/pricing/free-trial/)
	* Azure Machine Learning Studio workspace
* Text Editor, I'll be using Sublime Text 3
* Github.com account (to receive code)
* PowerBI.com account (for Dashboard portion)
* .NET up to date + windows (for testing portion)

## Cloning the Repo for Code & Materials
```
git clone https://www.github.com/datasciencedojo/meetup.git
```
Folder: Building a Real-time Sentiment Pipeline for Live Tweets using Python, R, & Azure

## The Predictive Model

### Supervised Twitter Dataset
* Azure ML Reader Module:
	* Data source: Azure Blob Storage
	* Authentication type: PublicOrSAS
	* URI: http://azuremlsampleexperiments.blob.core.windows.net/datasets/Sentiment140.tenPercent.sample.tweets.tsv
	* File format: TSV
	* URI has header row: Checked
* Import and save dataset

### Preprocessing & Cleaning
* Azure ML Metadata Editor: Cast categorical sentiment_label
* Azure ML Group Categorical Values: Casting '0' as Negative, '4' as positive

### Algorithm Selection
* [Algorithm Cheat Sheet](https://azure.microsoft.com/en-us/documentation/articles/machine-learning-algorithm-cheat-sheet/)
* [Beginer's Guide to Choosing Algorithms](https://azure.microsoft.com/en-us/documentation/articles/machine-learning-algorithm-choice/)
* [Azure ML's Support Vector Machines](https://msdn.microsoft.com/en-us/library/azure/dn905835.aspx)
* [Support Vector Machines in General](https://en.wikipedia.org/wiki/Support_vector_machine)

### Text Processing
* Filtering
	* Stop words
	* Stemming and Lemmatization