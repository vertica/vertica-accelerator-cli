# openapi_client.ScheduleIdleShutdownV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_idle_shutdown_delete**](ScheduleIdleShutdownV1Api.md#v1_vaas_databases_dbname_idle_shutdown_delete) | **DELETE** /v1/vaas/databases/{dbname}/idle-shutdown | 
[**v1_vaas_databases_dbname_idle_shutdown_get**](ScheduleIdleShutdownV1Api.md#v1_vaas_databases_dbname_idle_shutdown_get) | **GET** /v1/vaas/databases/{dbname}/idle-shutdown | 
[**v1_vaas_databases_dbname_idle_shutdown_put**](ScheduleIdleShutdownV1Api.md#v1_vaas_databases_dbname_idle_shutdown_put) | **PUT** /v1/vaas/databases/{dbname}/idle-shutdown | 


# **v1_vaas_databases_dbname_idle_shutdown_delete**
> InlineResponse2001 v1_vaas_databases_dbname_idle_shutdown_delete(dbname, body=body)



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
    api_instance = openapi_client.ScheduleIdleShutdownV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject13() # InlineObject13 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_idle_shutdown_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleIdleShutdownV1Api->v1_vaas_databases_dbname_idle_shutdown_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject13**](InlineObject13.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_idle_shutdown_get**
> InlineResponse200 v1_vaas_databases_dbname_idle_shutdown_get(dbname, enabled=enabled)



Get idle-shutdown configuration for specific database.

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
    api_instance = openapi_client.ScheduleIdleShutdownV1Api(api_client)
    dbname = 'dbname_example' # str | 
enabled = True # bool | Filter result by the enable flag. All schedule configures will be returned if no flag is specified. (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_idle_shutdown_get(dbname, enabled=enabled)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleIdleShutdownV1Api->v1_vaas_databases_dbname_idle_shutdown_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **enabled** | **bool**| Filter result by the enable flag. All schedule configures will be returned if no flag is specified. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | No data is found |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_databases_dbname_idle_shutdown_put**
> InlineResponse2001 v1_vaas_databases_dbname_idle_shutdown_put(dbname, body=body)



Upsert idle-shutdown configuration for specific database.

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
    api_instance = openapi_client.ScheduleIdleShutdownV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.DBSessionMonitorJobConfig() # DBSessionMonitorJobConfig |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_idle_shutdown_put(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleIdleShutdownV1Api->v1_vaas_databases_dbname_idle_shutdown_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**DBSessionMonitorJobConfig**](DBSessionMonitorJobConfig.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

