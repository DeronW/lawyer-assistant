from net import get

class Partner():
    """
    touch a file , contains partners content
    """

    company_key = None
    nature_nodes = []

    unsolved_nodes = []
    solved_company_keys = []

    # keyNo: ['名称', '投资者类型', '一级股东', '占股比例']

    def __init__(self, company_key):
        self.company_key = company_key

    def add_node(self, d, nested_level):
        self.nature_nodes.append({ 
            'name': d['name'], 
            'level': nested_level + d['Level'],
            'amount': d['FundedAmount'], 
            'rate': d['FundedRate'] 
        })

    def arrest_children(self, children, nested_level):
        for i in children:
            print(i['KeyNo'], i['name'], i['ShortName'])
            if i['KeyNo'] in self.solved_company_keys:
                continue
            elif i['ShortName'] == '自然人股东':
                self.add_node(i, nested_level)
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
            print('Error', 'Failed when fetching Partners', j['Result']['Message'])
        else:
            node = j['Result']['Node']
            if node['ShortName'] == '国有资产经营': # 国有资产, 下面不再有股东
                self.add_node(node, nested_level)
            else:
                for i in node['children']:
                    if i['Category'] == 3: # 这是一个股东节点
                        if i['children']:
                            self.arrest_children(i['children'], nested_level)
                        else:
                            self.add_node(node, nested_level) # 没有上级股东, 这是一个追溯到头的股权所有 人/机构

    def start(self):
        self.query(self.company_key, 0)

        while self.unsolved_nodes:
            n = self.unsolved_nodes.pop()
            self.query(n['KeyNo'], n['nested_level'])

def generate_partner(company_key):
    """
    :param company_key: pick from URL, this is UUID for a company
    :returns: None

    when func finished, a file should be touch & contain all partners with properties

    """

    partners = Partner(company_key)
    partners.start()

    # print(partners.company_key)
    # print(partners.nature_nodes)
    # print(partners.unsolved_nodes)
    # print(partners.solved_company_keys)

    return partners.nature_nodes


