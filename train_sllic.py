import ssl_image_classifcation as sslic

print(sslic.__version__)

# Get argument parser from sslic
parser = sslic.get_arg_parser(console_args=True)

# Parse arguments
parser_args = parser.parse_args()

# Save parser_args as python dictionary
parser_args = vars(parser_args)

sslic.main(args=parser_args)