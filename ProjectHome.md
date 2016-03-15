# Due to time constraints this project is not actively developed anymore. If you wish to take over send an email to the owner. #

The goal of the project is to combine several python statistics modules into a single package. This project is being run under the auspices of the [Python Project for the Google Highly Open Participation Contest](http://code.google.com/p/google-highly-open-participation-psf/)

Typical use case:

```
from statlib import stats

a = [1, 2, 3, 4 ]
# mean and standard deviation
print stats.mean(a), stats.stdev(a)

# vector operations
from statlib.matfunc import Vec
a = Vec( [ 4, -2,  5 ] ) 
b = Vec( [ 3, 10, -6 ] )

# vector dot and cross products
print a * b, a.cross(b)
```

For more information see the following pages:

  * the **stats** module (see StatsDoc) contains a collection of basic statistical functions for python
  * the **pstat** module (see PstatDoc) contains useful list and array manipulation routines modeled after those found in the [|Stat](http://oldwww.acm.org/perlman/stat/) package by Gary Perlman
  * the **matfunc** module (see [this help page](http://users.rcn.com/python/download/matfunc.htm)) is a python module for vector, matrix, and table math operations

**Note:** This a _pure-python_ package with no other dependency. For high performance numerical/scientific computing we recommend [numpy](http://numpy.scipy.org/).

## Installation ##

If you have setuptools installed (see [easy\_install](http://peak.telecommunity.com/DevCenter/EasyInstall)) simply type:

```
easy_install statlib
```

Otherwise visit the [download](http://code.google.com/p/python-statlib/downloads/list) page and download the version for your operating system.

## Credits ##

See the [Contributors](Contributors.md) page

## Change Log ##

### Version 1.1, Dec 19, 2007 ###
  * _Gary Strangman_ re-released his code under MIT license. _Many Thanks!_
  * all code relicensed under MIT license.
  * **stats.py** now works with numpy arrays.

### Version 1.0, Dec 17, 2007 ###
  * Project created as a Python GHOP task.
  * Package creation.
  * This release is tagged **release-1.0** in the repository