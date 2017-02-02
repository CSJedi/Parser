import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soap = BeautifulSoup(html, 'html.parser')
    table = soap.find('div', class_='container-fluid cols_table show_visited')
    rows = table.find_all('div', class_='row')
    projects = []
    for row in rows:
        projects.append({
            'title': row.a.text,
            'category': row.find('a', class_='text-muted').text, 
            'price': str(row.find('div', class_='col-sm-1 amount title').text.split()).strip('[\'\']'),
            'application`s count': row.find('div', class_='col-sm-3 text-right text-nowrap hidden-xs').text.split()[0]
        })
       
    
    for project in projects:
        print(project)
    #return rows

def main():
    html = get_html('https://www.weblancer.net/jobs/')
    parse(html)
    
if __name__ == '__main__':
    main() 
