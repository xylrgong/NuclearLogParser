regex_month = '(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'

SW1 = {
   'time': '()(\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}.\d{2})', \
   # 'time2': '()(\d{2}:\d{2}:\d{2}.\d{2})', \
   'type': '(<)((\S)*)(>)', \
   'Media': '(Media )((\d)*T)', \
   'action' : '()((remove)|(insert)|(Toggling AdminState)|(link UP)|(link down)|(shutdown)|(re-enable))', \
   'port' : '(Port )([(]?(\d)*)[)]?', \
   # 'power_state' : '(portLinkState[\S\s]*)((down)|(up))' , \
   'login/out_state' : '()(passed|failed|message repeated 2 additional times|logout)', \
   'pif' : '(pif )(0x[\dabcdef]*)', \
   'speed' : '(speed )(\d Gbps)', \
   'mode' : '()(full-duplex)', \
}

cron = {
    'time': '()('+regex_month+'\s* \d* \d{2}:\d{2}:\d{2})', \
    'type': '()(info|warning|error|debug)', \
    'CROND': '(CROND\[)(\d*)',\
    'command': '(CMD \(. )(\S*)(\))'
}

maillog = {
    'time': '()('+regex_month+'\s* \d* \d{2}:\d{2}:\d{2})', \
    'type': '()(info|warning|error|debug)', \
    'postfix/master': '(postfix/master\[)(\d*)',\
    'postfix-script': '(postfix-script\[)(\d*)',\
    'terminate': '(terminating on )(signal \d*)', \
    'version': '(version )([\d\.]*)'
    }

secure = {
    'time': '()('+regex_month+'\s* \d* \d{2}:\d{2}:\d{2})', \
    'type': '()(info|warning|error|debug)', \
    'sshd': '(sshd\[)(\d*)', \
    'Accept publickey from': '(Accepted publickey for \S* from )([\d\.]*)', \
    'port': '(port )(\d*)', \
    'Receive disconnect from': '(Received disconnect from )([\d\.]*)', \
    'TTY': '(TTY=)(\S*)', \
    'PWD': '(PWD=)(\S*)', \
    'USER': '(USER=)(\S*)', \
    'COMMAND': '(COMMAND=)([\S\s]*)'
    }

messages = {
    'time': '()('+regex_month+'\s* \d* \d{2}:\d{2}:\d{2})', \
    'type': '()(info|warning|error|debug)', \
    'abrt': '(abrt\[)(\d*)', \
    'init': '(init: )([\S\s\(\)]*)',
    'EFI': '(EFI: )(mem\d*)', \
    'EFI_mem_type': '(EFI: mem\d*: type=)(\d*)', \
    'EFI_mem_attr': '(type=\d*, attr=)(\S*)', \
    'EFI_mem_range': '(attr=\S*, range=\[)(\S*)(\))', \
    'BIOS': '(BIOS-\S*: )(\S* - \S*)', \
    'NetworkManager': '()(NetworkManager\[\S*\]: [\S\s\(\)]*)', \
    'audit_pid': '(audit_pid=)(\S*)', \
    'old': '(old=)(\S*)', \
    'auid': '(auid=)(\S*)', \
    'sig': '(sig=)(\S*)', \
    'pf': '(pf=)(\S*)', \
    'revision': '(revision=)(\S*)', \
    'PM': '(PM: )([\S\s\(\)]*)',
    'PERCPU': '(PERCPU: )([\S\s\(\)]*)',
    'dmar': '(dmar: )([\S\s\(\)]*)',
    'PCI-DMA': '(PCI-DMA: )([\S\s\(\)]*)',
    'Console': '(Console: )([\S\s\(\)]*)',
    'TSC': '(TSC: )([\S\s\(\)]*)',
    'TIMER': '(TIMER: )([\S\s\(\)]*)',
    'NET': '(NET: )([\S\s\(\)]*)',
    'pci_bus': '()(pci_bus \S{4}:\S{2}: [\S\s\(\)]*)',
    'pci_root': '()(pci_root [\S]*:\S{2}: [\S\s\(\)]*)',
    'pci': '()(pci \S{4}:\S{2}:\S{2}.\S: [\S\s\(\)]*)',
    'ACPI': '(ACPI: )([\S\s\(\)]*)',
    'vgaarb': '(vgaarb: )([\S\s\(\)]*)',
    'NetLabel': '(usbcore: )([\S\s\(\)]*)',
    'HPET': '(HPET: )([\S\s\(\)]*)',
    'system': '()(system \S{2}:\S{2}: [\S\s\(\)]*)',
    'efifb': '(efifb: )([\S\s\(\)]*)',
    'ehci_hcd': '(ehci_hcd: )([\S\s\(\)]*)',
    'usb': '(usb )([\S]*: [\S\s\(\)]*)',
    'igb': '()(igb \S{4}:\S{2}:\S{2}.\S: [\S\s\(\)]*)',
    'udev': '(udev: )([\S\s\(\)]*)',
    'platform microcode': '(platform microcode: )([\S\s\(\)]*)',
    'netlink': '(netlink: )([\S\s\(\)]*)',
    'modem-manager': '(modem-manager: )([\S\s\(\)]*)',
    'dhclient': '()(dhclient\[\S*\]: [\S\s\(\)]*)',
    'snmpd': '()(snmpd\[\S*\]: [\S\s\(\)]*)',
    'xinetd': '()(xinetd\[\S*\]: [\S\s\(\)]*)',
    'Start': '(Starting )(Session [\d]*)',
    'User': '()(root)(.^)',
    'Stop': '(Stopping )(User Slice)',
    'Remove': '(Removed )(User Slice)',
    'Create': '(Created )(User Slice)'
}

dmesg = {
    'time': 'TIME_NOT_DEFINED', # '()(\[    [\d\.]*\])',
    'type': '()(info|warning|error|debug)',
    ' BIOS-e820': '(BIOS-e820: )([\S\s\(\)]*)',
    'ACPI': '(ACPI: )([\S\s\(\)]*)',
    'SRAT': '(SRAT: )([\S\s\(\)]*)',
    'DMA zone': '(DMA zone: )([\S\s\(\)]*)',
    'Normal zone': '(Normal zone: )([\S\s\(\)]*)',
    'PM': '(PM: )([\S\s\(\)]*)',
    'pcpu-alloc': '(pcpu-alloc: )([\S\s\(\)]*)',
    'x86/fpu': '(x86/fpu: )([\S\s\(\)]*)',
    'EVM': '(EVM: )([\S\s\(\)]*)',
    'pci': '(pci \d{4}:\d{2}:[\S]{2}.\d: )([\S\s\(\)]*)',
    'NetLabel': '(NetLabel:  )([\S\s\(\)]*)',
    'RAPL PMU': '(RAPL PMU: )([\S\s\(\)]*)',
    'random': '(random: )([\S\s\(\)]*)',
    'systemd[1]': '(systemd[1]: )([\S\s\(\)]*)',
}
