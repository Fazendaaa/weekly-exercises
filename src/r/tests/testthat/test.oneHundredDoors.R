# devtools::test_active_file(file = 'tests/testthat/test.oneHundredDoors.R')
context('Practical One Hundred Doors Challenge')

test_that('Wanted example', {
  input <- 100
  output <- TRUE

  expect_equal(oneHundredDoors(input), output)
})
