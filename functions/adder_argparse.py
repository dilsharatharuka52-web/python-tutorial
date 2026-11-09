from  argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument('square', help='Echo the give squer number', type=int)

# parser.add_argument('-v', '--verbose', help='Provides a verbose desc', action='store_true')

parser.add_argument('-m', '--merbose', help='Provides a verbose desc', type=int, choices=[0, 1, 2])


args: Namespace = parser.parse_args()

if args.merbose == 0:
   print("Option 1")

if args.merbose == 1:
   print("Option 2")

if args.merbose == 2:
   print("Option 3")
else:
   print(args.square ** 2)


# sample 
# if args.verbose:
#    print(f'{args.square} squared is: {args.square ** 2}')
# else:
#    print(args.square ** 2)