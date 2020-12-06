import Control.Applicative
import Control.Monad
import System.IO

sum_of_squares n = n * (n+1) * (2*n + 1) / 6
square_of_sum n = (n * (n+1) / 2) ** 2
answer n = square_of_sum n - sum_of_squares n

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Double
        print(round (answer n))

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret

