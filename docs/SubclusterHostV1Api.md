# openapi_client.SubclusterHostV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get**](SubclusterHostV1Api.md#v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get) | **GET** /v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts | 
[**v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post**](SubclusterHostV1Api.md#v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post) | **POST** /v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts | 


# **v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get**
> v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get(database_name, subcluster_name)



Returns hosts details for a specific subcluster including instance metadata.

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
    api_instance = openapi_client.SubclusterHostV1Api(api_client)
    database_name = 'database_name_example' # str | 
subcluster_name = 'subcluster_name_example' # str | 

    try:
        api_instance.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get(database_name, subcluster_name)
    except ApiException as e:
        print("Exception when calling SubclusterHostV1Api->v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_name** | **str**|  | 
 **subcluster_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post**
> v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post(database_name, subcluster_name, body=body)



Starts a new instances and adds a new host to the subcluster. (records this in the list of active hosts for the subcluster)

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
    api_instance = openapi_client.SubclusterHostV1Api(api_client)
    database_name = 'database_name_example' # str | 
subcluster_name = 'subcluster_name_example' # str | 
body = openapi_client.InlineObject9() # InlineObject9 |  (optional)

    try:
        api_instance.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post(database_name, subcluster_name, body=body)
    except ApiException as e:
        print("Exception when calling SubclusterHostV1Api->v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_name** | **str**|  | 
 **subcluster_name** | **str**|  | 
 **body** | [**InlineObject9**](InlineObject9.md)|  | [optional] 

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
**201** | Success created |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

