## NEURAL NETWORK R CODE using neuralnet packages

library(neuralnet)

Input <- expand.grid(c(1,0),c(1,0))

XOR <- c(0,1,1,0)

Truthtable.XOR <- data.frame(Input,XOR)

net.XOR <- neuralnet(XOR~Var1+Var2,Truthtable.XOR,
                     hidden = 2, rep =1000)

plot(net.XOR, rep = "best")

