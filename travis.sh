#!/bin/bash
./some_tests --gtest_output=xml --gtest_color=yes > gtest_output.txt 2>&1
EXIT_CODE=$?

echo "
╔════════════════════════════════════╗
║              Overview              ║
╚════════════════════════════════════╝"
./print-gtest.py test_detail.xml


echo "
╔════════════════════════════════════╗
║               Output               ║
╚════════════════════════════════════╝"
cat gtest_output.txt

exit $EXIT_CODE
