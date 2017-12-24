library(genalg)
library(ggplot2)


From <- c(1, 2, 3, 4, 5, 2, 3)
To <- c(2, 3, 4, 5, 1, 5, 5)

Length <- c(9, 6, 3, 5, 4, 15, 20)

Cost.table <- data.frame(cbind(From, To, Length))

len_chrome <- length(From) # or To or Length
num_V <- 5
Punishment <- 1000


evalFunc <- function(gene){
  
  temp <- data.frame(Cost.table[which(gene == 1), c("From", "To")])
  
  len_gene <- length(temp$From)
  
  if (len_gene < num_V){ return (Punishment) }

  Checker_From <- c(rep(0,num_V))
  # From [0,0,0,0,0]
  Checker_To <- c(rep(0,num_V))
  # To [0,0,0,0,0]
  
  for (i in 1:len_gene){
    num_From <- temp$From[i]
    num_To <- temp$To[i]
    
    Checker_From[num_From] <- Checker_From[num_From] + 1
    Checker_To[num_To] <- Checker_To[num_To] + 1
    
    if (Checker_From[num_From] > 1 || Checker_To[num_To] > 1){
      return(Punishment)
    }
  }
  
  Fitness <- gene %*% Cost.table$Length
  return (Fitness)
}

GAmodel <- rbga.bin(size=len_chrome, popSize=200, 
                    iters = 100, mutationChance = 0.01, 
                    elitism = FALSE, evalFunc=evalFunc)


#cat(summary(GAmodel))
plot(GAmodel)
