# devtools::test_active_file(file = 'tests/testthat/test.cryptoSquare.R')
context('Testing Crypto Square')

test_that('Wanted example', {
  input <- 'If man was meant to stay on the ground, god would have given us roots.'
  output <- c(
    'imtgdvs',
    'fearwer',
    'mayoogo',
    'anouuio',
    'ntnnlvt',
    'wttddes',
    'aohghn ',
    'sseoau '
  )

  expect_equal(cryptoSquare(input), output)
})
