# OpenVPN prometheus metric exporter

No dependency Python3 script for openvpn server metrics.

Compatible with and inspired by: [kumina/openvpn_exporter](https://github.com/kumina/openvpn_exporter)

## Metrics

- `openvpn_server_connected_clients` - number of connected clients
- `openvpn_server_client_received_bytes_total` - bytes received by client from server
- `openvpn_server_client_sent_bytes_total` - bytes sent to server by client

## how to use

1. Setup node_exporter with `--collector.textfile.directory /root/prom_path`
2. Setup openvpn server with `--status /run/openvpn-server/status-server.log --status-version 2`
3. Save the script at ex. `/root/openvpn.py`
3. Add to your crontab: `* * * * * root python3 /root/openvpn.py > /root/prom_path/openvpn.prom`
4. Check your node exporter metrics for openvpn metrics