import argparse
import sys

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


parser.add_argument("--key_pairs", dest="my_dict", action=StoreDict, nargs="+", metavar='KEY=VALUE')
args = parser.parse_args(sys.argv[1:])
print(args)
