# -*- coding: UTF-8 -*-

from configobj import ConfigObj
from collections import namedtuple
from dbconnection.connectionfactory import ConnectionFactory

###############################################################################
class Configuration(dict):

    # -------------------------------------------------------------------------
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__ = self


    # -------------------------------------------------------------------------
    def add_argparser_values(self, argparser):
        setattr(self, 'processname', argparser.prog.split(".")[0])
        namespace = argparser.parse_args()
        for arg in vars(namespace):
            if arg == "databases":
                self._databases(getattr(namespace, arg))
            setattr(self, arg, getattr(namespace, arg))

    # -------------------------------------------------------------------------
    def _databases(self, databases, dbconfig="/etc/databases.cnf"):

        parser = ConfigObj(dbconfig)

        for db in databases:
            connection = self._db_connection(parser, db[1], db[2])
            setattr(self, db[0], connection)

    # -------------------------------------------------------------------------
    def _db_connection(self, parser, host, database):

        engine = parser[host][database]['engine']

        if engine == "sqlite":
            return ConnectionFactory(
                        engine=engine,
                        connectionParameters=namedtuple(
                            'Parameters', "database")(database=database))

        username = parser[host][database]['user']
        password = parser[host][database]['password']
        return ConnectionFactory(
                    engine=engine,
                    connectionParameters=namedtuple(
                        'Parameters', "auth, host, database")(
                            namedtuple("Auth", "username, password")(
                                username=username,
                                password=password
                                ), host=host, database=database
                        ))

    # -------------------------------------------------------------------------
    def __str__(self):
        state = ["{} = {}".format(attribute, value)
                 for (attribute, value)
                 in self.__dict__.items()]
        return '\n'.join(state)