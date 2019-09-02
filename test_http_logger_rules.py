# coding: utf-8
# © 2016-2019 Resurface Labs Inc.

from test_helper import *
from usagelogger import HttpLogger, HttpRules


def test_manages_default_rules():
    assert HttpLogger.default_rules() == HttpRules.strict_rules()
    try:
        HttpLogger.set_default_rules('')
        assert HttpLogger.default_rules() == ''
        assert len(HttpRules.parse(HttpLogger.default_rules())) == 0

        HttpLogger.set_default_rules(' include default')
        assert HttpLogger.default_rules() == ''

        HttpLogger.set_default_rules('include default\n')
        assert HttpLogger.default_rules() == ''

        HttpLogger.set_default_rules(' include default\ninclude default\n')
        assert len(HttpRules.parse(HttpLogger.default_rules())) == 0

        HttpLogger.set_default_rules(' include default\ninclude default\nsample 42')
        rules = HttpRules.parse(HttpLogger.default_rules())
        assert len(rules) == 1
        assert len(list(filter(lambda rule: rule.verb == 'sample', rules))) == 1
    finally:
        HttpLogger.set_default_rules(HttpRules.strict_rules())


def test_overrides_default_rules():
    assert HttpLogger.default_rules() == HttpRules.strict_rules()
    try:
        logger = HttpLogger(url="https://mysite.com")
        assert logger.rules == HttpRules.strict_rules()
        logger = HttpLogger(url="https://mysite.com", rules="# 123")
        assert logger.rules == "# 123"

        HttpLogger.set_default_rules("")
        logger = HttpLogger(url="https://mysite.com")
        assert logger.rules == ""
        logger = HttpLogger(url="https://mysite.com", rules="   ")
        assert logger.rules == ""
        logger = HttpLogger(url="https://mysite.com", rules=" sample 42")
        assert logger.rules == " sample 42"

        HttpLogger.set_default_rules("skip_compression")
        logger = HttpLogger(url="https://mysite.com")
        assert logger.rules == "skip_compression"
        logger = HttpLogger(url="https://mysite.com", rules="include default\nskip_submission\n")
        assert logger.rules == "skip_compression\nskip_submission\n"

        HttpLogger.set_default_rules("sample 42\n")
        logger = HttpLogger(url="https://mysite.com")
        assert logger.rules == "sample 42\n"
        logger = HttpLogger(url="https://mysite.com", rules="   ")
        assert logger.rules == "sample 42\n"
        logger = HttpLogger(url="https://mysite.com", rules="include default\nskip_submission\n")
        assert logger.rules == "sample 42\n\nskip_submission\n"
    finally:
        HttpLogger.set_default_rules(HttpRules.strict_rules())


def test_uses_allow_http_url_rules():
    logger = HttpLogger(url="http://mysite.com")
    assert logger.enableable is False
    logger = HttpLogger(url="http://mysite.com", rules="")
    assert logger.enableable is False
    logger = HttpLogger(url="https://mysite.com")
    assert logger.enableable is True
    logger = HttpLogger(url="http://mysite.com", rules="allow_http_url")
    assert logger.enableable is True
    logger = HttpLogger(url="http://mysite.com", rules="allow_http_url\nallow_http_url")
    assert logger.enableable is True


def test_uses_copy_session_field_rules():
    assert None is None  # todo finish


def test_uses_copy_session_field_and_remove_rules():
    assert None is None  # todo finish


def test_uses_copy_session_field_and_stop_rules():
    assert None is None  # todo finish


def test_uses_remove_rules():
    assert None is None  # todo finish


def test_uses_remove_if_rules():
    assert None is None  # todo finish


def test_uses_remove_if_found_rules():
    assert None is None  # todo finish


def test_uses_remove_unless_rules():
    assert None is None  # todo finish


def test_uses_remove_unless_found_rules():
    assert None is None  # todo finish


def test_uses_replace_rules():
    assert None is None  # todo finish


def test_uses_replace_rules_with_complex_expressions():
    assert None is None  # todo finish


def test_uses_sample_rules():
    queue = []

    try:
        HttpLogger(queue=queue, rules="sample 10\nsample 99")
        assert False is True
    except Exception as e:
        assert str(e) == 'Multiple sample rules'

    logger = HttpLogger(queue=queue, rules="sample 10")
    for i in range(1, 101): logger.log(request=mock_request_with_json2(), response=mock_response_with_html())
    assert 2 <= len(queue) <= 20


def test_uses_skip_compression_rules():
    logger = HttpLogger(url="http://mysite.com")
    assert logger.skip_compression is False
    logger = HttpLogger(url="http://mysite.com", rules="")
    assert logger.skip_compression is False
    logger = HttpLogger(url="http://mysite.com", rules="skip_compression")
    assert logger.skip_compression is True


def test_uses_skip_submission_rules():
    logger = HttpLogger(url="http://mysite.com")
    assert logger.skip_submission is False
    logger = HttpLogger(url="http://mysite.com", rules="")
    assert logger.skip_submission is False
    logger = HttpLogger(url="http://mysite.com", rules="skip_submission")
    assert logger.skip_submission is True


def test_uses_stop_rules():
    assert None is None  # todo finish


def test_uses_stop_if_rules():
    assert None is None  # todo finish


def test_uses_stop_if_found_rules():
    assert None is None  # todo finish


def test_uses_stop_unless_rules():
    assert None is None  # todo finish


def test_uses_stop_unless_found_rules():
    assert None is None  # todo finish
