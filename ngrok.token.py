#!/usr/bin/env python

import os 


print("""
____ _ _ _ ____ _   _ ___  _ 
[__  | | | |  |  \_/    /  | 
___] |_|_| |__|   |    /__ |

""")
authtoken  =   input ( "ngrok authtoken gir:")

authtoken = os.system("ngrok "+authtoken)

os.system("python ngrok.py")
