import os
import sys

import configs

config_name = '../.env'

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, config_name)
# print(config_path)
# print(application_path)

configs.init(config_path)
if __name__ == '__main__':
    from configs import databaseConfig
    print(databaseConfig.url)
