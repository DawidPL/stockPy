from faker import Faker

faker = Faker()


def faker_helper(*args, num=20):
    faker_list = []
    for arg in args:
        faker_list.append(arg * faker_number(num))
    return faker_list


def faker_number(num):
    return num
