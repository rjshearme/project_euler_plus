import Control.Monad

maxOrNeg xs
  | null xs = -1
  | otherwise = maximum xs

answer :: Int -> [Int]
answer n = [a*b*c | a <- [1..(n`div`3)], let b =((n*n-2*n*a)`div`(2*n-2*a)), let c=n-a-b, a^2+b^2==c^2]

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print(maxOrNeg . answer $ n)
