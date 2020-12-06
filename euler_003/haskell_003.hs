import Control.Applicative
import Control.Monad
import System.IO

primes = 2 : filter (null . tail . primeFactors) [3,5..]

primeFactors n = factor n primes
    where
        factor n (p:ps)
            | p*p > n        = [n]
            | n `mod` p == 0 = p : factor (n `div` p) (p:ps)
            | otherwise      =     factor n ps

answer n = last . primeFactors $ n


main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print(answer n)


getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret