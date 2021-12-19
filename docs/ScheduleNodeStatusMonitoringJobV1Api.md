# openapi_client.ScheduleNodeStatusMonitoringJobV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_node_status_delete**](ScheduleNodeStatusMonitoringJobV1Api.md#v1_vaas_databases_dbname_node_status_delete) | **DELETE** /v1/vaas/databases/{dbname}/node-status | 
[**v1_vaas_databases_dbname_node_status_get**](ScheduleNodeStatusMonitoringJobV1Api.md#v1_vaas_databases_dbname_node_status_get) | **GET** /v1/vaas/databases/{dbname}/node-status | 
[**v1_vaas_databases_dbname_node_status_put**](ScheduleNodeStatusMonitoringJobV1Api.md#v1_vaas_databases_dbname_node_status_put) | **PUT** /v1/vaas/databases/{dbname}/node-status | 


# **v1_vaas_databases_dbname_node_status_delete**
> v1_vaas_databases_dbname_node_status_delete(dbname, body=body)



Delete idle-shutdown configuration for specific database.

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
    api_instance = openapi_client.ScheduleNodeStatusMonitoringJobV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject14() # InlineObject14 |  (optional)

    try:
        api_instance.v1_vaas_databases_dbname_node_status_delete(dbname, body=body)
    except ApiException as e:
        print("Exception when calling ScheduleNodeStatusMonitoringJobV1Api->v1_vaas_databases_dbname_node_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject14**](InlineObject14.md)|  | [optional] 

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

# **v1_vaas_databases_dbname_node_status_get**
> v1_vaas_databases_dbname_node_status_get(dbname, enabled=enabled)



Get node status monitoring job schedule configuration for specific database.

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
    api_instance = openapi_client.ScheduleNodeStatusMonitoringJobV1Api(api_client)
    dbname = 'dbname_example' # str | 
enabled = True # bool | Filter result by the enable flag. All schedule configures will be returned if no flag is specified. (optional)

    try:
        api_instance.v1_vaas_databases_dbname_node_status_get(dbname, enabled=enabled)
    except ApiException as e:
        print("Exception when calling ScheduleNodeStatusMonitoringJobV1Api->v1_vaas_databases_dbname_node_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **enabled** | **bool**| Filter result by the enable flag. All schedule configures will be returned if no flag is specified. | [optional] 

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
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_node_status_put**
> v1_vaas_databases_dbname_node_status_put(dbname)



Upsert node status configuration for specific database.

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
    api_instance = openapi_client.ScheduleNodeStatusMonitoringJobV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_instance.v1_vaas_databases_dbname_node_status_put(dbname)
    except ApiException as e:
        print("Exception when calling ScheduleNodeStatusMonitoringJobV1Api->v1_vaas_databases_dbname_node_status_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 

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

