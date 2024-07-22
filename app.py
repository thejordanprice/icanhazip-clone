from flask import Flask, request
import ipaddress

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Get the CF-Connecting-IP header if present
    cf_ip = request.headers.get("CF-Connecting-IP")
    if cf_ip:
        # Check if the CF-Connecting-IP is a valid IPv6 address
        try:
            ip = ipaddress.ip_address(cf_ip)
            if ip.version == 4:
                return cf_ip  # Return if it's an IPv4 address
        except ValueError:
            pass  # Not a valid IP address

    # Fallback to X-Forwarded-For header
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")
    for ip in x_forwarded_for:
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.version == 4:
                return ip  # Return if it's an IPv4 address
        except ValueError:
            pass  # Not a valid IP address

    # Fallback to request.remote_addr
    return request.remote_addr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
