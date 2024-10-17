import unittest
import logging


class TestLogging(unittest.TestCase):
    def test_log_warning(self):
        logger = logging.getLogger(__name__)
        logger.error("This is a error message")
        logger.info("This is a info message")
        logger.warning("This is a warning message")
        logger.critical("This is a critical message")

        with self.assertLogs(logger=logger, level='WARNING'):  # debug -> info -> warning -> error -> critical
            logger.warning("This is a warning message")


if __name__ == '__main__':
    unittest.main()
