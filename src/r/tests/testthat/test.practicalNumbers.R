# devtools::test_active_file(file = 'tests/testthat/test.practicalNumbers.R')
context('Practical Numbers Challenge')

test_that('Given #1 example', {
  input <- 1
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('Given #2 example', {
  input <- 2
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('Given #3 example', {
  input <- 3
  output <- FALSE

  expect_equal(isPractical(input), output)
})

test_that('Given #4 example', {
  input <- 10
  output <- FALSE

  expect_equal(isPractical(input), output)
})

test_that('Given #5 example', {
  input <- 12
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('Wanted example', {
  input <- 10000
  output <- 6804107

  expect_equal(sum(practicalNumbers(input)), output)
})

#test_that('Bonus example', {
#  input <- 12
#  output <- TRUE
#
#  expect_equal(practicalNumbers(input), output)
#})
