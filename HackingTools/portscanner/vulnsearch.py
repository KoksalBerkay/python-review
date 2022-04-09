import requests
import json

def get_id(keyword):
    params = {'keyword': keyword, 'startIndex': 0,
              'resultsPerPage': 100}

    resp = requests.get('https://services.nvd.nist.gov/rest/json/cves/1.0/', params=params)
    data = resp.json()

    count = 0
    total_results = data['totalResults']
    f = open('vulns.txt', 'a')

    while count < total_results:
        f.write("{0} - {1}".format(data['result']['CVE_Items'][count]['cve']['CVE_data_meta']['ID'], data['result']['CVE_Items'][count]['cve']['description']['description_data'][0]['value']))
        f.write('\n')
        count += 1

key = input("[+] Type your open port banner to search exploits: ")
get_id(key)

