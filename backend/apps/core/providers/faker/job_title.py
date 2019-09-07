from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

level_list = [
    'Junior', 'Mid-level', 'Experienced', 'Senior', 'Lead'
]

tech_list = [
    'Python', 'Javascript', 'Django', 'Flask', 'React',
    'Angular', 'Java', 'C', 'C++', 'C#', '.NET', 'Vue',
    'Ruby', 'Golang', 'Sinatra', 'PHP', 'Laravel', 'AWS'
]

position_list = [
    'Developer', 'Engineer', 'Architect'
]


class Provider(BaseProvider):
    def job_title(self):
        level = fake.word(ext_word_list=level_list)
        tech = fake.word(ext_word_list=tech_list)
        position = fake.word(ext_word_list=position_list)

        return f'{level} {tech} {position}'
