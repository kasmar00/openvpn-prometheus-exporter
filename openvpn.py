from typing import List 

class ClientHeader:
    COMMON_NAME = "Common Name"
    REAL_ADDRESS = "Real Address"
    VIRTUAL_ADDRESS="Virtual Address"
    BYTES_RECEIVED = "Bytes Received"
    BYTES_SENT = "Bytes Sent"
    CONNECTED_SINCE = "Connected Since"
    CONNECTED_SINCE_T = "Connected Since (time_t)"
    USERNAME = "Username"
    CLIENT_ID = "Client ID"
    PEER_ID = "Peer ID"

def handleClient(line: List[str], clientHeader: List[str]):
    client = { k: v for (k, v) in  zip(clientHeader, line) }
    print(
        """openvpn_server_client_received_bytes_total{{common_name="{0}",connection_time="{1}",real_address="{2}",status_path="{3}",username="{4}",virtual_address="{5}"}} {6}"""
          .format(
              client[ClientHeader.COMMON_NAME],
              client[ClientHeader.CONNECTED_SINCE_T],
              client[ClientHeader.REAL_ADDRESS],
              path,
              client[ClientHeader.USERNAME],
              client[ClientHeader.VIRTUAL_ADDRESS],
              client[ClientHeader.BYTES_RECEIVED])
          )
    print(
        """openvpn_server_client_sent_bytes_total{{common_name="{0}",connection_time="{1}",real_address="{2}",status_path="{3}",username="{4}",virtual_address="{5}"}} {6}"""
          .format(
              client[ClientHeader.COMMON_NAME],
              client[ClientHeader.CONNECTED_SINCE_T],
              client[ClientHeader.REAL_ADDRESS],
              path,
              client[ClientHeader.USERNAME],
              client[ClientHeader.VIRTUAL_ADDRESS],
              client[ClientHeader.BYTES_SENT]
          )
        )
    

path = "/run/openvpn-server/status-server.log"

def main():
    with open(path) as file:
        clientCount = 0
        for line in file.readlines():
            split = line[:-1].split(",")
            if (split[0] in ["TITLE", "GLOBAL_STATS", "END", "TIME"]):
                continue
            if (split[0] == "HEADER"):
                if (split[1] == "CLIENT_LIST"):
                    clientHeader = split[1:]
            if (split[0] == "CLIENT_LIST"):
                handleClient(split, clientHeader)
                clientCount += 1
        print(f"openvpn_server_connected_clients{{status_path=\"{path}\"}} {clientCount}")
        



if __name__=='__main__':
    main()


# openvpn_server_client_received_bytes_total{common_name="...",connection_time="...",real_address="...",status_path="...",username="...",virtual_address="..."} 139583
# openvpn_server_client_sent_bytes_total{common_name="...",connection_time="...",real_address="...",status_path="...",username="...",virtual_address="..."} 710764
# openvpn_server_route_last_reference_time_seconds{common_name="...",real_address="...",status_path="...",virtual_address="..."} 1.493018841e+09
# openvpn_status_update_time_seconds{status_path="..."} 1.490089154e+09
# openvpn_up{status_path="..."} 1
# openvpn_server_connected_clients 1