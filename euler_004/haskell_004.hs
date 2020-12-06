import Control.Applicative
import Control.Monad
import System.IO

import Math.NumberTheory.Logarithms


answer limit = maximum [prod | x <- [100..999], y <- [x..999], let prod=x*y, let s=show prod, s==reverse s, prod < limit]

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
