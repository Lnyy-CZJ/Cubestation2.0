import logging

def log_assertion_error(test_case_name, error_message):
    logging.info(f'{test_case_name} 断言失败！')
    logging.error(error_message)
