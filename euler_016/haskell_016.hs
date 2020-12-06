import Control.Applicative
import Control.Monad
import System.IO
import Data.Char


answer n = sum . map digitToInt . show $ (2^n)

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print(answer n)