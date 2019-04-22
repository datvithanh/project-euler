import requests
from parsel import Selector
url = 'https://projecteuler.net/show=all'

response = requests.get(url)
sel = Selector(response.text)

temp = sel.xpath("//div[contains(@class,'info')]/h3/*[1]/text()").extract()

problems = []
p = ''

for item in temp:
    if 'Problem' == item[:7]:
        if p != '':
            problems.append(p)
        p = item
    else:
        p = p + item

problems.append(p)

solved_problems = {}
with open('status.txt', 'r') as f:
    content = f.read()
    for line in content.split('\n'):
        if line != '\n':
            index = int(line.split('|')[0])
            solved_problems[index] = line.split('|')[1:]

readme = """# Project Euler solutions
----
python3, gcc 5.2 c++14

| Problem | File | Result |
|----|----|----|"""

for key, val in enumerate(problems):
    if key + 1 in solved_problems.keys():
        readme = readme + '\n|{}|{}|{}|'.format(val, solved_problems[key+1][0], solved_problems[key+1][1])
    else:
        readme = readme + '\n|{}|{}|{}|'.format(val, '', '')

with open('README.MD', 'w+') as f:
    f.write(readme)
