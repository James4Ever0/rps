# ------------------------------------------------------------------------------
# @Lucent- https://github.com/Lucent-
# A Python script to display active TCP connections along with
# their local and foreign addresses, state, process ID, and 
# associated process names. This script utilizes the psutil library
# for system and network-related information.
# ------------------------------------------------------------------------------


import psutil

def get_active_connections():
    # Get the active TCP connections
    connections = psutil.net_connections(kind='tcp')
    connection_details = []

    for conn in connections:
        # Get local and foreign address information
        local_address = f"{conn.laddr.ip}:{conn.laddr.port}"
        foreign_address = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        
        # Get the connection state
        state = conn.status
        
        # Get the process ID associated with the connection, if any
        pid = conn.pid
        process_name = None
        if pid:
            try:
                process = psutil.Process(pid)
                process_name = process.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                process_name = "N/A"

        # Gather additional information about the connection
        connection_details.append({
            "Local Address": str(local_address),
            "Foreign Address": str(foreign_address),
            "State": str(state),
            "PID": str(pid),
            "Process Name": str(process_name),
        })

    return connection_details

def display_connections(connections):
    print(f"{'Local Address':<30} {'Foreign Address':<30} {'State':<15} {'PID':<10} {'Process Name':<25}")
    print("=" * 120)
    for conn in connections:
        print(f"{conn['Local Address']:<30} {conn['Foreign Address']:<30} {conn['State']:<15} {conn['PID']:<10} {conn['Process Name']:<25}")

# one listening port at process listening port, making sure this process is running
# active process (with ongoing client requests) determination:
# local address with process listening port, foreign address, and state "ESTABLISHED"

# if we first put incoming packets into netfilter queue, will we get false active connections?

# use root user to run this command

if __name__ == "__main__":
    active_connections = get_active_connections()
    display_connections(active_connections)
