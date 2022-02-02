# mat2csv
Transforms data from *.mat (matlab table) to *.csv (comma separated values table) <br>

This script was develop to transform a dataset from the LANL experimental tests, regarding the “Bookshelf Frame Structure - DSS 2000”.<br>
<br>
f_1_List, timest_List:
  - List of raw data folder paths, corresponding to each scenario
  - List of initial timestamps for each scenario <br>

Returns a set of csv files:
  - Header is predefined
  - Channel name convetion follows ray data convention
  - 9th column data is corrupted and thus replaced by 26th column data
