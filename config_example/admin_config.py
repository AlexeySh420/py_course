import configparser

def main():
    config = configparser.ConfigParser()
    print(config.read('my_conf.ini'))

    print('Sections:', config.sections(), '\n')
    print()
    print('ADMIN section:')
    print('User email:', config['admin']['usr_email'])
    print('User name:', config['admin']['usr_name'])
    print('User password:', config['admin']['usr_pass'])
    print()
    print('FILES section:')
    print('Old file:', config['files']['source'])
    print('New file:', config['files']['dist'])

if __name__ == '__main__':
    main()
