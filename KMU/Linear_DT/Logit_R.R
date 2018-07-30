getwd()
setwd("/Users/Jinho/Dropbox/[Lecture]/18_이공계기반구매엔지니어양성과정/정형데이터/Data")

library(dplyr)
library(Metrics)

Raw <- data.frame(read.csv("./diabetes.csv"))
Data <- Raw

train <- sample_frac(Data, 0.7)
trainIndex <- as.numeric(row.names(train))
test <- Data[-trainIndex, ]

train <- arrange(train)
test <- arrange(test)

#### Linear Regression

#Diabet_logit <- glm(Outcome ~ .,family = binomial, data=train) # 0.7652174
Diabet_logit <- glm(Outcome ~ Glucose+BMI+Age+Pregnancies,family = binomial, data=train) # .7782609

summary(Diabet_logit)
par(mfrow=c(2,2))
plot(Diabet_logit)

predict_Dia <- predict(Diabet_logit, test)
result <- ifelse(predict_Dia > 0.5, 1, 0)

accuracy(result, test$Outcome)
logit.table <- table(test$Outcome, result)
logit.table
