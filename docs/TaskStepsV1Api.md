# openapi_client.TaskStepsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_tasks_task_name_steps_get**](TaskStepsV1Api.md#v1_vaas_tasks_task_name_steps_get) | **GET** /v1/vaas/tasks/{task_name}/steps | 


# **v1_vaas_tasks_task_name_steps_get**
> v1_vaas_tasks_task_name_steps_get(task_name)



Returns the task steps.

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
    api_instance = openapi_client.TaskStepsV1Api(api_client)
    task_name = 'task_name_example' # str | 

    try:
        api_instance.v1_vaas_tasks_task_name_steps_get(task_name)
    except ApiException as e:
        print("Exception when calling TaskStepsV1Api->v1_vaas_tasks_task_name_steps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_name** | **str**|  | 

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

