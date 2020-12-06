import Control.Monad
import Data.List
import Data.Maybe

calcScor :: (Int, String) -> Int
calcScor (position, name) = position * nameValue name
  where nameValue [] = 0
        nameValue (x:xs) = 1 + (fromJust $ elemIndex x ['A'..'Z']) + nameValue xs

getMultipleLines :: Int -> IO [String]
getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    names <- getMultipleLines n
    let sorted_names = sort names
    let names_scores = zip (map calcScor (zip [1..] $ sort names)) sorted_names
    q_temp <- getLine
    let q = read q_temp :: Int
    forM_ [1..q] $ \a0  -> do
      query_input <- getLine
      print(fst . head $ filter (\x -> snd x == query_input) names_scores)