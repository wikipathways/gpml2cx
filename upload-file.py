import ndex2
import os

print(os.environ['NDEX_USER'])
NDEX_USER=os.environ['NDEX_USER']
NDEX_PWD=os.environ['NDEX_PWD']

wikipathways_template = ndex2.create_nice_cx_from_file('./wikipathways_template.cx')
result = wikipathways_template.upload_to(server='http://test.ndexbio.org', username=NDEX_USER, password=NDEX_PWD)
print(result)
