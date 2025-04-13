# devtools::test_active_file(file = 'tests/testthat/test.oneHundredDoors.R')
context('Practical One Hundred Doors Challenge')

generateBooleanResult <- function(limit, open) {
  output <- rep(FALSE, limit)
  item <- 1

  while (item <= limit) {
    if (item %in% open) {
      output[item] <- TRUE
    }

    item <- item + 1
  }

  return(output)
}

test_that('Wanted example', {
  input <- 100
  open <- c(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
  output <- generateBooleanResult(input, open)

  expect_equal(oneHundredDoors(input), output)
})
