import Control.Applicative
import Control.Monad
import System.IO


showWord :: Int -> [Char]
showWord n
  | n == 0 = ""
  | n == 1 = "One"
  | n == 2 = "Two"
  | n == 3 = "Three"
  | n == 4 = "Four"
  | n == 5 = "Five"
  | n == 6 = "Six"
  | n == 7 = "Seven"
  | n == 8 = "Eight"
  | n == 9 = "Nine"
  | n == 10 = "Ten"
  | n == 11 = "Eleven"
  | n == 12 = "Twelve"
  | n == 13 = "Thirteen"
  | n == 14 = "Fourteen"
  | n == 15 = "Fifteen"
  | n == 16 = "Sixteen"
  | n == 17 = "Seventeen"
  | n == 18 = "Eighteen"
  | n == 19 = "Nineteen"
  | n == 20 = "Twenty"
  | n == 30 = "Thirty"
  | n == 40 = "Forty"
  | n == 50 = "Fifty"
  | n == 60 = "Sixty"
  | n == 70 = "Seventy"
  | n == 80 = "Eighty"
  | n == 90 = "Ninety"
  | (n `div` billion > 0) = showWord (n `div` billion)  ++ " Billion " ++ showWord (n `mod` billion)
  | (n `div` million > 0) = showWord (n `div` million)  ++ " Million " ++ showWord (n `mod` million)
  | (n `div` thousand > 0) = showWord (n `div` thousand)  ++ " Thousand " ++ showWord (n `mod` thousand)
  | (n `div` hundred > 0) = showWord (n `div` hundred)  ++ " Hundred " ++ showWord (n `mod` hundred)
  | n `div` 10 > 0 = showWord ((n `div` 10) * 10) ++ " " ++ showWord(n `mod` 10)
  where billion = 1000000000
        million = 1000000
        thousand = 1000
        hundred = 100

strip_last_if_empty :: [Char] -> [Char]
strip_last_if_empty (x:xs)
  | xs == " " = [x]
  | xs == "" = [x]
  | otherwise = x:strip_last_if_empty (xs)


main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        putStrLn (strip_last_if_empty (showWord n))
