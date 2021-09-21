# Home Assistant Addon: Flare DNS

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield] ![Supports armhf Architecture][armhf-shield] ![Supports armv7 Architecture][armv7-shield] ![Supports i386 Architecture][i386-shield]

Flare DNS is a Home Assistant Addon for easy dyndns integration based on cloudflare.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg


## Installation

Follow these steps to get the add-on installed on your system:

1. Navigate in your Home Assistant frontend to **Supervisor** -> **Add-on Store**.
2. Find the "FlareDNS" add-on and click it.
3. Click on the "INSTALL" button.

## Configuration

A plugin configuration may look as followed:

```yaml
zones:
  - name: example.com
    domains:
      - subdomain1.example.com
      - subdomain2.example.com
token: yourCloudFlareApiToken
ip_lookup_service: https://api.ipify.org
interval: 900
```

### Option `zones`

A List of zones to be handled by the addon.

### Option `zone[].name`

The name of the zone to search for dns records

### Option `zone[].domains`

The list of domain records which will be updated with the public ip

### Option `token`

The Cloudflare Api token

### Option `ip_lookup_service`

An url which will be used to perform the public ip (external ip) lookup

### Option `interval`

Define the interval in seconds for reapeating the public ip update step
