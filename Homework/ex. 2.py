import re
from collections import defaultdict

def analyze_log_file(input_file, output_file):
    try:
        status_code_counts = defaultdict(int)
        ip_counts = defaultdict(int)
        method_counts = defaultdict(int)

        with open(input_file, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) < 7:
                    continue  

                ip_address = parts[0]
                request_method = parts[5][1:]  
                status_code = int(parts[-2])

                status_code_counts[status_code] += 1
                ip_counts[ip_address] += 1
                method_counts[request_method] += 1

        most_common_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        most_common_methods = sorted(method_counts.items(), key=lambda x: x[1], reverse=True)

        with open(output_file, 'w') as out_file:
            out_file.write("Log Analysis Results\n")
            out_file.write("Total number of requests: {}\n".format(sum(status_code_counts.values())))
            out_file.write("Requests by status code:\n")
            for code, count in status_code_counts.items():
                out_file.write(f"{code}: {count}\n")
            out_file.write("Top 3 most common IP addresses:\n")
            for ip, count in most_common_ips:
                out_file.write(f"{ip}: {count}\n")
            out_file.write("Request methods breakdown:\n")
            for method, count in most_common_methods:
                out_file.write(f"{method}: {count}\n")

        print(f"Analysis complete. Results written to {output_file}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

analyze_log_file('C:/Users/5308-2/Desktop/python/first.txt', 'C:/Users/5308-2/Desktop/python/second.txt')
