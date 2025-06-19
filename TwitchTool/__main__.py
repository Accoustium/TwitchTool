import os
import eel

# Set web files folder
path = os.path.dirname(os.path.abspath(__file__))
eel.init(os.path.join(path, 'web'))

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('index.html', size=(300, 200))  # Start