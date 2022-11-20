import base64
import requests
import json
from functools import wraps

KEY = "e8xau6dh13h5sa1kz3cpp5tue38oat3f5mcddh49nuism9cgn38y"
KEY_B64 = base64.b64encode(f"apikey:{KEY}".encode()).decode() 

class API:
    def __init__(self, KEY_B64):
        self.headers = {"Authorization": f"Basic {KEY_B64}"}
        self.host = "https://fastreport.cloud"

        self.REQUEST_TYPES = {
            "GET": requests.get,
            "DELETE": requests.delete,
            "POST": requests.post,
            "PUT": requests.put
        }

        pass
    
    # Makes API call to FastReports Cloud
    def _make_request(self, TYPE, URL, DATA):
        if TYPE in ["POST", "PUT"]:
            response = self.REQUEST_TYPES[TYPE](url=self.host+URL,
                                headers=self.headers,
                                json=DATA)
        else:
             response = self.REQUEST_TYPES[TYPE](url=self.host+URL,
                                headers=self.headers,
                                params=DATA)

        if response.text:
            try:
                return json.loads(response.text)
            except Exception as e:
                return str(response.text)

    # Decorator that makes request on API funcs
    def _api_call(func):
        def wrapper(self, *args,**kwargs):
            print(func, args, self)
            return self._make_request(*func(self, *args, **kwargs))
        return wrapper

    @_api_call
    def get_subscriptions(self, id=None):
        TYPE = "GET"
        URL = f"/api/manage/v1/Subscriptions/{id if id else ''}"
        DATA = {}

        return TYPE, URL, DATA
    
    # DATA SOURCES
    @_api_call
    def get_datasources(self, id, skip=0, take=10):
        TYPE = "GET"
        URL = f"/api/data/v1/DataSources"
        DATA = {"subscription_id": id,
                "skip": skip,
                "take": take}

        return TYPE, URL, DATA
    
    @_api_call
    def get_datasource(self, id):
        TYPE = "GET"
        URL = f"/api/data/v1/DataSources/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def put_datasource_connectionstring(self, id, connectionString=None):
        TYPE = "PUT"
        URL = f"/api/data/v1/DataSources/{id}/ConnectionString"
        DATA = {"connectionString": connectionString}

        return TYPE, URL, DATA
    
    # Tasks  /api/tasks
    @_api_call
    def get_tasks(self, id, skip=0, take=10):
        TYPE = "GET"
        URL = f"/api/tasks"
        DATA = {"subscription_id": id,
                "skip": skip,
                "take": take}

        return TYPE, URL, DATA
    
    @_api_call
    def get_task(self, id):
        TYPE = "GET"
        URL = f"/api/tasks/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def post_task(self, id, name="New task", format="Pdf", type="ExportTemplate"):
        TYPE = "POST"
        URL = f"/api/tasks"
        DATA = {"subscriptionId": id,
                "name": name,
                "format": format,
                "type": type}
            
        print(DATA)

        return TYPE, URL, DATA
    
    @_api_call
    def put_task(self, id, s_id, name=None, format=None, type="ExportTemplate", inputFileName=None, inputFileId=None, inputType=None,
                outputFileName=None, outputFolderId=None, outputType=None):
        TYPE = "PUT"
        URL = f"/api/tasks/{id}"
        DATA = {"name": name,
                "format": format,
                "type": type }
        
        if inputFileName:
                DATA["inputFile"] = {
                    "fileName": inputFileName,
                    "entityId": inputFileId,
                    "type": inputType
                }

        if outputFileName:
                DATA["outputFile"] = {
                    "fileName": outputFileName,
                    "folderId": outputFolderId,
                    "type": outputType
                }
        
        print(DATA)

        return TYPE, URL, DATA
    
    @_api_call
    def delete_task(self, id):
        TYPE = "DELETE"
        URL = f"/api/tasks/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    # GROUPS
    @_api_call
    def get_groups(self, id, skip=0, take=10):
        TYPE = "GET"
        URL = f"/api/manage/v1/Subscriptions/{id}/groups"
        DATA = {"skip": skip,
                "take": take}

        return TYPE, URL, DATA
    
    @_api_call
    def get_group(self, id):
        TYPE = "GET"
        URL = f"/api/manage/v1/Groups/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def post_group(self, id, name="New group"):
        TYPE = "POST"
        URL = f"/api/manage/v1/Groups"
        DATA = {"subscriptionId": id,
                "name": name }

        return TYPE, URL, DATA
    
    @_api_call
    def put_group_rename(self, id, name=None):
        TYPE = "PUT"
        URL = f"/api/manage/v1/Groups/{id}/rename"
        DATA = {"name": name}

        return TYPE, URL, DATA
    
    @_api_call
    def delete_group(self, id):
        TYPE = "DELETE"
        URL = f"/api/manage/v1/Groups/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def get_group_users(self, id):
        TYPE = "GET"
        URL = f"/api/manage/v1/Groups/{id}/Users"
        DATA = {}

        return TYPE, URL, DATA

    # USERS
    @_api_call
    def get_users(self, id, take=100):
        TYPE = "GET"
        URL = f"/api/manage/v1/Subscriptions/{id}/users"
        DATA = {"take": take}

        return TYPE, URL, DATA
    
    @_api_call
    def get_user(self, id):
        TYPE = "GET"
        URL = f"/api/manage/v1/UserProfile/{id}"
        DATA = {}

        return TYPE, URL, DATA
    # TEMPLATES

    @_api_call
    def get_templates_folder_and_files_count(self, id):
        TYPE = "GET"
        URL = f"/api/rp/v1/Templates/Folder/{id}/CountFolderAndFiles"
        DATA = {}

        return TYPE, URL, DATA

    @_api_call
    def get_templates_folder_and_files(self, id, skip=0, take=10, order_by="None", desc=False, search_pattern='', use_regex=False):
        TYPE = "GET"
        URL = f"/api/rp/v1/Templates/Folder/{id}/ListFolderAndFiles"
        DATA = {"skip": skip,
                "take": take,
                "order_by": order_by,
                "desc": desc,
                "search_pattern": search_pattern,
                "use_regex": use_regex }

        return TYPE, URL, DATA
    
    @_api_call
    def delete_templates_folder(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Templates/Folder/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def delete_templates_file(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Templates/File/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def post_templates_folder(self, id, name="New Folder"):
        TYPE = "POST"
        URL = f"/api/rp/v1/Templates/Folder/{id}/Folder"
        DATA = {"name": name}

        print(TYPE, URL, DATA)
        return TYPE, URL, DATA
    
    @_api_call
    def post_templates_file(self, id, name="New File", file_path=None):
        with open(file_path, 'r') as f:
            content = f.read()
            content = base64.b64encode(content.encode()).decode()

            TYPE = "POST"
            URL = f"/api/rp/v1/Templates/Folder/{id}/File"
            DATA = {"name": name, "content": content}

        return TYPE, URL, DATA
    
    @_api_call
    def put_templates_file(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Templates/File/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA

    @_api_call
    def put_templates_folder(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Templates/Folder/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA
    
    # Reports
    @_api_call
    def get_reports_folder_and_files_count(self, id):
        TYPE = "GET"
        URL = f"/api/rp/v1/Reports/Folder/{id}/CountFolderAndFiles"
        DATA = {}

        return TYPE, URL, DATA

    @_api_call
    def get_reports_folder_and_files(self, id, skip=0, take=10, order_by="None", desc=False, search_pattern='', use_regex=False):
        TYPE = "GET"
        URL = f"/api/rp/v1/Reports/Folder/{id}/ListFolderAndFiles"
        DATA = { "id": id,
                "skip": skip,
                "take": take,
                "order_by": order_by,
                "desc": desc,
                "search_pattern": search_pattern,
                "use_regex": use_regex }

        return TYPE, URL, DATA
    
    @_api_call
    def delete_reports_folder(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Reports/Folder/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def delete_reports_file(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Reports/File/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def post_reports_folder(self, id, name="New Folder"):
        TYPE = "POST"
        URL = f"/api/rp/v1/Reports/Folder/{id}/Folder"
        DATA = {"name": name}

        print(TYPE, URL, DATA)
        return TYPE, URL, DATA
    
    @_api_call
    def post_reports_file(self, id, name="New File", file_path=None):
        with open(file_path, 'rb') as f:
            content = f.read()
            content = base64.b64encode(content).decode()

            TYPE = "POST"
            URL = f"/api/rp/v1/Reports/Folder/{id}/File"
            DATA = {"name": name, "content": content}

        print(TYPE, URL, DATA)

        return TYPE, URL, DATA
    
    @_api_call
    def put_reports_file(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Reports/File/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA

    @_api_call
    def put_reports_folder(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Reports/Folder/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA

    # Exports
    @_api_call
    def get_exports_folder_and_files_count(self, id):
        TYPE = "GET"
        URL = f"/api/rp/v1/Exports/Folder/{id}/CountFolderAndFiles"
        DATA = {}

        return TYPE, URL, DATA

    @_api_call
    def get_exports_folder_and_files(self, id, skip=0, take=10, order_by="None", desc=False, search_pattern='', use_regex=False):
        TYPE = "GET"
        URL = f"/api/rp/v1/Exports/Folder/{id}/ListFolderAndFiles"
        DATA = { "id": id,
                "skip": skip,
                "take": take,
                "order_by": order_by,
                "desc": desc,
                "search_pattern": search_pattern,
                "use_regex": use_regex }

        return TYPE, URL, DATA
    
    @_api_call
    def delete_exports_folder(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Exports/Folder/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def delete_exports_file(self, id):
        TYPE = "DELETE"
        URL = f"/api/rp/v1/Exports/File/{id}"
        DATA = {}

        return TYPE, URL, DATA
    
    @_api_call
    def post_exports_folder(self, id, name="New Folder"):
        TYPE = "POST"
        URL = f"/api/rp/v1/Exports/Folder/{id}/Folder"
        DATA = {"name": name}

        print(TYPE, URL, DATA)
        return TYPE, URL, DATA
    
    @_api_call
    def post_exports_file(self, id, name="New File", file_path=None):
        with open(file_path, 'r') as f:
            content = f.read()
            content = base64.b64encode(content.encode()).decode()

            TYPE = "POST"
            URL = f"/api/rp/v1/Exports/Folder/{id}/File"
            DATA = {"name": name, "content": content}

        return TYPE, URL, DATA
    
    @_api_call
    def put_exports_file(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Exports/File/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA

    @_api_call
    def put_exports_folder(self, id, name="New File"):
        TYPE = "PUT"
        URL = f"/api/rp/v1/Exports/Folder/{id}/Rename"
        DATA = {"name": name}

        return TYPE, URL, DATA
    
    @_api_call
    def post_export_file(self, id, folderId, format, ColorSpace="RBG", PageRange="All", PdfCompliance="None"):
        TYPE = "POST"
        URL = f"/api/rp/v1/Reports/File/{id}/Export"
        DATA = {"folderId": folderId,
                "format": format,
                "exportParameters": {
                    "ColorSpace": ColorSpace,
                    "PageRange": PageRange,
                    "PdfCompliance": PdfCompliance
                }}

        print(TYPE, URL, DATA)
        return TYPE, URL, DATA