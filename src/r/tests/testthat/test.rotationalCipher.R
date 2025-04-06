# devtools::test_active_file(file = 'tests/testthat/test.rotationalCipher.R')
context('Testing Rotational Cipher')

test_that('Wanted example - 1', {
  input <- list(
    ROT = 5,
    text = 'omg'
  )
  output <- 'trl'

  expect_equal(rotationalCipher(input), output)
})

test_that('Wanted example - 2', {
  input <- list(
    ROT = 0,
    text = 'c'
  )
  output <- 'c'

  expect_equal(rotationalCipher(input), output)
})

test_that('Wanted example - 3', {
  input <- list(
    ROT = 26,
    text = 'Cool'
  )
  output <- 'Cool'

  expect_equal(rotationalCipher(input), output)
})

test_that('Wanted example - 4', {
  input <- list(
    ROT = 13,
    text = 'The quick brown fox jumps over the lazy dog.'
  )
  output <- 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'

  expect_equal(rotationalCipher(input), output)
})

test_that('Wanted example - 5', {
  input <- list(
    ROT = 13,
    text = 'Gur dhvpx oebja sbk whzcf bire gur ynml qbt.'
  )
  output <- 'The quick brown fox jumps over the lazy dog.'

  expect_equal(rotationalCipher(input), output)
})
