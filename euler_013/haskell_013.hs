import Control.Monad (replicateM)
import Data.Maybe

readManyInteger :: Int -> IO ([Integer])
readManyInteger n = do
    xss    <- replicateM n readInteger
    return (xss)

readInteger :: IO Integer
readInteger = do
    t_temp <- getLine
    let t = read t_temp :: Integer
    return t

getInt :: IO Int
getInt = do
  s <- getLine
  return (read s :: Int)

solve :: [Integer] -> String
solve (x:xs) = take 10 (show $ sum(x:xs))

-- show
main :: IO ()
main = do
  n <- getInt
  list <- readManyInteger n
  putStrLn $ solve list
-- /show