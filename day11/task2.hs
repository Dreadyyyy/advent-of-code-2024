import Data.Map.Strict qualified as Map

readLine :: String -> [Int]
readLine "\n" = []
readLine s = x : readLine rest
  where
    (x, rest) = head (reads s :: [(Int, String)])

lengthAfter :: (Int, Int) -> Map.Map (Int, Int) Int -> (Int, Map.Map (Int, Int) Int)
lengthAfter (n, left) m
  | left == 0 = (1, m)
  | n == 0 = memo (1, left - 1) m
  | even l = let (v, m') = memo (nl, left - 1) m; (v', m'') = memo (nr, left - 1) m' in (v + v', m'')
  | otherwise = memo (n * 2024, left - 1) m
  where
    l = length $ show n
    nl = read (take (l `div` 2) (show n))
    nr = read (drop (l `div` 2) (show n))

memo :: (Int, Int) -> Map.Map (Int, Int) Int -> (Int, Map.Map (Int, Int) Int)
memo k m = case Map.lookup k m of
  Just v -> (v, m)
  Nothing -> let (v, m') = lengthAfter k m in (v, Map.insert k v m')

main = do
  contents <- readFile "input.txt"
  let (r, _) = foldl (\(acc, m) x -> let (v, m') = memo (x, 75) m in (acc + v, m')) (0, Map.empty) $ readLine contents
  print r
