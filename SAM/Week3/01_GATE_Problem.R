## NEURAL NETWORK R CODE using neuralnet packages

library(neuralnet)

AND <- c(rep(0,7),1)
OR <- c(0,rep(1,7))

binary.data <- data.frame(expand.grid(c(0,1),c(0,1),c(0,1)))

# expand.grid(c(0,1),c(0,1))!

print(net<-neuralnet(
  AND+OR~Var1+Var2+Var3, binary.data, hidden=0, 
  rep = 1, err.fct="ce", linear.output=FALSE))

plot(net, rep="best")


XOR <- c(0,1,1,0)
xor.data <- data.frame(expand.grid(c(0,1), c(0,1)), XOR)
print(net.xor <- neuralnet(XOR~Var1+Var2, xor.data, hidden=2, rep=5))
plot(net.xor, rep="best")
