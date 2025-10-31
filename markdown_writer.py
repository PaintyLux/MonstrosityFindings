import os

MD_ROOT = os.path.join( os.getcwd(), 'md' )

def generate_order_markdown_file( monster_order_data, monster_data, order_name ):
    output_file_name = os.path.join( MD_ROOT, f"{order_name.lower()}.MD" )

    if not os.path.exists( os.path.dirname( output_file_name ) ):
        os.mkdir( os.path.dirname( output_file_name ) )

    with open( output_file_name, "w" ) as output:
        output.write(f"## {order_name}:\n")
        order_data = monster_order_data[order_name]

        for family_name in order_data:
            print_table_of_contents( output, family_name, order_data[family_name] )

        for family_name in order_data:
            output.write(f"### {family_name} Family:\n")

            for species_name in order_data[family_name]:
                print_species_data( output, monster_data, species_name )

            output.write("---\n")

def print_table_of_contents( output, family_name, species_list ):
    output.write(f"**{family_name}** Family:  \n&nbsp;&nbsp;")

    for species_name in species_list[:-1]:
        output.write(f"[{species_name}](#{species_name.lower().replace(" ", "-")}) &#x2022; ")

    last_species_name = species_list[-1]
    output.write(f"[{last_species_name}](#{last_species_name.lower().replace(" ", "-")})  \n")


def print_species_data( output, monster_data, species_name ):
    species_data = monster_data[species_name]
    output.write(f"#### {species_data["name"]}\n")

    output.write(f"- Size: **{species_data["size"]}**\n")
    output.write(f"- **{species_data["job_1"]}**/**{species_data["job_2"]}**\n\n")

    if "unlock" in species_data:
        output.write("| Unlock requirements |   |\n")
        output.write("|--------------------:|:-:|\n")

        unlock_data = species_data["unlock"]

        if "infamy" in unlock_data:
            output.write(f"| Infamy | {unlock_data["infamy"]} |\n")

        if "level" in unlock_data:
            for req_family in unlock_data["level"]:
                req_order = monster_data[req_family]["order"].lower() or "INVALID"
                output.write(f"| Min. [{req_family}](/md/{req_order}.MD#{req_family.lower()}-family) level | {unlock_data["level"][req_family]} |\n")