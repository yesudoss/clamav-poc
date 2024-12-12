import clamd

def scan_file(file_path):
    try:
        cd = clamd.ClamdNetworkSocket(host='clamav', port=3310)  # Connect to ClamAV daemon
        print("Connected to ClamAV successfully!")
        scan_result = cd.scan(file_path)
        print("Scan Result: ", )
        if scan_result:
            print(f"Scan result for {file_path}: {scan_result}")
        else:
            print(f"No results returned for {file_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # file_path = input("Enter the full path of the file to scan: ")
    file_path = "etc/profile.d"
    scan_file(file_path)
