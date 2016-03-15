A collection of basic statistical functions for python.

  * ### Dispatch ###
```
The Dispatch class, care of David Ascher, allows different functions to
be called depending on the argument types.  This way, there can be one
function name regardless of the argument type.  To access function doc
in stats.py module, prefix the function with an 'l' or 'a' for list or
array arguments, respectively.  That is, print stats.lmean.__doc__ or
print stats.amean.__doc__ or whatever.
```


## Function List ##
  * ### F\_oneway ###
```
Performs a 1-way ANOVA, returning an F-value and probability given
any number of groups.  From Heiman, pp.394-7.

Usage:   F_oneway(*lists)    where *lists is any number of lists, one per
                                  treatment group
Returns: F value, one-tailed p-value
```


  * ### writecc ###
```
Writes a list of lists to a file in columns, customized by the max
size of items within the columns (max size of items in col, +2 characters)
to specified file.  File-overwrite is the default.

Usage:   writecc (listoflists,file,writetype='w',extra=2)
Returns: None
```


  * ### gammln ###
```
Returns the gamma function of xx.
    Gamma(z) = Integral(0,infinity) of t^(z-1)exp(-t) dt.
(Adapted from: Numerical Recipies in C.)

Usage:   lgammln(xx)
```


  * ### trimboth ###
```
Slices off the passed proportion of items from BOTH ends of the passed
list (i.e., with proportiontocut=0.1, slices 'leftmost' 10% AND 'rightmost'
10% of scores.  Assumes list is sorted by magnitude.  Slices off LESS if
proportion results in a non-integer slice index (i.e., conservatively
slices off proportiontocut).

Usage:   ltrimboth (l,proportiontocut)
Returns: trimmed version of list l
```


  * ### summult ###
```
Multiplies elements in list1 and list2, element by element, and
returns the sum of all resulting multiplications.  Must provide equal
length lists.

Usage:   lsummult(list1,list2)
```


  * ### friedmanchisquare ###
```
Friedman Chi-Square is a non-parametric, one-way within-subjects
ANOVA.  This function calculates the Friedman Chi-square test for repeated
measures and returns the result, along with the associated probability
value.  It assumes 3 or more repeated measures.  Only 3 levels requires a
minimum of 10 subjects in the study.  Four levels requires 5 subjects per
level(??).

Usage:   lfriedmanchisquare(*args)
Returns: chi-square statistic, associated p-value
```


  * ### outputpairedstats ###
```
Prints or write to a file stats for two groups, using the name, n,
mean, sterr, min and max for each group, as well as the statistic name,
its value, and the associated p-value.

Usage:   outputpairedstats(fname,writemode,
                           name1,n1,mean1,stderr1,min1,max1,
                           name2,n2,mean2,stderr2,min2,max2,
                           statname,stat,prob)
Returns: None
```


  * ### cumsum ###
```
Returns a list consisting of the cumulative sum of the items in the
passed list.

Usage:   lcumsum(inlist)
```


  * ### geometricmean ###
```
Calculates the geometric mean of the values in the passed list.
That is:  n-th root of (x1 * x2 * ... * xn).  Assumes a '1D' list.

Usage:   lgeometricmean(inlist)
```


  * ### ss ###
```
Squares each value in the passed list, adds up these squares and
returns the result.

Usage:   lss(inlist)
```


  * ### sum ###
```
Returns the sum of the items in the passed list.

Usage:   lsum(inlist)
```


  * ### scoreatpercentile ###
```
Returns the score at a given percentile relative to the distribution
given by inlist.

Usage:   lscoreatpercentile(inlist,percent)
```


  * ### spearmanr ###
```
Calculates a Spearman rank-order correlation coefficient.  Taken
from Heiman's Basic Statistics for the Behav. Sci (1st), p.192.

Usage:   lspearmanr(x,y)      where x and y are equal-length lists
Returns: Spearman's r, two-tailed p-value
```


  * ### samplestdev ###
```
Returns the standard deviation of the values in the passed list using
N for the denominator (i.e., DESCRIBES the sample stdev only).

Usage:   lsamplestdev(inlist)
```


  * ### harmonicmean ###
```
Calculates the harmonic mean of the values in the passed list.
That is:  n / (1/x1 + 1/x2 + ... + 1/xn).  Assumes a '1D' list.

Usage:   lharmonicmean(inlist)
```


  * ### median ###
```
Returns the computed median value of a list of numbers, given the
number of bins to use for the histogram (more bins brings the computed value
closer to the median score, default number of bins = 1000).  See G.W.
Heiman's Basic Stats (1st Edition), or CRC Probability & Statistics.

Usage:   lmedian (inlist, numbins=1000)
```


  * ### trim1 ###
