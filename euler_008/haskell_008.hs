import Control.Applicative
import Control.Monad
import System.IO

import Data.Char

get_string [] k = []
get_string (num_word:words) k = filter ((==k) . length) [[num_word] ++ take (k-1) words] ++  get_string words k

get_product [] = 1
get_product (n:ns) = digitToInt n * get_product ns

answer word k = maximum $ map get_product (get_string word k)


main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n_t = words n_temp
        let n = read $ n_t!!0 :: Int
        let k = read $ n_t!!1 :: Int
        num <- getLine
        print (answer num k)



getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret

