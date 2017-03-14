completeBook <- function()  {
  book <- rep(FALSE,192)
  numIteration <-0
  while(!all(book)){
    book[sample(192,1)] <-TRUE
    numIteration <- numIteration + 1
  }
  numIteration
}

iterations <- rep(0,10000)

for(i in 1:10000) {
  iterations[i]<-completeBook()
}

hist(iterations)
