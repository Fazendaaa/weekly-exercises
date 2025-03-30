# devtools::test_active_file(file = 'tests/testthat/test.oneHundrerdPrisoners.R')
context('Testing Prisoners Challenge')

test_that('Wanted example', {
  prisoners <- 100
  simulations <- 1000
  output <- list(
    random =  0,
    optimal = 31
  )

  expect_equal(prisonersChallenge(prisoners, simulations), output, tolerance = 1e-1)
})
