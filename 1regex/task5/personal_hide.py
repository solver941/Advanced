import re


def phone_hide(persons: list[str]) -> list[str]:
    #structure = r"*: [0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]"
    result = [re.sub(r"\d{3}-", "***-", person) for person in persons]
    return result


def email_hide(persons: list[str]) -> list[str]:
    return [re.sub(r": ([a-z])[a-z.]+([a-z])@[a-z]+([a-z])", r": \1***\2@***\3", person) for person in persons]
    # result = []
    # pattern = re.compile(r'([A-Z][a-z]): (?P[a-z])@(?P[a-z])\.(?P[a-z]+)')
    # for i in persons:
    #     match = re.match(pattern, i)
    #     if match:
    #         modified_email = match.group('name') + '***' + match.group('first')[0] + '@' + match.group(
    #             'domain_name') + '.' + match.group('domain')
    #         result.append(modified_email)
    #     else:
    #         result.append(i)  # If pattern doesn't match, keep original email
    # return result



