=================
Cvedetails-lookup
=================

**Small script to perform CVE lookup on cvedetails.com Database (https://www.cvedetails.com)**.

This script requests cvedetails.com to search for CVE on a given product.

============
Installation
============

Install Python3 dependencies:

.. code-block:: console

    sudo pip3 install -r requirements.txt


=====
Usage
=====

**Search for CVE by providing a list services.txt

services.txt format "product name" - "version"

**Run command as follows

python script.py 

**Output gets saved in result output.csv

=======
Example
=======

Save "Nginx - 1.14.21" in services.txt
 
python script.py



Credits: Vishesh Grover 
Github: Rover141





