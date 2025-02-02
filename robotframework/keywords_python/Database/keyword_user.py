from typing import Sequence, Optional
from config.GLOBAL import TRACE_ENABLED

from utils.onchenv import trace_robot
from robot.api.logger import *
from robot.api.deco import *
from OncheDatabase.tools.DatabaseManager import DatabaseManager


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
         types={'utilisateur': str})
def create_user(utilisateur: str, **kwargs) -> None:
    """
    Créer un utilisateur dans la base de donnée
    :param utilisateur:
    :return: None
    """
    DatabaseManager().create_user(utilisateur)

@trace_robot(TRACE_ENABLED)
@keyword("Effacer l'utilisateur ${utilisateur}",
         types={'utilisateur': str})
def delete_user(utilisateur: str, **kwargs) -> None:
    """
    Efface un utilisateur dans la base de donnée
    :param utilisateur:
    :return: None
    """
    DatabaseManager().delete_users(utilisateur)

@trace_robot(TRACE_ENABLED)
@keyword("Ajouter les droits ${right} à l'utilisateur ${utilisateur} sur les bases de donnée ${databases}",
         types={'right': Sequence[str] ,'utilisateur': str, 'databases': Sequence[str]})
def add_right_to_user(right: Sequence[str], utilisateur: str, databases: Sequence[str], **kwargs) -> None:
    """
    Ajoute un droit à un utilisateur
    :param right: les droits à ajouter
    :param utilisateur: l'utilisateur dont on modifie les droits
    :param databases: les databases sur lesquelles on donne un droit
    :param kwargs: None
    :return: None
    """
    DatabaseManager().add_right_user(utilisateur, right, databases)

@trace_robot(TRACE_ENABLED)
@keyword("Ajouter les droits ${right} à l'utilisateur ${utilisateur} sur les bases de donnée ${databases}",
         types={'right': Sequence[str] ,'utilisateur': str, 'databases': Sequence[str]})
def revoke_right_to_user(right: Sequence[str], utilisateur: str, databases: Sequence[str], **kwargs) -> None:
    """
    Retire un droit à un utilisateur
    :param right: les droits à ajouter
    :param utilisateur: l'utilisateur dont on modifie les droits
    :param databases: les databases sur lesquelles on donne un droit
    :param kwargs: None
    :return: None
    """
    DatabaseManager().revoke_right_user(utilisateur, right, databases)