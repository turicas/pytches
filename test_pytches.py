#!/usr/bin/env python
#coding: utf-8

from nose.tools import assert_equal
from pytches import get_pitch_info, salts_from_La4, get_frequency


def test_get_pitch_info():
    assert_equal(get_pitch_info('La', 4, 350), ('La', 4, 350))
    assert_equal(get_pitch_info('La-3', 4, 350), ('La', 3, 350))
    assert_equal(get_pitch_info('Do#-7', 4, 350), ('Do#', 7, 350))
    assert_equal(get_pitch_info('Do#-7:200', 4, 350), ('Do#', 7, 200))
    assert_equal(get_pitch_info('Fa:500', 5, 400), ('Fa', 5, 500))
    assert_equal(get_pitch_info('_', 3, 250), ('_', 3, 250))

def test_salts_from_La4():
    assert_equal(salts_from_La4('La-4'), 0)
    assert_equal(salts_from_La4('La#-4'), 1)
    assert_equal(salts_from_La4('Do-2'), -33)
    assert_equal(salts_from_La4('La-4'), 0)
    assert_equal(salts_from_La4('Re-3'), -19)
    assert_equal(salts_from_La4('Do-7'), 27)

def test_frequencies():
    assert_equal(int(round(get_frequency('La-4'))), 440)
    assert_equal(int(round(get_frequency('Do-2'))), 65)
    assert_equal(int(round(get_frequency('La#-4'))), 466)
    assert_equal(int(round(get_frequency('Do-7'))), 2093)
