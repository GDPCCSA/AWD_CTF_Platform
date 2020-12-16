# coding:utf-8
import hashlib

round_index = 1  # 轮次
flag_server = 'http://172.17.0.4:8000/adm1n_ap1'
user_count = 2  # 数量
round_time = 5 * 60
secret_key = 'b14b8581ba16a0ff3902e9a18e689259'
flag_key = '0b911f1273ebbe6214387a2cad5520d4'
lib = {
"user01": "172.17.0.2",
"user02": "172.17.0.3",
}
check_port = 80
