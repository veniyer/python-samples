from faker import Faker
from jinja2 import Environment, FileSystemLoader
import sys


def create_fake_data():
	faker = Faker()
	env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True)
	
	template = env.get_template('./record.json')
	i = 0
	while i < 100:
		conf_content = template.render(job=faker.name(),company=faker.name())
		filename = "records" + "/" + str(i) + ".json"
		with open(filename,"w") as fh:
			fh.write(conf_content)
			print("Created", filename)
		i=i+1

def main(argv):
	create_fake_data()

if __name__ == "__main__":
   main(sys.argv[1:])