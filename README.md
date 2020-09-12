# Migrating to new Package
1. Refactor package name: https://stackoverflow.com/questions/16804093/rename-package-in-android-studio#answer-18637004
2. Update your Google service json file(if you have included)
3. Put [this](./R-resolver.py) program inside your Android root package. You need to change PARENT_DIR global variable of the program. Run the program.
4. If you have used service from Facebook then you will get error like this `The application could not be installed: INSTALL_FAILED_CONFLICTING_PROVIDER`. To solve this: 
- Watch this [video](https://youtu.be/2ZdzG_XObDM) to add facebook app id


## R-resolver.py
```
usage: R-resolver.py [-h] -o OLD_FILE -n NEW_FILE

optional arguments:
  -h, --help            show this help message and exit
  -o OLD_FILE, --old_file OLD_FILE
                        Old package name
  -n NEW_FILE, --new_file NEW_FILE
                        New package name
```