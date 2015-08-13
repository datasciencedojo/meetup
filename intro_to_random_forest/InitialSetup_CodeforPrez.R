#Set working directory

setwd("C:\\Users\\consultant\\Dropbox\\Presentations\\RandomForests")


# Create new image and Save it

save.image("./randomforest2.Rdata")

# Install packages( if necessary, install using 'Packages' tab)
#install.packages("randomForest")
#install.packages("caret")
#install.packages("rpart")

# clear all the variables
rm(list=ls())

train=read.csv("./data//train.csv")
test=read.csv("./data//test.csv")
head(test)
# Add "Survived" column to test, to help combine with train data
test$Survived=NA

# Combine train and test
combi=rbind(train,test)

# Convert names to character
combi$Name<-as.character(combi$Name)

# Split 'Name' to isolate a person's title using strsplit
strsplit(combi$Name[1],split='[,.]')

# test of how strsplit works
strsplit(combi$Name[1],split='[,.]')[[1]]
strsplit(combi$Name[1],split='[,.]')[[1]][2]

# apply function to dataset
# This will isolate title for all rows

combi$Title <- sapply(combi$Name, FUN=function(x){strsplit(x,split='[,.]')[[1]][2]})

# remove empty spaces from the 'Title' field
combi$Title=gsub(' ','',combi$Title)

# Review contents of 'Title' field
table(combi$Title)

# Reduce 'Title' contenst into fewer categories
combi$Title[combi$Title %in% c('Mme', 'Mlle')] <- 'Mlle'
combi$Title[combi$Title %in% c('Capt', 'Don', 'Major', 'Sir')] <- 'Sir'
combi$Title[combi$Title %in% c('Dona', 'Lady', 'the Countess', 'Jonkheer')] <- 'Lady'

# Change Title to a factor
combi$Title <- factor(combi$Title)

# Combine sibling and parent/child variables into FamilySize variable
combi$FamilySize <- combi$SibSp + combi$Parch + 1

# Identifying families by combining last name and family size
# # identify surname
combi$Surname <- sapply(combi$Name, FUN=function(x) {strsplit(x, split='[,.]')[[1]][1]})
# # combine with family size
combi$FamilyID <- paste(as.character(combi$FamilySize), combi$Surname, sep="")
# Categorize family size less than 2 as small
combi$FamilyID[combi$FamilySize <= 2] <- 'Small'
# Review results
table(combi$FamilyID)
# Further consolidate results( some families may have different last names)
famIDs <- data.frame(table(combi$FamilyID))
famIDs <- famIDs[famIDs$Freq <= 2,]
combi$FamilyID[combi$FamilyID %in% famIDs$Var1] <- 'Small'
combi$FamilyID <- factor(combi$FamilyID)

# Splitting this new dataset back into train and test datasets
train <- combi[1:891,]
test <- combi[892:1309,]

# PRESENTATION START
# PRESENTATION START

