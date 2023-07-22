import json
import random
import time
import requests
import sys
import datetime


def run(imei: str):
    attempts: int = 6
    while attempts:
        try:
            url = 'http://client3.aipao.me/api/%7Btoken%7D/QM_Users/Login_AndroidSchool?IMEICode=' + imei
            create_dialogue = requests.get(url=url, headers={'version': '2.44'}).text
            dialogue_token = json.loads(create_dialogue).get('Data').get('Token')

            run_start_s1_latitude = '31.28' + str(random.randint(0, 900)).zfill(3)
            run_start_s2_longitude = '118.37' + str(random.randint(4300, 9999))
            run_start_url = 'http://client3.aipao.me/api/' + dialogue_token + \
                            '/QM_Runs/SRS?S1=' + run_start_s1_latitude + '&S2=' + run_start_s2_longitude + '&S3=3000'

            run_data = requests.get(run_start_url).text
            run_end_s1_runid = json.loads(run_data).get('Data').get('RunId')
            run_end_s6_routes = json.loads(run_data).get('Data').get('Routes')
            run_end_s7_bool = '1'
            if random.randint(0, 1):
                run_end_s4_time = 'jddj'
                run_end_s5_distance = 'oddd'
                run_end_s8_verification = 'djnorthgsm'
                run_end_s9_step = 'd'
            else:
                run_end_s4_time = 'agrg'
                run_end_s5_distance = 'qwwa'
                run_end_s8_verification = 'watqgrxjml'
                run_end_s9_step = 'tmww'
            run_end_url = 'http://client3.aipao.me/api/' + dialogue_token + '/QM_Runs/ES?S1=' + run_end_s1_runid + \
                          '&S4=' + run_end_s4_time + '&S5=' + run_end_s5_distance + '&S6=' + run_end_s6_routes + \
                          '&S7=' + run_end_s7_bool + '&S8=' + run_end_s8_verification + '&S9=' + run_end_s9_step

            result = requests.get(run_end_url).text

            current_time = datetime.datetime.now()

            print('\n---------------------------------------------------------')
            print('current_time:    {0}'.format(str(current_time)))
            print('imei:    {0}\n{1}'.format(imei, result))
            print('---------------------------------------------------------\n')
            time.sleep(random.randint(4, 6))
            break
        except BaseException:
            attempts -= 1
            time.sleep(random.randint(4, 6))


if __name__ == '__main__':
    dir = {
        '': '',
    }
    # log = open('log.txt', 'a')
    # sys.stdout = log
    # sys.stderr = log

    for imei in dir.values():
        run(imei)


