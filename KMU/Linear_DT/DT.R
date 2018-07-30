library(dplyr)
library(Metrics)

library(caret)
library(rpart)
library(rpart.plot)

Raw <- data.frame(read.csv("./diabetes.csv"))
Data <- Raw

train <- sample_frac(Data, 0.7)
trainIndex <- as.numeric(row.names(train))
test <- Data[-trainIndex, ]

train <- arrange(train)
test <- arrange(test)

#dia_tree <- rpart(Outcome ~. , data=train, method="class") # Accuracy : 0.7783
dia_tree <- rpart(Outcome ~ Glucose+BMI+Age+Pregnancies, data = train, method = "class") # Accuracy : 0.7783

testPred <- predict(dia_tree, test, type="class")

rpart.plot(dia_tree)

confusionMatrix(testPred, as.factor(test$Outcome))

