module Main where

import qualified Data.Map as M
import qualified Data.Set as S
import qualified Data.Tuple as T
import qualified Data.List as L
import Data.Function (on)
import Control.Monad (when)
import Control.Monad.Trans.State

type Divisors = [Int]
type NumberDivisors = M.Map Int Divisors

upperBound = 10000

allPrimes = evalState eratos ([2], [3, 5 .. upperBound])

filterByX x = filter (\y -> y `mod` x /= 0)

eratos = do
  (primes, current:xs) <- get
  let updatedNums = filterByX current xs
  let updatedPrimes = current:primes
  put (updatedPrimes, updatedNums)
  if null updatedNums then return $ reverse updatedPrimes
                      else eratos

merge :: Ord a => [a] -> [a] -> [a]
merge [] x = x
merge x [] = x
merge (x:xs) (y:ys) | y == x    = merge xs (y:ys)
                    | y < x     = y : merge (x:xs) ys
                    | otherwise = x : merge xs (y:ys)

properDivisorsForUpperBound :: [Int] -> NumberDivisors
properDivisorsForUpperBound ps = M.map init $ execState (mapM_ (properDivisors ps) [2 .. upperBound]) $ M.insert 1 [1] M.empty

properDivisors ps x = do
  divisorsSoFar <- get
  if x `M.member` divisorsSoFar then return $ divisorsSoFar M.! x
                                else do
                                  let firstDivisor = head $ filter (\p -> x `mod` p == 0) ps
                                  let remainder = x `div` firstDivisor
                                  properDivisorsOfSmaller <- properDivisors ps remainder
                                  let properDivisorsOfX = merge properDivisorsOfSmaller $ map (* firstDivisor) properDivisorsOfSmaller
                                  modify $ M.insert x properDivisorsOfX
                                  return properDivisorsOfX

getAmicableNumbers :: M.Map Int Int -> S.Set Int
getAmicableNumbers numbersToSums = let elements = M.toList numbersToSums
                                       action (x, y) = do
                                         when (y `M.member` numbersToSums) $ do
                                           let y' = numbersToSums M.! y
                                           when (y' == x && x /= y) $
                                            modify ((S.insert x) . (S.insert y))
                                       cumAction = mapM_ action elements
                                       in execState cumAction S.empty

main :: IO ()
main = do
  let primes = allPrimes
  let numbersToSums = M.map sum $ properDivisorsForUpperBound primes
  let result = S.foldr (+) 0 $ getAmicableNumbers numbersToSums
  print result
