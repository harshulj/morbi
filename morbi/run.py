import sys
import cmd

from users import User
from locations import Location
from utils import parse_line, match_users


class MorbiCmdProcessor(cmd.Cmd, object):
    '''
    This Processos is used for handling commandline inputs.
    Add functions to add more commands to this class.
    '''
    def __init__(self, *args, **kwargs):
        self.users = {}
        # This is redundant but a good to have for constant time lookup
        # while matching users. Also this is storing just the reference
        self.users_by_name  = {}
        super(MorbiCmdProcessor, self).__init__(*args, **kwargs)


    def do_add_user(self, line):
        '''
        This command adds a single user to the list of users
        USAGE: ad_user PersonE {(17, 42), [Running, Reading, Trekking]}
        '''
        try:
            name, x, y, interests, attributes = parse_line(line.strip())
        except Exception as e:
            print 'Unable to add user: ERROR: %s' % e
            return
        location = Location(x, y)
        user = User(name, location, interests, **attributes)
        cell = location.cell()
        if cell in self.users:
            self.users[cell].append(user)
        else:
            self.users[cell] = [user]
        self.users_by_name[name] = user
        print 'User added'


    def do_users(self, line):
        '''
        This commands prints the list of users
        USAGE: users
        '''
        print self.users


    def do_match_very_near(self, line):
        '''
        This command matches existing user with other users who are very near
        USAGE: match_very_near PersonA age:20 gender:m
        '''
        self._match(line)


    def do_match_near(self, line):
        '''
        This command matches existing user with other users who are near
        USAGE: match_near PersonA age:20 gender:m
        '''
        self._match(line, 'NEAR')


    def do_match_further(self, line):
        '''
        This command matches existing user with other users who are slightly further
        USAGE: match_further PersonA age:20 gender:m
        '''
        self._match(line, 'FURTHER_AWAY')


    def _match(self, line, distance='VERY_NEAR'):
        data = line.split(' ')
        name = data[0].strip()
        attrs = {}
        for attr in data[1:]:
            attr = attr.split(':')
            attrs[attr[0]] = attr[1]
        try:
            user = self.users_by_name[name]
        except Exception as e:
            print 'ERROR: %s does not exist' % e
            return

        users, sim = match_users(self.users, user, distance, attrs)
        for user in users:
            print user.name, sim[user]


    def do_user(self, name):
        '''
        This command prints a user details.
        USAGE: user PersonF
        '''
        try:
            user = self.users_by_name[name]
        except Exception as e:
            print 'ERROR: %s does not exist' % e
            return
        print user.__dict__


    def do_EOF(self, line):
        return True


def run():
    MorbiCmdProcessor().cmdloop()

if __name__ == '__main__':
    MorbiCmdProcessor().cmdloop()
