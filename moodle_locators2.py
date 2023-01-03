from faker import Faker

fake = Faker(locale='en_CA')
moodle_url = 'http://54.245.196.124/'
moodle_login_url = 'http://54.245.196.124/login/index.php'
moodle_users_main_page = 'http://54.245.196.124/admin/user.php'
moodle_username = 'admin'
moodle_password = 'Moodle$erver001!#'
moodle_dashboard_url = 'http://54.245.196.124/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
country = fake.country()
description = fake.text(1000)
pic_desc = fake.user_name()
phonetic_firstname = fake.first_name()
phonetic_lastname = fake.last_name()
phonetic_middlename = fake.first_name()
phonetic_alternatename = fake.last_name()
list_of_interests = [new_username, new_password, first_name, city, email]
id = fake.pyint(11111111, 99999999)
institution = fake.pyint(111111, 999999)
department = fake.lexify(text='????')
phone1 = fake.phone_number()
phone2 = fake.phone_number()
address = fake.address()
address = fake.address().replace("\n","")
full_name=f'{first_name} {last_name}'

