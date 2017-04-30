#!/bin/bash
./some_tests --gtest_output=xml --gtest_color=yes > gtest_output.txt 2>&1
./print-gtest.py test_detail.xml
cat gtest_output.txt
