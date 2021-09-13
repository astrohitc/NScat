.. test documentation master file, created by
   sphinx-quickstart on Mon Aug 23 21:31:52 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: <isonum.txt>

.. _reference:

The McGill-Magnetar-Catalog
==================

.. automodule:: magcat



This python package is used for querying the McGill magnetar catalog,  (Olausen & Kaspi, 2014), and please refer to the URL (http://www.physics.mcgill.ca/~pulsar/magnetar/main.html).

While using the catalog from the specified URL, the user neither has an option to search directly nor can search by specifying any conditions on the parameters of magnetars. 

This package attempts to solve this problem. It provides a python interface to the user to query the McGill Magnetar Catalog. 

We also plan to add a graph plotter. 

It is neither affiliated nor endorsed by the Magnetar group at McGill University. 

Comments and suggestions are welcome. This package is under development. 




Installation
============

This package is right now uploaded on the test instance of PyPI so it can be installed using the following command:-

This command can be run on the Ananconda prompt on Windows and the Linux terminal for Linux users. The can package can installed using::
         
                     ``pip install -i https://test.pypi.org/simple/ mag-pip-rc1`` 




Requirements
------------



The requirements for installing the code are:

 * :mod:`requests`
 * :mod:`pandas`
 * :mod:`numpy`
 * :mod:`io`
 * :mod:`matplotlib`
 




Examples
========

Downloading the full database can be simply achieved via

    >>> from mag_pip_rci import code
    >>> mag = code.mag()
    
    
   
To search by specifying condition of parameters(in this e.g-spin period)

   >>> mag.loc[(mag['Period < 5']), ['Name', 'Period']]
   
   >>> mag.loc[(mag['Name'] == '1E 1841-045'), ['Name', 'RA', 'Decl','Age','Ref_Radio', 'Ref_MidIR', 'Assoc', 'SNRAge']]    
   
   
To search

Welcome to Magcat!
please refer to the documentation
                     Name  Period(McGill)  Period(atnf)     B(McGill)  \
0   CXOU J010043.1-721134        8.020392      8.020392  3.930000e+14   
1              4U 0142+61        8.688692      8.688994  1.340000e+14   
2           SGR 0418+5729        9.078388      9.078388  6.100000e+12   
3           SGR 0501+4516        5.762069      5.762097  1.870000e+14   
4             SGR 0526-66        8.054400      8.047000  5.600000e+14   
5          1E 1048.1-5937        6.457875      6.452077  3.860000e+14   
6          1E 1547.0-5408        2.072125      2.069833  3.180000e+14   
7          PSR J1622-4950        4.326100      4.327020  2.740000e+14   
8             SGR 1627-41        2.594578      2.594578  2.250000e+14   
9   CXOU J164710.2-455216       10.610644     10.610660  6.590000e+13   
10  1RXS J170849.0-400910       11.005025     11.006260  4.680000e+14   
11  CXOU J171405.7-381031        3.825352      3.824936  5.010000e+14   
12         SGR J1745-2900        3.763638      3.763733  2.310000e+14   
13            SGR 1806-20        7.547730      7.555920  1.960000e+15   
14          XTE J1810-197        5.540354      5.540743  2.100000e+14   
15     Swift J1818.0-1607        1.363490      8.437721  3.540000e+14   
16     Swift J1822.3-1606        8.437721      7.565408  1.360000e+13   
17          SGR 1833-0832        7.565408      2.482302  1.650000e+14   
18     Swift J1834.9-0846        2.482302     11.788980  1.420000e+14   
19            1E 1841-045       11.788978     11.558710  7.030000e+14   
20  3XMM J185246.6+003317       11.558713      5.198346  4.070000e+13   
21            SGR 1900+14        5.199870      3.244980  7.000000e+14   
22          SGR 1935+2154        3.245065      6.979071  2.180000e+14   
23            1E 2259+586        6.979043           NaN  5.880000e+13   
24        SGR 0755-2933 #             NaN           NaN           NaN   
25          SGR 1801-23 #             NaN           NaN           NaN   
26          SGR 1808-20 #             NaN           NaN           NaN   
27      AX J1818.8-1559 #             NaN           NaN           NaN   
28      AX J1845.0-0258 #        6.971270           NaN           NaN   
29          SGR 2013+34 #             NaN           NaN           NaN   
30      PSR J1846-0258 ##        0.326571           NaN  4.880000e+13   

         B(atnf)  
0   3.930000e+14  
1   1.330000e+14  
2   6.170000e+12  
3   1.850000e+14  
4   7.320000e+14  
5   5.020000e+14  
6   2.220000e+14  
7   1.110000e+14  
8            NaN  
9   9.510000e+13  
10  4.700000e+14  
11  4.800000e+14  
12  2.600000e+14  
13  2.060000e+15  
14  1.270000e+14  
15  1.360000e+13  
16  1.630000e+14  
17  1.420000e+14  
18  7.030000e+14  
19           NaN  
20  7.000000e+14  
21           NaN  
22  5.800000e+13  
23           NaN  
24           NaN  
25           NaN  
26           NaN  
27           NaN  
28           NaN  
29           NaN  
30           NaN  
type s if you want to query a single parameter else type m for multiple parameterss
What parameter would you like to queryName
                     Name
0   CXOU J010043.1-721134
1              4U 0142+61
2           SGR 0418+5729
3           SGR 0501+4516
4             SGR 0526-66
5          1E 1048.1-5937
6          1E 1547.0-5408
7          PSR J1622-4950
8             SGR 1627-41
9   CXOU J164710.2-455216
10  1RXS J170849.0-400910
11  CXOU J171405.7-381031
12         SGR J1745-2900
13            SGR 1806-20
14          XTE J1810-197
15     Swift J1818.0-1607
16     Swift J1822.3-1606
17          SGR 1833-0832
18     Swift J1834.9-0846
19            1E 1841-045
20  3XMM J185246.6+003317
21            SGR 1900+14
22          SGR 1935+2154
23            1E 2259+586
24        SGR 0755-2933 #
25          SGR 1801-23 #
26          SGR 1808-20 #
27      AX J1818.8-1559 #
28      AX J1845.0-0258 #
29          SGR 2013+34 #
30      PSR J1846-0258 ##
if you want to save the table as a csv file type 'y' else type 'n' :n

 
 