```
Slices off the passed proportion of items from ONE end of the passed
list (i.e., if proportiontocut=0.1, slices off 'leftmost' or 'rightmost'
10% of scores).  Slices off LESS if proportion results in a non-integer
slice index (i.e., conservatively slices off proportiontocut).

Usage:   ltrim1 (l,proportiontocut,tail='right')  or set tail='left'
Returns: trimmed version of list l
```


  * ### mode ###
```
Returns a list of the modal (most common) score(s) in the passed
list.  If there is more than one such score, all are returned.  The
bin-count for the mode(s) is also returned.

Usage:   lmode(inlist)
Returns: bin-count for mode(s), a list of modal value(s)
```


  * ### ttest\_ind ###
```
Calculates the t-obtained T-test on TWO INDEPENDENT samples of
scores a, and b.  From Numerical Recipies, p.483.  If printit=1, results
are printed to the screen.  If printit='filename', the results are output
to 'filename' using the given writemode (default=append).  Returns t-value,
and prob.

Usage:   lttest_ind(a,b,printit=0,name1='Samp1',name2='Samp2',writemode='a')
Returns: t-value, two-tailed prob
```


  * ### pointbiserialr ###
```
Calculates a point-biserial correlation coefficient and the associated
probability value.  Taken from Heiman's Basic Statistics for the Behav.
Sci (1st), p.194.

Usage:   lpointbiserialr(x,y)      where x,y are equal-length lists
Returns: Point-biserial r, two-tailed p-value
```


  * ### rankdata ###
```
Ranks the data in inlist, dealing with ties appropritely.  Assumes
a 1D inlist.  Adapted from Gary Perlman's |Stat ranksort.

Usage:   lrankdata(inlist)
Returns: a list of length equal to inlist, containing rank scores
```


  * ### kruskalwallish ###
```
The Kruskal-Wallis H-test is a non-parametric ANOVA for 3 or more
groups, requiring at least 5 subjects in each group.  This function
calculates the Kruskal-Wallis H-test for 3 or more independent samples
and returns the result.  

Usage:   lkruskalwallish(*args)
Returns: H-statistic (corrected for ties), associated p-value
```


  * ### ranksums ###
```
Calculates the rank sums statistic on the provided scores and
returns the result.  Use only when the n in each condition is > 20 and you
have 2 independent samples of ranks.

Usage:   lranksums(x,y)
Returns: a z-statistic, two-tailed p-value
```


  * ### variation ###
```
Returns the coefficient of variation, as defined in CRC Standard
Probability and Statistics, p.6.

Usage:   lvariation(inlist)
```


  * ### tiecorrect ###
```
Corrects for ties in Mann Whitney U and Kruskal Wallis H tests.  See
Siegel, S. (1956) Nonparametric Statistics for the Behavioral Sciences.
New York: McGraw-Hill.  Code adapted from |Stat rankind.c code.

Usage:   ltiecorrect(rankvals)
Returns: T correction factor for U or H
```


  * ### paired ###
```
Interactively determines the type of data and then runs the
appropriated statistic for paired group data.

Usage:   lpaired(x,y)
Returns: appropriate statistic name, value, and probability
```


  * ### sumdiffsquared ###
```
Takes pairwise differences of the values in lists x and y, squares
these differences, and returns the sum of these squares.

Usage:   lsumdiffsquared(x,y)
Returns: sum[(x[i]-y[i])**2]
```


  * ### betai ###
```
Returns the incomplete beta function:

    I-sub-x(a,b) = 1/B(a,b)*(Integral(0,x) of t^(a-1)(1-t)^(b-1) dt)

where a,b>0 and B(a,b) = G(a)*G(b)/(G(a+b)) where G(a) is the gamma
function of a.  The continued fraction formulation is implemented here,
using the betacf function.  (Adapted from: Numerical Recipies in C.)

Usage:   lbetai(a,b,x)
```


  * ### percentileofscore ###
```
Returns the percentile value of a score relative to the distribution
given by inlist.  Formula depends on the values used to histogram the data(!).

Usage:   lpercentileofscore(inlist,score,histbins=10,defaultlimits=None)
```


  * ### z ###
```
Returns the z-score for a given input score, given that score and the
list from which that score came.  Not appropriate for population calculations.

Usage:   lz(inlist, score)
```


  * ### var ###
```
Returns the variance of the values in the passed list using N-1
for the denominator (i.e., for estimating population variance).

Usage:   lvar(inlist)
```


  * ### describe ###
```
Returns some descriptive statistics of the passed list (assumed to be 1D).

Usage:   ldescribe(inlist)
Returns: n, mean, standard deviation, skew, kurtosis
```


  * ### wilcoxont ###
```
Calculates the Wilcoxon T-test for related samples and returns the
result.  A non-parametric T-test.

Usage:   lwilcoxont(x,y)
Returns: a t-statistic, two-tail probability estimate
```


  * ### findwithin ###
