# openapi_client.SubclusterHostDetailV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete**](SubclusterHostDetailV1Api.md#v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete) | **DELETE** /v1/vaas/databases/{database_name}/subclusters/{subcluster_name}/hosts/{host_id} | 


# **v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete**
> v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete(host_id, database_name, subcluster_name)



Removes a host from the subcluster and stops the host. (removes this in the list of active hosts for the subcluster)

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
    api_instance = openapi_client.SubclusterHostDetailV1Api(api_client)
    host_id = 'host_id_example' # str | 
database_name = 'database_name_example' # str | 
subcluster_name = 'subcluster_name_example' # str | 

    try:
        api_instance.v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete(host_id, database_name, subcluster_name)
    except ApiException as e:
        print("Exception when calling SubclusterHostDetailV1Api->v1_vaas_databases_database_name_subclusters_subcluster_name_hosts_host_id_delete: %s\n" % e)
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

