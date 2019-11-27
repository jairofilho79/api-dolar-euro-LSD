import json
import requests
import sys

url_base = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)'

if __name__ == '__main__':
	moeda = sys.argv[1]
	data = '11-27-2019'

	url_base += '?@moeda=\''+moeda+'\'&@dataCotacao=\''+data+'\'&$top=100&$format=json'

	r = requests.get(url_base)

	obj = json.loads(r.text)

	last = obj['value'][-1]['cotacaoVenda']

	print('R$',last)
