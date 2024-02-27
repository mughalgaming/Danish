import os, sys
os.system("git pull")
try:
    _import_('DANI05').DANI()
except Exception as e:
      exit(str(e))
