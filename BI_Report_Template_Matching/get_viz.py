import pandas as pd

from powerbiclient import Report, models
from powerbiclient.authentication import InteractiveLoginAuthentication
device_auth = InteractiveLoginAuthentication()

# group_id = "1e4c934b-97de-47ce-bfa0-e64ed96aeb24"
# report_id = "495034f3-1c93-414f-929d-0f06ec036afa"

ROOT_PATH = r'C:\\Users\\SRNADIMP\\OneDrive - Capgemini\\New Laptop\\OneDrive - Capgemini\\Desktop\\BI_Report_Template_Matching'

def get_pbi_metadata(group_id,report_id,report_name):
    report = Report(group_id = group_id, report_id = report_id, auth = device_auth)
    pages = report.get_pages()
    visuals_data = []
    content_page = next((page for page in pages if page['displayName'] != ' '), None)

    # Iterate through each page in the report
    for page in pages:
        page_name = page['displayName']
        print(page_name)
        # Fetch visuals from each page
        visuals = report.visuals_on_page(page_name=content_page['name'])
        #print(visuals)
        for visual in visuals:
            visual_title = visual['title']
            visual_type = visual['type']
            visual_name = visual['name']
            
            # Store metadata in a dictionary
            visual_info = {
                'Page Name': page_name,
                'Visual Title': visual_title,
                'Visual Type': visual_type,
                'Visual Name': visual_name
            }
            visuals_data.append(visual_info)

    visuals_df = pd.DataFrame(visuals_data)
    excel_file_path = f'{ROOT_PATH}\{report_name}_metadata.xlsx'
    visuals_df.to_excel(excel_file_path, index=False, sheet_name='Visual Metadata')
    
get_metadata = get_pbi_metadata("653fc201-df39-4f8d-9bb1-b9de4e2b03be","6f1bd60a-d7a2-41b8-9850-00c0b0d2c01e","POC_Artificial_Intelligence_Sample")