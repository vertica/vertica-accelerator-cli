# openapi_client.BackupV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_backups_config_dbname_config_script_base_post**](BackupV1Api.md#v1_vaas_backups_config_dbname_config_script_base_post) | **POST** /v1/vaas/backups/config/{dbname}/{config_script_base} | 
[**v1_vaas_backups_config_script_base_archive_id_get**](BackupV1Api.md#v1_vaas_backups_config_script_base_archive_id_get) | **GET** /v1/vaas/backups/{config_script_base}/{archive_id} | 
[**v1_vaas_backups_dbname_get**](BackupV1Api.md#v1_vaas_backups_dbname_get) | **GET** /v1/vaas/backups/{dbname} | 
[**v1_vaas_backups_dbname_post**](BackupV1Api.md#v1_vaas_backups_dbname_post) | **POST** /v1/vaas/backups/{dbname} | 


# **v1_vaas_backups_config_dbname_config_script_base_post**
> v1_vaas_backups_config_dbname_config_script_base_post(dbname, config_script_base, body=body)



Add the backup configuration ini file

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupV1Api(api_client)
    dbname = 'dbname_example' # str | 
config_script_base = 'config_script_base_example' # str | 
body = openapi_client.InlineObject() # InlineObject |  (optional)

    try:
        api_instance.v1_vaas_backups_config_dbname_config_script_base_post(dbname, config_script_base, body=body)
    except ApiException as e:
        print("Exception when calling BackupV1Api->v1_vaas_backups_config_dbname_config_script_base_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **config_script_base** | **str**|  | 
 **body** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The backup configuration is created |  -  |
**400** | Incorrect data is provided |  -  |
**428** | Connection timeout error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_backups_config_script_base_archive_id_get**
> v1_vaas_backups_config_script_base_archive_id_get(config_script_base, archive_id)



Returns details for a specific backup archive.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupV1Api(api_client)
    config_script_base = 'config_script_base_example' # str | 
archive_id = 'archive_id_example' # str | 

    try:
        api_instance.v1_vaas_backups_config_script_base_archive_id_get(config_script_base, archive_id)
    except ApiException as e:
        print("Exception when calling BackupV1Api->v1_vaas_backups_config_script_base_archive_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_script_base** | **str**|  | 
 **archive_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_backups_dbname_get**
> InlineResponse200 v1_vaas_backups_dbname_get(dbname)



Returns all the backups that have been created for all vbr configuration files ( *.ini ) that are located in the /opt/vertica/config directory.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_backups_dbname_get(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupV1Api->v1_vaas_backups_dbname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_backups_dbname_post**
> InlineResponse2001 v1_vaas_backups_dbname_post(dbname, body=body)



Create backup archive based on ini file

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BackupV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject1() # InlineObject1 |  (optional)

    try:
        api_response = api_instance.v1_vaas_backups_dbname_post(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BackupV1Api->v1_vaas_backups_dbname_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject1**](InlineObject1.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Incorrect data is provided |  -  |
**428** | Connection timeout error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

