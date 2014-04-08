#!/bin/bash
hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input /data/books -output output -file search_map.py search_reduce.py -mapper search_map.py -reducer search_reduce.py
