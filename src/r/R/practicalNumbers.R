#         [2023-05-19] Challenge #400 [Intermediate] Practical Numbers
#
# Background
# A practical number is a positive integer N such that all smaller positive
# integers can be represented as sums of distinct divisors of N. For example,
# 12 is a practical number because all the numbers from 1 to 11 can be expressed
# as sums of the divisors of 12, which are 1, 2, 3, 4, and 6. (Wikipedia.)
# However, 10 is not a practical number, because 4 and 9 cannot be expressed as
# a sum of 1, 2, and 5. For more detailed explanation and examples, see this
# recent Numberphile video.
#
# Challenge
# Write a function that returns whether a given positive integer is a practical
# number.
#
# practical(1) => true
# practical(2) => true
# practical(3) => false
# practical(10) => false
# practical(12) => true
#
# You should be able to handle numbers up to 10,000 efficiently. The sum of all
# practical numbers up to 10,000 inclusive is 6,804,107. Test your code by
# verifying this value.
#
# Optional bonus challenge
# Consider the numbers X in the range 1 to 10,000 inclusive. The sum of all X
# such that 1019 + X is a practical number is 1,451,958. Find the sum of all X
# such that 1020 + X is a practical number. I found the section Characterization
# of practical numbers in the Wikipedia article useful here.
#
# I do not have any plans to resume posting here regularly. I just saw the Numberphile video and thought it would make a good challenge.
#
# Reference:
#   - https://www.reddit.com/r/dailyprogrammer/comments/13m4bz1/20230519_challenge_400_intermediate_practical/
#   - https://rosettacode.org/wiki/Practical_numbers
#

#'
#' @export
#'
isPractical <- function(number) {
  divisors <- allDivisors(number, FALSE)

  for (prime in unique(primeFactors(number))) {
    if (FALSE == (prime - 1) %in% divisors) {
      return(FALSE)
    }
  }

  return(TRUE)
}

#'
#' @export
#'
practicalNumbers <- function(limit) {
  item <- 1
  practical <- c()

  while (item <= limit) {
    if (isPractical(item)) {
      practical <- c(practical, item)
    }

    item <- item + 1
  }

  return(practical)
}
