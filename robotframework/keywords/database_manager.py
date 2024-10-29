from robot.api.logger import *
from robot.api.deco import *
from OncheDatabase.database_manager import DatabaseManager
from typing import Sequence


@keyword("Montrer toutes les bases de donnée")
def show_all_database() -> Sequence[str]:
    """
    Return all the database
    :return: List of all database
    """
    print(DatabaseManager().available_databases())
    return DatabaseManager().available_databases()