# openapi_client.ScheduleJobStateV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_db_name_schedule_job_state_job_name_get**](ScheduleJobStateV1Api.md#v1_vaas_databases_db_name_schedule_job_state_job_name_get) | **GET** /v1/vaas/databases/{db_name}/schedule-job-state/{job_name} | 


# **v1_vaas_databases_db_name_schedule_job_state_job_name_get**
> v1_vaas_databases_db_name_schedule_job_state_job_name_get(job_name, db_name)



Get schedule job state for specific database

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
    api_instance = openapi_client.ScheduleJobStateV1Api(api_client)
    job_name = 'job_name_example' # str | 
db_name = 'db_name_example' # str | 

    try:
        api_instance.v1_vaas_databases_db_name_schedule_job_state_job_name_get(job_name, db_name)
    except ApiException as e:
        print("Exception when calling ScheduleJobStateV1Api->v1_vaas_databases_db_name_schedule_job_state_job_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_name** | **str**|  | 
 **db_name** | **str**|  | 

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
**404** | No data is found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

