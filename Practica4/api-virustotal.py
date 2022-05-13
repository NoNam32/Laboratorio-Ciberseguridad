import json
import requests

def archivo(api, path):
    api_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = dict(apikey= str(api))
    with open(str(path), 'rb') as file:
      files = dict(file=('<file path>', file))
      response = requests.post(api_url, files=files, params=params)
    if response.status_code == 200:
      result=response.json()
      print(json.dumps(result, sort_keys=False, indent=4))

def informe_archivo(api, id):
    api_url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = dict(apikey= str(api), resource=str(id))
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
      result=response.json()
      print(json.dumps(result, sort_keys=False, indent=4))

    if response.status_code == 200:
      result=response.json()
      for key in result['scans']:
        print(key)
        print(' Detected: ', result['scans'][key]['detected'])
        print(' Version: ', result['scans'][key]['version'])
        print(' Update: ', result['scans'][key]['update'])
        print(' Result: ', result['scans'][key]['result'])

def url(api, url_page):
    api_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = dict(apikey=str(api), url=str(url_page))
    response = requests.post(api_url, data=params)
    if response.status_code == 200:
      result=response.json()
      print(json.dumps(result, sort_keys=False, indent=4))

def informe_url(api, url):
    api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = dict(apikey=str(api), resource=str(url), scan=0)
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
      result=response.json()
      print(json.dumps(result, sort_keys=False, indent=4))

def dominios(api, dominio):
    api_url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = dict(apikey=str(api), domain=str(dominio))
    response = requests.get(api_url, params=params)

opcion = int(input('Escoge la opcion 1)Escanear archivos 2)Hisorial de escaneos de archivos 3)Escaneo de url 4)Historial de Escaneo Url 5)Escaneo de dominios'))
api = str(input('Escribe tu apikey: '))
if opcion == 1:
    arch = str(input('Escribe al path a escanear: '))
    archivo(api, arch)
elif opcion == 2:
    arch = str(input('Escribe la id del reporte: '))
    informe_archivo(api, arch)
elif opcion == 3:
    urlscans = str(input('Escribe la url a escanear: '))
    url(api, urlscans)
elif opcion == 4:
    urlscans = str(input('Escribe la id del reporte para la url'))
    informe_url(api, urlscans)
elif opcion == 5:
    dominioscan = str(input('Escribe el dominio a escanear: '))
    dominios(api, dominioscan)
