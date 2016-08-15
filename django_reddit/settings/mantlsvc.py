import dns.resolver
import socket

def find_database(service):
    """

    :param service: str containing fqdn of mongo service
    :return: list containing (host,port) tuples
    """
    resolver = dns.resolver.Resolver()
    results = []
    for rdata in resolver.query(service, 'SRV'):
        results.append((str(rdata.target), rdata.port))
    print('Resolved Service locations as {}'.format(results))
    return results
