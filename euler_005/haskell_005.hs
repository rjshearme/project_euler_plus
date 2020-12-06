import Control.Applicative
import Control.Monad
import System.IO
import Data.Array.Unboxed
import Data.Fixed

is_prime n
    | n <= 1 = False
    | n == 2 = True
    | otherwise = n `mod'` 2 /= 0 && length [x | x <- [3,5..sqrt n + 1], n `mod'` x == 0 && n /= x] == 0

lesser_prime_factors n = [x | x <- [1..n], is_prime x]

max_exponed_prime_factors n = [x ** (fromIntegral (floor (logBase x n)))  | x <- lesser_prime_factors n]

answer n = product (max_exponed_prime_factors n)

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Float
        print (round (answer n))


getMultipleLines :: Int -> IO [String]
getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret

