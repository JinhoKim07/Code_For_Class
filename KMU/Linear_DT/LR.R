getwd()
setwd("/Users/Jinho/Dropbox/[Lecture]/18_이공계기반구매엔지니어양성과정/정형데이터/Data")

library(dplyr)
library(Metrics)

Raw <- data.frame(read.table("./winequality-red.csv",sep=";",header = T))
Data <- Raw

train <- sample_frac(Data, 0.7)
trainIndex <- as.numeric(row.names(train))
test <- Data[-trainIndex, ]

train <- arrange(train)
test <- arrange(test)

#### Linear Regression

#wine_lr <- lm(quality ~ ., data=train)
wine_lr <- lm(quality ~ volatile.acidity + citric.acid + total.sulfur.dioxide + alcohol , data=train)

summary(wine_lr)
par(mfrow=c(2,2))
plot(wine_lr)

preidct_wine <- predict(wine_lr, test)
mae(test$quality, preidct_wine)
