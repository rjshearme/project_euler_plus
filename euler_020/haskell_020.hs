import Control.Applicative
import Control.Monad
import System.IO
import Data.Char

fac :: Integer -> Integer
fac 0 = 1
fac n = n * fac(n-1)

solve :: Int -> Int
solve n = sum . (map digitToInt) . show . fac . toInteger $ n


main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int

    forM_ [1..t] $ \a0  -> do
        n_input <- getLine
        let n = read n_input :: Int
        print(solve n)