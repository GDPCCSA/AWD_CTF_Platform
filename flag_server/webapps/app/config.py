#coding:utf-8
import hashlib

secret_key = 'fbb7f76e28ec4c660cb46a35573611bc'
flag_score = 100 # 一个flag的分数
Year, month, day, Hour, Minute, Second = 2018, 11, 10, 20, 52, 43  # 在此设置比赛结束的时间 年月日时分秒
round_time = 5  # 一轮五分钟
user_count = 4 # 用户数量
round_index = 1 # 第一轮
run = 1
fraction = 10000 #初始分数
status = []
score = []
for i in range(1, user_count + 1):
    user_name = 'user' + str(i).zfill(2)
    token = hashlib.md5((user_name +'moxiaoxi7777').encode('utf-8')).hexdigest()
    status.append([user_name, run,round_index])
    score.append([user_name, fraction, token])