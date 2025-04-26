# devtools::test_active_file(file = 'tests/testthat/test.armstrongNumbers.R')
context('Testing Armstrong Numbers')

test_that('First example', {
  input <- 9
  output <- TRUE

  expect_equal(armstrongNumbers(input), output)
})

test_that('Second example', {
  input <- 10
  output <- FALSE

  expect_equal(armstrongNumbers(input), output)
})

test_that('Third example', {
  input <- 153
  output <- TRUE

  expect_equal(armstrongNumbers(input), output)
})

test_that('Fourth example', {
  input <- 154
  output <- FALSE

  expect_equal(armstrongNumbers(input), output)
})
