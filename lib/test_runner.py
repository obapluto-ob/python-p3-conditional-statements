#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from testing.lib_test import *

def run_tests():
    test_classes = [TestAdminLogin, TestHowsTheWeather, TestFizzBuzz, TestCalculator]
    total_tests = 0
    passed_tests = 0
    
    for test_class in test_classes:
        print(f"\nRunning {test_class.__name__}:")
        instance = test_class()
        
        for method_name in dir(instance):
            if method_name.startswith('test_'):
                total_tests += 1
                try:
                    method = getattr(instance, method_name)
                    method()
                    print(f"  PASS {method_name}")
                    passed_tests += 1
                except Exception as e:
                    print(f"  FAIL {method_name}: {e}")
    
    print(f"\n{passed_tests}/{total_tests} tests passed")
    return passed_tests == total_tests

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)