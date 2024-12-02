readline :: String -> [Int]
readline "" = []
readline s =
  let (n, s') = head (reads s :: [(Int, String)])
   in (n : readline s')

readlines :: [String] -> [[Int]]
readlines = foldr ((:) . readline) []

cond :: Int -> Int -> Bool
cond a b = (\x -> x >= 1 && x <= 3) (abs (a - b))

safe :: [Int] -> Bool
safe [] = True
safe [_] = True
safe [x1, x2] = cond x1 x2
safe (x1 : x2 : x3 : xs) =
  (x1 < x2 && x2 < x3 || x1 > x2 && x2 > x3)
    && cond x1 x2
    && cond x2 x3
    && safe (x2 : x3 : xs)

removeOne :: [Int] -> [Int] -> Int -> [Int]
removeOne [] _ _ = []
removeOne (x : xs) (i : is) n =
  if i == n
    then xs
    else x : removeOne xs is n

options :: [Int] -> [[Int]]
options xs = foldl (\acc n -> removeOne xs [0 ..] n : acc) [] [0 .. length xs]

main = do
  contents <- readFile "input.txt"
  let l = readlines $ lines contents
  print $
    foldl
      ( \acc xs ->
          if foldl (\acc' xs' -> acc' || safe xs') False $ options xs
            then acc + 1
            else acc
      )
      0
      l
