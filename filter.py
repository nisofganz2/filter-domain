def filter_domains(input_file, output_file, domain_type):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        buffer = []
        for line in infile:
            domain = line.strip()
            if domain.endswith(domain_type):
                buffer.append(domain + '\n')
        
        outfile.writelines(buffer)

if __name__ == "__main__":
    input_file = input("List Domain: ")
    output_file = input("Result: ")
    domain_type = input("Domain: ")
    filter_domains(input_file, output_file, domain_type)