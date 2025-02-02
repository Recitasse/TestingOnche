from typing import Sequence, Optional
from config.GLOBAL import TRACE_ENABLED

from utils.onchenv import trace_robot
from robot.api.logger import *
from robot.api.deco import *
from OncheDatabase.tools.DatabaseManager import DatabaseManager


@trace_robot(TRACE_ENABLED)
@keyword("Montrer toutes les bases de donnée de Onche")
def show_all_database(*args, **kwargs) -> Optional[Sequence[str]]:
    """
    Retourne toutes les bases de données
    :return: Liste des bases de donnée
    """
    databases = DatabaseManager().get_all_database(startswith="Onch")
    if not databases:
        warn("Il n'y a aucune base de donnée Onche", html=True)
    return databases

@trace_robot(TRACE_ENABLED)
@keyword("Montrer toutes les bases de donnée")
def show_all_database(*args, **kwargs) -> Optional[Sequence[str]]:
    """
    Retourne toutes les bases de données
    :return: Liste des bases de donnée
    """
    databases = DatabaseManager().get_all_database()
    if not databases:
        warn("Il n'y a aucune base de donnée", html=True)
    return databases

@trace_robot(TRACE_ENABLED)
@keyword("Créer la base de donnée ${database}",
         types={'database': str})
def create_database(database: str, **kwargs) -> None:
    """
    Créer une base de donnée de no donnée
    :param database: nom de la base de donnée
    :return: None
    """
    DatabaseManager().create_database(database)

@trace_robot(TRACE_ENABLED)
@keyword("Effacer la base de donnée ${database}",
         types={'database': str})
def create_database(database: str, **kwargs) -> None:
    """
    Efface une base de donnée de no donnée
    :param database: nom de la base de donnée
    :return: None
    """
    DatabaseManager().delete_database(database)
