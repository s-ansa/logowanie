import sys
import logging


def logging_config(level, stream):
    """
    ...
    """
    if not stream.strip().lower() in ['file', 'console']:
        print(
            f'ERROR: Incorrect stream: "{stream}". Logging disabled. Available streams: file, console.')
        return
    level_translator = {'DEBUG':    logging.DEBUG,
                        'INFO':     logging.INFO,
                        'WARNING':  logging.WARNING,
                        'ERROR':    logging.ERROR,
                        'CRITICAL': logging.CRITICAL}
    try:
        _level = level_translator[level.strip().upper()]
    except KeyError:
        print(
            f'ERROR: Incorrect logging level: "{level}". Logging disabled. Available logging levels: debug, info, warning, error, critical (case-insensitive).')
    else:
        logger = logging.getLogger(__name__)
        logger.setLevel(_level)
        formatter = logging.Formatter('%(name)s | %(levelname)s | %(message)s')
        if stream.strip().lower() == 'file':
            handler = logging.FileHandler(f'{__name__}.log', mode='w')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        elif stream.strip().lower() == 'console':
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        # TODO: overwrite log or not?
        # TODO: custom path?
        return logger


def testing():
    logger = logging_config('debug', 'console')
    logger.debug('test logging!')


# testing()
