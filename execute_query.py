#!/usr/bin/python

from ansible.module_utils.basic import *

def store_in_file(data):
    has_file = True
    meta = {"Stored": "Query executed and output stored"}
    return (has_file, meta)

def execute(data):
    has_file = False
    meta = {"Executed": "Query executed only"}
    return (has_file, meta)


def main():
    
    fields = {
            "query" : {"required": True, "type": "str"},
            "dbname": {"required": True, "type": "str"},
            "dbuser": {"required": True, "type": "str"},
            "dbpass": {"required": True, "type": "str"},
            "file": {
                "default": True,
                "choices": [True, False],
                "type": "str"
                },
            "filename": {"required": False, "type": "str"}
            }
    choice_map = {
            'yes': store_in_file,
            'no' : execute,
            }
#    module = AnsibleModule(argument_spec={})
#    response = {"Test":"Success"}
#    module.exit_json(changed=False, meta=response)
    module = AnsibleModule(argument_spec=fields)
    has_file, result = choice_map.get(module.params['file'])(module.params)
    module.exit_json(changed=has_file, meta=result)

# select * from movie where title='Batman' into outfile '/tmp/<filename>' fields terminated by ',' enclosed by '"' lines terminated by '\n';



if __name__ == '__main__':
    main()
