from samaker import samaker
from samaker.cache import config
from samaker.log import logger


@samaker.command("--hello", help="say hello ", default="hello,aomaker", show_default=True)
def hello2(word):
    config.set("word", word)


@samaker.hook
def say_hello():
    word = config.get("word")
    logger.success(word)
