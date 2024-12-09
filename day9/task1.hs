move :: [(Int, String)] -> [(Int, String)] -> [String]
move ((i, x) : xs) ((j, x') : xs')
  | i > j = []
  | x' == "." = move ((i, x) : xs) xs'
  | x /= "." = x : move xs ((j, x') : xs')
  | otherwise = x' : move xs xs'

expand :: [Int] -> [String] -> [String]
expand _ [] = []
expand (i : is) (c : cs)
  | even i = [show (i `div` 2) | _ <- [1 .. read c]] ++ expand is cs
  | otherwise = ["." | _ <- [1 .. read c]] ++ expand is cs

main = do
  input <- readFile "input.txt"
  let chars = filter (/= "\n") $ map (: []) input
  let expanded = expand [0 ..] chars
  let moved = move (zip [0 ..] expanded) (reverse $ zip [0 ..] expanded)
  print $ foldl (\acc (i, c) -> acc + i * read c) 0 $ zip [0 ..] moved
