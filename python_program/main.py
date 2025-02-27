from arg_parser import create_parser
from log_helper import setup_recursive_logger

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    # Set up the root handler
    setup_recursive_logger(args.log_level)

    # AutomatedWalkTableGenerator should be imported only after setting the logger!
    from automatic_walk_time_tables.automatic_walk_time_table_generator import AutomatedWalkTableGenerator

    generator = AutomatedWalkTableGenerator(args)
    generator.run()
