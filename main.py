import sys
import json
import mdutils

postman_file = sys.argv[1]

mdFile = mdutils.MdUtils(file_name='Documentation API')

with open(postman_file) as json_file:
    data = json.load(json_file)

    mdFile.new_header(level=1, title=data['info']['name'])    # style is set 'atx' format by default.
    mdFile.new_paragraph(data['info']['description'])    # style is set 'atx' format by default.

    mdFile.new_line('****')

    for route in data['item']:        
        mdFile.insert_code("+ "+route['request']['method'] + " " + route['name'], language='diff')
        mdFile.new_paragraph(route['request']['description'])

        try:
            mdFile.new_header(level=2, title="Headers:")
            for header in route['request']['header']:
                mdFile.new_paragraph(">Key: " + header['key'] + "\n" + "| " + header['value'])
        except(KeyError):
            print('[PostPY] '+ route['info']['name'] + ' No header found')


        try:
            mdFile.new_header(level=2, title="["+route['request']['body']['mode']+"] Body:")
            
            for body_request in route['request']['body']['urlencoded']:
                print(body_request['key'])
                mdFile.new_header(level=3, title=body_request['key']+" *" + body_request['type'] + "*")
                mdFile.new_paragraph(body_request['description'])

        except(KeyError):
            print('[PostPY] {'+ route['name'] + '} No body found')

        mdFile.new_line('****')

mdFile.create_md_file()
