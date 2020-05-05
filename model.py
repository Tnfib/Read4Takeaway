import pickle
import os
"""
Modeling: (internal states)
    - current online-lists
    - current onsite-list
"""


def init():
    """
    inintialize the two objects
    reload if database can be reloaded
    else init a database
    return two bills objects
    """
    database = "database.pkl"

    onsite_bills = BillID(database)
    online_bills = BillID(database)

    return onsite_bills, online_bills


class BillID(object):
    """
    - controls internal states of bills:  -> Done
    - 1 lists:
        - ready_to_go -> Done
    - fucntions:
        - remove() -> done
        - add() -> done
        - save() -> Done
        - load() -> Done
    """
    def __init__(self, database):
        super(BillID, self).__init__()
        self.database = database
        self.ready_list = self.load(database)

    def remove(self, bill_id):
        # support multiple elems additinos
        bill_id = bill_id.replace('\n', ' ').replace('  ', ' ')
        bills = bill_id.split(' ')
        failed_cases = []
        for bill in bills:
            if bill != '':
                if bill not in self.ready_list:
                    bill = int(bill)
                    failed_cases.append(bill)
                else:
                    self.ready_list.remove(bill)
        self.save()
        return failed_cases

    def add(self, bill_id):
        # support multiple elems additinos
        bill_id = bill_id.replace('\n', ' ').replace('  ', ' ')
        bills = bill_id.split(' ')
        failed_cases = []
        success_cases = []
        for bill in bills:
            if bill != '':
                if bill in self.ready_list:
                    bill = int(bill)
                    failed_cases.append(bill)
                else:
                    self.ready_list.append(bill)
                    success_cases.append(bill)
        self.save()
        return failed_cases, success_cases

    def reset(self):
        self.ready_list = []
        #self.save()

    def save(self):
        with open(self.database, 'wb') as f:
            pickle.dump(self.ready_list, f)
        return

    def load(self, database):
        result = []
        if os.path.exists(database):
            try:
                with open(self.database, 'rb') as f:
                    result = pickle.load(f)
            except Exception as e:
                print('database could not be loaded')
        return result

    def tolist(self):
        return self.ready_list
