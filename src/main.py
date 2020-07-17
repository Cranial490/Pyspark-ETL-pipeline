#!/usr/bin/python
import argparse
import sys
from pyspark import SparkContext


sys.path.insert(0, './jobs')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a PySpark job')


