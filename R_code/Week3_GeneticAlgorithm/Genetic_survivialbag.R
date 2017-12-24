library(genalg)
library(ggplot2)

dataset <- data.frame(
  item = c("pocketknife","beans","potatoes",
           "onions","sleeping bag","rope",
           "compass","lighter"),
  survivalpoints = c(10,20,15,2,30,10,30,50),
  weight = c(1,5,10,1,7,5,1,1)
  )
 
#beans, sleeping bag, compass, lighter, smartphone

weightlimit <- 20

evalFunc <- function(x){
  current_solution_survivalpoints <- x %*% dataset$survivalpoints
  current_solution_weight <- x %*% dataset$weight
  
  
  if (current_solution_weight > weightlimit){
    return (0)
  }
  else{ 
    return(-current_solution_survivalpoints)
  }
}

GAmodel <- rbga.bin(size=8, popSize=200, iters = 100, 
                    mutationChance = 0.01, elitism = T, 
                    evalFunc=evalFunc)

#cat(summary(GAmodel))
plot(GAmodel)

