# /usr/bin/env python
# -*- coding: UTF-8 -*-

from configure.configure import Configuration
from defaultargs.defaultargs import databaseargs, defaultargs


# ----------------------------------------------------------------------
def main():

    conf = Configuration(keyword="Keyword Value")
    conf.add_argparser_values(parseargs())

    conf.variable1 = "Variable1 Value"
    conf['Varable 2'] = "Variable 2 Value"
    print(conf)
    print(len(conf))

    print(conf.variable1)
    print(conf['variable1'])
    SQL = "SELECT * FROM AccountDirectDebitInstructions"
    selection = conf.ms.select(SQL)
    for r in selection:
        print(r)


# ----------------------------------------------------------------------
@databaseargs
def parseargs():
    pass


# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
