from flask import Flask, request
import ipaddress

app = Flask(__name__)

@app.route('/')
def get_ip():
    # Get the CF-Connecting-IP header if present
    cf_ip = request.headers.get("CF-Connecting-IP")
    if cf_ip:
        try:
            ip = ipaddress.ip_address(cf_ip)
            if ip.version == 4:
                return cf_ip  # Return if it's an IPv4 address
        except ValueError:
            pass  # Not a valid IP address

    # Check the X-Forwarded-For header
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        # The X-Forwarded-For header can contain multiple IPs, we need the first one
        for ip in x_forwarded_for.split(','):
            ip = ip.strip()
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
