import os
import re
import shutil
import traceback

def move_file(src_path, dst_path, file):
    # print('from : ',src_path)
    # print('to : ',dst_path)
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print ('move_file ERROR: ',e)
        traceback.print_exc()

if __name__ == '__main__':
    basedir = '../LOG/TERMINAL/CCT/APPLOG\cma_clientexe'
    dstdir = 'test_log_handled/'
    pattr_app_done = '^[A-Za-z_0-9]+-(\d)*.log'
    pattr_app_in_progress = '^[A-Za-z_0-9]+.log'
    pattr_sys_done = '^(cron|message|maillog|secure|boot)-(\d)*'
    pattr_sys_in_progress = '^(cron|message|maillog|secure|boot)'
    loglist = os.listdir(basedir)
    for logname in loglist:
        APP_DONE = bool(re.search(pattr_app_done, logname))
        APP_IN_PROGRESS = bool(re.search(pattr_app_in_progress, logname))
        SYS_DONE = bool(re.search(pattr_sys_done, logname))
        SYS_IN_PROGRESS = bool(re.search(pattr_sys_in_progress, logname))
        if APP_DONE or SYS_DONE:
            print('Now parse log:', logname)
            print('parse the log and remove the file to another dir')
            move_file(basedir, dstdir, logname)
        elif APP_IN_PROGRESS or SYS_IN_PROGRESS:
            print('Now parse log:', logname)
            print('parse the log and remember the line number parsed')
        else:
            print('logname cannot handled:', logname)
            print('something wrong maybe pattern not completed')
