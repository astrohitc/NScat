.. test documentation master file, created by
   sphinx-quickstart on Mon Aug 23 21:31:52 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to test's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`




.. psrqpy documentation master file, created by
   sphinx-quickstart on Thu Nov 23 21:34:43 2017.
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




This package provides a way to directly query the `ATNF Pulsar Catalogue <http://www.atnf.csiro.au/people/pulsar/psrcat/>`_ [1]_ using Python. It does this by
downloading and parsing the full catalogue database, which itself is cached and can
be reused. It is primarily aimed at astronomers wanting access to the latest pulsar
information via a script, rather than through the standard web interface.

Other functionality that it includes:

 * it can produce a :math:`P-\dot{P}` :ref:`diagram <make-p-pdot-diagram>` using the latest catalogue information.
 * a function (:func:`~psrqpy.utils.get_glitch_catalogue`) to access the `Jodrell Bank pulsar glitch catalogue <http://www.jb.man.ac.uk/pulsar/glitches.html>`_.

Installation
============

This package is right now uploaded on the test instance of PyPI so it can be installed using the following command:-

This command can be run on the Ananconda prompt on Windows and the Linux terminal for Linux users. The can package can installed using::
         
                     ``pip install -i https://test.pypi.org/simple/ mag-pip-rc1`` 
 




       ``pip install -i https://test.pypi.org/simple/ mag-pip-rc1`` 





This package can be installed using ``pip`` via ``pip install psrqpy`` or ``conda`` using ``conda install -c conda-forge psrqpy``. Alternatively
the source code can be obtained from `github <https://github.com/mattpitkin/psrqpy>`_, and installed using::

    python setup.py install

with ``sudo`` if wanted to install system wide, and with the ``--user`` flag
if just installing for an individual user.

Requirements
------------



The requirements for installing the code are:

 * :mod:`requests`
 * :mod:`pandas`
 * :mod:`numpy`
 * :mod:`io`
 * :mod:`matplotlib`
 




The requirements for installing the code are:

 * :mod:`requests`
 * :mod:`bs4`
 * :mod:`numpy`
 * :mod:`astropy`
 * :mod:`pandas`
 * :mod:`scipy`

The :mod:`ads` module and :mod:`matplotlib` are optional requirements to get the full functionality.

Examples
========

Downloading the full database can be simply achieved via

    >>> from mag_pip_rci import code
    >>> mag = code.mag()
    
    
   
To search by specifying condition of parameters(in this e.g-spin period)

   >>> mag.loc[(mag['Period < 5']), ['Name', 'Period']]
   
   >>> mag.loc[(mag['Name'] == '1E 1841-045'), ['Name', 'RA', 'Decl','Age','Ref_Radio', 'Ref_MidIR', 'Assoc', 'SNRAge']]          

 
 
 
 

From this query the database can then be accessed as an :class:`astropy.table.Table` via

    >>> table = query.table

or as a :class:`pandas.DataFrame` via

    >>> df = query.pandas

