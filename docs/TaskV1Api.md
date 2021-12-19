# openapi_client.TaskV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_tasks_get**](TaskV1Api.md#v1_vaas_tasks_get) | **GET** /v1/vaas/tasks | 


# **v1_vaas_tasks_get**
> InlineResponse200 v1_vaas_tasks_get(type=type, dbname=dbname)



Returns a list of tasks.

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
    api_instance = openapi_client.TaskV1Api(api_client)
    type = 'all' # str | Type of tasks to return. (optional) (default to 'all')
dbname = 'dbname_example' # str | Name of database to return tasks for. (optional)

    try:
        api_response = api_instance.v1_vaas_tasks_get(type=type, dbname=dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskV1Api->v1_vaas_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of tasks to return. | [optional] [default to &#39;all&#39;]
 **dbname** | **str**| Name of database to return tasks for. | [optional] 

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

