import Control.Monad

answer :: Int -> Integer
answer x = (4*((m*n*n) - (((m - 1)*m*16) `quot` 2) - ((8*m*(m - 1)*(m - 2)) `quot` 3)) - (6*((n - 1)*(n + 1) `quot` 4)) + 1) `mod` 1000000007
  where m = toInteger $ (n-1) `div` 2
        n = toInteger x

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print(answer n)
