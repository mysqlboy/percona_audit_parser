#!/usr/bin/python
import json
import os.path
from optparse import OptionParser

def parse_options():
    """
    Parse options from the command line
    """
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename")

    #(options, args) = parser.parse_args()

    return parser.parse_args()


def read_file(auditname):
    """
    Open and read the audit file
    """
    jdata = ''
    if os.path.exists(auditname):
        try:
            jdata = open(auditname,'r')
        except IOError, e :
            print "Unable to open file: %s. %s" % (auditname, e) 
    
    return jdata

def parseAudit(auditFile):
    data = read_file(auditFile)
    for i in data:
        json_decoded = json.loads(i)
        audit_record = json_decoded['audit_record']
        try:
            audit_user = ('%s') % (audit_record["priv_user"])
            audit_dt = audit_record["timestamp"]
            if len(audit_user) != 0 and audit_user not in user:
             user.append((audit_dt, audit_user))
        except:
            pass

def getUniqueUsers(users):
        uniq = []
        for i in user:
                user_name = i[1]
                uniq.append(user_name)

        myset = set(uniq)
        for i in myset:
                print i

def main():
        global options
        global user
        (options, args) = parse_options()
        user=[]

        audit_file = options.filename

        parseAudit(audit_file)

        # print "=================="
        # print "uniq list of users"
        # print "=================="
        print len(getUniqueUsers(user))

if __name__ == '__main__':
        main()
