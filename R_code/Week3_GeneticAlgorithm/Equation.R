library(genalg)
library(ggplot2)

score <- c(8,4,2,1)

Fitness <- function(gene){
   eval_x <- gene %*% score
   y <- -eval_x*(eval_x-16)+16
  return(-y)
}

GAmodel <- rbga.bin(size=4, popSize=16, iters = 100, 
                    mutationChance = 0.25, elitism = T, 
                    evalFunc=Fitness)
cat(summary(GAmodel))
plot(GAmodel)
