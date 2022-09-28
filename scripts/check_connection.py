import os
import sys

sys.path.append('.')
import configs

config_name = '.env'
configs.init(config_name)
if __name__ == '__main__':
    from configs import databaseConfig
    print(databaseConfig.url)
