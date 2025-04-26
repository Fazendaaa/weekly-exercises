# devtools::test_active_file(file = 'tests/testthat/test.luhn.R')
context('Testing Luhn')

test_that('First example', {
  input <- '4539 3195 0343 6467'
  output <- TRUE

  expect_equal(luhn(input), output)
})

test_that('Second example', {
  input <- '8273 1232 7352 0569'
  output <- FALSE

  expect_equal(luhn(input), output)
})
