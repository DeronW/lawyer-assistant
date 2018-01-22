
from net import get

class Investment():
    """
    touch a file , contains investment content
    """

    company_key = None
    nature_nodes = []

    unsolved_nodes = []
    solved_company_keys = []

    def __init__(self, company_key):
        self.company_key = company_key

    def add_node(self, d, nested_level):
        self.nature_nodes.append({ 
            'name': d['name'], 
            'level': nested_level + d['Level'],
            'amount': d['FundedAmount'],
            'rate': d['FundedRate'],
            'short_name': d['ShortName']
        })

    def arrest_children(self, children, nested_level):
        for i in children:
            print(i['KeyNo'], i['name'], i['ShortName'])
            if i['KeyNo'] in self.solved_company_keys:
                continue
            elif i['children']:
                self.arrest_children(i['children'], nested_level)
                self.add_node(i, nested_level)
                self.solved_company_keys.append(i['KeyNo'])
            else:
                i['nested_level'] = nested_level + i['Level']
                self.unsolved_nodes.append(i)

    def query(self, k, nested_level):
        r = get('/cms_map', { 'keyNo': k, 'upstreamCount': 4, 'downstreamCount': 4})
        j = r.json()
        if j['Status'] != 200:
            print('Error', 'Failed when fetching Partners', j['Message'])
        else:
            node = j['Result']['Node']

            for i in node['children']:
                if i['Category'] == 2: # 这是一个 对外投资 节点
                    if i['children']:
                        self.arrest_children(i['children'], nested_level)
                    else:
                        self.add_node(node, nested_level)

    def start(self):
        self.query(self.company_key, 0)

        while self.unsolved_nodes:
            n = self.unsolved_nodes.pop()
            self.query(n['KeyNo'], n['nested_level'])

def generate_investment(company_key):
    """
    :param company_key: pick from URL, this is UUID for a company
    :returns: None

    when func finished, a file should be touch & contain all partners with properties

    """

    investment = Investment(company_key)
    investment.start()

    return investment.nature_nodes
