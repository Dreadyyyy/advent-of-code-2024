import Data.List (sort, zip)

readNums :: String -> (Int, Int)
readNums s =
  let (n, s') = head (reads s :: [(Int, String)])
      (n', _) = head (reads s' :: [(Int, String)])
   in (n, n')

readLines :: [String] -> ([Int], [Int])
readLines [] = ([], [])
readLines (x : xs) =
  let (n, n') = readNums x
      (ns, ns') = readLines xs
   in (n : ns, n' : ns')

distance :: [Int] -> [Int] -> Int
distance xs xs' = foldl (\acc (x, y) -> acc + abs (x - y)) 0 (zip (sort xs) (sort xs'))

main = do
  contents <- readFile "input.txt"
  let (l, l') = readLines $ lines contents
  print $ distance l l'
