from files import get_file_list
from markdown_writer import generate_order_markdown_file

import yaml

monster_order_data = {}
monster_data = {}

def main():
    file_list = get_file_list()

    for file_name in file_list:
        with open( file_name, "r" ) as raw_data:
            yaml_data = yaml.load( raw_data, Loader=yaml.Loader )
            parse_yaml_data( yaml_data )

    for order_name in monster_order_data:
        generate_order_markdown_file( monster_order_data, monster_data, order_name )

def parse_yaml_data( yaml_data ):
    for order_name in yaml_data:
        monster_order_data[order_name] = {}
        for family_name in yaml_data[order_name]:
            monster_order_data[order_name][family_name] = [species for species in yaml_data[order_name][family_name] ]

            for species_name in yaml_data[order_name][family_name]:
                species_data = yaml_data[order_name][family_name][species_name]
                species_data["order"] = order_name
                species_data["family"] = family_name
                species_data["name"] = species_name
                monster_data[species_name] = species_data

if __name__ == '__main__':
    main()