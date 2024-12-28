import argparse
import time
import traceback
from datetime import datetime
from subprocess import Popen, list2cmdline, PIPE
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from lib import lib_sys
from lib.util import logger as log
from addon.bot_skype.func.skype_tempo import *



boom_groupid = '19:6426f40c062a412783f7866498ab0438@thread.skype'
ggb_groupid = '19:1d1843f0785946de88aedf8086a9a977@thread.skype'
#investor_groupid = '19:30cb4c69867e4dc49ee50e09bf842afe@thread.skype'
#ob_groupid = '19:bdec9acc3d434829816773d27f5ac9cd@thread.skype'
#hcm_groupid = '19:2cf640084c8343b5bb280c18d1315b3d@thread.skype'
#fcm_groupid = '19:b8c7172ae0874c20a8007d6efcbcee13@thread.skype'
#pay_groupid = '19:98f7c1569fc04ae58cb2c3c5e6c44919@thread.skype'
#trading_groupid = '19:6d54445bf27e4d49a316c86854f445ae@thread.skype'
#re_groupid = '19:e358f9eb9fb1459f8a3ab008782bfe37@thread.skype'
#intern_groupid = '19:5ba25ba32aad4a5dafe2011013f432c7@thread.skype'
#intern_FPT = '19:e0ee04393d2945a4b6494a8319ad1da5@thread.skype'
qtcmt_groupid = '19:b1fa1889169e46eba664e1b5822dacfb@thread.skype'
aanb_groupid = '19:9a39222952e847e9beb6883646e0b0c9@thread.skype'
cmt_groupid = '19:5470a101a09149cd80f64542da299ec2@thread.skype'
ah_groupid = '19:e4a92e544fdd49909b64e76cbdfd75c3@thread.skype'
au_groupid = '19:7708c18fc9294263ae3c907a0b555226@thread.skype'


def exec_commands(cmds, cpu=4):
    ''' Exec commands in parallel in multiple process
    (as much as we have CPU)
    '''
    if not cmds: return # empty list

    def done(p):
        return p.poll() is not None
    def success(p):
        return p.returncode == 0
    def fail():
        sys.exit(1)

    num_cpu = min(cpu, cpu_count() - 2)
    log.info(f'Number of CPU used: {num_cpu}')

    processes = []
    while True:
        while cmds and len(processes) < num_cpu:
            task = cmds.pop()
#            print(list2cmdline(task))
            p = Popen(task, stdout=PIPE, stderr=PIPE)
#            log.info('Process %s : %s' %(p.pid, str(task)))
            processes.append(p)

        for p in processes:
            if done(p):
                if success(p):
#                    log.info('Process Success %s' %(p.pid))
                    processes.remove(p)
                else:
                    log.error(p.stdout.read())
                    log.error(p.stderr.read())
                    processes.remove(p)

        if not processes and not cmds:
            break
        else:
            time.sleep(5)



