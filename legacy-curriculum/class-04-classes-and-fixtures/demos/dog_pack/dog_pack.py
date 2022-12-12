class Pack:

    all = []

    def __init__(self, leader, members=[]):
        self.leader = leader
        self.members = members
        self.__class__.all.append(self)

    def __repr__(self):
        return f'{self.leader} - {self.members}'

    def __str__(self):
        return f'The pack is led by {self.leader}, the members are {self.members}'

    @staticmethod
    def get_pack_oath():
        return 'all for one, one for all'

    @classmethod
    def create_from_data(cls, data):
        """Create a new Pack with member Dogs
        with given data.
        Data is a string in form
        Each line has 'dog name, breed'
        First line is leader, rest followers



        Arguments:
            data {[type]} -- [description]
        """

        lines = data.split('\n')

        leader_line = lines[0]

        # Rex,Terrier -> Terrier('Rex')
        line_parts = leader_line.split(',')
        dog_name = line_parts[0]
        dog_breed = line_parts[1]

        if dog_breed == 'Terrier':
            leader = Terrier(dog_name)

        followers = [Puggle('Jolene'), Bullhuahua('Keanu')]
        return Pack(leader, followers)

class Dog:

    # class attribute
    dog_list = []

    def __init__(self, name, breed='mutt'):
        self.name = name
        self.breed = breed
        self.__class__.dog_list.append(self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'I am a {self.__class__.__name__} named {self.name}'

    @classmethod
    def get_dogs(cls):
        return cls.dog_list


class Bullhuahua(Dog):

    def __init__(self, name):
        super().__init__(name, 'bullhuahua')

    def do_cute_thing(self):
        return 'take on a dog 10 times your size'


class Terrier(Dog):

    def __init__(self, name):
        super().__init__(name, 'terrier')

    def do_cute_thing(self):
        return 'chase every squirrel in neighborhood'


class Puggle(Dog):

    def __init__(self, name):
        super().__init__(name, 'puggle')

    def do_cute_thing(self):
        return 'warm human feet'

