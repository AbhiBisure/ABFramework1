from faker import Faker

def generate_fake_data(field):
    """Generate fake data based on the specified field."""
    fake = Faker()
    if field == "first_name":
        return fake.first_name()
    elif field == "email":
        return fake.email()
    else:
        raise ValueError("Invalid field name. Please choose from: first_name, email")
