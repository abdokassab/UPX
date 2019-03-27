###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal, getpass
###################################################################
'''
     Jangan Direcode ya bosku , tinggal make apa susahnya sih
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
        W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
        W = ''
        G = ''
        R = ''
###################################################################
#                      Exception
try:
        import requests
except ImportError:
        print R + '_     _'.center(44)
        print "o' \.=./ `o".center(44)
        print '(o o)'.center(44)
        print 'ooO--(_)--Ooo'.center(44)
        print W + ' '
        print ('O S I F').center(44)
        print ' '
        print "[!] Can't import module 'requests'\n"
        sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#                       I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
        try:
                token = open('cookie/token.log','r').read()
                r = requests.get('https://graph.facebook.com/me?access_token=' + token)
                a = json.loads(r.text)
                name = a['name']
                n.append(a['name'])

                print R + '_     _'.center(44)
                print "o' \.=./ `o".center(44)
                print '(o o)'.center(44)
                print 'ooO--(_)--Ooo'.center(44)
                print ' ' + W
                print ('[*] ' + name + ' [*]').center(44)
                print ' '

        except (KeyError,IOError):
                print R + '_     _'.center(44)
                print "o' \.=./ `o".center(44)
                print '(o o)'.center(44)
                print 'ooO--(_)--Ooo'.center(44)
                print ' ' + W
                print ('U P X').center(44)
                print (W + '     [' + G +'Open Source Information Facebook'+ W + ']')
