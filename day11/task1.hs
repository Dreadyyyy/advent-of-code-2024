import Data.List (drop, iterate, take)

readLine :: String -> [Int]
readLine "\n" = []
readLine s = x : readLine rest
  where
    (x, rest) = head (reads s :: [(Int, String)])

blink :: [Int] -> [Int]
blink [] = []
blink (x : xs)
  | x == 0 = 1 : blink xs
  | even l = read (take (l `div` 2) s) : read (drop (l `div` 2) s) : blink xs
  | otherwise = 2024 * x : blink xs
  where
    s = show x
    l = length s

main = do
  contents <- readFile "input.txt"
  print $ length $ iterate blink (readLine contents) !! 25
