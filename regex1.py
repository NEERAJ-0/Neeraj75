import re

print(re.findall('[0-9]','abcdef12cfc345'))
print(re.findall('[^0-9]','abc def12cf6345'))
print(re.findall('.','abc def&*12cfc345'))
print(re.findall('[0-9]+','abc8t&123b$c56fc945'))
print(re.findall('[0-9]*','abc8t&123b$c56fc945'))
print(re.findall('[0-9]?','abc8t&123b$c56fc945'))
print(re.findall('[0-9]{2}','abc8t&123b$c56fc945'))
print(re.findall('[0-9]{2,3}','abc8t&123b$c4346fc945'))
