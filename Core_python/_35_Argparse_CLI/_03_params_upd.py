import json
import argparse
import os
import sys
from jinja2 import Template

parser = argparse.ArgumentParser(description='Parse key pair into a dictionary')


class StoreDict(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        self.nargs = nargs
        super(StoreDict, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        my_dict = {}
        print(f"Values: {values}")
        for kv in values:
            k, v = kv.split('=')
            my_dict[k] = v
        setattr(namespace, self.dest, my_dict)


parser.add_argument("--kp", dest="my_dict", action=StoreDict, nargs="+", metavar='KEY=VALUE')
args = parser.parse_args(sys.argv[1:])


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="JSON file to be processed")
parser.add_argument('-d', '--docker', help="Docker file path provided")
arguments = parser.parse_args()
inp = ""
path = ""
if arguments.input and arguments.docker:
    path = arguments.docker
    inp = arguments.input

else:
    print("usage: program -i <input json> -d <docker path>")
    sys.exit(-1)

d = json.loads(inp)
profileInfo = {}

profileInfo.update(d)
print(profileInfo)


orginal = ['raisebugs', 'jiraenv', 'loglevel', 'slack', 'emailnotifications', 'symmetrickey', 'teamsnotifications',
           'consolidatedmail','enabledatabase', 'enabletestmanagement', 'enablepushtestartifacts']

exp = list(profileInfo.keys())
diffls = list(set(orginal) - set(exp))
if len(diffls) == 0:
    pass
else:
    print('missed json keys:', diffls)
    sys.exit(-1)

print(path)

if os.path.isfile(path):
    tm = Template(open(path).read())
    file = tm.render(profileInfo)
    doc = open('params_upd.py', 'w')
    succ = doc.write(file)
    # print('hi')
    sys.exit(0)
else:
    # print('hello')
    sys.exit(-1)
