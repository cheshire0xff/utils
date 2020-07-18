import os
import sys
import command_parser as c_p

def rename(directory, replacement_table, dry_run = True):
    for entry in os.scandir(directory):
        if entry.is_file():
            new_name = entry.name
            replaced_something = False
            for replacement_entry in replacement_table:
                if replacement_entry[0] not in new_name:
                    continue
                replaced_something = True
                new_name = new_name.replace(replacement_entry[0], replacement_entry[1])
            if not replaced_something:
                continue
            new_path = os.path.join(directory, new_name)
            if os.path.exists(new_path):
                print(f'File already exists: {new_name}')
                continue
            if dry_run:
                print(entry.name + " : " + new_name)
            else:
                os.rename(os.path.join(directory, entry.name),new_path)
        elif entry.is_dir():
            rename(entry.path, replacement_table, dry_run)

def help():
    print('rename [string] [replacement_string]')
    print('\t-n, --dry-run\t it has to be 3rd argument, otherwise it will get treated as string')

if __name__=="__main__":
    argmap = c_p.parse(sys.argv)
    if len(sys.argv) == 1 or 'h' in argmap:
        help()
        exit()
    r_table = ((sys.argv[1], sys.argv[2]),)
    if 'dry-run' in argmap and argmap['dry-run'] == 3:
        rename('.', r_table, True)
    elif 'n' in argmap and argmap['n'] == 3:
        rename('.', r_table, True)
    else:
        rename('.', r_table, False)


