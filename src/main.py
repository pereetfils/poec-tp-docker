from calc import apply_vat
import sys

price = sys.argv[1]
percent= sys.argv[2]
price=float(price)
percent= float(percent)
print (apply_vat(price, percent))