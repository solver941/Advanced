import re


def phone_hide(persons: list[str]) -> list[str]:
    #result = [re.sub(r"\d{3}-\d{3}-\d{3}", "***-***-"+person[:-4], person) for person in persons]
    result = [re.sub(r"\d{3}-", "***-", person) for person in persons]
    return result


def email_hide(persons: list[str]) -> list[str]:
    for i in persons:
        username, domain = i.split('@')
        hidden_username = username[0] + '*' * (len(username) - 2) + username[-1]
        hidden_domain = domain[0] + '*' * (len(domain) - 2) + domain[-1]



    return f"{hidden_username}@{hidden_domain}"



