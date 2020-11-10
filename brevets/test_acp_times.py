"""
Nose tests for acp_times.py

We cannot test for randomness here (no effective oracle),
but we can test that the elements in the returned string
are correct.
"""

import arrow
import acp_times

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

startTime = arrow.get("2020-11-09T00:00:00-08:00")

def same(s, t):
    """
    Same times
    in two strings s and t.
    """
    return s == t

def test_lt_60_close():
    assert same("2020-11-09T01:45:00-08:00", acp_times.close_time(15, 200, startTime))
    assert same("2020-11-09T03:15:00-08:00", acp_times.close_time(45, 100, startTime))
    

def test_open_200():
    assert same("2020-11-09T00:00:00-08:00", acp_times.open_time(0, 200, startTime))
    assert same("2020-11-09T01:46:00-08:00", acp_times.open_time(60, 200, startTime))
    assert same("2020-11-09T03:32:00-08:00", acp_times.open_time(120, 200, startTime))
    assert same("2020-11-09T05:53:00-08:00", acp_times.open_time(200, 200, startTime))
    assert same("2020-11-09T05:53:00-08:00", acp_times.open_time(205, 200, startTime))

def test_open_1000():
    print(acp_times.open_time(0, 1000, startTime))
    assert same("2020-11-09T00:00:00-08:00", acp_times.open_time(0, 1000, startTime))
    assert same("2020-11-09T05:53:00-08:00", acp_times.open_time(200, 1000, startTime))
    assert same("2020-11-09T12:08:00-08:00", acp_times.open_time(400, 1000, startTime))
    assert same("2020-11-09T18:48:00-08:00", acp_times.open_time(600, 1000, startTime))
    assert same("2020-11-10T01:57:00-08:00", acp_times.open_time(800, 1000, startTime))
    assert same("2020-11-10T09:05:00-08:00", acp_times.open_time(1000, 1000, startTime))
    assert same("2020-11-10T09:05:00-08:00", acp_times.open_time(1100, 1000, startTime))

def test_close_1000():
    assert same("2020-11-09T01:00:00-08:00", acp_times.close_time(0, 1000, startTime))
    assert same("2020-11-09T13:20:00-08:00", acp_times.close_time(200, 1000, startTime))
    assert same("2020-11-10T02:40:00-08:00", acp_times.close_time(400, 1000, startTime))
    assert same("2020-11-10T16:00:00-08:00", acp_times.close_time(600, 1000, startTime))
    assert same("2020-11-11T09:30:00-08:00", acp_times.close_time(800, 1000, startTime))
    assert same("2020-11-12T03:00:00-08:00", acp_times.close_time(1000, 1000, startTime))
    assert same("2020-11-12T03:00:00-08:00", acp_times.close_time(1100, 1000, startTime))

def test_close_200():
    assert same("2020-11-09T01:00:00-08:00", acp_times.close_time(0, 200, startTime))
    assert same("2020-11-09T04:00:00-08:00", acp_times.close_time(60, 200, startTime))
    assert same("2020-11-09T08:00:00-08:00", acp_times.close_time(120, 200, startTime))
    assert same("2020-11-09T13:30:00-08:00", acp_times.close_time(200, 200, startTime))
    assert same("2020-11-09T13:30:00-08:00", acp_times.close_time(205, 200, startTime))