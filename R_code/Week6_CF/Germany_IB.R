#!setwd("/Users/Jinho/Lecture/Lecture-IR4.0/Week6_CF")
#getwd()

# http://www.last.fm -> Today's Example data

data.germany <- read.csv(file = "lastfm-matrix-germany.csv")
head(data.germany[,c(1:8)])

data.germany.ibs <- (data.germany[,!(names(data.germany) %in% c("user"))])
head(data.germany.ibs[,c(1:8)])

getCosine <- function(x,y){
  this.cosine <- sum(x*y) / sqrt(sum(x*x)) / sqrt(sum(y*y))
  return(this.cosine)
}

data.germany.ibs.similarity  <- matrix(NA, 
                                       nrow=ncol(data.germany.ibs),
                                       ncol=ncol(data.germany.ibs),
                                       dimnames=list(colnames(data.germany.ibs),
                                                     colnames(data.germany.ibs)))

for (i in 1:ncol(data.germany.ibs)) {
  for (j in 1:ncol(data.germany.ibs)){
    data.germany.ibs.similarity[i,j] <- getCosine(as.matrix(data.germany.ibs[i]),as.matrix(data.germany.ibs[j]))
  }
}

#data.germany.ibs.similarity <- as.data.frame(data.germany.ibs.similarity)
data.germany.ibs.similarity <- as.data.frame(data.germany.ibs.similarity)

data.germany.neighbours <- matrix(NA, 
                                  nrow=ncol(data.germany.ibs.similarity),
                                  ncol=10,
                                  dimnames=list(colnames(data.germany.ibs.similarity)))

for(i in 1:ncol(data.germany.ibs)) {
  data.germany.neighbours[i,]  <- (t(head(n=10,rownames(data.germany.ibs.similarity
                           [order(data.germany.ibs.similarity[,i],decreasing=TRUE),][i]))))
}
data.germany.neighbours["beyonce",c(1:10)]
