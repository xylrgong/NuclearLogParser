from parse_log import *

if __name__ == '__main__':
    # pattr = messages
    # addr = log_dir['CCT']
    # device_name = 'CCT'
    # keys = list(pattr.keys())
    # values = list(pattr.values())
    # timetype = time_dict['messages']
    #
    # raw_data = 'NetworkManager[2406]: <info> NetworkManager (version 0.8.1-75.el6) is starting...'
    # res = parse_a_sentence(raw_data, device_name, keys, values, timetype)
    # insert_log(res)
    # print(res)

    line_num_content_dict = read_line_num_content_from_json()
    start_parse(line_num_content_dict)
    exit_save(line_num_content_dict)