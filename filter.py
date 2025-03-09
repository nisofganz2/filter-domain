def filter_domains(input_file, output_file, domain_types):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        buffer = []
        for line in infile:
            domain = line.strip()
            if any(domain.endswith(domain_type) for domain_type in domain_types):
                buffer.append(domain + '\n')
        
        outfile.writelines(buffer)

if __name__ == "__main__":
    input_file = input("List Domain: ")
    output_file = input("Result: ")
    domain_types = input("Domain (pisahkan dengan koma): ").split(',')
    domain_types = [domain.strip() for domain in domain_types]
    filter_domains(input_file, output_file, domain_types)