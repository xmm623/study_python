from filetools import write_files,read_files
import requests

token=read_files("/Users/weixiaoyu/Downloads/test.txt")
u=""
req_h={"content-type": "application/json","token":token}
