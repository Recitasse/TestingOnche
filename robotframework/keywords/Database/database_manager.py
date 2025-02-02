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
    else:
        info(f"", html=True)
    return databases

@trace_robot(TRACE_ENABLED)
@keyword("Vérifier la connexion à MySQL")
def check_connection(*args, **kwargs) -> bool:
    """
    Renvoie true si la connection à Mysql est établie
    :return: True sit connection établie
    """
    return bool(DatabaseManager())

@trace_robot(TRACE_ENABLED)
@keyword("Montrer tous les utilisateurs MySQL pour Onche")
def show_all_users(*args, **kwargs) -> Optional[Sequence[str]]:
    """
    Montre et renvoie tous les utilisateurs
    :return: None
    """
    users = DatabaseManager().get_all_users(startswith="Onch")
    if not users:
        warn("Il n'y a aucun utilisateur Onche", html=True)
    else:
        info(f"Liste des utilisateurs {users}", html=True)
    return users

@trace_robot(TRACE_ENABLED)
@keyword("Créer l'utilisateur ${utilisateur}",
         types={'utilisateur': 'str'})
def create_user(utilisateur: str, **kwargs) -> None:
    """
    Créer un utilisateur dans la base de donnée
    :param utilisateur:
    :return: None
    """
    DatabaseManager().create_user(utilisateur)
