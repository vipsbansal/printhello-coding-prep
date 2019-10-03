"""
Print Hello is a initiative which is led by two coding enthusiasts Naveen and Vipin who want to change the world with their belief that everyone can code and that too beautifully.
"""


def why_study_python():

    benefits_python_set1 = {
        
        'Be Pythonic' : "To start, I like Python as a language. In some sense the language is a jack-of-all-trades — you can follow a reasonable object-oriented paradigm, and can even get a taste for some functional programming ideas.",

        'You can have it all' : "If you’re looking for a batteries included solution to get a project off the ground, consider the framework Django. The project’s claim to fame is to “take care of much of the hassle of web development.” The idea is that tons of functionality is already built into an out-of-the-box Django app when you get it fired up, such as database solutions and HTML templating abilities (i.e. make pages generate content on the fly)."

        'You can have enough' : 'In stark contrast to Django (at least in the world of Python web frameworks) is the popular Flask framework. The first thing you’ll learn about Flask is that it’s a “micro” framework — one of its primary design goals is to have a light-weight core that developers can choose to extend in many ways. Flask is my framework of choice for your typical site where users surf around pages with dynamic content.',

    }

    benefits_python_set2 = {

        'Leverage the world of Python' : "Back to the language itself, Python is well-known for having a package for just about anything. I believe the core set of Python packages are very well-documented too, which makes a big difference. Some great examples are the widely used Numpy and SciPy packages to help with scientific computing.",

        'Easy deployment' : "At some point you’ll have an amazing web application that people need to see. Luckily, I’ve had a great experience deploying a Python application to the web. I’m a fan of Heroku for much of this task — Heroku takes care of lots of things for you, including building a virtual environment to install your Python dependencies, easy code changes by linking an app to a GitHub repository, creating a means to access your app on the web before dealing with domains and DNS if you wish, extremely useful error logging, and a nice way to add more computing power if you so decide.",

        'Great options for database work' : "Earlier I alluded to the flexibility I’ve experienced programming with the Flask framework. This point is especially true when it comes to database decisions. Python has a great suite of packages to deal with database connectivity, querying, and management."
    }

    for title,description in benefits_python_set1+benefits_python_set2:
        print title, description
        