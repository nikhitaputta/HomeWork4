#!/bin/bash
hadoop jar /root/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar -input /data/numbers -output output -file mathstats_map.py mathstats_reduce.py -mapper mathstats_map.py -reducer mathstats_reduce.py
