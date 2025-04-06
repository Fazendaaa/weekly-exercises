#'
#' @export
#'
parallelizeData <- function(data, toParallel) {
  toRunData <- function(data, start, end, toParallel) {
    item <- start
    results <- list()

    while (item <= end) {
      curr <- data[item]
      results[[as.character(item)]] <- toParallel(curr)
      item <- item + 1
    }

    return (results)
  }
  library(doParallel)

  nCores <- detectCores() / 2
  cluster <- makeCluster(nCores)
  limit <- length(data)
  load <- floor(limit / nCores)

  results <- list()

  registerDoParallel(cluster)

  toRunData <- toRunData
  toParallel <- toParallel

  results <- foreach(index = 1:nCores, .export = ls(globalenv())) %dopar% {
    start <- ((index - 1) * load) + 1
    end <- index * load

    return (toRunData(data, start, end, toParallel))
  }

  stopCluster(cl = cluster)

  lastOne <- nCores * load

  # Handle the remaining load
  if (lastOne < limit) {
    results <- c(results, toRunData(data, lastOne + 1, limit, toParallel))
  }

  return(results)
}