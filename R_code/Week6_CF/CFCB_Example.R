mat <- matrix(c(5, 3, 4, 3, 1, 
                3, 1, 3, 3, 5,
                4, 2, 4, 1, 5,
                4, 3, 3, 5, 2,
                NA,3, 5, 4, 1),
              ncol = 5, nrow = 5)

pearson <- function(mat, i, j){

  mat <- t(na.omit(t(mat)))
  numer <- sum( (mat[i, ] - mean(mat[i, ])) * (mat[j, ] - mean(mat[j, ])))
  denom1 <- sqrt(sum((mat[i, ] - mean(mat[i, ]))^2))
  denom2 <- sqrt(sum((mat[j, ] - mean(mat[j, ]))^2))

  
  return(numer / (denom1 * denom2)) 
  
}

pearson(mat,1,2)
pearson(mat,1,3)
pearson(mat,1,4)
pearson(mat,1,5)



adjustcosine <- function(mat, i, j){ 
  
  mat <- na.omit(mat)
  
  numer <- sum(mat[,i]*mat[,j])  
  denom1 <- sqrt(sum(mat[,i]^2)) 
  denom2 <- sqrt(sum(mat[,j]^2)) 

  return(numer / (denom1 * denom2)) 
}

adjustcosine(mat, 5, 1)
adjustcosine(mat, 5, 2)
adjustcosine(mat, 5, 3)
adjustcosine(mat, 5, 4)
adjustcosine(mat, 5, 5)
