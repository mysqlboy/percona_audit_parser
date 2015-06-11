#!/usr/bin/python
import json
import os.path
from optparse import OptionParser
#



#   TODO:
#       - GREP
#            - each flavour; mcafee, percona, mariadb
#       - New modes


def parse_options():
    """
    Parse options from the command line
    """
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default="./audit.log")

    #parser.add_option("-m", "--mode", default="logins", dest="mode")
    #(options, args) = parser.parse_args()

    return parser.parse_args()


def read_file(fn):
    """
    Open and read the audit file
    """
    jdata = []
    if os.path.exists(fn):
        try:
            fdata = open(fn,'r')
        except IOError, e :
            print "Unable to open file: %s. %s" % (fn, e)

    for i in fdata:
        jdata.append(i)

    return jdata


def main():
        global options
        global user

        (options, args) = parse_options()

        audit_file = options.filename

        a = read_file(audit_file)
        events = []

        for i in a:
            try:
                event_date = json.dumps(json.loads(i)['audit_record']['timestamp'])
                event_user = json.dumps(json.loads(i)['audit_record']['user'])
                event = '%s,%s' % (event_user,event_date)
                events.append(event)

                # print event_user, event_date
            except ValueError, e:
                print e
            except KeyError, e:
                pass
        
        print min(events)

if __name__ == '__main__':
        main()
