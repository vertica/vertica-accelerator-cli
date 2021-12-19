# openapi_client.CronUpdateConfigV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_vaas_cron_dbname_schedule_name_post**](CronUpdateConfigV1Api.md#v1_vaas_cron_dbname_schedule_name_post) | **POST** /v1/vaas/cron/{dbname}/{schedule_name} | 
[**v1_vaas_cron_dbname_schedule_name_put**](CronUpdateConfigV1Api.md#v1_vaas_cron_dbname_schedule_name_put) | **PUT** /v1/vaas/cron/{dbname}/{schedule_name} | 


# **v1_vaas_cron_dbname_schedule_name_post**
> InlineResponse200 v1_vaas_cron_dbname_schedule_name_post(schedule_name, dbname, body=body)



Enable or Disable a cron job from the database.

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
    api_instance = openapi_client.CronUpdateConfigV1Api(api_client)
    schedule_name = 'schedule_name_example' # str | 
dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject7() # InlineObject7 |  (optional)

    try:
        api_response = api_instance.v1_vaas_cron_dbname_schedule_name_post(schedule_name, dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronUpdateConfigV1Api->v1_vaas_cron_dbname_schedule_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_name** | **str**|  | 
 **dbname** | **str**|  | 
 **body** | [**InlineObject7**](InlineObject7.md)|  | [optional] 

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
**200** | Successfully updated |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vaas_cron_dbname_schedule_name_put**
> InlineResponse200 v1_vaas_cron_dbname_schedule_name_put(schedule_name, dbname, body=body)



Update an existing cron job.

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
    api_instance = openapi_client.CronUpdateConfigV1Api(api_client)
    schedule_name = 'schedule_name_example' # str | 
dbname = 'dbname_example' # str | 
body = openapi_client.InlineObject6() # InlineObject6 |  (optional)

    try:
        api_response = api_instance.v1_vaas_cron_dbname_schedule_name_put(schedule_name, dbname, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CronUpdateConfigV1Api->v1_vaas_cron_dbname_schedule_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_name** | **str**|  | 
 **dbname** | **str**|  | 
 **body** | [**InlineObject6**](InlineObject6.md)|  | [optional] 

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
**200** | Updated Successfully |  -  |
**408** | Timeout Error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

