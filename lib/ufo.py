
import pandas

df = pandas.read_csv( "data/ufo/ufo_awesome.tsv", sep="\t", index_col=[], 
                        names=['sighted','reported','location'],parse_dates = True)