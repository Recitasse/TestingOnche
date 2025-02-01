from robot.api.logger import *
from robot.api.deco import *
from OncheDatabase.tools.DatabaseManager import DatabaseManager


@keyword("Montrer toutes les bases de donnée")
def show_all_database():
    """
    Return all the database
    :return: List of all database
    """
    info(DatabaseManager().get_all_database(), html=True)
