import json
pattr = {'time': '()(\S+ \d{1,2} \d{2}:\d{2}:\d{2})()', \
         'device': '(\S+ \d+ \d{2}:\d{2}:\d{2} )(\S+)()', \
         'level': '()(kernel|info)()', \
         'SMBIOS': '(SMBIOS=)(0x(\S)+)()', \
         # 'ACPI': '(ACPI=)(0x(\S)*)()', \
         'ACPI 2.0': '(ACPI 2.0=)(0x(\S)*)()', \
         'EFI': '(EFI: )([A-Za-z0-9 \w\S\s:,=\[\]\(\)\-]*)()', \
         'ACPI': '(ACPI:)([\s*\S*]+)', \
         'Registered nosave memory': '(Registered nosave memory:)([A-Za-z0-9 ]* - [A-Za-z0-9 ]*)'
         }
regex_pattr = json.dumps(pattr)
print(regex_pattr)