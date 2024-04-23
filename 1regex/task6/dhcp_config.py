import re


def check_dhcp_config(line: str) -> bool:
    return re.search(r"([a-z]*\.[a-z]*\.[a-z]*\s*ha=[0-9a-fA-F]{12}:ip=[\d]+\.[\d]+\.[\d]+\.[\d]+:)", line) is not None


def transfer_dhcp_config(text: str) -> str:
    pattern = r'^(.*?)(?=ha)'
    url = re.search(pattern, text)
    #ha_pattern = r"?=ha*:"
    #ha = re.search(ha_pattern,  text)
    link_address = re.search(r'ha=(.*?):ip=', text).group(1)
    fix_address = re.search(r'ip=(.*?):', text).group(1)
    split_text = [link_address[i:i + 2] for i in range(0, len(fix_address), 2)]
    final_link_address = ":".join(split_text)[:-1]
    result = "host "+url.group(1)+"{\nlink address "+final_link_address+";\nfix address "+fix_address
    return result
