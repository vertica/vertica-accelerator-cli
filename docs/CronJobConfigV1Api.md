# openapi_client.CronJobConfigV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_cron_dbname_delete**](CronJobConfigV1Api.md#v1_vaas_cron_dbname_delete) | **DELETE** /v1/vaas/cron/{dbname} | 
[**v1_vaas_cron_dbname_get**](CronJobConfigV1Api.md#v1_vaas_cron_dbname_get) | **GET** /v1/vaas/cron/{dbname} | 
[**v1_vaas_cron_dbname_post**](CronJobConfigV1Api.md#v1_vaas_cron_dbname_post) | **POST** /v1/vaas/cron/{dbname} | 


# **v1_vaas_cron_dbname_delete**
> InlineResponse200 v1_vaas_cron_dbname_delete(dbname, body=body)



Delete a scheduled start/stop cron job.

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
    api_instance = openapi_client.CronJobConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject5() # InlineObject5 |  (optional)

    try:
        api_response = api_instance.v1_vaas_cron_dbname_delete(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronJobConfigV1Api->v1_vaas_cron_dbname_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject5**](InlineObject5.md)|  | [optional] 

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
**200** | Successfully deleted |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_cron_dbname_get**
> InlineResponse200 v1_vaas_cron_dbname_get(dbname)



Get a list of cron job associated with the database.

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
    api_instance = openapi_client.CronJobConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 

    try:
        api_response = api_instance.v1_vaas_cron_dbname_get(dbname)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronJobConfigV1Api->v1_vaas_cron_dbname_get: %s\n" % e)
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

# **v1_vaas_cron_dbname_post**
> InlineResponse200 v1_vaas_cron_dbname_post(dbname, body=body)



Create a scheduled start/stop cron job.

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
    api_instance = openapi_client.CronJobConfigV1Api(api_client)
    dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject4() # InlineObject4 |  (optional)

    try:
        api_response = api_instance.v1_vaas_cron_dbname_post(dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronJobConfigV1Api->v1_vaas_cron_dbname_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbname** | **str**|  | 
 **body** | [**InlineObject4**](InlineObject4.md)|  | [optional] 

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
**201** | Successfully created |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

