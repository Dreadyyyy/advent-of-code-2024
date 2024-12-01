import Data.List (sort)

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

shrinkRec :: [Int] -> Int -> Int -> [(Int, Int)]
shrinkRec [] n c = [(n, c)]
shrinkRec (x : xs) n c =
  if x == n
    then shrinkRec xs n (c + 1)
    else (n, c) : shrinkRec xs x 1

shrink :: [Int] -> [(Int, Int)]
shrink [] = []
shrink (x : xs) = shrinkRec (x : xs) x 0

similarity :: [(Int, Int)] -> [(Int, Int)] -> Int
similarity [] _ = 0
similarity _ [] = 0
similarity ((x, a) : xs) ((x', a') : xs')
  | x == x' = x * a * a' + similarity xs xs'
  | x > x' = similarity ((x, a) : xs) xs'
  | otherwise = similarity xs ((x', a') : xs')

main = do
  contents <- readFile "input.txt"
  let (l, l') = readLines $ lines contents
  print $ similarity (shrink $ sort l) (shrink $ sort l')
