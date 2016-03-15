## Pstat Function List ##

This module provides some useful list and array manipulation routines
modeled after those found in the |Stat package by Gary Perlman, plus a
number of other useful list/file manipulation functions.  The list-based
functions include:

  * ### duplicates ###
```
Returns duplicate items in the FIRST dimension of the passed list.

Usage:   duplicates (inlist)
```


  * ### simpleabut ###
```
Concatenates two lists as columns and returns the result.  '2D' lists
are also accomodated for either argument (source or addon).  This DOES NOT
repeat either list to make the 2 lists of equal length.  Beware of list pairs
with different lengths ... the resulting list will be the length of the
FIRST list passed.

Usage:   simpleabut(source,addon)  where source, addon=list (or list-of-lists)
Returns: a list of lists as long as source, with source on the 'left' and
                 addon on the 'right'
```


  * ### nonrepeats ###
```
Returns items that are NOT duplicated in the first dim of the passed list.

Usage:   nonrepeats (inlist)
```


  * ### replace ###
```
Replaces all occurrences of 'oldval' with 'newval', recursively.

Usage:   replace (inlst,oldval,newval)
```


  * ### list2string ###
```
Converts a 1D list to a single long string for file output, using
the string.join function.

Usage:   list2string (inlist,delimit=' ')
Returns: the string created from inlist
```


  * ### recode ###
```
Changes the values in a list to a new set of values (useful when
you need to recode data from (e.g.) strings to numbers.  cols defaults
to None (meaning all columns are recoded).

Usage:   recode (inlist,listmap,cols=None)  cols=recode cols, listmap=2D list
Returns: inlist with the appropriate values replaced with new ones
```


  * ### printl ###
> `Alias for pl.`


  * ### linedelimited ###
```
Returns a string composed of elements in inlist, with each element
separated by 'delimiter.'  Used by function writedelimited.  Use '	'
for tab-delimiting.

Usage:   linedelimited (inlist,delimiter)
```


  * ### roundlist ###
```
Goes through each element in a 1D or 2D inlist, and applies the following
function to all elements of FloatType ... round(element,digits).

Usage:   roundlist(inlist,digits)
Returns: list with rounded floats
```


  * ### printincols ###
```
Prints a list of lists in columns of (fixed) colsize width, where
colsize is an integer.

Usage:   printincols (listoflists,colsize)
Returns: None
```


  * ### makelol ###
```
Converts a 1D list to a 2D list (i.e., a list-of-lists).  Useful when you
want to use put() to write a 1D list one item per line in the file.

Usage:   makelol(inlist)
Returns: if l = [1,2,'hi'] then returns [[1],[2],['hi']] etc.
```


  * ### pl ###
```
Prints a list of lists, 1 list (row) at a time.

Usage:   pl(listoflists)
Returns: None
```


  * ### flat ###
```
Returns the flattened version of a '2D' list.  List-correlate to the a.flat()
method of NumPy arrays.

Usage:    flat(l)
```


  * ### remap ###
```
Remaps values in a given column of a 2D list (listoflists).  This requires
a criterion as a function of 'x' so that the result of the following is
returned ... map(lambda x: 'criterion',listoflists).  

Usage:   remap(listoflists,criterion)    criterion=string
Returns: remapped version of listoflists
```


  * ### dm ###
```
Returns rows from the passed list of lists that meet the criteria in
the passed criterion expression (a string as a function of x; e.g., 'x[3]>=9'
will return all rows where the 4th column>=9 and "x[2]=='N'" will return rows
with column 2 equal to the string 'N').

Usage:   dm (listoflists, criterion)
Returns: rows from listoflists that meet the specified criterion.
```


  * ### collapse ###
```
Averages data in collapsecol, keeping all unique items in keepcols
(using unique, which keeps unique LISTS of column numbers), retaining the
unique sets of values in keepcols, the mean for each.  Setting fcn1
and/or fcn2 to point to a function rather than None (e.g., stats.sterr, len)
will append those results (e.g., the sterr, N) after each calculated mean.
cfcn is the collapse function to apply (defaults to mean, defined here in the
pstat module to avoid circular imports with stats.py, but harmonicmean or
others could be passed).

Usage:    collapse (listoflists,keepcols,collapsecols,fcn1=None,fcn2=None,cfcn=None)
Returns: a list of lists with all unique permutations of entries appearing in
     columns ("conditions") specified by keepcols, abutted with the result of
     cfcn (if cfcn=None, defaults to the mean) of each column specified by
     collapsecols.
```


  * ### abut ###
```
Like the |Stat abut command.  It concatenates two lists side-by-side
and returns the result.  '2D' lists are also accomodated for either argument
(source or addon).  CAUTION:  If one list is shorter, it will be repeated
until it is as long as the longest list.  If this behavior is not desired,
use pstat.simpleabut().

Usage:   abut(source, args)   where args=any # of lists
Returns: a list of lists as long as the LONGEST list past, source on the
         'left', lists in <args> attached consecutively on the 'right'
```


  * ### lineincustcols ###
```
Returns a string composed of elements in inlist, with each element
right-aligned in a column of width specified by a sequence colsizes.  The
length of colsizes must be greater than or equal to the number of columns
in inlist.

Usage:   lineincustcols (inlist,colsizes)
Returns: formatted string created from inlist
```


  * ### printcc ###
```
Prints a list of lists in columns, customized by the max size of items
within the columns (max size of items in col, plus 'extra' number of spaces).
Use 'dashes' or '\n' in the list-of-lists to print dashes or blank lines,
respectively.

Usage:   printcc (lst,extra=2)
Returns: None
```


  * ### unique ###
```
Returns all unique items in the passed list.  If the a list-of-lists
is passed, unique LISTS are found (i.e., items in the first dimension are
compared).

Usage:   unique (inlist)
Returns: the unique elements (or rows) in inlist
```


  * ### linexand ###
```
Returns the rows of a list of lists where col (from columnlist) = val
(from valuelist) for EVERY pair of values (columnlist[i],valuelists[i]).
len(columnlist) must equal len(valuelist).

Usage:   linexand (listoflists,columnlist,valuelist)
Returns: the rows of listoflists where columnlist[i]=valuelist[i] for ALL i
```


  * ### colex ###
```
Extracts from listoflists the columns specified in the list 'cnums'
(cnums can be an integer, a sequence of integers, or a string-expression that
corresponds to a slice operation on the variable x ... e.g., 'x[3:]' will colex
columns 3 onward from the listoflists).

Usage:   colex (listoflists,cnums)
Returns: a list-of-lists corresponding to the columns from listoflists
         specified by cnums, in the order the column numbers appear in cnums
```


  * ### lineincols ###
```
Returns a string composed of elements in inlist, with each element
right-aligned in columns of (fixed) colsize.

Usage:   lineincols (inlist,colsize)   where colsize is an integer
```


  * ### linexor ###
```
Returns the rows of a list of lists where col (from columnlist) = val
(from valuelist) for ANY pair of values (colunmlist[i],valuelist[i[).
One value is required for each column in columnlist.  If only one value
exists for columnlist but multiple values appear in valuelist, the
valuelist values are all assumed to pertain to the same column.

Usage:   linexor (listoflists,columnlist,valuelist)
Returns: the rows of listoflists where columnlist[i]=valuelist[i] for ANY i
```


  * ### sortby ###
```
Sorts a list of lists on the column(s) specified in the sequence
sortcols.

Usage:   sortby(listoflists,sortcols)
Returns: sorted list, unchanged column ordering
```