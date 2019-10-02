"""
Print Hello is a initiative which is led by two coding enthusiasts Naveen and Vipin who want to change the world with their belief that everyone can code and that too beautifully.
"""

def get_applications_python_datascience():
    python_applications = ["Python is free, open-source software, and consequently anyone can write a library package to extend its functionality. Data science has been an early beneficiary of these extensions, particularly Pandas, the big daddy of them all", "Pandas is the Python Data Analysis Library, used for everything from importing data from Excel spreadsheets to processing sets for time-series analysis. Pandas puts pretty much every common data munging tool at your fingertips. This means that basic cleanup and some advanced manipulation can be performed with Pandas’ powerful dataframes." "Pandas is built on top of NumPy, one of the earliest libraries behind Python’s data science success story. NumPy’s functions are exposed in Pandas for advanced numeric analysis." , "If you need something more specialized, chances are it’s out there", "SciPy is the scientific equivalent of NumPy, offering tools and techniques for analysis of scientific data. Statsmodels focuses on tools for statistical analysis.", "Scilkit-Learn and PyBrain are machine learning libraries that provide modules for building neural networks and data preprocessing."]

    for python_application_index in range(0, len(python_applications)+1):
        print python_applications[python_application_index]

         