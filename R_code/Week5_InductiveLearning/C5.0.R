Heart_data <- read.csv('http://www-bcf.usc.edu/~gareth/ISL/Heart.csv')
str(Heart_data)
summary(Heart_data)
#AHD : Factor w/ 2 levels "No","YES"

library(C50)

# Select Train data -> 0.7
trainIdx <- sample(1:nrow(Heart_data),size=nrow(Heart_data) * 0.7)
trainIdx <- sort(trainIdx)

train_Heart <- Heart_data[trainIdx,]
test_Heart <- Heart_data[-trainIdx,]
summary(train_Heart)

HeartC5 <- C5.0(AHD~., data= train_Heart, method="class")
summary(HeartC5)

predictHeart <- predict.C5.0(HeartC5, test_Heart)

accuracy <- function(actual, predict){
  sum(actual==predict)/length(actual)
}

accuracy(test_Heart$AHD, predictHeart)


