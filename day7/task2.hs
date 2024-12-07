readLine :: String -> (Int, [Int])
readLine s = (read n, map read nums)
  where
    (n, _ : rest) = break (== ':') s
    nums = words rest

cat :: Int -> Int -> Int
cat a b = read $ show a ++ show b

check :: [Int] -> Int -> Int -> Bool
check [] acc n = acc == n
check (x : xs) acc n = or [check xs r n | r <- [acc + x, acc * x, acc `cat` x], r <= n]

main = do
  input <- readFile "input.txt"
  print $ sum [n | (n, x : xs) <- map readLine $ lines input, check xs x n]
