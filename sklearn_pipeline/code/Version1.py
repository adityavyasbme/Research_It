import argparse 

parser = argparse.ArgumentParser(description="random")
parser.add_argument('-r1','--random1',type=int,metavar="",required=True, help='random')
parser.add_argument('-r','--random',type=str,metavar="",required=True,help='random')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action = 'store_true',help = 'print quiet')
group.add_argument('-v','--verbose',action = 'store_true',help = 'print verbose')

args = parser.parse_args()


if __name__=='__main__':

    if args.quiet:
        print("Quiet")
    elif args.verbose:
        print('Verbose')
    else:
        print("Random : {}".format(args.random))
        print("Random1 : {}".format(args.random1))
        





class data_packet():
    def __init__(self):
        



