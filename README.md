# FRED_API_Observation_Processor README

A Python script to read St. Louis Federal Reserve Bank Observations and insert them into a database. 

## Setup

This section will cover the setup and dependencies required to run the processor.

Ensure [Python 3.5][python] and Python package manager [PIP][pip] has been installed on your system.

Once PIP has been installed, install the following modules:

    pip install --user datetime
    pip install --user requests
    pip install --user configparser
    pip install --user psycopg2

Create or initialize a local Postgres database and run the script "FRED_Project/postgres/DDL/Create_Tables.sql" to initialize the example database tables.

Create an account for [Federal Reserve Bank of St. Louis][FRED] and request an API key to query the FRED API.

Once the database has been setup and an API key obtained, use the provided example configuration file "FRED_Project/config/config.example.ini" to create a configuration file named "FRED_Project/config/config.ini".  Populate with the appropriate database and login information. 

Once the setup is complete, the main file may be run using the command:

    python3.5 main.py

## License

This product uses the [FRED® API][FRED_API] but is not endorsed or certified by the Federal Reserve Bank of St. Louis.


#### (The MIT License)

Copyright (c) 2014 Bill Gooch

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
        distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

        The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
        EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
        IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
        TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



[python]: http://python.org/
[pip]: https://pip.pypa.io/en/stable/
[FRED]: https://fred.stlouisfed.org/
[FRED_API]: https://research.stlouisfed.org/docs/api/




