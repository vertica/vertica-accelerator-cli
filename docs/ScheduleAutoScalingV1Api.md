# openapi_client.ScheduleAutoScalingV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_databases_dbname_auto_scaling_delete**](ScheduleAutoScalingV1Api.md#v1_vaas_databases_dbname_auto_scaling_delete) | **DELETE** /v1/vaas/databases/{dbname}/auto-scaling | 
[**v1_vaas_databases_dbname_auto_scaling_get**](ScheduleAutoScalingV1Api.md#v1_vaas_databases_dbname_auto_scaling_get) | **GET** /v1/vaas/databases/{dbname}/auto-scaling | 
[**v1_vaas_databases_dbname_auto_scaling_put**](ScheduleAutoScalingV1Api.md#v1_vaas_databases_dbname_auto_scaling_put) | **PUT** /v1/vaas/databases/{dbname}/auto-scaling | 


# **v1_vaas_databases_dbname_auto_scaling_delete**
> InlineResponse2002 v1_vaas_databases_dbname_auto_scaling_delete(dbname, body=body)



Delete auto-scaling configuration for specific database.

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
    api_instance = openapi_client.ScheduleAutoScalingV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject12() # InlineObject12 |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_auto_scaling_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleAutoScalingV1Api->v1_vaas_databases_dbname_auto_scaling_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject12**](InlineObject12.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

# **v1_vaas_databases_dbname_auto_scaling_get**
> InlineResponse200 v1_vaas_databases_dbname_auto_scaling_get(dbname, enabled=enabled)



Get auto-scaling configuration for specific database.

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
    api_instance = openapi_client.ScheduleAutoScalingV1Api(api_client)
    dbname = 'dbname_example' # str | 
enabled = True # bool | Filter result by the enable flag. All schedule configures will be returned if no flag is specified. (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_auto_scaling_get(dbname, enabled=enabled)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleAutoScalingV1Api->v1_vaas_databases_dbname_auto_scaling_get: %s\n" % e)
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

# **v1_vaas_databases_dbname_auto_scaling_put**
> InlineResponse2002 v1_vaas_databases_dbname_auto_scaling_put(dbname, body=body)



Upsert auto-scaling configuration for specific database.

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
    api_instance = openapi_client.ScheduleAutoScalingV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.DBAutoscalingJobConfig() # DBAutoscalingJobConfig |  (optional)

    try:
        api_response = api_instance.v1_vaas_databases_dbname_auto_scaling_put(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScheduleAutoScalingV1Api->v1_vaas_databases_dbname_auto_scaling_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**DBAutoscalingJobConfig**](DBAutoscalingJobConfig.md)|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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
**428** | Success |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

