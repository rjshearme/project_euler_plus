import Control.Applicative
import Control.Monad
import System.IO
import Data.Time.Calendar
import Data.List.Split

answerWrapper :: (Integer, Int, Int) -> (Integer, Int, Int) -> Int
answerWrapper (y1, m1, d1) (y2, m2, d2) = countSundaysFirstOfMonth start end
  where start = firstDate y1 m1 d1
        end = fromGregorian y2 m2 d2


firstDate :: Integer -> Int -> Int -> Day
firstDate year month day
  | day == 1 = fromGregorian year month day
  | month < 12 = fromGregorian year (month+1) 1
  | otherwise  = fromGregorian (year+1) 1 1


countSundaysFirstOfMonth :: Day -> Day -> Int
countSundaysFirstOfMonth date end_date
  | date > end_date = 0
  | otherwise = (if (zeller_congruence (toGregorian date)) == 1 then 1 else 0) + countSundaysFirstOfMonth (addGregorianMonthsClip 1 date) end_date


zeller_congruence :: (Integer, Int, Int) -> Int
zeller_congruence (year, month, day) = (q + ((13*m +13) `div` 5) + k + (k `div` 4) + (j `div` 4) - 2*j) `mod` 7
  where m = if month <= 2 then month + 12 else month
        y = fromIntegral (if month <= 2 then year -1 else year)
        q = day
        k = y `mod` 100
        j = y `div` 100

list_to_tuple :: [Int] -> (Integer, Int, Int)
list_to_tuple [y, d, m] = (toInteger y, d, m )

main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        date_start_input <- getLine
        date_end_input <- getLine
        let date_start = list_to_tuple( map read (splitOn " " date_start_input) :: [Int])
        let date_end = list_to_tuple( map read (splitOn " " date_end_input) :: [Int])
        print(answerWrapper date_start date_end)