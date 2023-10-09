from faker import Faker
fake = Faker()

def generate_names(n):
    names = []
    for i in range(n):
        name = (fake.ssn(), fake.first_name(), fake.last_name(), fake.address(), fake.date())
        names.append(name)
    return names