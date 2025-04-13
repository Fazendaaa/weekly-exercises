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

test_that('From Rosetta Code #1 example', {
  input <- 6
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #2 example', {
  input <- 8
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #3 example', {
  input <- 16
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #4 example', {
  input <- 18
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #5 example', {
  input <- 20
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #6 example', {
  input <- 24
  output <- TRUE

  expect_equal(isPractical(input), output)
})

test_that('From Rosetta Code #7 example', {
  input <- 288
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
