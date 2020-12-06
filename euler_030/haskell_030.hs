import Data.Char

answer n = sum $ filter (\x -> sum_eq_str x n) [10..1000000]
   where sum_eq_str x n = x == (sum $ map (^n) (map digitToInt . show $ x))

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    print(answer n)