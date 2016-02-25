# Getting Started with VowPal Wabbit: A Hands-on Tutorial

The code and tutorials are provided in conjunction with a Data Science Dojo Meetup.

## Overview of VowPal Wabbit
The Vowpal Wabbit (VW) project is a fast out-of-core learning system sponsored by Yahoo! Research and written by John Langford along with a number of contributors.

Via parallel learning, it can exceed the throughput of any single machine network interface when doing linear learning, a first amongst learning algorithms.

What does it do well? Online learning & scalable solutions

Its scalability is aided by several factors:
* Out-of-core learning (no need to load all data into memory)
* Exploiting multi-core CPUs (input and learning are done in separate threads)
* Compiled C++ Code

### Languages 
* C++
* [C#] (http://www.nuget.org/packages/VowpalWabbit/)
* Python 
* Java
* [R] (https://cran.r-project.org/web/packages/RVowpalWabbit/RVowpalWabbit.pdf)

## Requirements 

* Linux Operating System (Ubuntu, Debian etc.)
* Anaconda 3.5 or Python 3.5
* Github.com account
* Text editor

## Installation

VowPal Wabbit was developed to be run on the open source Debian operating system. Therefore, it is fairly simple to install on Linux operating systems, like Ubuntu. Ubuntu installation is demonstrated in the meet-up. 

If you have a Windows operating system and would like to install VowPal Wabbit, [this tutorial] (http://mlwave.com/install-vowpal-wabbit-on-windows-and-cygwin/) may be helpful. It will take about 20 minutes to complete if you don’t have the Cygwin compiling packages already installed. Some further troubleshooting may be required. 

To install on Ubuntu, the following packages need to be installed:


(Ubuntu 12.04)

```
sudo apt-get install libboost1.48-all-dev libboost-python-dev
```
(Ubuntu 13.10)

```
sudo apt-get install zlib1g-dev
```

Use this code to install vw on a Linux operating system

```
git clone git://github.com/JohnLangford/vowpal_wabbit.git
cd vowpal_wabbit
./configure
make
```
Check to make sure that it worked. This code should generate a list of commands. 
```
vw --help
```

## Cloning the Repository for Code & Materials 

```
$ git clone https://www.github.com/datasciencedojo/meetup.git
```
Folder: Getting Started with VowPal Wabbit

## Titanic Predictive Model

We will use VowPal Wabbit (vw) to develop a model to predict whether a passenger would survive or die on the Titanic. This demo is based on a [code from MLwave] (http://mlwave.com/tutorial-titanic-machine-learning-from-distaster/)

### Data Input & Exploration 

The [Commandline](https://github.com/JohnLangford/vowpal_wabbit/wiki/Command-line-arguments) list on github provides useful commands in C++. We will use Python for some of the manipulations. 

VowPal Wabbit has a specific [input format](https://github.com/JohnLangford/vowpal_wabbit/wiki/Input-format). We will use the provided python code (convert_csv_to_vw.py) to convert the train.csv and test.csv files.

```
python convert_csv_to_vw.py
```
This should generate two new new files called train.vw and test.vw

### Generating a predictive model
Now that the data is in vw format, we can start training a model. 
```
vw train.vw -f model.vw --binary --passes 20 -c -q ff --adaptive --normalized --l1 0.00000001 --l2 0.0000001 -b 24
```
A explanation of each command is provided in vw_model_options_cheat_sheet.txt

### Predicting Survival using the Model

Now we want our model to predict whether the test.csv passengers will survive or not. 

```
vw -d test_titanic.vw -t -i model.vw -p preds_titanic.txt
```
This has saved the predictions into a text file. 

### Converting format

If you want to submit your vw model to the [Kaggle](http://www.kaggle.com) competition, use the provided python script to convert to the Kaggle format. 
```
python convert_vw_to_kaggle.py
```