def parse(args):
    argmap = {}
    for index, arg in enumerate(args):
        if arg.startswith("--"):
            arg = arg[2:]
            argmap[arg] = index
        elif arg.startswith("-"):
            arg = arg[1:]
            for a in arg:
                if a in argmap:
                    raise SyntaxError('Identical multiple flags')
                argmap[a] = index
    return argmap

if __name__=="__main__":
    import sys
    from pprint import pprint as pp
    pp(parse(sys.argv))
