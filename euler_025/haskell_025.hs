import Control.Monad

fibonacci_numbers = 0:1:(zipWith (+) fibonacci_numbers (tail fibonacci_numbers))

f = [(i, len) | (i, x) <- zip [0..] fibonacci_numbers, let len=length. show $ x]

answer n = fst . head $ filter (\x -> (snd x) >= n) f

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print(answer n)
