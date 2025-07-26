import logging

# Set up a logger
logger = logging.getLogger("myapp")

def do_something():
    logger.warning("Something might be wrong")
    logger.info("Just FYI")
    return True

def test_logging(caplog):
    with caplog.at_level(logging.INFO):
        result = do_something()
        assert result is True
        assert "Something might be wrong" in caplog.text
        assert "Just FYI" in caplog.text
