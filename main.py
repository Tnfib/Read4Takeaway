from PyQt5 import QtWidgets  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

from model import init
from control import UserOP, CounterOP

"""
open:
    - view set content  -> Done
Missing:
    - relative design- >done
    - set up on windows machine-> Done
    - or mac. No idea.
Done
    - Key:
        - add item: blink blink 1 minute  -> not working yet
        - add item: play sound ->Done
    - chang control.py to main.py  -> done
        - database: refresh view. -> done
        - database save/load -> done
        - alert function -> Done
    - Warning: number not found, wrong number  -> Done
        - warning :
            - add: duplicate -> Done
            - remove: not existing -> done
        - Remove works -> Done
        - add list (clear before) -> Done
        - Font bigger/smaller
        - child UI update
        - bigger UI for add/remove-> Doen
        - add list: split string to add  -> Done
    - view_update (disabled) -> Done
        - update op-view -> Done
        - update user-view-> DOne

View:  - Done
    - User-view
        online-column
        onsite-column
    - Operator-view
        - user-view (upper)
        - control view (lower)
Control elements:
Group: online -> Done
    ready_group:
        ready_butt
        ready_field
    done_group:
        done_button
        done_field
    reset
Group onsite. -> Done
    ready_group:
        ready_button -> dones
        ready_field  -> done
    done_group:  -> done
        done_button -> done
        done_field -> done
    reset -> done

Modeling: (internal states) -> done
    - basic operations -> done
    - current online-lists -> Done
    - current onsite-list -> Done
Debugging & running:
    - set up Pycharm
    -
"""
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    online_bills, onsite_bills = init()
    # We set the form to be our ExampleApp (design)
    user_view = UserOP(online_bills, onsite_bills)
    user_view.show()  # Show the form
    # We set the form to be our ExampleApp (design)
    op_view = CounterOP(online_bills, onsite_bills, user_view)
    op_view.show()  # Show the form

    app.exec_()  # and execute the app


if __name__ == '__main__':
    # if we're running file directly and not importing it
    main()  # run the main function
