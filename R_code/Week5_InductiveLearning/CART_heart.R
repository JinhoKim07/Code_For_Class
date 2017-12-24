Heart_data <- read.csv('http://www-bcf.usc.edu/~gareth/ISL/Heart.csv')
str(Heart_data)
summary(Heart_data)
#AHD : Factor w/ 2 levels "No","YES"

library(caret)
library(rpart)
library(rpart.plot)

set.seed(20161129)

# Select Train data -> 0.7
trainIdx <- sample(1:nrow(Heart_data),size=nrow(Heart_data) * 0.7)
trainIdx <- sort(trainIdx)

train_Heart <- Heart_data[trainIdx,]
test_Heart <- Heart_data[-trainIdx,]

HeartTree <- rpart(AHD~., data= train_Heart, method="class")
HeartTree

predictHeart <- predict(HeartTree, test_Heart, type="class")

rpart.plot(HeartTree)

confusionMatrix(predictHeart, test_Heart$AHD)


### Pruning