```
Returns an integer representing a binary vector, where 1=within-
subject factor, 0=between.  Input equals the entire data 2D list (i.e.,
column 0=random factor, column -1=measured values (those two are skipped).
Note: input data is in |Stat format ... a list of lists ("2D list") with 
one row per measured value, first column=subject identifier, last column=
score, one in-between column per factor (these columns contain level
designations on each factor).  See also stats.anova.__doc__.

Usage:   lfindwithin(data)     data in |Stat format
```


  * ### shellsort ###
```
Shellsort algorithm.  Sorts a 1D-list.

Usage:   lshellsort(inlist)
Returns: sorted-inlist, sorting-index-vector (for original list)
```


  * ### zs ###
```
Returns a list of z-scores, one for each score in the passed list.

Usage:   lzs(inlist)
```


  * ### relfreq ###
```
Returns a relative frequency histogram, using the histogram function.

Usage:   lrelfreq(inlist,numbins=10,defaultreallimits=None)
Returns: list of cumfreq bin values, lowerreallimit, binsize, extrapoints
```


  * ### square\_of\_sums ###
```
Adds the values in the passed list, squares the sum, and returns
the result.

Usage:   lsquare_of_sums(inlist)
Returns: sum(inlist[i])**2
```


  * ### F\_value ###
```
Returns an F-statistic given the following:
        ER  = error associated with the null hypothesis (the Restricted model)
        EF  = error associated with the alternate hypothesis (the Full model)
        dfR-dfF = degrees of freedom of the numerator
        dfF = degrees of freedom associated with the denominator/Full model

Usage:   lF_value(ER,EF,dfnum,dfden)
```


  * ### kurtosis ###
```
Returns the kurtosis of a distribution, as defined in Numerical
Recipies (alternate defn in CRC Standard Probability and Statistics, p.6.)

Usage:   lkurtosis(inlist)
```


  * ### linregress ###
```
Calculates a regression line on x,y pairs.  

Usage:   llinregress(x,y)      x,y are equal-length lists of x-y coordinates
Returns: slope, intercept, r, two-tailed prob, sterr-of-estimate
```


  * ### sterr ###
```
Returns the standard error of the values in the passed list using N-1
in the denominator (i.e., to estimate population standard error).

Usage:   lsterr(inlist)
```


  * ### itemfreq ###
```
Returns a list of pairs.  Each pair consists of one of the scores in inlist
and it's frequency count.  Assumes a 1D list is passed.

Usage:   litemfreq(inlist)
Returns: a 2D frequency table (col [0:n-1]=scores, col n=frequencies)
```


  * ### fprob ###
```
Returns the (1-tailed) significance level (p-value) of an F
statistic given the degrees of freedom for the numerator (dfR-dfF) and
the degrees of freedom for the denominator (dfF).

Usage:   lfprob(dfnum, dfden, F)   where usually dfnum=dfbn, dfden=dfwn
```


  * ### mean ###
```
Returns the arithematic mean of the values in the passed list.
Assumes a '1D' list, but will function on the 1st dim of an array(!).

Usage:   lmean(inlist)
```


  * ### chisqprob ###
```
Returns the (1-tailed) probability value associated with the provided
chi-square value and df.  Adapted from chisq.c in Gary Perlman's |Stat.

Usage:   lchisqprob(chisq,df)
```


  * ### skew ###
```
Returns the skewness of a distribution, as defined in Numerical
Recipies (alternate defn in CRC Standard Probability and Statistics, p.6.)

Usage:   lskew(inlist)
```


  * ### stdev ###
```
Returns the standard deviation of the values in the passed list
using N-1 in the denominator (i.e., to estimate population stdev).

Usage:   lstdev(inlist)
```


  * ### ttest\_rel ###
```
Calculates the t-obtained T-test on TWO RELATED samples of scores,
a and b.  From Numerical Recipies, p.483.  If printit=1, results are
printed to the screen.  If printit='filename', the results are output to
'filename' using the given writemode (default=append).  Returns t-value,
and prob.

Usage:   lttest_rel(a,b,printit=0,name1='Sample1',name2='Sample2',writemode='a')
Returns: t-value, two-tailed prob
```


  * ### samplevar ###
```
Returns the variance of the values in the passed list using
N for the denominator (i.e., DESCRIBES the sample variance only).

Usage:   lsamplevar(inlist)
```


  * ### ksprob ###
```
Computes a Kolmolgorov-Smirnov t-test significance level.  Adapted from
Numerical Recipies.

Usage:   lksprob(alam)
```


  * ### zprob ###
