import sys

from net import get
from partner import generate_partner
from investment import generate_investment

COMPANY_KEY = sys.argv[1]

def run():
    if COMPANY_KEY is None:
        print('Error, empty company key')
    else:
        company_name = ''
        # r = get('/tax_view', { 'keyno': COMPANY_KEY, 'ajaxflag': 1 })
        # j = r.json()
        # print('')
        # print('公司名称: ', j['data']['Name'])
        # print('社保号: ', j['data']['CreditCode'])
        # print('\n开始检索...\n')

        partners = generate_partner(COMPANY_KEY)
        generate_investment(COMPANY_KEY)


        print(partners)
        
        # with open('股权追溯表-%s.xlsx' % company_name, 'w') as f:
            # for i in partners:
                # print(partners)


if __name__ == '__main__':
    run()

    # https://www.qichacha.com/cms_map?keyNo=a09a6f17f057b29817b68309e74f42d5&upstreamCount=4&downstreamCount=4
    # https://www.qichacha.com/cms_map?keyNo=334fc9a2f047d077446af39766fcd76b&upstreamCount=4&downstreamCount=4
    # http://www.qichacha.com/cms_map?keyNo=g1f7e3ad3d22373aba19fd2e758883fe&upstreamCount=4&downstreamCount=4
    # http://www.qichacha.com/cms_map?keyNo=3e4827c062dd71b6cea7db52691ab881&upstreamCount=4&downstreamCount=4
