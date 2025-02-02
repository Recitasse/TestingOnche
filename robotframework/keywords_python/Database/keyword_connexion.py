from typing import Sequence, Optional
from config.GLOBAL import TRACE_ENABLED

from utils.onchenv import trace_robot
from robot.api.logger import *
from robot.api.deco import *
from OncheDatabase.tools.DatabaseManager import DatabaseManager


@trace_robot(TRACE_ENABLED)
@keyword("Vérifier la connexion à MySQL")
def check_connection(*args, **kwargs) -> bool:
    """
    Renvoie true si la connection à Mysql est établie
    :return: True sit connection établie
    """
    return bool(DatabaseManager())