```
Returns the area under the normal curve 'to the left of' the given z value.
Thus, 
    for z<0, zprob(z) = 1-tail probability
    for z>0, 1.0-zprob(z) = 1-tail probability
    for any z, 2.0*(1.0-zprob(abs(z))) = 2-tail probability
Adapted from z.c in Gary Perlman's |Stat.

Usage:   lzprob(z)
```


  * ### ks\_2samp ###
```
Computes the Kolmogorov-Smirnof statistic on 2 samples.  From
Numerical Recipies in C, page 493.

Usage:   lks_2samp(data1,data2)   data1&2 are lists of values for 2 conditions
Returns: KS D-value, associated p-value
```


  * ### sem ###
```
Returns the estimated standard error of the mean (sx-bar) of the
values in the passed list.  sem = stdev / sqrt(n)

Usage:   lsem(inlist)
```


  * ### pearsonr ###
```
Calculates a Pearson correlation coefficient and the associated
probability value.  Taken from Heiman's Basic Statistics for the Behav.
Sci (2nd), p.195.

Usage:   lpearsonr(x,y)      where x and y are equal-length lists
Returns: Pearson's r value, two-tailed p-value
```


  * ### kendalltau ###
```
Calculates Kendall's tau ... correlation of ordinal data.  Adapted
from function kendl1 in Numerical Recipies.  Needs good test-routine.@@@

Usage:   lkendalltau(x,y)
Returns: Kendall's tau, two-tailed p-value
```


  * ### obrientransform ###
```
Computes a transform on input data (any number of columns).  Used to
test for homogeneity of variance prior to running one-way stats.  From
Maxwell and Delaney, p.112.

Usage:   lobrientransform(*args)
Returns: transformed data for use in an ANOVA
```


  * ### histogram ###
```
Returns (i) a list of histogram bin counts, (ii) the smallest value
of the histogram binning, and (iii) the bin width (the last 2 are not
necessarily integers).  Default number of bins is 10.  If no sequence object
is given for defaultreallimits, the routine picks (usually non-pretty) bins
spanning all the numbers in the inlist.

Usage:   lhistogram (inlist, numbins=10, defaultreallimits=None,suppressoutput=0)
Returns: list of bin values, lowerreallimit, binsize, extrapoints
```


  * ### erfcc ###
```
Returns the complementary error function erfc(x) with fractional
error everywhere less than 1.2e-7.  Adapted from Numerical Recipies.

Usage:   lerfcc(x)
```


  * ### ttest\_1samp ###
```
Calculates the t-obtained for the independent samples T-test on ONE group
of scores a, given a population mean.  If printit=1, results are printed
to the screen.  If printit='filename', the results are output to 'filename'
using the given writemode (default=append).  Returns t-value, and prob.

Usage:   lttest_1samp(a,popmean,Name='Sample',printit=0,writemode='a')
Returns: t-value, two-tailed prob
```


  * ### medianscore ###
```
Returns the 'middle' score of the passed list.  If there is an even
number of scores, the mean of the 2 middle scores is returned.

Usage:   lmedianscore(inlist)
```


  * ### betacf ###
```
This function evaluates the continued fraction form of the incomplete
Beta function, betai.  (Adapted from: Numerical Recipies in C.)

Usage:   lbetacf(a,b,x)
```


  * ### moment ###
```
Calculates the nth moment about the mean for a sample (defaults to
the 1st moment).  Used to calculate coefficients of skewness and kurtosis.

Usage:   lmoment(inlist,moment=1)
Returns: appropriate moment (r) from ... 1/n * SUM((inlist(i)-mean)**r)
```


  * ### chisquare ###
```
Calculates a one-way chi square for list of observed frequencies and returns
the result.  If no expected frequencies are given, the total N is assumed to
be equally distributed across all groups.

Usage:   lchisquare(f_obs, f_exp=None)   f_obs = list of observed cell freq.
Returns: chisquare-statistic, associated p-value
```


  * ### cumfreq ###
```
Returns a cumulative frequency histogram, using the histogram function.

Usage:   lcumfreq(inlist,numbins=10,defaultreallimits=None)
Returns: list of cumfreq bin values, lowerreallimit, binsize, extrapoints
```


  * ### mannwhitneyu ###
```
Calculates a Mann-Whitney U statistic on the provided scores and
returns the result.  Use only when the n in each condition is < 20 and
you have 2 independent samples of ranks.  NOTE: Mann-Whitney U is
significant if the u-obtained is LESS THAN or equal to the critical
value of U found in the tables.  Equivalent to Kruskal-Wallis H with
just 2 groups.

Usage:   lmannwhitneyu(data)
Returns: u-statistic, one-tailed p-value (i.e., p(z(U)))
```


  * ### incr ###
```
Simulate a counting system from an n-dimensional list.

Usage:   lincr(l,cap)   l=list to increment, cap=max values for each list pos'n
Returns: next set of values for list l, OR -1 (if overflow)
```