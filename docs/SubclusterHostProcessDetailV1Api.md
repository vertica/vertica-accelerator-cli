# openapi_client.SubclusterHostProcessDetailV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete**](SubclusterHostProcessDetailV1Api.md#v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete) | **DELETE** /v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts/{host_id}/process | 
[**v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post**](SubclusterHostProcessDetailV1Api.md#v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post) | **POST** /v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts/{host_id}/process | 


# **v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete**
> v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete(host_id, database_name, subcluster_name)



Stops the instance and then stops the vertica process on a specific host.

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
    api_instance = openapi_client.SubclusterHostProcessDetailV1Api(api_client)
    host_id = 'host_id_example' # str | 
database_name = 'database_name_example' # str | 
subcluster_name = 'subcluster_name_example' # str | 

    try:
        api_instance.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete(host_id, database_name, subcluster_name)
    except ApiException as e:
        print("Exception when calling SubclusterHostProcessDetailV1Api->v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **database_name** | **str**|  | 
 **subcluster_name** | **str**|  | 

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
**204** | Success deleted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post**
> v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post(host_id, database_name, subcluster_name, body=body)



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
    api_instance = openapi_client.SubclusterHostProcessDetailV1Api(api_client)
    host_id = 'host_id_example' # str | 
database_name = 'database_name_example' # str | 
subcluster_name = 'subcluster_name_example' # str | 
body = openapi_client.InlineObject10() # InlineObject10 |  (optional)

    try:
        api_instance.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post(host_id, database_name, subcluster_name, body=body)
    except ApiException as e:
        print("Exception when calling SubclusterHostProcessDetailV1Api->v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**|  | 
 **database_name** | **str**|  | 
 **subcluster_name** | **str**|  | 
 **body** | [**InlineObject10**](InlineObject10.md)|  | [optional] 

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

