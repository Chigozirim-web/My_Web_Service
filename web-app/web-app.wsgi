
import sys
sys.path.insert(0, 'carukwe/public_html/web-app')
        ##change this path later...(no longer on clamv)
activate_this = 'path of virtual env.../bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_read(), dict(__file__=activate_this))

import app as application
