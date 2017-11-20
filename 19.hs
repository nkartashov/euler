module Main where

data Year = Basic | Leap

mapLeapYear x = if x `mod` 4 == 0 && x `mod` 400 /= 0 then Leap else Basic

mapYear Basic = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mapYear Leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

walkMonth (acc, day) monthLength = let result = acc + if day == 5 then 1 else 0
                                       newDay = (day + monthLength) `mod` 7
                                    in (result, newDay)

sundays :: Int -> [Int] -> Int
sundays day = fst . foldl walkMonth (0, day)

main = do
  let years = concatMap mapYear $ map mapLeapYear [1901..2000]
  print $ sundays 0 years

