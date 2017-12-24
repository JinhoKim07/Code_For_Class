## NEURAL NETWORK R CODE using neuralnet packages

library(neuralnet)
# R에서는 코드를 직접 작성하는 것도 가능합니다.
# 하지만, 거의 모든 문제에 대해 쉽게 적용할 수 있도록 라이브러리가 개발이 되어 있습니다.
# Neural Network의 경우 'neuralnet'과 같이, 라이브러리가 존재합니다.

Input <- expand.grid(c(1,0),c(1,0))
# c는 Vector에 대한 함수로, 여러개의 동일한 형태의 데이터를 모아서 함께 저장하는 것을 의미
# c(1,2,3,4)는 [1,2,3,4]로 이루어진 vector를 의미합니다.
#expand.grid는 "Create a data frame from all combianations of the supplied vectors of factors.
#(1,0)과 (1,0) 으로 가능한 모든 조합은? -> (1,1), (1,0), (0,1), (0,0)

AND <- c(1,0,0,0)

Truthtable.AND <- data.frame(Input,AND)

net.AND<-neuralnet(AND~Var1+Var2, Truthtable.AND, hidden=0, 
                   threshold = 0.001, stepmax = 1e+05, rep = 10, 
                   err.fct="sse", act.fct='logistic',linear.output = FALSE)
# neuralnet의 모델을 구성하는 부분입니다.
# nueralnet(정답~변수+변수+..., 전체데이터, hidden layer의 노드 수,
#           errorfunction의 미분 값이 0.001이하로 내려가면 모델 학습 종료, 
#           step이 1e+05번 이상되면 학습종료
#           training할 모델 갯수,
#           error 산출 모델 (sse (sum of squred error), ce (Cross entropy)) )
#           activation function -> logistic(sigmoid), tanh
#           Linear.output : if act.fct should not be applied to the output neurons
#           set linear output to TRUE, otherwise to FALSE.

net.AND
# 모델에 의해 생성된 결과를 확인해 봅시다.
plot(net.AND, rep="best")
# 구조 및 가중치가 어떻게 되는지 확인해 봅시다.



OR <- c(1,1,1,0)
Truthtable.OR  <- data.frame(Input,OR)
net.OR<-neuralnet(OR~Var1+Var2, Truthtable.OR, hidden=0, 
                   threshold = 0.001, stepmax = 1e+05, rep = 10, 
                   err.fct="sse", act.fct='logistic',linear.output = FALSE)
net.OR
plot(net.OR, rep="best")
