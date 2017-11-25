module Main where

import Data.Char
import Data.List.Split
import qualified Data.Map as M
import qualified Data.List as L

namesPath = "p022_names.txt"

alphaZero = fromEnum 'a'

letterMap = M.fromList $ zip "abcdefghijklmnopqrstuvwxyz" [1..]

letterScore c = letterMap M.! c

alphabeticScore :: String -> Integer
alphabeticScore = sum . map letterScore

calculateNames :: [String] -> [Integer]
calculateNames names = let sortedNames = L.sort names
                           in map (\(i, s) -> i * alphabeticScore s) $ zip [1..] sortedNames

stripNames = map ((map toLower) . init . tail) . splitOn ","


main :: IO ()
main = do
  names <- readFile namesPath
  let cleanNames = stripNames names
  print $ sum $ calculateNames cleanNames
