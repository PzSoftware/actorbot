import traceback
import importlib
from actorbot.utils import logger

def safe_import(module_name, class_name):
    if type(class_name) is list:
        for name in class_name:
            safe_import(module_name, name)
        return
    package = __package__
    if not package:
        package = __name__
    try:
        module = importlib.import_module(module_name, package)
        globals()[class_name] = getattr(module, class_name)
    except ImportError as error:
        logger.warning("Can't Import class: '%s.%s', %s",
                       module_name, class_name, error)
        logger.debug("%s", traceback.format_exc())


safe_import('.basemessage', 'Services')
safe_import('.basemessage', 'BaseMessage')
safe_import('.basemessage', 'MessageOut')
safe_import('.basemessage', 'Body')
safe_import('.basemessage', 'Peer')
safe_import('.basemessage', 'FileLocation')
safe_import('.basemessage', 'FileBytes')
safe_import('.basemessage', 'BotCommand')
safe_import('.basemessage', 'random_id')
