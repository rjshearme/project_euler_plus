import Control.Applicative
import Control.Monad
import System.IO
import Data.Fixed

is_prime n
    | n <= 1 = False
    | n == 2 = True
    | otherwise = n `mod'` 2 /= 0 && length [x | x <- [3,5..sqrt n + 1], n `mod'` x == 0 && n /= x] == 0

prime_gens = [x | x <- [1..], is_prime x]

answer n = prime_gens!!(n-1)

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print (round ( answer n ))


getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret

