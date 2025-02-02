from robot.api.logger import trace, error
from functools import wraps


def trace_robot(enabled: bool = True):
    def decorator(func):
        """
        Decorateur pour la trace
        :param func: la fonction à tracer
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            :param args: args de la fonction initiale
            :param kwargs: kwargs de la fonction initiale
            :return: Resultats de la fonction
            """
            if not enabled:
                return func(args, kwargs)

            result = None
            trace("------------------TRACE------------------", html=True)
            trace(f"Fonction {func.__name__}", html=True)
            if args:
                trace(
                    f"Avec les arguments suivants :\n{'\t'.join(
                        [str(arg)+'\n' for arg in args]
                    )}",
                    html=True
                )
            if kwargs:
                trace(
                    f"Avec les keywords arguments suivants :\n{'\t'.join(
                        [str(key)+':'+str(value)+'\n' for key, value in kwargs.items()]
                    )}",
                    html=True)
            try:
                result = func(*args, **kwargs)
                trace(
                    f"La fonction {func.__name__} "
                    f"s'est bien exécuté", html=True
                )
                if result:
                    trace(
                        f"Avec comme résultats : ", html=True
                    )
                    trace(result, html=True)
            except Exception as e:
                error(e.__str__(), html=True)
            trace("------------------TRACE------------------", html=True)
            return result
        return wrapper
    return decorator

__all_ = [
    'trace_robot'
]
