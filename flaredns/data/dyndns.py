from requests import get
import json
import CloudFlare

def read_options():
    """ Read Options from Homeassitant configuration UI """
    with open('/data/options.json', mode="r") as options_file:
        options = json.load(options_file) 

    return options

def detect_public_ip(service_url="https://api.ipify.org"):
    """ Lookup the public ip (external ip) """
    public_ip = get(service_url).text
    print('My Public IP IS: %s' % public_ip)

    return public_ip

def get_zone_id(cf, zone_name):
    """" Get a zone to handle """
    try:
        zones = cf.zones.get(params = {'name':zone_name,'per_page':1})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print('/zones.get %d %s - api call failed' % (e, e))
    except Exception as e:
        print('/zones.get - %s - api call failed' % (e))

    if len(zones) == 0:
        print('No zones found')
        return

    zone = zones[0]
    zone_id = zone['id']

    print('Got zone_id %s for %s' % (zone_id, zone_name))

    return zone_id

def get_dns_records(cf, zone_id):
    """ Get all dns records for a given zone_id """
    try:
        dns_records = cf.zones.dns_records.get(zone_id, params= {'type': 'A', 'proxied': False})
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print('/zones/dns_records.get %d %s - api call failed' % (e, e))
        return []

    print('Got %s DNS Records' % len(dns_records))

    return dns_records

def update_dns_records(cf, public_ip, dns_records, whitelist, zone_id): 
    for record in dns_records:
        if record['name'] not in whitelist:
            print("Missing dns record %s in whitelist. Ignore record" % record['name'])
            continue
        if record['content'] == public_ip:
            print('Ip for dns record %s is already %s. Skip record' % (record['name'], public_ip))
            continue

        try:
            print('Update %s: %s => %s' % (record['name'], record['content'], public_ip))
            cf.zones.dns_records.patch(zone_id, record['id'], data={'content': public_ip})
            print('UPDATED %s: %s -> %s'% (record['name'], record['content'], public_ip))
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            print('/zones.dns_records.patch %s - %d %s - api call failed' % (record['name'], e, e))
            

def main():
    options = read_options()
    cf = CloudFlare.CloudFlare(token=options['token'])

    public_ip = detect_public_ip(options['ip_lookup_service'])
    for zone in options['zones']:
        zone_id   = get_zone_id(cf, zone['name'])
        dns_records = get_dns_records(cf, zone_id);
        update_dns_records(cf, public_ip, dns_records, zone['domains'], zone_id)

if __name__ == '__main__':
    main()