if __name__ == '__main__':
    parser = argparse.ArgumentParser('Skype Bot Cronjob', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--service', help='Service name', default='')
    # parser.add_argument('-func', '--func', help='Function to run in service', default='')
    # parser.add_argument('-u', '--username', help='Skype username', default='')
    # parser.add_argument('-p', '--password', help='Skype password', default='')
    # parser.add_argument('-c', '--cpu', help='Number of CPUs used', default=1)

    args = parser.parse_args()
    service = args.service
    # func = args.func
    # username = args.username
    # password = args.password
    # cpu = int(args.cpu)

# ================================================================
    lib_sys.init_log()

    log.printt('Skype Bot Cronjob: START..')
    try:
        bot_skype = bot_skype()
    except:
        log.error(traceback.format_exc())

    if service == 'notify_break_time':
        try:
            bot_skype.send_group_message(boom_groupid, '<at id="*">all</at> Reset 15 mins.')
        except:
            log.error(traceback.format_exc())

    if service == 'ggb_meeting':
        try:
            bot_skype.send_group_message(ggb_groupid, '<at id="*">all</at> GGB Meeting.')
        except:
            log.error(traceback.format_exc())

    if service == 'investor_meeting':
        try:
            bot_skype.send_group_message(investor_groupid, '<at id="*">all</at> Meeting.')
        except:
            log.error(traceback.format_exc())

    if service == 'update_daily':
        try:
            bot_skype.update_skype_data()
        except:
            log.error(traceback.format_exc())

    if service == 'notify_break_time_intern':
        try:
            bot_skype.send_group_message(intern_groupid, '<at id="*">all</at> Reset 15 mins.')
        except:
            log.error(traceback.format_exc())

    if service == 'notify_break_time_qtcmt':
        try:
            bot_skype.send_group_message(qtcmt_groupid, '<at id="*">all</at> Reset 15 mins.')
        except:
            log.error(traceback.format_exc())

    if service == 'notify_break_time_aanb':
        try:
            bot_skype.send_group_message(aanb_groupid, '<at id="*">all</at> Reset 15 mins.')
        except:
            log.error(traceback.format_exc())

    if service == 'notify_break_time_cmt':
        try:
            bot_skype.send_group_message(cmt_groupid, '<at id="*">all</at> Reset 15 mins.')
        except:
            log.error(traceback.format_exc())

    if service == 'notify_report_ah':
        try:
            bot_skype.send_group_message(ah_groupid, '<at id="*">all</at> TTS Report Task Outcome file Tong The: iHugeNewRevenue & Next Action Top-iUp <br> WIN TỔNG THỂ iHugeIMPROVE cOL-iP #1 NỆN công nghiệp iDirect các Yêu Cầu iHugeNewRevenue Top-iUp*iShowOff*iSimple*iGấp*iDirect  ra các Middleman Leaders bên ngoài)
        except:
            log.error(traceback.format_exc())

    if service == 'notify_report_au':
        try:
            bot_skype.send_group_message(au_groupid, '<at id="*">all</at> TTS Report Task Outcome file Tong The: iHugeNewRevenue & Next Action Top-iUp <br> WIN TỔNG THỂ iHugeIMPROVE cOL-iP #1 NỆN công nghiệp iDirect các Yêu Cầu iHugeNewRevenue Top-iUp*iShowOff*iSimple*iGấp*iDirect  ra các Middleman Leaders bên ngoài')
        except:
            log.error(traceback.format_exc())

    log.printt('Skype Bot Cronjob: DONE')

    if service == 'notify_report_qt':
        try:
            bot_skype.send_group_message(qtcmt_groupid, '<at id="*">all</at> TTS Report Task Outcome: iHugeNewRevenue & Next Action Top-iUp <br> WIN TỔNG THỂ iHugeIMPROVE cOL-iP #1 NỆN công nghiệp iDirect các Yêu Cầu iHugeNewRevenue Top-iUp*iShowOff*iSimple*iGấp*iDirect  ra các Middleman Leaders bên ngoài')
        except:
            log.error(traceback.format_exc())

    log.printt('Skype Bot Cronjob: DONE')

    if service == 'notify_report_aanb':
        try:
            bot_skype.send_group_message(aanb_groupid, '<at id="*">all</at> TTS Report Task Outcome: iHugeNewRevenue & Next Action Top-iUp <br> WIN TỔNG THỂ iHugeIMPROVE cOL-iP #1 NỆN công nghiệp iDirect các Yêu Cầu iHugeNewRevenue Top-iUp*iShowOff*iSimple*iGấp*iDirect  ra các Middleman Leaders bên ngoài')
        except:
            log.error(traceback.format_exc())

    log.printt('Skype Bot Cronjob: DONE')

    if service == 'notify_report_cmt':
        try:
            bot_skype.send_group_message(cmt_groupid, '<at id="*">all</at> TTS Report Task Outcome: iHugeNewRevenue & Next Action Top-iUp <br> WIN TỔNG THỂ iHugeIMPROVE cOL-iP #1 NỆN công nghiệp iDirect các Yêu Cầu iHugeNewRevenue Top-iUp*iShowOff*iSimple*iGấp*iDirect  ra các Middleman Leaders bên ngoài')
        except:
            log.error(traceback.format_exc())

    log.printt('Skype Bot Cronjob: DONE')



