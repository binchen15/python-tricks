# generator_expession.py
# build data pipeline using generator expressions
# ref https://realpython.com/introduction-to-python-generators/

file_name = "techcrunch.csv"
lines     = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols      = next(list_line)
dict_line = (dict(zip(cols, data)) for data in list_line)
funding = ( int(d["raisedAmt"]) for d in dict_line 
								if d["round"] == "a" )
#total_series_a = sum(funding)
total_series_a = 0
count_series_a = 0
for f in funding:
	total_series_a += f
	count_series_a += 1
avg = total_series_a/count_series_a
print( f"Num of Series A fundrasing {count_series_a}, "
	   f"Total fundraising: ${total_series_a}, "
       f"Average fundraising ${avg:.2f}" )
