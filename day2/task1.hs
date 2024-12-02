readline :: String -> [Int]
readline "" = []
readline s =
  let (n, s') = head (reads s :: [(Int, String)])
   in (n : readline s')

readlines :: [String] -> [[Int]]
readlines = foldr ((:) . readline) []

cond :: Int -> Int -> Bool
cond a b = (\x -> x >= 1 && x <= 3) (abs (a - b))

monot :: [Int] -> Bool
monot [] = True
monot [_] = True
monot [x1, x2] = cond x1 x2
monot (x1 : x2 : x3 : xs) =
  (x1 < x2 && x2 < x3 || x1 > x2 && x2 > x3)
    && cond x1 x2
    && cond x2 x3
    && monot (x2 : x3 : xs)

main = do
  contents <- readFile "input.txt"
  let l = readlines $ lines contents
  print $ foldl (\acc xs -> if monot xs then acc + 1 else acc) 0 l
