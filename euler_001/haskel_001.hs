import Control.Applicative
import Control.Monad
import System.IO

step1 n fact = n `div` fact
step2 n fact = fact * (div_nums) * (div_nums + 1) where div_nums = step1 n fact
answer n = ((step2 (n-1) 3) + (step2 (n-1) 5) - (step2 (n-1) 15)) `div` 2


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