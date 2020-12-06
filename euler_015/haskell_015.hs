import Control.Applicative
import Control.Monad
import System.IO
import qualified Data.Text as T

fac :: Integer -> Integer
fac x = product [1..x]

paths :: Integer -> Integer -> Integer
paths m n = fac (m+n) `div` fac m `div` fac n `mod` (10^9 + 7)



main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        line <- getLine
        let temp_n_m = T.splitOn (T.pack " ") (T.pack line)
        let temp_n = T.unpack (temp_n_m !! 0)
        let temp_m = T.unpack (temp_n_m !! 1)
        let n = read temp_n :: Integer
        let m = read temp_m :: Integer
        print(paths m n)