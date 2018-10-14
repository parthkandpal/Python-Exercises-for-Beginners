import logging

logger=logging.getlogger(__name__)
formatter=logging.formatter('%(levelname)s:%(message)s')

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(message)s',filename='employee.log')


class employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Employee created: {} - {} '.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = employee('John', 'Doe')
emp_2 = employee('John', 'Smith')