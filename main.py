from notion_client import Client
from pprint import pprint

notion_token = 'secret_DWsytfw0VbrX1EJZE1Pndn5hHH62X70YToFay4igxWL'
notion_page_id = 'All-Tasks-30c713a4a06b4cf1ad0ace54244fae4f?pvs=4'

def main():
    client = Client(auth=notion_token)

    page_response = client.pages.retrieve(notion_page_id)

    pprint(page_response, indent=2)

if __name__ == '__main__':
    main()
          