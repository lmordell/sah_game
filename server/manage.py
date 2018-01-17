# manage.py

""" Entry point for the main Flask Application. Create the app & run it """

###########
# Imports #
###########

from flask_script import Manager

from app import APP

MANAGER = Manager(APP)

################
# Run main app #
################

if __name__ == '__main__':
    MANAGER.run()
