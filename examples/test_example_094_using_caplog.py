import logging

def func_to_test():
    logging.getLogger("my_logger").info("Starting process")
    logging.getLogger("my_logger").warning("Something might be wrong")
    logging.getLogger("my_logger").error("Process failed")

def test_logging_messages(caplog):
    with caplog.at_level(logging.INFO, logger="my_logger"):
        func_to_test()

    # Check log messages
    assert "Starting process" in caplog.text
    assert "Something might be wrong" in caplog.text
    assert "Process failed" in caplog.text

    # You can also filter by level
    warning_messages = [rec.message for rec in caplog.records if rec.levelname == "WARNING"]
    assert warning_messages == ["Something might be wrong"]
