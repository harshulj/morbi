import re

LINE_REGEX = re.compile('(\w+)\ \{\((\d+),\ (\d+)\), \[(.*)\], \{(.*)\}\}')

def parse_line(line):
    groups = LINE_REGEX.search(line)
    name = groups.group(1)
    x = int(groups.group(2))
    y = int(groups.group(3))
    interests = groups.group(4).split(',')
    attrs = groups.group(5).strip(', \n')
    attributes = {}
    if attrs:
        attrs = attrs.split(',')
        for attr in attrs:
            attr = attr.split(':')
            attributes[attr[0].strip()] = attr[1].strip()
    return name, x, y, interests, attributes


def similarity(x_i, y_i):
    set_x = set(x_i)
    set_y = set(y_i)
    return len(set_x & set_y) / float(len(set_x | set_y))


def match_users(all_users, user, distance, preferences):
    cell = user.location.cell()
    users = []
    if distance == 'VERY_NEAR':
        users = all_users.get(cell, [])
    elif distance == 'NEAR':
        for cell in user.location.adjacent_cells():
            users += all_users.get(cell, [])
    else:
        for cell in user.location.away_cells():
            users += all_users.get(cell, [])

    if user in users:
        users.remove(user)

    sim = {}
    matching_users = []
    for u in users:
        if u.match_preferences(preferences):
            sim[u] = similarity(u.interests, user.interests)
            matching_users.append(u)

    matching_users.sort(key=lambda x: sim[x], reverse=True)
    return matching_users, sim
